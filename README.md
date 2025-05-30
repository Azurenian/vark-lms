# VARK Suite - Fullstack Web Application

## Project Structure

- `backend-django/` — Django backend (API)
- `frontend-nuxt/` — Nuxt 3 frontend (student/teacher dashboards)

---

## Project Setup

### Django Backend

- Django project structure with basic configuration
- Environment variables support via `django-environ`
- SQLite database (default)
- Admin interface available

### Nuxt Frontend

- Nuxt 3 with Vuetify UI framework
- TypeScript support
- Student and teacher dashboards
- Responsive design

---

## Quick Start (Development)

1. **Backend:**

   ```sh
   cd backend-django
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

2. **Frontend:**
   ```sh
   cd frontend-nuxt
   npm install
   npm run dev
   ```

---

## Development Notes

- Backend runs on `http://localhost:8000`
- Frontend runs on `http://localhost:3000`
- Environment-specific settings can be configured in `.env` files
- Database migrations are handled by Django's built-in system

---

## Features to Implement

- [ ] User authentication system
- [ ] VARK learning style assessment
- [ ] Content management
- [ ] Performance analytics
- [ ] AI-powered chatbot
- [ ] Lesson generation tools

---

Ready for development! Start by implementing the core features you need for your VARK Suite application.
