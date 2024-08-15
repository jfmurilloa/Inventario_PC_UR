class Ubicacion:
    def __init__(self,nom,desc,id=None):
        self.__nombre=nom
        self.__descripcion=desc
        self.__id=id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nom):
        self.__nombre=nom    
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,desc):
        self.__descripcion=desc
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id= id