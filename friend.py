# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Friend:

    db_name='first_flask'

    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['first_name']
        self.apellido = data['last_name']
        self.ocupacion = data['ocupation']
        self.creado = data['created_at']
        self.actualizado = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(cls.db_name).query_db(query)
        #result es un resultset
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def save(cls, data ):
        # first_name , last_name , ocupation , created_at, updated_at  son los de la tabla en la base de datos
        query = "INSERT INTO friends ( first_name , last_name , ocupation , created_at, updated_at ) VALUES ( %(d_name)s , %(d_name)s , %(d_occ)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(cls.db_name).query_db( query, data )

    def __str__(self):
        return self.nombre+' '+self.apellido