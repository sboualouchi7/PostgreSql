import psycopg2


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = 'root'
    DATABASE = 'itemsdb'
    PORT = '5432'
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()


def save(self, connection):

    query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)"
    values = (self.name, self.price)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
        print(f"Item '{self.name}' saved successfully.")
    except Exception as error:
        connection.rollback()
        print(f"Error saving item: {error}")


def delete(self, connection):

    query = "DELETE FROM Menu_Items WHERE item_name = %s"
    values = (self.name,)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
        print(f"Item '{self.name}' deleted successfully.")
    except Exception as error:
        connection.rollback()
        print(f"Error deleting item: {error}")


def update(self, connection, new_name=None, new_price=None):

    updates = []
    values = []
    if new_name:
        updates.append("item_name = %s")
        values.append(new_name)
        self.name = new_name

    if new_price is not None:
        updates.append("item_price = %s")
        values.append(new_price)
        self.price = new_price

    if not updates:
        print("No updates provided.")
        return

    original_name = self.name if not new_name else new_name
    values.append(original_name)

    query = f"UPDATE Menu_Items SET {', '.join(updates)} WHERE item_name = %s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
        print("Item updated successfully.")
    except Exception as error:
        connection.rollback()
        print(f"Error updating item: {error}")

