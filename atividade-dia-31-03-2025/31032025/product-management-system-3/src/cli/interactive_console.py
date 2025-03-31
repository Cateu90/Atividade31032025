# interactive_console.py

import sys
from services.product_service import ProductRepo
from models.product import Product
from utils.validators import validate_product_data

def display_menu():
    print("\nProduct Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

def main():
    product_repo = ProductRepo()

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            product_data = {"name": name, "price": price, "stock": stock}

            if validate_product_data(product_data):
                product = Product(**product_data)
                product_repo.create_product(product)
                print("Product added successfully.")
            else:
                print("Invalid product data.")

        elif choice == '2':
            products = product_repo.get_all_products()
            for product in products:
                print(product)

        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            stock = int(input("Enter new product stock: "))
            product_data = {"id": product_id, "name": name, "price": price, "stock": stock}

            if validate_product_data(product_data):
                product = Product(**product_data)
                product_repo.update_product(product)
                print("Product updated successfully.")
            else:
                print("Invalid product data.")

        elif choice == '4':
            product_id = int(input("Enter product ID to delete: "))
            product_repo.delete_product(product_id)
            print("Product deleted successfully.")

        elif choice == '5':
            print("Exiting the application.")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()