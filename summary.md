## People_Management
- Manages a list of people.
- Provides authentication and authorization features.
- Allows superusers to add and remove people.
- Includes user registration and login functionality.

# Conceptual Summary of the Django Application

## Django
- High-level web framework for Python.
- Follows the MVT (Model-View-Template) architecture.

## MVT Architecture
- **Model**: Represents the data structure. Interacts with the database.
- **View**: Handles the logic of the application. Processes requests and returns responses.
- **Template**: Defines the structure and layout of the web pages. Uses Django's template language to dynamically insert data.

## Models
- Represent the data structure.
- Defined as Python classes.
- Mapped to database tables.
- Example: `People` model with `name` and `surname` fields.

## ORM (Object-Relational Mapping)
- Interacts with the database using Python objects.
- Simplifies data manipulation without writing SQL queries.

## Authentication and Superuser
- Built-in authentication system.
- Superuser has full administrative privileges.
- Created using `createsuperuser` command or Django shell.

## Views
- Handle the application logic.
- Receive HTTP requests and return HTTP responses.
- Can be function-based or class-based.
- Examples: `people_list`, `SignUpView`.

## Templates
- HTML files that define the structure of web pages.
- Use Django's template language to dynamically insert data.
- Example: `list.html`.

## URL Configuration
- Maps URLs to corresponding views.
- Defines which views should be called for specific URLs.
- Example: `urls.py`.

## Configuration File (`settings.py`)
- Contains all project configurations.
- Database settings, installed apps, middleware, etc.
- Example: Authentication settings (`LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`).


