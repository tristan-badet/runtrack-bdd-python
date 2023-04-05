import database2
from database2 import *
import CRUD

affichagesalairesup3000 = "SELECT * FROM employes WHERE salaire > 3000.00"

database2.cursor2.execute(affichagesalairesup3000)

result = database2.cursor2.fetchall()

print(result)

affichageNom = "SELECT id,nom FROM employes"
affichageNomService = "SELECT id,nom FROM services"

database2.cursor2.execute(affichageNom)

for x in database2.cursor2:
    print(x)

database2.cursor2.execute(affichageNomService)

for x in database2.cursor2:
    print(x)

#Test des CRUDs

CRUD.Modifications.read("nom")





CRUD.Modifications.delete('4')


