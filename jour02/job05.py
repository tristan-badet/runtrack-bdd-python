import database
from database import *

superficie_totale = 0

database.cursor.execute("SELECT SUM(superficie) FROM etage")

print("La superficie de la Plateforme est de {} m2".format(database.cursor.fetchall()[0][0]))
