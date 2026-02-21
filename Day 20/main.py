from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from database import cursor, conn
import random
import string

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret123")

templates = Jinja2Templates(directory="templates")

# =========================
# HOME - STUDENTS VIEW
# =========================
@app.get("/", response_class=HTMLResponse)
async def show_students(request: Request):
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "students": students})

# =========================
# STUDENT CRUD
# =========================
@app.post("/add-student")
async def add_student(name: str = Form(...), age: int = Form(...), course: str = Form(...)):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s,%s,%s)", (name, age, course))
    conn.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/delete-student/{id}")
async def delete_student(id: int):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    return RedirectResponse("/", status_code=303)

# =========================
# TODO FULL CRUD
# =========================
@app.get("/todos", response_class=HTMLResponse)
async def todos(request: Request):
    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()
    return templates.TemplateResponse("todos.html", {"request": request, "tasks": tasks})

@app.post("/add-task")
async def add_task(title: str = Form(...)):
    cursor.execute("INSERT INTO todos (title,status) VALUES (%s,'Pending')", (title,))
    conn.commit()
    return RedirectResponse("/todos", status_code=303)

@app.get("/complete-task/{id}")
async def complete_task(id: int):
    cursor.execute("UPDATE todos SET status='Completed' WHERE id=%s", (id,))
    conn.commit()
    return RedirectResponse("/todos", status_code=303)

@app.get("/delete-task/{id}")
async def delete_task(id: int):
    cursor.execute("DELETE FROM todos WHERE id=%s", (id,))
    conn.commit()
    return RedirectResponse("/todos", status_code=303)

# =========================
# BOOK MANAGEMENT
# =========================
@app.get("/books", response_class=HTMLResponse)
async def books(request: Request):
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return templates.TemplateResponse("books.html", {"request": request, "books": books})

@app.post("/add-book")
async def add_book(title: str = Form(...), author: str = Form(...)):
    cursor.execute("INSERT INTO books (title,author) VALUES (%s,%s)", (title, author))
    conn.commit()
    return RedirectResponse("/books", status_code=303)

@app.get("/delete-book/{id}")
async def delete_book(id: int):
    cursor.execute("DELETE FROM books WHERE id=%s", (id,))
    conn.commit()
    return RedirectResponse("/books", status_code=303)

# =========================
# NOTES APP
# =========================
@app.get("/notes", response_class=HTMLResponse)
async def notes(request: Request):
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    return templates.TemplateResponse("notes.html", {"request": request, "notes": notes})

@app.post("/add-note")
async def add_note(content: str = Form(...)):
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    conn.commit()
    return RedirectResponse("/notes", status_code=303)

@app.get("/delete-note/{id}")
async def delete_note(id: int):
    cursor.execute("DELETE FROM notes WHERE id=%s", (id,))
    conn.commit()
    return RedirectResponse("/notes", status_code=303)

# =========================
# MOVIES
# =========================
@app.get("/movies", response_class=HTMLResponse)
async def movies(request: Request):
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    return templates.TemplateResponse("movies.html", {"request": request, "movies": movies})

@app.get("/movie/{id}", response_class=HTMLResponse)
async def movie_detail(request: Request, id: int):
    cursor.execute("SELECT * FROM movies WHERE id=%s", (id,))
    movie = cursor.fetchone()
    return templates.TemplateResponse("movie_detail.html", {"request": request, "movie": movie})

# =========================
# INVENTORY
# =========================
@app.get("/inventory", response_class=HTMLResponse)
async def inventory(request: Request):
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    return templates.TemplateResponse("inventory.html", {"request": request, "items": items})

@app.post("/add-item")
async def add_item(name: str = Form(...), quantity: int = Form(...)):
    cursor.execute("INSERT INTO inventory (product_name,quantity) VALUES (%s,%s)", (name, quantity))
    conn.commit()
    return RedirectResponse("/inventory", status_code=303)

@app.get("/delete-item/{id}")
async def delete_item(id: int):
    cursor.execute("DELETE FROM inventory WHERE id=%s", (id,))
    conn.commit()
    return RedirectResponse("/inventory", status_code=303)

# =========================
# LOGIN SYSTEM
# =========================
@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)", (username, password))
    conn.commit()
    return RedirectResponse("/login", status_code=303)

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        request.session["user"] = username
        return RedirectResponse("/dashboard", status_code=303)
    return RedirectResponse("/login", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if "user" not in request.session:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": request.session["user"]})

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=303)

# =========================
# URL SHORTENER
# =========================
@app.get("/shortener", response_class=HTMLResponse)
async def shortener_page(request: Request):
    return templates.TemplateResponse("shortener.html", {"request": request})

@app.post("/shorten")
async def shorten_url(long_url: str = Form(...)):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    cursor.execute("INSERT INTO urls (long_url, short_code) VALUES (%s,%s)", (long_url, code))
    conn.commit()
    return RedirectResponse(f"/{code}", status_code=303)

@app.get("/{code}")
async def redirect_url(code: str):
    cursor.execute("SELECT long_url FROM urls WHERE short_code=%s", (code,))
    result = cursor.fetchone()
    if result:
        return RedirectResponse(result.long_url)
    return RedirectResponse("/")