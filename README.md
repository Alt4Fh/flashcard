[![Open in Codeanywhere](https://codeanywhere.com/img/open-in-codeanywhere-btn.svg)](https://app.codeanywhere.com/#https://github.com/Codeanywhere-Templates/django)

This is a template project for Django web applications in [Codeanywhere](https://codeanywhere.com/). [Try it out](https://app.codeanywhere.com/#https://github.com/Codeanywhere-Templates/django)

## Getting Started

When you first open this template, you can run your Django development server with:

```bash
cd test_project
python manage.py runserver 0.0.0.0:8000
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## Features

- Development container for Django web applications
- Pre-installed Django and essential packages
- PostgreSQL client for database connectivity
- Code formatting and linting tools (Black, Flake8, Pylint)
- VS Code extensions for Django development
- Fast development-to-preview workflow

## Project Structure

This template project has the following structure:

```
test_project/
├── core/                  # A basic Django app
│   ├── migrations/        # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py            # URL routing for the app
│   └── views.py           # View functions/classes
├── test_project/          # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md              # Project README
```

## Learn More

To learn more about Django, take a look at the following resources:

- [Django Documentation](https://docs.djangoproject.com/) - learn about Django features and API
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) - create your first Django app
- [Django REST Framework](https://www.django-rest-framework.org/) - build APIs with Django
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/) - debug and analyze your Django apps

## Want to contribute?


Feel free to [open a PR](https://github.com/Codeanywhere-Templates/django) with any suggestions for this template project 😃
