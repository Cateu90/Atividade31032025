# main.py

import sys
from database.db_connection import DatabaseConnection
from services.product_service import ProductRepo
from models.product import Product

def display_menu():
    print("\nProduct Management System")
    print("1. Add Product")
    print("2. View Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

def main():
    db_connection = DatabaseConnection('products.db')
    product_repo = ProductRepo(db_connection)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            product = Product(name=name, description=description, price=price)
            product_repo.create_product(product)
            print("Product added successfully.")

        elif choice == '2':
            product_id = int(input("Enter product ID to view: "))
            product = product_repo.get_product(product_id)
            if product:
                print(product)
            else:
                print("Product not found.")

        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            description = input("Enter new product description: ")
            price = float(input("Enter new product price: "))
            product = Product(id=product_id, name=name, description=description, price=price)
            product_repo.update_product(product)
            print("Product updated successfully.")

        elif choice == '4':
            product_id = int(input("Enter product ID to delete: "))
            product_repo.delete_product(product_id)
            print("Product deleted successfully.")

        elif choice == '5':
            print("Exiting the program.")
            db_connection.close()
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()