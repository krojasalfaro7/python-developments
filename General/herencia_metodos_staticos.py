class BaseDatabase:
    database_name = None  # Variable de clase

    @staticmethod
    def connect():
        if BaseDatabase.database_name is not None:
            print(f"Connecting to {BaseDatabase.database_name}")
        else:
            print("No database specified")

class MySQLDatabase(BaseDatabase):
    database_name = "MySQL"

    @staticmethod
    def query():
        print("Executing MySQL query")

# Crear instancia de la subclase y llamar al método estático
mysql_db = MySQLDatabase()
mysql_db.connect()  # Accede al atributo de la subclase utilizando la variable de clase
mysql_db.query()    # Llama al método estático de la subclase
