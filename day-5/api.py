from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

app = FastAPI()

# Configuration de la base de données
DB_CONFIG = {
    'dbname': 'itemsdb',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}


# Modèle Pydantic pour la validation des données
class MenuItemCreate(BaseModel):
    item_name: str
    item_price: float


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    item_price: Optional[float] = None


@contextmanager
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()



@app.post("/menu-items/", status_code=201)
def create_menu_item(item: MenuItemCreate):
    with get_db_connection() as conn:
        try:
            with conn.cursor() as cur:
                query = "INSERT INTO Menu_Items(item_name, item_price) VALUES (%s, %s) RETURNING item_name, item_price"
                cur.execute(query, (item.item_name, item.item_price))
                conn.commit()
                created_item = cur.fetchone()
                return {"message": f"Item '{item.item_name}' saved successfully",
                        "item": {"item_name": created_item[0], "item_price": created_item[1]}}
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=400, detail=f"Error saving item: {str(e)}")


@app.delete("/menu-items/{item_name}")
def delete_menu_item(item_name: str):
    with get_db_connection() as conn:
        try:
            with conn.cursor() as cur:
                query = "DELETE FROM Menu_Items WHERE item_name = %s RETURNING item_name"
                cur.execute(query, (item_name,))
                deleted_item = cur.fetchone()
                conn.commit()

                if not deleted_item:
                    raise HTTPException(status_code=404, detail=f"Item '{item_name}' not found")

                return {"message": f"Item '{item_name}' deleted successfully"}
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=400, detail=f"Error deleting item: {str(e)}")


@app.put("/menu-items/{item_name}")
def update_menu_item(item_name: str, item_update: MenuItemUpdate):
    with get_db_connection() as conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Vérifier si l'élément existe
                cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (item_name,))
                existing_item = cur.fetchone()

                if not existing_item:
                    raise HTTPException(status_code=404, detail=f"Item '{item_name}' not found")

                updates = []
                values = []

                if item_update.item_name is not None:
                    updates.append("item_name = %s")
                    values.append(item_update.item_name)
                    new_name = item_update.item_name
                else:
                    new_name = item_name

                if item_update.item_price is not None:
                    updates.append("item_price = %s")
                    values.append(item_update.item_price)

                if not updates:
                    return {"message": "No updates provided", "item": existing_item}

                query = f"UPDATE Menu_Items SET {', '.join(updates)} WHERE item_name = %s RETURNING item_name, item_price"
                values.append(item_name)

                cur.execute(query, values)
                updated_item = cur.fetchone()
                conn.commit()

                return {"message": "Item updated successfully", "item": updated_item}
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=400, detail=f"Error updating item: {str(e)}")


@app.get("/menu-items/")
def get_all_menu_items():
    with get_db_connection() as conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM Menu_Items")
                items = cur.fetchall()
                return {"items": items}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@app.get("/menu-items/{item_name}")
def get_menu_item(item_name: str):
    with get_db_connection() as conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (item_name,))
                item = cur.fetchone()

                if not item:
                    raise HTTPException(status_code=404, detail=f"Item '{item_name}' not found")

                return {"item": item}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)