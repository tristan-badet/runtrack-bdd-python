import database2
from database2 import *

class Modifications():

    def insert(id, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employes VALUES (%s, %s, %s, %s, %s)"    
        val = ("{}".format(id),"{}".format(nom), "{}".format(prenom), "{}".format(salaire), "{}".format(id_service))
        database2.cursor2.execute(sql, val)
        database2.mydb2.commit()

    def read(colonne):
        sql = "SELECT {} FROM employes".format(colonne)
        database2.cursor2.execute(sql)
        affich = database2.cursor2.fetchall()
        print(affich)

    def  update(salaire, prenom):
        sql = "UPDATE employes SET salaire = {} WHERE prenom = {}".format(salaire, prenom)
        database2.cursor2.execute(sql)
        database2.mydb2.commit()

    def delete(id):
        sql = "DELETE FROM `employes` WHERE `id` = {}".format(id)
        database2.cursor2.execute(sql)
        database2.mydb2.commit()