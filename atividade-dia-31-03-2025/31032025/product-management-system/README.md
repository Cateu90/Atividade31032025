# Product Management System

This project is a simple console-based product management system that allows users to perform CRUD (Create, Read, Update, Delete) operations on products using an SQLite database. The system is built with Python and utilizes Pydantic for data validation.

## Features

- Add new products with details such as name, description, and price.
- Retrieve product information by ID.
- Update existing product details.
- Delete products from the database.
- Input validation to ensure data integrity.

## Project Structure

```
product-management-system
├── src
│   ├── main.py                # Entry point for the console application
│   ├── database
│   │   └── db_connection.py    # Database connection management
│   ├── models
│   │   └── product.py          # Product model with Pydantic validation
│   ├── services
│   │   └── product_service.py   # Service layer for product CRUD operations
│   ├── utils
│   │   └── validators.py        # Input validation utilities
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files and directories to ignore in version control
└── README.md                   # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd product-management-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

Upon running the application, you will be presented with a menu that allows you to choose from various options to manage products. Follow the prompts to add, view, update, or delete products.

## License

This project is licensed under the MIT License.