Introduction

During our era, we had to walk several miles to homes of friends to discuss assignments or projects from school. Sometimes you arrive unwelcomed and have to return back to your home. With the advancement in Technology today, as my project, I planned on developing the backend api for an online educational platform where students can register and login to share projects, collaborate with other colleagues to seek insight on projects or topics, without needing to walk to someone's home unwelcomed. This gives rise to an online collaborative and study platform for students - 📚 StudyHub

📚 StudyHub Backend API
A collaborative learning platform backend built with Django REST Framework, enabling students to register, create project teams, collaborate, and share comments.
This backend powers StudyHub — a platform where students connect, form teams, upload projects, and communicate efficiently to share ideas on projects.
________________________________________
🚀 Features
👥 Accounts
•	User registration & login
•	JWT authentication
•	Profile management
•	Roles (student / mentor support if added)
📁 Projects
•	Create, update, delete projects
•	Add collaborators
•	Search & filter projects
•	Upload media (optional S3 config)
💬 Comments
•	Add comments to projects
•	Moderate/delete comments
•	Thread-safe design
🔐 Secure API
•	JWT Auth (access + refresh)
•	Custom permissions
•	Rate limiting (optional)
________________________________________
🛠️ Tech Stack
•	Python 3.x
•	Django 5+
•	Django REST Framework
•	SimpleJWT
•	SQLite (Dev)
•	Swagger / Redoc docs
________________________________________
📂 Project Structure
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
________________________________________
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/qwabena37/studyhub_api.git
cd studyhub_api
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Start Server
python manage.py runserver



{"username":["Vanessa"],"password":["Abena123."]}