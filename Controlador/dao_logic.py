import mysql.connector
from tkinter import messagebox
from Modelo.owner import *

class Dao:
    def __init__(self,db):
        self.db=db
    
    def crear_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular)
        insert='insert into cuentadante(documento,nombres,apellidos,correo,celular) values (%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El cuentadante ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)

