class MenuManager:
    def get_by_name(self, conn, item_name):
        query = "SELECT * FROM Menu_Items WHERE item_name = %s"
        try:
            with conn.cursor() as cur:
                cur.execute(query, (item_name,))
                return cur.fetchone()
        except Exception as e:
            print(f"Error retrieving menu item: {e}")
            return None

    def all_items(self, conn):
        query = "SELECT * FROM Menu_Items"
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        except Exception as e:
            print(f"Error retrieving all menu items: {e}")
            return []