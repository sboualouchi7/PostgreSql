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

    def save(self,TableName: str, name: str, price: float):
        query = f"INSERT INTO {TableName} (item_name, item_price) VALUES ('{name}',{price})"
        self.cursor.execute(query)
        self.connection.commit()

item = MenuItem('Item 1', 100)
item.save(TableName='menu_items', name='Item1', price=100)



