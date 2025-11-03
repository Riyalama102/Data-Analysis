import json
import os

# File Handling Functions
def load_products():
    products = []
    try:
        if not os.path.exists("product.txt"):
            return []
        file = open("product.txt", "r")
        try:
            for line in file:
                if line.strip():
                    products.append(json.loads(line))
        except Exception as e:
            print("Error reading file:", e)
        finally:
            file.close()
    except Exception as e:
        print("Error opening file:", e)
    return products


def save_products(products):
    try:
        file = open("product.txt", "w")
        try:
            for p in products:
                file.write(json.dumps(p) + "\n")
        except Exception as e:
            print("Error writing file:", e)
        finally:
            file.close()
    except Exception as e:
        print("Error opening file:", e)



# E-Commerce Operations

def add_product():
    try:
        products = load_products()
        pid = "p" + str(len(products) + 1)
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price (in Rs): "))
        qty = int(input("Enter product quantity: "))

        product = {"id": pid, "name": name, "price": price, "quantity": qty}
        products.append(product)
        save_products(products)
        print("Product added successfully!")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print("Error adding product:", e)


def view_products():
    try:
        products = load_products()
        if not products:
            print("No products found!")
            return
        print("\nID\tName\t\tPrice (Rs)\tQuantity")
        for p in products:
            print(p["id"], "\t", p["name"], "\t", "Rs", p["price"], "\t", p["quantity"])
    except Exception as e:
        print("Error viewing products:", e)


def remove_product():
    try:
        products = load_products()
        pid = input("Enter product ID to remove: ").strip()
        found = False
        for p in products:
            if p["id"] == pid:
                products.remove(p)
                save_products(products)
                print("Product removed successfully!")
                found = True
                break
        if not found:
            print("Product not found.")
    except Exception as e:
        print("Error removing product:", e)


def search_product():
    try:
        products = load_products()
        term = input("Enter name to search: ").lower()
        found = [p for p in products if term in p["name"].lower()]
        if not found:
            print("No product found.")
            return
        print("\nID\tName\t\tPrice (Rs)\tQuantity")
        for p in found:
            print(p["id"], "\t", p["name"], "\t", "Rs", p["price"], "\t", p["quantity"])
    except Exception as e:
        print("Error searching product:", e)


# Main Menu
def main():
    while True:
        print("\nE-Commerce Menu")
        print("1. Add Product")
        print("2. View Products")
        print("3. Remove Product")
        print("4. Search Product")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                add_product()
            elif choice == "2":
                view_products()
            elif choice == "3":
                remove_product()
            elif choice == "4":
                search_product()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
