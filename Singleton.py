class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._connection = cls._create_connection()
        return cls._instance

    @staticmethod
    def _create_connection():
        return "Database Connection Established"

    def get_connection(self):
        return self._connection

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.get_connection())  
print(db1 == db2)           
