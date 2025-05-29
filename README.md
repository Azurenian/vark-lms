# VARK Suite - Fullstack LTI Integration Project

## Project Structure

- `backend-django/` — Django backend (LTI provider, API)
- `frontend-nuxt/` — Nuxt 3 frontend (student/teacher dashboards)

---

## Chronological Setup & Configuration

### 1. Django Backend Setup

- Created Django project and app structure.
- Added `authentication` app for LTI launch endpoint.
- Implemented `/auth/lti/launch/` endpoint to handle LTI 1.1 POST requests from Moodle.
- Extracted user info and role from LTI POST, validated consumer key/secret from settings.
- Redirected to frontend with user info and role as query params.
- Added LTI consumer key/secret to `settings.py` (now loaded from `.env`).
- Included `authentication.urls` in main `urls.py`.
- Installed and configured `django-environ` to load environment variables from `.env`.
- Created `.env` file for backend with all sensitive and environment-specific settings.
- Ran all Django migrations to set up the database.

### 2. Nuxt Frontend Setup

- Created Nuxt 3 project structure with Vuetify.
- Implemented `/auth/lti` page to handle LTI login redirect, store user info in localStorage, and redirect to dashboard.
- Updated student and teacher dashboards to display user name, role, and user ID from localStorage.
- Added `.env` file for frontend to store API and LTI redirect URLs.
- Updated `nuxt.config.ts` to use runtimeConfig and load from `.env`.

### 3. Moodle LTI Integration

- Configured Moodle as LTI consumer:
  - Added external tool in Moodle site admin (Manage tools).
  - Set Tool/Launch URL to `http://127.0.0.1:8000/auth/lti/launch/` (or production URL).
  - Set consumer key/secret to match backend `.env`.
  - Set launch container to "New window" for best UX.
- Added the external tool to a course for testing.
- Verified LTI launch flow: Moodle POSTs to Django, Django redirects to Nuxt, Nuxt displays correct dashboard and user info.

---

## Next Steps (Checklist)

- [ ] **Productionize Django:**
  - Use Gunicorn or uWSGI instead of `runserver`.
  - Set `DEBUG=False` and configure `ALLOWED_HOSTS` in `.env`.
  - Serve static files with `python manage.py collectstatic` and a web server (e.g., Nginx).
- [ ] **Productionize Nuxt:**
  - Run `npm run build` and `npm run generate` for static output, or `npm run start` for SSR.
  - Serve built files with Nginx/Apache or Node.js.
- [ ] **Update Redirect URLs for Production:**
  - Change LTI redirect in Django to point to production Nuxt URL.
  - Update `.env` files for both backend and frontend with production domains.
- [ ] **Secure Deployment:**
  - Use HTTPS for both backend and frontend.
  - Set secure cookies and CORS as needed.
- [ ] **Moodle Privacy Settings:**
  - Ensure Moodle external tool is set to share user name/email if needed.
- [ ] **(Optional) User Sessions:**
  - Implement persistent sessions or JWT tokens for deeper integration.
- [ ] **(Optional) Advanced Features:**
  - Integrate with Moodle API for course/user management if required.

---

## Quick Start (Development)

1. **Backend:**
   ```sh
   cd backend-django
   pip install -r requirements.txt  # or manually install dependencies
   python manage.py migrate
   python manage.py runserver
   ```
2. **Frontend:**
   ```sh
   cd frontend-nuxt
   npm install
   npm run dev
   ```
3. **Moodle:**
   - Add the external tool to a course and test the LTI launch.

---

## Notes

- All environment-specific settings are now in `.env` files for both backend and frontend.
- LTI authentication is only possible via the Moodle external tool launch, not by direct link.
- For production, update all URLs and secrets in `.env` and use production servers.

---

For any further setup or deployment help, see the checklist above or ask for a step-by-step deployment guide!
