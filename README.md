# CountryModel - Django Project

A Django REST Framework API project that implements CRUD operations for `Country`, `User`, and `Blog` models. It also includes JWT authentication for secure access to the API.

 # Project Structure

The project is divided into several files and directories:

countrymodel/ ├── app/ # The main Django app containing models, views, serializers, etc.
│ ├── admin.py # Admin configurations to manage models in Django Admin │ 
├── apps.py # App configuration │
├── models.py # Database models (Country, User, Blog) │
├── serializers.py # Serializers to convert model instances to JSON │
├── views.py # Views to handle API requests │
├── urls.py # API routes for different endpoints (Country, Blog, User) │ 
└── filters.py # Filters for querying Country, Blog, User models 
├── countrymodel/ # Project settings │ 
├── init.py # Python package indicator │ 
├── settings.py # Django settings including database, installed apps, and JWT configuration │
├── urls.py # Root URL configurations │ 
├── wsgi.py # WSGI application entry point for deployments │ 
└── asgi.py # ASGI application entry point (for asynchronous server support) 
├── manage.py # Command-line utility to manage the Django project 
└── db.sqlite3 # SQLite database file (default, can be changed in settings)

## Requirements

Make sure you have the following installed

- Python 3.x
- Django 5.x
- Django REST Framework
- Django SimpleJWT
- Django Filters

You can install the dependencies using `pip`

```bash
pip install -r requirements.txt

Setting Up the Project
Clone the repository

git clone <repository_url>
cd countrymodel

Install dependencies:

Copy code
pip install -r requirements.txt

Make sure to apply database migrations

Copy code
python manage.py migrate

Create a superuser to access the Django Admin

Copy code
python manage.py createsuperuser

The server will be accessible at http://127.0.0.1:8000.

# API Endpoints

Authentication
POST /api/auth/register/ - Register a new user
POST /api/auth/login/ - Login and obtain JWT tokens (access & refresh)
POST /api/auth/token/refresh/ - Refresh the JWT access token using the refresh token
POST /api/auth/token/verify/ - Verify the JWT token
POST /api/auth/logout/ - Logout (blacklist the refresh token).

Country Endpoints
GET /api/countries/ - List all countries
POST /api/countries/ - Create a new country
GET /api/countries/{id}/ - Retrieve details of a specific country
PUT /api/countries/{id}/ - Update a country
DELETE /api/countries/{id}/ - Delete a country.

Blog Endpoints
GET /api/blogs/ - List all blogs
POST /api/blogs/ - Create a new blog (authentication required)
GET /api/blogs/{id}/ - Retrieve details of a specific blog
PUT /api/blogs/{id}/ - Update a blog
DELETE /api/blogs/{id}/ - Delete a blog.

User Endpoints
GET /api/users/ - List all users
POST /api/users/ - Create a new user
GET /api/users/{id}/ - Retrieve details of a specific user
PUT /api/users/{id}/ - Update a user
DELETE /api/users/{id}/ - Delete a user.

Features
JWT Authentication: Secures API endpoints with token-based authentication.
Filtering: Filters are implemented for Country, Blog, and User models using django_filters.
Expanding Related Data: The expand query parameter can be used to include related data in API responses (e.g., fetching Country details with User data).
Custom User Model: A custom User model with additional fields like date_of_birth and bio.


Here’s an example of a README.md file that explains your project structure and how to run the application:

markdown
Copy code
# CountryModel - Django Project

A Django REST Framework API project that implements CRUD operations for `Country`, `User`, and `Blog` models. It also includes JWT authentication for secure access to the API.

## Project Structure

The project is divided into several files and directories:

countrymodel/ ├── app/ # The main Django app containing models, views, serializers, etc. │ ├── admin.py # Admin configurations to manage models in Django Admin │ ├── apps.py # App configuration │ ├── models.py # Database models (Country, User, Blog) │ ├── serializers.py # Serializers to convert model instances to JSON │ ├── views.py # Views to handle API requests │ ├── urls.py # API routes for different endpoints (Country, Blog, User) │ └── filters.py # Filters for querying Country, Blog, User models ├── countrymodel/ # Project settings │ ├── init.py # Python package indicator │ ├── settings.py # Django settings including database, installed apps, and JWT configuration │ ├── urls.py # Root URL configurations │ ├── wsgi.py # WSGI application entry point for deployments │ └── asgi.py # ASGI application entry point (for asynchronous server support) ├── manage.py # Command-line utility to manage the Django project └── db.sqlite3 # SQLite database file (default, can be changed in settings)

markdown
Copy code

## Requirements

Make sure you have the following installed:

- Python 3.x
- Django 5.x
- Django REST Framework
- Django SimpleJWT
- Django Filters

You can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
Setting Up the Project
Clone the repository:
bash
Copy code
git clone <repository_url>
cd countrymodel
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Make sure to apply database migrations:
bash
Copy code
python manage.py migrate
Create a superuser to access the Django Admin:
bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the superuser.

Run the development server:
bash
Copy code
python manage.py runserver
The server will be accessible at http://127.0.0.1:8000.

API Endpoints
Authentication
POST /api/auth/register/ - Register a new user.
POST /api/auth/login/ - Login and obtain JWT tokens (access & refresh).
POST /api/auth/token/refresh/ - Refresh the JWT access token using the refresh token.
POST /api/auth/token/verify/ - Verify the JWT token.
POST /api/auth/logout/ - Logout (blacklist the refresh token).
Country Endpoints
GET /api/countries/ - List all countries.
POST /api/countries/ - Create a new country.
GET /api/countries/{id}/ - Retrieve details of a specific country.
PUT /api/countries/{id}/ - Update a country.
DELETE /api/countries/{id}/ - Delete a country.
Blog Endpoints
GET /api/blogs/ - List all blogs.
POST /api/blogs/ - Create a new blog (authentication required).
GET /api/blogs/{id}/ - Retrieve details of a specific blog.
PUT /api/blogs/{id}/ - Update a blog.
DELETE /api/blogs/{id}/ - Delete a blog.
User Endpoints
GET /api/users/ - List all users.
POST /api/users/ - Create a new user.
GET /api/users/{id}/ - Retrieve details of a specific user.
PUT /api/users/{id}/ - Update a user.
DELETE /api/users/{id}/ - Delete a user.
Features
JWT Authentication: Secures API endpoints with token-based authentication.
Filtering: Filters are implemented for Country, Blog, and User models using django_filters.
Expanding Related Data: The expand query parameter can be used to include related data in API responses (e.g., fetching Country details with User data).
Custom User Model: A custom User model with additional fields like date_of_birth and bio.
Testing
You can write unit tests for your views and models. You can test the API with tools like Postman or curl by interacting with the endpoints.

