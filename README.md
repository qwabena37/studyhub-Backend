# 📚 StudyHub Backend API

A collaborative learning platform backend built with **Django REST Framework**, enabling students to register, create projects, collaborate with peers, and exchange ideas through comments.

StudyHub powers an online environment where students can connect, form project teams, upload work, and communicate efficiently—eliminating the need for physical meetups and enabling seamless academic collaboration.

---

## 📖 Introduction

In earlier days, students often had to walk long distances to meet friends for discussions on assignments or projects—sometimes arriving unwelcomed and returning home without progress.

With advancements in technology, **StudyHub** was designed to solve this problem by providing an **online collaborative and study platform**. Students can now register, log in, share projects, collaborate with colleagues, and seek insights on academic topics—anytime, anywhere.

---

## 🚀 Features

### 👥 Accounts

* User registration & authentication
* JWT-based login (access & refresh tokens)
* Profile management
* Role-based access (students, mentors – extensible)

### 📁 Projects

* Create, update, and delete projects
* Add collaborators to projects
* Search and filter projects
* Media uploads (optional cloud storage support)

### 💬 Comments

* Add comments to projects
* Moderate and delete comments
* Scalable and thread-safe design

### 🔐 Security

* JWT Authentication
* Custom permission classes
* Rate limiting (optional / configurable)

---

## 🛠️ Tech Stack

* **Python** 3.x
* **Django** 5+
* **Django REST Framework**
* **SimpleJWT**
* **SQLite** (Development)
* **Swagger / Redoc** (API Documentation)

---

## 📂 Project Structure

```bash
studyhub_api/
│── manage.py
│── requirements.txt
│
├── studyhub/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── permissions.py
│
├── projects/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── filters.py
│
└── comments/
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/qwabena37/studyhub_api.git
cd studyhub_api
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

* **Linux / macOS**

```bash
source venv/bin/activate
```

* **Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

---

## 📑 API Documentation

Once the server is running, access:

* **Swagger UI:** `/swagger/`
* **ReDoc:** `/redoc/`

---

## 🧪 Sample Data

### Sample Users

```json
{
  "username": "David",
  "password": "kofi123"
}
```

```json
{
  "username": "John",
  "password": "john123"
}
```

### Sample Projects

```json
{
  "title": "Tech in Africa",
  "description": "Positive effects of technology in Africa"
}
```

```json
{
  "title": "Females in Tech",
  "description": "The importance of involving females in technology across Africa"
}
```

---

## 📌 Future Enhancements

* Mentor & reviewer roles
* Real-time chat (WebSockets)
* Notifications system
* Cloud media storage (AWS S3 / Cloudinary)
* CI/CD & containerization support

---

## 🤝 Contributing

Contributions are welcome!
Please fork the repository, create a feature branch, and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---
