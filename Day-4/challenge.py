import requests
import random
import psycopg2

# Database configuration
DB_CONFIG = {
    'dbname': 'web_api',
    'user': 'superuser',
    'password': 'aza',
    'host': 'localhost',
    'port': '5432'
}


def get_countries():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return []


def save_countries_to_db(countries, count=10):
    if len(countries) > count:
        countries = random.sample(countries, count)

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for country in countries:
            try:
                name = country['name']['common']
                capital = country.get('capital', ['Unknown'])[0] if country.get('capital') else 'Unknown'
                flag = country.get('flags', {}).get('png', None)
                subregion = country.get('subregion', 'Unknown')
                population = country.get('population', 0)


                cursor.execute("""
                    INSERT INTO countries (name, capital, flag, subregion, population)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                """, (name, capital, flag, subregion, population))

                country_id = cursor.fetchone()[0]
                print(f"Added: {name} (ID: {country_id})")

            except Exception as e:
                print(f"Error processing {country.get('name', {}).get('common', 'Unknown country')}: {e}")

        conn.commit()
        print(f"Successfully added {len(countries)} countries to database")

    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()


def main():
    print("Fetching countries from API...")
    countries = get_countries()

    if not countries:
        print("No countries found. Exiting.")
        return

    print(f"Found {len(countries)} countries. Adding 10 random countries to database...")
    save_countries_to_db(countries)
    print("Process complete")


if __name__ == "__main__":
    main()