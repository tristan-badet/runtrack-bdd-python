from database import *
import database

database.cursor.execute("SELECT * FROM etudiants")
affichage = database.cursor.fetchall()
print(affichage)