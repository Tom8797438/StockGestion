import psycopg2

# Configuration de la connexion à la base de données PostgreSQL
DB_NAME = "gestion_stock"
DB_USER = "dev2"
DB_PASSWORD = "123456"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

def connect_to_db():
    """Se connecter à la base de données PostgreSQL"""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connexion à la base de données réussie")
        conn.close()
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")

if __name__ == "__main__":
    connect_to_db()
