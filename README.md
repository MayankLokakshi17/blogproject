# Django Blog Project (ready-to-run)

## Quick setup (inside project folder)

1. Create virtual environment:
   - `python -m venv .venv`
   - Activate: Windows `.venv\Scripts\activate`  or macOS/Linux `source .venv/bin/activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

3. Run initial migrations:
   - `python manage.py migrate`

4. Create superuser (for admin):
   - `python manage.py createsuperuser`

5. Run server:
   - `python manage.py runserver`

Open http://127.0.0.1:8000/ in your browser.

This scaffold contains a simple `blog` app with Post model, list/detail views,
create/edit form, admin registration, and basic templates.
