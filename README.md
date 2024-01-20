# blogs_redberry

API for managing blogs and categories. This API allows you to perform CRUD operations on blogs and categories. Explore the documentation to understand the available endpoints and their functionalities.

## Endpoints

- **GET /blogs/**
  - List all blogs.

- **GET /blogs/{id}/**
  - Retrieve details of a specific blog.

- **POST /blogs/**
  - Create a new blog.

- **GET /categories/**
  - List all categories.

- **POST /login/**
  - Authenticate a user and get a token.

## Authentication

- The API supports token-based authentication.
- To authenticate, make a POST request to `/login/` with a valid email.
- Include the token in the Authorization header for subsequent authenticated requests.

## Documentation

- Explore the API using Swagger UI: [/swagger/]
- View API documentation in ReDoc: [/redoc/]

## Getting Started

1. Clone the repository.
2. Set up your Python environment.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the development server: `python manage.py runserver`.

## Dependencies

- Django
- Django Rest Framework
- Django Filters

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.
