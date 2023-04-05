from database import *
import database

database.cursor.execute("SELECT nom, capacite FROM salles")
for nom, capacite in database.cursor:
    print(nom, capacite)