import database
from database import *

database.cursor.execute("SELECT SUM(capacite) FROM salles")

print("La capacité de toutes les salles est de : {}".format(database.cursor.fetchall()[0][0]))
