# POS System - Django Project

A Point of Sale system built with Django, using the SB Admin Bootstrap template for the frontend.

## Setup Complete ✓

The Django project has been successfully set up with:

- Django 5.1.2 installed in virtual environment
- Project name: `pos_system`
- Landing page configured using SB Admin template
- Templates and static files properly configured

## Project Structure

```
point-of-sale-sysetm/
├── .venv/                          # Python virtual environment
├── pos_system/                     # Django project settings
│   ├── settings.py                 # Project settings
│   ├── urls.py                     # URL routing
│   ├── views.py                    # View functions
│   └── wsgi.py
├── startbootstrap-sb-admin-gh-pages/  # Bootstrap template
│   ├── index.html                  # Landing page (with Django static tags)
│   ├── assets/                     # Images and demo files
│   ├── css/                        # Stylesheets
│   └── js/                         # JavaScript files
├── manage.py                       # Django management script
└── db.sqlite3                      # SQLite database
```

## Running the Server

To start the development server:

```bash
"E:/project/POS Django/point-of-sale-sysetm/.venv/Scripts/python.exe" manage.py runserver
```

Then visit: **http://127.0.0.1:8000/**

## Features Configured

- ✓ Landing page route (`/`) renders the SB Admin dashboard template
- ✓ Django static files configured for CSS, JavaScript, and assets
- ✓ Template directory points to the bootstrap template folder
- ✓ Database migrations applied
- ✓ Development server running

## Next Steps

You can now:

1. Create additional Django apps for different POS modules
2. Add database models for products, sales, inventory, etc.
3. Configure user authentication
4. Customize the template pages for your specific needs
5. Add more views and URL routes

## Development Commands

```bash
# Run development server
python manage.py runserver

# Create a new Django app
python manage.py startapp <app_name>

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```
