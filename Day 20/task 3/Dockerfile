# Task 8
# FROM python:3.11
# COPY app.py .
# CMD ["python", "app.py"]

# Task 9
# FROM python:3.11
# RUN pip install flask
# COPY app.py .
# CMD ["python", "app.py"]

#Task 10 
# FROM python:3.11
# RUN pip install fastapi uvicorn
# COPY main.py .
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#Task 11
# FROM python:3.11
# WORKDIR /app
# COPY . .
# CMD ["python", "app.py"]

# Task 12
# FROM python:3.11
# ENV APP_ENV=production
# CMD ["python", "-c", "import os; print(os.getenv('APP_ENV'))"]

# Task 13
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["ls"]
