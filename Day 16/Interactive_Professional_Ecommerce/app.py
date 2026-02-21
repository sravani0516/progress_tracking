
import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from functools import wraps
from pydantic import BaseModel, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# ---------------- Models ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(300))
    image = db.Column(db.String(200))

# ---------------- Pydantic ----------------
class ItemSchema(BaseModel):
    name: str
    price: float
    description: str | None = None

# ---------------- Decorators ----------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Admin access required")
            return redirect(url_for("dashboard"))
        return f(*args, **kwargs)
    return wrapper

# ---------------- Home ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- Register ----------------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("All fields required")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("register"))

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, password=hashed, role="user")
        db.session.add(user)
        db.session.commit()
        flash("Registration successful")
        return redirect(url_for("login"))

    return render_template("register.html")

# ---------------- Login ----------------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["role"] = user.role
            return redirect(url_for("dashboard"))

        flash("Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

# ---------------- Dashboard ----------------
@app.route("/dashboard")
@login_required
def dashboard():
    search = request.args.get("search")
    min_price = request.args.get("min_price")

    query = Item.query

    if search:
        query = query.filter(Item.name.contains(search))

    if min_price:
        query = query.filter(Item.price >= float(min_price))

    items = query.all()
    return render_template("dashboard.html", items=items)

# ---------------- Add Product ----------------
@app.route("/add-product", methods=["GET","POST"])
@login_required
@admin_required
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        description = request.form.get("description")
        image = request.files.get("image")

        if not name or not price:
            flash("Name and Price required")
            return redirect(url_for("add_product"))

        filename = None
        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        item = Item(name=name, price=float(price), description=description, image=filename)
        db.session.add(item)
        db.session.commit()

        flash("Product Added Successfully")
        return redirect(url_for("dashboard"))

    return render_template("add_product.html")

# ---------------- Cart ----------------
@app.route("/add-to-cart/<int:id>")
@login_required
def add_to_cart(id):
    if session.get("role") != "user":
        flash("Only users can add to cart")
        return redirect(url_for("dashboard"))

    cart = session.get("cart", [])
    cart.append(id)
    session["cart"] = cart
    flash("Added to cart")
    return redirect(url_for("dashboard"))

@app.route("/remove-from-cart/<int:id>")
@login_required
def remove_from_cart(id):
    cart = session.get("cart", [])
    if id in cart:
        cart.remove(id)
    session["cart"] = cart
    flash("Removed from cart")
    return redirect(url_for("checkout"))

@app.route("/checkout")
@login_required
def checkout():
    cart = session.get("cart", [])
    items = Item.query.filter(Item.id.in_(cart)).all()
    total = sum(i.price for i in items)
    return render_template("checkout.html", items=items, total=total)

@app.route("/payment", methods=["POST"])
@login_required
def payment():
    session["cart"] = []
    flash("Payment Successful 🎉")
    return redirect(url_for("dashboard"))

# ---------------- REST API ----------------
@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([{"id":i.id,"name":i.name,"price":i.price} for i in items])

@app.route("/items", methods=["POST"])
def create_item():
    try:
        data = ItemSchema(**request.json)
        item = Item(name=data.name, price=data.price, description=data.description)
        db.session.add(item)
        db.session.commit()
        return jsonify({"message":"Item created"}),201
    except ValidationError as e:
        return jsonify(e.errors()),400

@app.route("/items/<int:id>", methods=["PUT"])
def update_item(id):
    item = Item.query.get_or_404(id)
    try:
        data = ItemSchema(**request.json)
        item.name = data.name
        item.price = data.price
        item.description = data.description
        db.session.commit()
        return jsonify({"message":"Updated"})
    except ValidationError as e:
        return jsonify(e.errors()),400

@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message":"Deleted"})

# ---------------- Run ----------------
if __name__ == "__main__":
    os.makedirs("static/uploads", exist_ok=True)

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            hashed = bcrypt.generate_password_hash("admin").decode("utf-8")
            admin = User(username="admin", password=hashed, role="admin")
            db.session.add(admin)
            db.session.commit()

    # Important change for Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
