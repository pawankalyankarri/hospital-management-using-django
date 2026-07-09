# Hospital Management System (Django)

A web application built with **Django** that lets a hospital's website visitors browse medical specialties, view doctors, and book an appointment slot with a doctor online — all through a simple, form-based interface. It also includes an admin panel to manage doctors and patient records.

This project was built as a learning/portfolio project to practice full end-to-end Django development: models, views, URL routing, templates, forms, and sessions.

---

## What This Project Does

Think of it as a mini version of a hospital's appointment-booking website:

1. **Home Page** – Shows the hospital's specialties (cardiology, neurology, orthopedics, etc.), a preview of doctors, and patient video testimonials.
2. **Patient Registration ("Patientop")** – A visitor fills in their name, age, gender, address, mobile number, and describes their problem (e.g. "chest pain"). The system automatically matches the described problem to a medical specialty (e.g. cardiology) and assigns the patient to a doctor from that specialty at random.
3. **Our Doctors** – Lists all doctors registered in the system, along with their specialty, gender, age, and photo.
4. **Add Doctor** – An internal-facing page (e.g. for hospital staff) to add a new doctor. When a doctor is added, the system automatically generates 15 appointment time slots for that doctor based on a starting time.
5. **Book an Appointment** – A patient picks a doctor and disease type, then selects an available time slot and date. The app checks whether that slot is already booked for the chosen date, and if free, books it and shows a success/confirmation page.
6. **Login Page** – A basic staff/employee login form (currently accepts input but doesn't yet validate credentials against the database — see [Known Limitations](#known-limitations--things-to-improve)).
7. **Admin Panel** – Django's built-in admin site is enabled for managing `Doctors`, `Patients`, and `Doc_slots` records directly.

---

## How It Works (Under the Hood)

The project follows Django's standard **MVT (Model–View–Template)** pattern, split into two Django "apps":

| App | Responsibility |
|---|---|
| `homepage` | The main patient-facing hospital site: home page, doctor listings, patient registration, appointment booking, and the booking success page. |
| `loginpage` | A simple login page for hospital employees. |

### Data Models (`homepage/models.py`)

- **`Doctors`** – Stores each doctor's name, specialty, gender, mobile number, age, and photo.
- **`Doc_slots`** – Stores 15 fixed time slots (`slot1`–`slot15`) generated for a specific doctor.
- **`SlotsAppointments`** – Tracks, per doctor and per date, whether each of the 15 slots is `"booked"` or free.
- **`Patients`** – Stores patient details and links each patient to the doctor they were assigned.

`loginpage/models.py` also defines an **`Employees`** model for hospital staff (name, gender, mobile, username, password), though the login view doesn't check against it yet.

### The Appointment-Booking Flow

1. **Symptom Specialty matching**: In `homepage/views.py`, a set of Python lists (`cardiology`, `neurology`, `dermatology`, etc.) map common symptoms/diseases to a medical specialty.
2. **Doctor assignment**: When a patient submits their problem, the app looks up which specialty list their symptom belongs to, filters doctors in that specialty, and picks one **at random**.
3. **Slot generation**: When a doctor is added, `generate_slots()` builds 15 appointment times starting from the doctor's given start time (20-minute intervals, with a break built in).
4. **Booking a slot**: When a patient selects a date and time, the app checks the `SlotsAppointments` table for that doctor/date combination. If the chosen slot is already `"booked"`, the patient is redirected back to pick another time. Otherwise, the slot is marked as booked and the appointment details are temporarily stored in the **Django session**, then shown on a confirmation ("Appointment Success") page.

### URL Routing

- `HospitalManagement/urls.py` — the project's main router. It sends:
 - `/admin/` Django admin
 - `/login/` the `loginpage` app
 - `/` (everything else) the `homepage` app
- `homepage/urls.py` — routes for home, doctor registration, appointments, doctor list, doctor slots, and the success page.
- `loginpage/urls.py` — the single login route.

### Templates

All HTML templates live in a shared `Templates/` folder (not inside each app), organized into:
- `Templates/home/` — home page, doctor pages, appointment & registration forms.
- `Templates/login/` — the login form.
- `Templates/messages/` — the appointment success page.
- `Templates/base.html` — a shared base layout other pages extend.

### Static & Media Files

- `static/` — CSS, JS, and images used across the site (hospital photos, specialty icons, etc.).
- `media/images/` — doctor profile photos, uploaded via the "Add Doctor" form and served through Django's media file handling.

---

## Project Structure

```
hospital-management-using-django/
├── HospitalManagement/ # Django project settings, main URLs, WSGI/ASGI config
├── homepage/ # Main app: doctors, patients, appointments
│ ├── models.py # Doctors, Doc_slots, SlotsAppointments, Patients
│ ├── views.py # Business logic (home, booking, doctor mgmt)
│ ├── urls.py
│ └── migrations/
├── loginpage/ # Simple staff login app
│ ├── models.py # Employees model
│ ├── views.py
│ └── urls.py
├── Templates/ # All HTML templates (shared across apps)
├── static/ # CSS/JS/images
├── media/ # User-uploaded doctor photos
├── manage.py # Django's command-line utility
├── package.json # Front-end dependency (Bootstrap Icons)
└── db.sqlite3 # (present in repo, though MySQL is configured — see below)
```

---

## Tech Stack

- **Backend:** Python, Django 5.2
- **Database:** MySQL (configured in `settings.py`)
- **Frontend:** Django Templates, HTML, CSS, JavaScript, Bootstrap Icons
- **Other:** Django's built-in Admin, Sessions framework, and media file handling

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/pawankalyankarri/hospital-management-using-django.git
cd hospital-management-using-django
```

### 2. Create a virtual environment & install Django
```bash
python -m venv venv
source venv/bin/activate # on Windows: venv\Scripts\activate
pip install django mysqlclient
```

### 3. Set up the database
The project is currently configured to use **MySQL** (see `HospitalManagement/settings.py`). Create a database named `hospitaldj` in your local MySQL server, and update the `USER`/`PASSWORD`/`HOST` fields in `settings.py` to match your own MySQL credentials.

> If you'd rather not set up MySQL, you can switch the `DATABASES` setting to SQLite for a quick local run:
> ```python
> DATABASES = {
> 'default': {
> 'ENGINE': 'django.db.backends.sqlite3',
> 'NAME': BASE_DIR / 'db.sqlite3',
> }
> }
> ```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create an admin user (optional, to access `/admin/`)
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser

---

## Known Limitations / Things to Improve

This project is a great learning base, but a few things are worth knowing if you plan to extend it:

- **Login isn't wired up yet** — the login form accepts submissions but doesn't verify them against the `Employees` table.
- **Hardcoded secrets** — the `SECRET_KEY` and MySQL password are committed directly in `settings.py`. Before deploying anywhere public, move these into environment variables.
- **`DEBUG = True`** — fine for local development, but must be turned off (and `ALLOWED_HOSTS` set) before any real deployment.
- **No automated tests** yet (the `tests.py` files are currently empty placeholders).
- **`node_modules/`** is committed to the repo — usually best to add this to `.gitignore` since it can be regenerated from `package.json`.

---

## Contributing

This is a personal/learning project, but suggestions and pull requests are welcome if you'd like to help improve it (e.g. wiring up authentication, adding tests, or improving the UI).

