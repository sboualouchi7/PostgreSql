import psycopg2

class MenuItem:
    def __init__(self, item_name: str, item_price: float):
        self.item_name = item_name
        self.item_price = item_price

    def save(self, conn):
        query = "INSERT INTO Menu_Items(item_name, item_price) VALUES (%s, %s)"
        values = (self.item_name, self.item_price)
        try:
            with conn.cursor() as cur:
                cur.execute(query, values)
                conn.commit()
            print(f"Item '{self.item_name}' saved successfully")
        except Exception as e:
            conn.rollback()
            print(f"Error saving item: {e}")

    def delete(self, conn):
        query = "DELETE FROM Menu_Items WHERE item_name = %s"
        values = (self.item_name,)
        try:
            with conn.cursor() as cur:
                cur.execute(query, values)
                conn.commit()
            print(f"Item '{self.item_name}' deleted successfully")
        except Exception as e:
            conn.rollback()
            print(f"Error deleting item: {e}")

    def update(self, conn, new_name=None, new_price=None):
        updates = []
        values = []

        if new_name:
            updates.append("item_name = %s")
            values.append(new_name)
            old_name = self.item_name
            self.item_name = new_name

        if new_price is not None:
            updates.append("item_price = %s")
            values.append(new_price)
            self.item_price = new_price

        if not updates:
            return
        
        original_name = old_name if new_name else self.item_name
        query = f"UPDATE Menu_Items SET {', '.join(updates)} WHERE item_name = %s"
        values.append(original_name)

        try:
            with conn.cursor() as cur:
                cur.execute(query, values)
                conn.commit()
            print(f"Item updated successfully")
        except Exception as e:
            conn.rollback()
            print(f"Error updating item: {e}")