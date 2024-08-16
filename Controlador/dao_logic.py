import mysql.connector
#from mysql.connector.errors import Error
from mysql.connector import Error
from tkinter import messagebox
from Modelo.owner import *
from Modelo.location import *
from Modelo.supplier import *


class Dao:
    def __init__(self,db):
        self.db=db
    
    #CRUD Cuentadante
    
    def crear_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular)
        insert='insert into cuentadante(documento,nombres,apellidos,correo,celular) values (%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El cuentadante ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_cuentadante(self,doc):
        criterio=(doc,)
        select='select * from cuentadante where documento= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_cue= self.db.cursor.fetchone()
            return obj_cue
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular,obj.id)
        update='update cuentadante set documento= %s, nombres= %s, apellidos=%s, correo=%s, celular=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_cuentadante(self,obj:Cuentadante):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from cuentadante where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    
    #CRUD Ubicacion
    
    def crear_ubicacion(self,obj:Ubicacion):
        val=(obj.nombre,obj.descripcion)
        insert='insert into ubicacion(nombre,descripcion) values (%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','La ubicación de ha almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_ubicacion(self,nom):
        criterio=(nom,)
        select='select * from ubicacion where nombre= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_ubi= self.db.cursor.fetchone()
            return obj_ubi
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_ubicacion(self,obj:Ubicacion):
        val=(obj.nombre,obj.descripcion,obj.id)
        update='update ubicacion set nombre= %s, descripcion=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_ubicacion(self,obj:Ubicacion):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from ubicacion where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    
    #CRUD Proveedor
    
    def crear_proveedor(self,obj:Proveedor):
        val=(obj.nit,obj.razon_social,obj.direccion,obj.telefono,obj.email)
        insert='insert into proveedor(nit,razon_social,direccion,telefono,email) values (%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El proveedor ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_proveedor(self,nit):
        criterio=(nit,)
        select='select * from proveedor where nit= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_pro= self.db.cursor.fetchone()
            return obj_pro
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_proveedor(self,obj:Proveedor):
        val=(obj.nit,obj.razon_social,obj.direccion,obj.telefono,obj.email,obj.id)
        update='update proveedor set nit= %s, razon_social= %s, direccion=%s, telefono=%s, email=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_proveedor(self,obj:Proveedor):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from proveedor where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False





