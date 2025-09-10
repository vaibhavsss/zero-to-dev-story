# 🌟 Django JWT Authentication Project

## The Birth of a New Project
Every great project begins with an idea — a need for **secure, modern authentication** in web applications. This project was born out of that desire: to build a **full-stack Django system** with **JWT authentication**, a **frontend UI**, and a clean, modern design.

From the humble beginnings of setting up a Django project and installing required dependencies, it has grown into a fully functional application where users can **sign up, log in, view a protected dashboard, and explore a list of all registered users**.

This README chronicles the journey of this project, from setup to completion.

---

## 🚀 Project Features
- **User Authentication**
  - Sign Up with username and password
  - Sign In using JWT tokens (access & refresh tokens)
  - Logout functionality with token cleanup
- **Protected Dashboard**
  - Only accessible with valid JWT tokens
  - Dynamic welcome message
- **User Management**
  - API endpoint to list all registered users
  - Frontend table displaying all users in a clean UI
- **Frontend UI**
  - Modern **dark theme** with interactive buttons and tables
  - Responsive design
  - Navigation bar for easy page access
- **API Ready**
  - Fully compatible with **Postman** for testing
  - JWT-secured endpoints

---

## 🛠 Technology Stack
| Layer           | Technology                        |
|-----------------|-----------------------------------|
| Backend         | Django 5.2, Django REST Framework |
| Database        | SQLite                           |
| Frontend        | HTML, CSS, Vanilla JS            |
| Authentication  | JWT (JSON Web Tokens)            |
| Development OS  | MacOS                            |
| Tools           | VS Code, Postman                 |

---

## 📁 Project Directory Structure
```
django-auth/
│
├── manage.py
├── db.sqlite3
├── venv/
├── .gitignore
├── README.md
│
├── config/
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
│
├── static/
│   └── css/style.css
│
└── Postman/
└── DjangoJWT.postman_collection.json

```


---

## ⚡ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-auth.git
   cd django-auth
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 🔗 API Documentation 

1. **Sign Up**
   ```
   POST /api/auth/signup/
   Content-Type: application/json
   {
     "username": "yourusername",
     "password": "yourpassword"
   }
   ```
2. **Login**
   ```
   POST /api/auth/login/
   Content-Type: application/json
   {
     "username": "yourusername",
     "password": "yourpassword"
   }
   ```

----

## Future Improvements
- Add email verification
- Implement password reset
- Add user roles (admin, regular user)
- Enhance frontend with React or Vue.js
- Add more API endpoints (e.g., update user profile, delete user)
- Implement rate limiting for API endpoints
- Add logging and monitoring for better debugging and performance tracking

## Conclusion
This project demonstrates full-stack JWT authentication in Django with a modern frontend, making it ideal for learning or bootstrapping a real-world application. From sign up to protected data viewing, users experience a smooth authentication workflow, and developers have a clean, modular project to build on.

## References
- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [JWT Authentication in Django](https://www.django-rest-framework.org/api-guide/authentication/#jwt-authentication)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [CSS Tricks](https://css-tricks.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [GitHub](https://github.com/)
- [Python.org](https://www.python.org/)
- [Django REST Framework JWT](https://github.com/GetBlimp/django-rest-framework-jwt)
- [Django CORS Headers](https://github.com/adamchainz/django-cors-headers)
- [Django Rest Auth](https://django-rest-auth.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)

License
MIT License