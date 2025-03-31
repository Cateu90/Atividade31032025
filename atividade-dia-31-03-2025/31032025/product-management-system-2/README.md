# Product Management System

This project is a simple product management system built using Python and SQLite. It allows users to perform CRUD (Create, Read, Update, Delete) operations on product data through an interactive console interface.

## Project Structure

```
product-management-system
├── src
│   ├── main.py                  # Entry point of the application
│   ├── database
│   │   └── db_connection.py      # Database connection management
│   ├── models
│   │   └── product.py            # Product model with data validation
│   ├── services
│   │   └── product_service.py     # CRUD operations for products
│   ├── utils
│   │   └── validators.py          # Custom validation functions
│   └── cli
│       └── interactive_console.py  # Interactive console interface
├── requirements.txt              # Project dependencies
├── .env                           # Environment variables
└── README.md                      # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd product-management-system
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your database connection settings.

## Usage

To start the application, run the following command:

```
python src/main.py
```

Follow the on-screen instructions to manage your products. You can add, view, update, and delete products through the interactive console. 

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project.