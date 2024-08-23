from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Modelo.owner import *
from Modelo.location import *
from Modelo.supplier import *
from Modelo.team import *
from Controlador.conexion import *
from Controlador.dao_logic import *

#variables globales para el manajo de instancias de las clases importadas
db=DataBase()
dao = Dao(db)

class MiVentanaPrincipal:
    def __init__(self,root):
        self.root=root
        self.root.title('Formulario Principal')
        self.root.config(bg='burlywood')
        self.root.state('zoomed')

        #Controles como atributos
        #espacio para la barra de menu
        self.barraMenu= Menu(self.root)
        self.root.config(menu=self.barraMenu, width=600, height=600)

        #menus dentro de la barra de menu
        self.cuentadanteMenu= Menu(self.barraMenu,tearoff=0)
        self.cuentadanteMenu.add_command(label='Admon_Cuentadantes',command=self.frm_cuentadante)
        self.cuentadanteMenu.add_command(label='Salir',command=self.salir)

        self.ubicacionMenu=Menu(self.barraMenu,tearoff=0)
        self.ubicacionMenu.add_command(label='Admon_Ubicaciones',command=self.frm_ubicacion)

        self.proveedorMenu=Menu(self.barraMenu,tearoff=0)
        self.proveedorMenu.add_command(label='Admon_Proveedores',command=self.frm_proveedor)

        self.equipoMenu=Menu(self.barraMenu,tearoff=0)
        self.equipoMenu.add_command(label='Admon_Equipos',command=self.frm_equipo)

        self.ayudaMenu=Menu(self.barraMenu,tearoff=0)
        self.ayudaMenu.add_command(label='Acerca de...')
        self.ayudaMenu.add_command(label='Licencia')

        #Agregar opciones a los menus
        self.barraMenu.add_cascade(label='Cuentadantes',menu=self.cuentadanteMenu)
        self.barraMenu.add_cascade(label='Proveedores',menu=self.proveedorMenu)
        self.barraMenu.add_cascade(label='Ubicaciones',menu=self.ubicacionMenu)
        self.barraMenu.add_cascade(label='Equipos',menu=self.equipoMenu)
        self.barraMenu.add_cascade(label='Ayuda',menu=self.ayudaMenu)

        #Variables vinculadas a los Entry
        self.caja1=StringVar()
        self.caja2=StringVar()
        self.caja3=StringVar()
        self.caja4=StringVar()
        self.caja5=StringVar()
        self.caja6=StringVar()
        self.caja7=StringVar()
        self.caja8=StringVar()
        self.caja9=StringVar()
        self.caja10=StringVar()
        self.caja11=StringVar()
        #Creacion de widgets en las ventanas secundarias
        self.txt_caja1=Entry()
        self.txt_caja2=Entry()
        self.txt_caja3=Entry()
        self.txt_caja4=Entry()
        self.txt_caja5=Entry()
        self.txt_caja6=Entry()
        self.txt_caja7=Entry()
        self.txt_caja8=ttk.Combobox()
        self.txt_caja9=ttk.Combobox()
        self.txt_caja10=ttk.Combobox()
        self.txt_caja11=ttk.Combobox()

        self.btn_nuevo=Button()
        self.btn_buscar=Button()
        self.btn_modificar=Button()
        self.btn_eliminar=Button()
        
    
    #metodos de validación
    def validar_numeros(self,action,proposed_text,current_text):
        if action == '1':
            if len(current_text) > 12:
                return False
            return proposed_text.isdigit()
        return True
    
    def validar_letras(self,action,proposed_text,current_text):
        if action == '1':
            if len(current_text) > 40:
                return False
            return all(c.isalpha() or c.isspace() for c in proposed_text)
        return True
    
    def validar_fecha(self, fecha):
        if len(fecha) >10:
            return False
        valores=[]

        for i,char in enumerate(fecha):
            if i in(4,7):
                valores.append(char=='-')
            else:
                valores.append(char.isdecimal())
        return all(valores)


    def salir(self):      
        rta=messagebox.askquestion('Salir','Desea salir de la aplicación?')
        if rta=='yes':
            self.root.destroy()
    

    def frm_cuentadante(self):
        ventana= Toplevel(self.root)
        ventana.title('Administración de cuentadantes')
        ventana.config(width=500,height=500)

        # Para los controles se adapten mejor a la ventana
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=25)
        ventana.columnconfigure(1, weight=2)
        ventana.rowconfigure(1, weight=1)

        frame1= Frame(ventana,bg='gray15')
        frame1.grid(row=0,column=0, sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=1,columnspan=1, sticky='nsew')

        
        lbl_id=Label(frame1,text='Id',width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1,state='readonly')
        self.txt_caja1.grid(row=0,column=1)

        lbl_documento=Label(frame1,text='Documento',width=15)
        lbl_documento.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2,
                            validate='key',validatecommand=(ventana.register(self.validar_numeros),'%d','%S','%P'))
        self.txt_caja2.grid(row=1,column=1)
        self.txt_caja2.focus()
        

        lbl_nombres=Label(frame1,text='Nombres',width=15)
        lbl_nombres.grid(row=2,column=0,padx=10,pady=10)
        self.txt_caja3=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja3,
                            validate='key',validatecommand=(ventana.register(self.validar_letras),'%d','%S','%P'))
        self.txt_caja3.grid(row=2,column=1)

        lbl_apellidos=Label(frame1,text='Apellidos',width=15)
        lbl_apellidos.grid(row=3,column=0,padx=10,pady=10)
        self.txt_caja4=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja4,
                            validate='key',validatecommand=(ventana.register(self.validar_letras),'%d','%S','%P'))
        self.txt_caja4.grid(row=3,column=1)

        lbl_correo=Label(frame1,text='Correo',width=15)
        lbl_correo.grid(row=4,column=0,padx=10,pady=10)
        self.txt_caja5=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja5)
        self.txt_caja5.grid(row=4,column=1)

        lbl_celular=Label(frame1,text='Celular',width=15)
        lbl_celular.grid(row=5,column=0,padx=10,pady=10)
        self.txt_caja6=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja6)
        self.txt_caja6.grid(row=5,column=1)
        
        #Colocar los botones en frame 2
        self.btn_nuevo= Button(frame2,width=10,font=('Arial',12,'bold'),text='Nuevo',bg='orange',bd=5,command=self.crear_cuentadante_v)
        self.btn_nuevo.grid(row=0,column=0,padx=10,pady=10)

        self.btn_buscar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Buscar',bg='orange',bd=5,command=self.buscar_cuentadante_v)
        self.btn_buscar.grid(row=0,column=1,padx=10,pady=10)

        self.btn_modificar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Modificar',bg='orange',bd=5,command=self.modificar_cuentadante_v)
        self.btn_modificar.grid(row=0,column=2,padx=10,pady=10)

        self.btn_eliminar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Eliminar',bg='orange',bd=5,command=self.eliminar_cuentadante_v)
        self.btn_eliminar.grid(row=0,column=3,padx=10,pady=10)

        ventana.focus()
        self.txt_caja2.focus()
        ventana.grab_set()
    
    def crear_cuentadante_v(self):
        if self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() !='':
            obj_cuentadante=Cuentadante(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get())
            dao.crear_cuentadante(obj_cuentadante)
            self.limpiar()
        else:
            messagebox.showerror('Error','Todos los campos son obligatorios...')
    
    def buscar_cuentadante_v(self):
        if self.caja2.get() != '':
            cuentadante= dao.buscar_cuentadante(self.caja2.get())
            if cuentadante != None:
                obj_cue=Cuentadante(cuentadante[1],cuentadante[2],cuentadante[3],cuentadante[4],cuentadante[5],cuentadante[0])
                self.caja1.set(obj_cue.id)
                self.caja2.set(obj_cue.documento)
                self.caja3.set(obj_cue.nombres)
                self.caja4.set(obj_cue.apellidos)
                self.caja5.set(obj_cue.correo)
                self.caja6.set(obj_cue.celular)
            else:
                messagebox.showwarning('No encontrado','Registro no encontrado...')
        else:
            messagebox.showwarning('No encontrado','debe enviar un criterio de busqueda...')

    def modificar_cuentadante_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() !='':
            obj_cuentadante= Cuentadante(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja1.get())
            dao.modificar_cuentadante(obj_cuentadante)
            self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def eliminar_cuentadante_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() !='':
            obj_cuentadante= Cuentadante(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja1.get())
            res=dao.eliminar_cuentadante(obj_cuentadante)
            if res:
                self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def limpiar(self):
        self.caja1.set('')
        self.caja2.set('')
        self.caja3.set('')
        self.caja4.set('')
        self.caja5.set('')
        self.caja6.set('')
        self.caja7.set('')
        self.caja8.set('')
        self.caja9.set('')
        self.caja10.set('')
        self.caja11.set('')
        self.txt_caja2.focus()
    
    #Formulario para ubicacion
    def frm_ubicacion(self):
        ventana= Toplevel(self.root)
        ventana.title('Administración de ubicaciones')
        ventana.config(width=500,height=500)

        # Para los controles se adapten mejor a la ventana
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=25)
        ventana.columnconfigure(1, weight=2)
        ventana.rowconfigure(1, weight=1)

        frame1= Frame(ventana,bg='gray15')
        frame1.grid(row=0,column=0, sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=1,columnspan=1, sticky='nsew')

        
        lbl_id=Label(frame1,text='Id',width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1,state='readonly')
        self.txt_caja1.grid(row=0,column=1)

        lbl_nombre=Label(frame1,text='Nombre',width=15)
        lbl_nombre.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2)
        self.txt_caja2.grid(row=1,column=1)        

        lbl_descripcion=Label(frame1,text='Descripcion',width=15)
        lbl_descripcion.grid(row=2,column=0,padx=10,pady=10)
        self.txt_caja3=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja3)
        self.txt_caja3.grid(row=2,column=1)        
        
        #Colocar los botones en frame 2
        self.btn_nuevo= Button(frame2,width=10,font=('Arial',12,'bold'),text='Nuevo',bg='orange',bd=5,command=self.crear_ubicacion_v)
        self.btn_nuevo.grid(row=0,column=0,padx=10,pady=10)

        self.btn_buscar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Buscar',bg='orange',bd=5,command=self.buscar_ubicacion_v)
        self.btn_buscar.grid(row=0,column=1,padx=10,pady=10)
        self.btn_modificar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Modificar',bg='orange',bd=5,command=self.modificar_ubicacion_v)
        self.btn_modificar.grid(row=0,column=2,padx=10,pady=10)

        self.btn_eliminar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Eliminar',bg='orange',bd=5,command=self.eliminar_ubicacion_v)
        self.btn_eliminar.grid(row=0,column=3,padx=10,pady=10)

        ventana.focus()
        self.txt_caja2.focus()
        ventana.grab_set()
    
    def crear_ubicacion_v(self):
        if self.caja2.get() and self.caja3.get() !='':
            obj_ubicacion=Ubicacion(self.caja2.get(),self.caja3.get())
            dao.crear_ubicacion(obj_ubicacion)
            self.limpiar()
        else:
            messagebox.showerror('Error','Todos los campos son obligatorios...')
    
    def buscar_ubicacion_v(self):
        if self.caja2.get() != '':
            ubicacion= dao.buscar_ubicacion(self.caja2.get())
            if ubicacion != None:
                obj_ubi=Ubicacion(ubicacion[1],ubicacion[2],ubicacion[0])
                self.caja1.set(obj_ubi.id)
                self.caja2.set(obj_ubi.nombre)
                self.caja3.set(obj_ubi.descripcion)
                
            else:
                messagebox.showwarning('No encontrado','Registro no encontrado...')
        else:
            messagebox.showwarning('No encontrado','debe enviar un criterio de busqueda...')

    def modificar_ubicacion_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get()!='':
            obj_ubicacion= Ubicacion(self.caja2.get(),self.caja3.get(),self.caja1.get())
            dao.modificar_ubicacion(obj_ubicacion)
            self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def eliminar_ubicacion_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() !='':
            obj_ubicacion= Ubicacion(self.caja2.get(),self.caja3.get(),self.caja1.get())
            res=dao.eliminar_ubicacion(obj_ubicacion)
            if res:
                self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def frm_proveedor(self):
        ventana= Toplevel(self.root)
        ventana.title('Administración de proveedores')
        ventana.config(width=500,height=500)

        # Para los controles se adapten mejor a la ventana
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=25)
        ventana.columnconfigure(1, weight=2)
        ventana.rowconfigure(1, weight=1)

        frame1= Frame(ventana,bg='gray15')
        frame1.grid(row=0,column=0, sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=1,columnspan=1, sticky='nsew')

        
        lbl_id=Label(frame1,text='Id',width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1,state='readonly')
        self.txt_caja1.grid(row=0,column=1)

        lbl_nit=Label(frame1,text='Nit',width=15)
        lbl_nit.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2)
        self.txt_caja2.grid(row=1,column=1)
                

        lbl_razon_social=Label(frame1,text='Razon Social',width=15)
        lbl_razon_social.grid(row=2,column=0,padx=10,pady=10)
        self.txt_caja3=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja3)
        self.txt_caja3.grid(row=2,column=1)

        lbl_direccion=Label(frame1,text='Direccion',width=15)
        lbl_direccion.grid(row=3,column=0,padx=10,pady=10)
        self.txt_caja4=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja4)
        self.txt_caja4.grid(row=3,column=1)

        lbl_telefono=Label(frame1,text='Telefono',width=15)
        lbl_telefono.grid(row=4,column=0,padx=10,pady=10)
        self.txt_caja5=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja5)
        self.txt_caja5.grid(row=4,column=1)

        lbl_email=Label(frame1,text='Email',width=15)
        lbl_email.grid(row=5,column=0,padx=10,pady=10)
        self.txt_caja6=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja6)
        self.txt_caja6.grid(row=5,column=1)
        
        #Colocar los botones en frame 2
        self.btn_nuevo= Button(frame2,width=10,font=('Arial',12,'bold'),text='Nuevo',bg='orange',bd=5,command=self.crear_proveedor_v)
        self.btn_nuevo.grid(row=0,column=0,padx=10,pady=10)

        self.btn_buscar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Buscar',bg='orange',bd=5,command=self.buscar_proveedor_v)
        self.btn_buscar.grid(row=0,column=1,padx=10,pady=10)

        self.btn_modificar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Modificar',bg='orange',bd=5,command=self.modificar_proveedor_v)
        self.btn_modificar.grid(row=0,column=2,padx=10,pady=10)

        self.btn_eliminar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Eliminar',bg='orange',bd=5,command=self.eliminar_proveedor_v)
        self.btn_eliminar.grid(row=0,column=3,padx=10,pady=10)

        ventana.focus()
        self.txt_caja2.focus()
        ventana.grab_set()
    
    def crear_proveedor_v(self):
        if self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() !='':
            obj_proveedor=Proveedor(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get())
            dao.crear_proveedor(obj_proveedor)
            self.limpiar()
        else:
            messagebox.showerror('Error','Todos los campos son obligatorios...')
    
    def buscar_proveedor_v(self):
        if self.caja2.get() != '':
            proveedor= dao.buscar_proveedor(self.caja2.get())
            if proveedor != None:
                obj_pro=Proveedor(proveedor[1],proveedor[2],proveedor[3],proveedor[4],proveedor[5],proveedor[0])
                self.caja1.set(obj_pro.id)
                self.caja2.set(obj_pro.nit)
                self.caja3.set(obj_pro.razon_social)
                self.caja4.set(obj_pro.direccion)
                self.caja5.set(obj_pro.telefono)
                self.caja6.set(obj_pro.email)
            else:
                messagebox.showwarning('No encontrado','Registro no encontrado...')
        else:
            messagebox.showwarning('No encontrado','debe enviar un criterio de busqueda...')

    def modificar_proveedor_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() !='':
            obj_proveedor= Proveedor(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja1.get())
            dao.modificar_proveedor(obj_proveedor)
            self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def eliminar_proveedor_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() !='':
            obj_proveedor= Proveedor(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja1.get())
            res=dao.eliminar_proveedor(obj_proveedor)
            if res:
                self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')
    
    def frm_equipo(self):
        ventana= Toplevel(self.root)
        ventana.title('Administración de equipos')
        ventana.config(width=500,height=500)

        # Para los controles se adapten mejor a la ventana
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=25)
        ventana.columnconfigure(1, weight=2)
        ventana.rowconfigure(1, weight=1)

        frame1= Frame(ventana,bg='gray15')
        frame1.grid(row=0,column=0, sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=1,columnspan=1, sticky='nsew')

        
        lbl_id=Label(frame1,text='Id',width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1,state='readonly')
        self.txt_caja1.grid(row=0,column=1)

        lbl_serial=Label(frame1,text='Serial',width=15)
        lbl_serial.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2)
        self.txt_caja2.grid(row=1,column=1)        
        

        lbl_marca=Label(frame1,text='Marca',width=15)
        lbl_marca.grid(row=2,column=0,padx=10,pady=10)
        self.txt_caja3=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja3)
        self.txt_caja3.grid(row=2,column=1)

        lbl_modelo=Label(frame1,text='Modelo',width=15)
        lbl_modelo.grid(row=3,column=0,padx=10,pady=10)
        self.txt_caja4=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja4)
        self.txt_caja4.grid(row=3,column=1)

        tipos=['Desktop','Laptop','All in one']
        lbl_tipo=Label(frame1,text='Tipo',width=15)
        lbl_tipo.grid(row=4,column=0,padx=10,pady=10)
        self.txt_caja5=ttk.Combobox(frame1,width=27,textvariable=self.caja5,values=tipos,state='readonly')
        self.txt_caja5.grid(row=4,column=1)

        lbl_fecha_compra_a=Label(frame1,text='aaaa-mm-dd',width=15)
        lbl_fecha_compra_a.grid(row=5,column=2,padx=10,pady=10)

        lbl_fecha_compra=Label(frame1,text='Fecha Compra',width=15)
        lbl_fecha_compra.grid(row=5,column=0,padx=10,pady=10)
        self.txt_caja6=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja6,
                            validate='key',validatecommand=(ventana.register(self.validar_fecha),'%P'))
        self.txt_caja6.grid(row=5,column=1)
        

        lbl_garantia=Label(frame1,text='Garantia',width=15)
        lbl_garantia.grid(row=6,column=0,padx=10,pady=10)
        self.txt_caja7=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja7)
        self.txt_caja7.grid(row=6,column=1)

        clasificacion=['Formación','Administración']
        lbl_clasificacion=Label(frame1,text='Clasificación',width=15)
        lbl_clasificacion.grid(row=7,column=0,padx=10,pady=10)
        self.txt_caja8=ttk.Combobox(frame1,width=27,textvariable=self.caja8,values=clasificacion,state='readonly')
        self.txt_caja8.grid(row=7,column=1)

        lst_cuentadantes=dao.listar_cuentadantes()
        cuentadantes=[ ]
        for cue in lst_cuentadantes:
            cuentadantes.append(cue[2]+'_'+cue[3])

        lbl_cuentadante=Label(frame1,text='Cuentadantes',width=15)
        lbl_cuentadante.grid(row=8,column=0,padx=10,pady=10)
        self.txt_caja9=ttk.Combobox(frame1,width=27,textvariable=self.caja9,values=cuentadantes,state='readonly')
        self.txt_caja9.grid(row=8,column=1)

        lst_ubicaciones=dao.listar_ubicaciones()
        ubicaciones=[ ]
        for ubi in lst_ubicaciones:
            ubicaciones.append(ubi[1])
        
        lbl_ubicacion=Label(frame1,text='Ubicación',width=15)
        lbl_ubicacion.grid(row=9,column=0,padx=10,pady=10)
        self.txt_caja10=ttk.Combobox(frame1,width=27,textvariable=self.caja10,values=ubicaciones,state='readonly')
        self.txt_caja10.grid(row=9,column=1)

        lst_proveedores=dao.listar_proveedores()
        proveedores=[]
        for pro in lst_proveedores:
            proveedores.append(pro[2])

        lbl_proveedor=Label(frame1,text='Proveedor',width=15)
        lbl_proveedor.grid(row=10,column=0,padx=10,pady=10)
        self.txt_caja11=ttk.Combobox(frame1,width=27,textvariable=self.caja11,values=proveedores,state='readonly')
        self.txt_caja11.grid(row=10,column=1)
        
        #Colocar los botones en frame 2
        self.btn_nuevo= Button(frame2,width=10,font=('Arial',12,'bold'),text='Nuevo',bg='orange',bd=5,command=self.crear_equipo_v)
        self.btn_nuevo.grid(row=0,column=0,padx=10,pady=10)

        self.btn_buscar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Buscar',bg='orange',bd=5,command=self.buscar_cuentadante_v)
        self.btn_buscar.grid(row=0,column=1,padx=10,pady=10)

        self.btn_modificar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Modificar',bg='orange',bd=5,command=self.modificar_cuentadante_v)
        self.btn_modificar.grid(row=0,column=2,padx=10,pady=10)

        self.btn_eliminar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Eliminar',bg='orange',bd=5,command=self.eliminar_cuentadante_v)
        self.btn_eliminar.grid(row=0,column=3,padx=10,pady=10)

        ventana.focus()
        self.txt_caja2.focus()
        ventana.grab_set()
    
    def crear_equipo_v(self):
        if self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() and self.caja7.get() and self.caja8.get() and self.caja9.get() and self.caja10.get() and self.caja11.get() !='':
            obj_equipo=Equipo(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),
                              self.caja7.get(),self.caja8.get(),self.caja9.get(),self.caja10.get(),self.caja11.get())
            dao.crear_equipo(obj_equipo)
            self.limpiar()
        else:
            messagebox.showerror('Error','Todos los campos son obligatorios...')
    
    
    
    
    





