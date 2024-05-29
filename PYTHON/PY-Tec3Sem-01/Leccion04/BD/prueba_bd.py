import psycopg2 # Conectamos con BD Postgresql
conexion = psycopg2.connect(
    user='postgres',        #Colocamos los datos de la conexion a la bd(var. de entorno)
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
#Creamos un objeto tipo cursor
cursor = conexion.cursor()
#Colocamos la sentencia que queremos llamar
sentencia = 'SELECT * FROM persona'  #Realizamos la consulta
cursor.execute(sentencia) #Ejecutamos
registros = cursor.fetchall()  #Recupera todos (all) registros de la sentencia

print(registros)

#Cerramos la bd:
cursor.close()
conexion.close()