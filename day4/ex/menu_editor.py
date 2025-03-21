import psycopg2
from menu_item import MenuItem

def show_user_menu(conn):
    while True:
        print("\nRestaurant Menu Editor")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == "V":
            view_item(conn)
        elif choice == "A":
            add_item_to_menu(conn)
        elif choice == "D":
            remove_item_from_menu(conn)
        elif choice == "U":
            update_item_from_menu(conn)
        elif choice == "S":
            show_restaurant_menu(conn)
        elif choice == "E":
            show_restaurant_menu(conn)
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu(conn):
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    
    item = MenuItem(name, price)
    item.save(conn)
    print("Item was added successfully.")

def remove_item_from_menu(conn):
    name = input("Enter item name to delete: ").strip()
    
    item = MenuItem(name, 0) 
    item.delete(conn)
    print("Item was deleted successfully.")

def update_item_from_menu(conn):
    name = input("Enter item name to update: ").strip()
    new_name = input("Enter new name (leave blank to keep the same): ").strip()
    new_price = input("Enter new price (leave blank to keep the same): ")
    
    new_price = float(new_price) if new_price else None
    
    item = MenuItem(name, 0) 
    item.update(conn, new_name if new_name else None, new_price)
    print("Item was updated successfully.")

def show_restaurant_menu(conn):
    query = "SELECT name, price FROM Menu_Items"
    with conn.cursor() as cur:
        cur.execute(query)
        items = cur.fetchall()
        
        print("\nRestaurant Menu:")
        for name, price in items:
            print(f"- {name}: ${price:.2f}")

def view_item(conn):
    name = input("Enter item name to view: ").strip()
    query = "SELECT name, price FROM Menu_Items WHERE name = %s"
    with conn.cursor() as cur:
        cur.execute(query, (name,))
        item = cur.fetchone()
        
        if item:
            print(f"\nItem: {item[0]}, Price: ${item[1]:.2f}")
        else:
            print("Item not found.")

if __name__ == "__main__":
    HOSTNAME = 'localhost'
    USERNAME = 'superuser'
    PASSWORD = 'aza'
    DATABASE = 'newdb'
    conn = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    
    show_user_menu(conn)
    conn.close()
