## Overview
The Blog project is a simple Django-based application designed to manage and display blog posts. It follows a clean architecture approach to ensure scalability, maintainability, and separation of concerns.

## Features
- Create, read, update, and delete blog posts.
- Modular design for easy extension.
- Separation of business logic, domain entities, and infrastructure.

## Architecture
The project is structured using the Clean Architecture principles, which emphasize the separation of concerns and independence of frameworks and tools. The main layers of the architecture are:

1. **Domain Layer**:
   - Located in `src/blog/domain`.
   - Contains the core business logic and domain entities.
   - Example: `post_entity.py` defines the `Post` entity.

2. **Application Layer**:
   - Located in `src/blog/application`.
   - Contains use cases that orchestrate the business logic.
   - Example: `usecases.py` implements application-specific workflows.

3. **Infrastructure Layer**:
   - Located in `src/blog/infrastructure`.
   - Contains Django models, admin configurations, and repository implementations.
   - Example: `models.py` defines the database schema for posts.

4. **Interface Layer**:
   - Located in `src/blog/interface`.
   - Contains serializers, views, and URL configurations for interacting with the application.
   - Example: `views.py` handles HTTP requests and responses.

## Design Patterns
The project employs several design patterns to ensure clean and maintainable code:

- **Repository Pattern**:
  - Abstracts data access logic.
  - Example: `post_repository.py` in the domain layer and `repositories_django.py` in the infrastructure layer.

- **Entity-Use Case Separation**:
  - Keeps domain entities independent of application workflows.

- **Modularization**:
  - Each layer is organized into separate modules for better separation of concerns.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mohamad-bigdeli/Blog.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

