import urllib.request
import json
import random
import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    'dbname': 'web_api',
    'user': 'superuser',
    'password': 'aza',
    'host': 'localhost',
    'port': '5432'
}

def fetch_all_countries():
    try:
        req = urllib.request.Request('https://restcountries.com/v3.1/all')
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"Error fetching countries: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return []

def select_random_countries(countries, count=10):
    if len(countries) <= count:
        return countries
    return random.sample(countries, count)

def insert_country(conn, country):
    try:
        name = country['name']['common']
        capital = country.get('capital', [None])[0]
        flag = country.get('flags', {}).get('png')
        subregion = country.get('subregion')
        population = country.get('population', 0)
        
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO countries (name, capital, flag, subregion, population)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
            """, (name, capital, flag, subregion, population))
            
            country_id = cur.fetchone()[0]
            conn.commit()
            print(f"Inserted country: {name} with ID: {country_id}")
            return country_id
    except Exception as e:
        conn.rollback()
        print(f"Error inserting country {country.get('name', {}).get('common')}: {e}")
        return None

def populate_random_countries():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        
        all_countries = fetch_all_countries()
        
        if not all_countries:
            print("No countries fetched from the API")
            return
        
        random_countries = select_random_countries(all_countries, 10)
        
        print(f"Selected {len(random_countries)} random countries")
        
        for country in random_countries:
            insert_country(conn, country)
        
        print("Database population complete")
    except Exception as e:
        print(f"Error in population process: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    populate_random_countries()