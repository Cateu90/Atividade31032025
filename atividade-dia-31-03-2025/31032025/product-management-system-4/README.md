# Product Management System

This project is a simple product management system that allows users to manage products through a console interface. It supports basic CRUD (Create, Read, Update, Delete) operations for product management.

## Project Structure

```
product-management-system
├── src
│   ├── main.py                # Entry point of the application
│   ├── models
│   │   └── produto.py         # Defines the Produto model
│   ├── repositories
│   │   └── produto_repo.py     # Implements CRUD operations for Produto
│   ├── services
│   │   └── produto_service.py   # Contains business logic related to products
│   ├── utils
│   │   └── __init__.py        # Initialization file for utils module
│   └── views
│       └── menu.py            # Displays menu options and handles user input
├── requirements.txt            # Lists project dependencies
└── README.md                   # Documentation for the project
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

- Upon running the application, you will be presented with a menu to choose from various options to manage products.
- You can add new products, list existing products, update product details, and delete products.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.