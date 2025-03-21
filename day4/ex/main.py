from menu_item import MenuItem
from menu_manager import MenuManager
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'superuser'
PASSWORD = 'aza'
DATABASE = 'newdb'

try:
    # Connect to the database
    conn = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    
    # Create a menu item and perform operations
    item = MenuItem('Burger', 35)
    item.save(conn)
    item.delete(conn)
    
    # Create a new item and update it
    new_item = MenuItem('Veggie Burger', 35)
    new_item.save(conn)
    new_item.update(conn, new_price=37)
    
    # Use the menu manager to retrieve items
    manager = MenuManager()
    item2 = manager.get_by_name(conn, 'Beef Stew')
    if item2:
        print(f"Found: {item2}")
    else:
        print("Item 'Beef Stew' not found")
    
    # Get all items
    items = manager.all_items(conn)
    print(f"Total menu items: {len(items)}")
    for i, menu_item in enumerate(items, 1):
        print(f"{i}. {menu_item}")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection
    if 'conn' in locals() and conn:
        conn.close()
        print("Database connection closed")