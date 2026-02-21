from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector, random, string

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret123")

templates = Jinja2Templates(directory="templates")

# ---------------- Database -----------------
conn = mysql.connector.connect(
    host="localhost", user="root", password="sravani@01", database="fastapi_db"
)
cursor = conn.cursor(dictionary=True)

# ---------------- Home -----------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---------------- 1. Hello User -----------------
@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello_user(request: Request, name: str):
    return templates.TemplateResponse("view.html", {"request": request, "data":[{"Greeting":f"Hello {name}!"}]})

# ---------------- Generic CRUD -----------------
tables_with_fields = {
    "students": ["name","age","course"],
    "todos": ["task","status"],
    "products": ["name","price","description"],
    "blogs": ["title","content"],
    "employees": ["name","department","role"],
    "quotes": ["quote","author"],
    "courses": ["name"],
    "urlshortener": ["long_url"],
    "movies":["name","director","year"],
    "books":["title","author","year"],
    "contacts":["name","phone","email"],
    "inventory":["product","quantity"],
    "events":["name","date","location"]
}

def fetch_table(table):
    cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()

def fetch_table_by_id(table, id):
    cursor.execute(f"SELECT * FROM {table} WHERE id=%s", (id,))
    return cursor.fetchone()

def delete_table(table, id):
    cursor.execute(f"DELETE FROM {table} WHERE id=%s", (id,))
    conn.commit()

# Create dynamic routes for CRUD
for table, fields in tables_with_fields.items():
    # View all
    @app.get(f"/{table}", response_class=HTMLResponse)
    async def view_table(request: Request, table=table):
        data = fetch_table(table)
        return templates.TemplateResponse("view.html", {"request": request, "data": data, "table":table})

    # Add page
    @app.get(f"/{table}/add", response_class=HTMLResponse)
    async def add_table_page(request: Request, table=table):
        return templates.TemplateResponse("add.html", {"request": request, "table":table})

    # Add post
    @app.post(f"/{table}/add")
    async def add_table_post(request: Request, table=table, **form_data):
        keys = fields
        values = tuple(form_data[k] for k in keys)
        placeholders = ",".join(["%s"]*len(keys))
        cursor.execute(f"INSERT INTO {table} ({','.join(keys)}) VALUES ({placeholders})", values)
        conn.commit()
        return RedirectResponse(f"/{table}", status_code=303)

    # Edit page
    @app.get(f"/{table}/edit/{{id}}", response_class=HTMLResponse)
    async def edit_table_page(request: Request, id:int, table=table):
        data = fetch_table_by_id(table,id)
        return templates.TemplateResponse("add.html", {"request": request, "data": data, "table":table})

    # Edit post
    @app.post(f"/{table}/edit/{{id}}")
    async def edit_table_post(id:int, table=table, **form_data):
        keys = fields
        values = tuple(form_data[k] for k in keys)
        assignments = ",".join([f"{k}=%s" for k in keys])
        cursor.execute(f"UPDATE {table} SET {assignments} WHERE id=%s", values + (id,))
        conn.commit()
        return RedirectResponse(f"/{table}", status_code=303)

    # Delete
    @app.get(f"/{table}/delete/{{id}}")
    async def delete_table_row(id:int, table=table):
        delete_table(table,id)
        return RedirectResponse(f"/{table}", status_code=303)

# ---------------- Random Quote -----------------
@app.get("/quote", response_class=HTMLResponse)
async def random_quote(request: Request):
    cursor.execute("SELECT * FROM quotes")
    data = cursor.fetchall()
    quote = random.choice(data) if data else {"quote":"No Quotes","author":""}
    return templates.TemplateResponse("view.html", {"request": request, "data":[quote]})

# ---------------- Login/Register -----------------
@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request, "table":"users"})

@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(username,password))
    conn.commit()
    return RedirectResponse("/login", status_code=303)

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request, "table":"login"})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
    user = cursor.fetchone()
    if user:
        request.session["user"]=username
        return RedirectResponse("/dashboard", status_code=303)
    return RedirectResponse("/login", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    user = request.session.get("user")
    return templates.TemplateResponse("view.html", {"request": request, "data":[{"Welcome":f"Welcome {user}"}]})

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)

# ---------------- URL Shortener -----------------
@app.get("/urlshortener", response_class=HTMLResponse)
async def url_shortener_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request, "table":"urlshortener"})

@app.post("/urlshortener/add")
async def create_short_url(long_url: str = Form(...)):
    short_code = ''.join(random.choices(string.ascii_letters+string.digits,k=6))
    cursor.execute("INSERT INTO urls (long_url, short_code) VALUES (%s,%s)",(long_url,short_code))
    conn.commit()
    return {"short_url":f"http://127.0.0.1:8000/{short_code}"}

@app.get("/{short_code}")
async def redirect_short_url(short_code: str):
    cursor.execute("SELECT long_url FROM urls WHERE short_code=%s",(short_code,))
    url = cursor.fetchone()
    return RedirectResponse(url["long_url"]) if url else {"error":"URL not found"}

# ---------------- Student Course Enrollment -----------------
@app.get("/enrollments", response_class=HTMLResponse)
async def view_enrollments(request: Request):
    cursor.execute("SELECT e.id, s.name as student, c.name as course FROM enrollments e JOIN students s ON e.student_id=s.id JOIN courses c ON e.course_id=c.id")
    data = cursor.fetchall()
    return templates.TemplateResponse("view.html", {"request": request, "data": data, "table":"enrollments"})

@app.get("/enrollments/add", response_class=HTMLResponse)
async def add_enrollment_page(request: Request):
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    return templates.TemplateResponse("add.html", {"request": request, "table":"enrollments", "students":students, "courses":courses})

@app.post("/enrollments/add")
async def add_enrollment(student_id:int = Form(...), course_id:int = Form(...)):
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s,%s)",(student_id,course_id))
    conn.commit()
    return RedirectResponse("/enrollments", status_code=303)