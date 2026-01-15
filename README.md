# Cake Bot

A Django-based application for managing cake orders with bot integration.

## Features

- **Order Management**: Create and track cake orders
- **Cake Catalog**: Browse and manage cake products with categories and sizes
- **Ingredient Tracking**: Track ingredients used in cakes
- **Bot Integration**: Automated bot for order processing
- **User Addresses**: Store and manage customer delivery addresses
- **Order Status Tracking**: Monitor order status from placement to delivery

## Project Structure

```
cake_bot/
├── cake/                    # Main application
│   ├── models.py           # Database models (Order, Cake, Category, Size, etc.)
│   ├── views.py            # View handlers
│   ├── bot.py              # Bot functionality
│   ├── admin.py            # Django admin configuration
│   ├── utils.py            # Utility functions
│   ├── tests.py            # Unit tests
│   └── migrations/         # Database migrations
├── cake_bot/               # Django project settings
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   ├── asgi.py             # ASGI configuration
│   ├── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
└── media/                  # Media files storage
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Database Models

- **Cake**: Cake products with size and ingredients
- **CakeCategory**: Categories for organizing cakes
- **Size**: Available cake sizes
- **Ingredient**: Cake ingredients inventory
- **Order**: Customer orders with status tracking
- **OrderElement**: Individual items in an order

## Usage

Access the Django admin interface at `http://localhost:8000/admin` to manage cakes, orders, and other data.

