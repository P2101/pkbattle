# pip install PyMySQL
import pandas as pd
import pymysql
from datetime import datetime
from main import Pykemon, Battle

# Parámetros de conexión
host = 'localhost'
port = 3306
user = 'root'
password = 'root'  # Reemplaza con tu contraseña

# Crear una instancia de Battle con una lista de Pykemons
# pykemons = [Pykemon('Pikachu', 1, 20, 20, 5, 4), Pykemon('Charmander', 4, 20, 20, 4, 4)]
# battle_instance = Battle(pykemons)

# Llamar al método battle para obtener el nombre del ganador
winner_name = Battle.battle()
print("El ganador es:", winner_name)

# Conectar a la base de datos y realizar la inserción
connection = pymysql.connect(host=host, port=port, user=user, password=password, db='historial')
cursor = connection.cursor()

# Insertar los datos en la base de datos
insert_query = "INSERT INTO data (name, date) VALUES (%s, %s)"
cursor.execute(insert_query, (winner_name, datetime.now()))

# Commit y cerrar la conexión
connection.commit()
cursor.close()
connection.close()
