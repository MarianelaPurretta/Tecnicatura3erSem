import psycopg2 as bd# Conectamos con BD Postgresql
conexion = bd.connect(
    user='postgres',        #Colocamos los datos de la conexion a la bd(var. de entorno)
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
#Creamos un objeto tipo cursor
try:
    # conexion.autocommit = False # Colocando el conexion.commit() no es necesario esto
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() #Hacemos el commit manualmente, sino esta en False y no de ejecuta
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
#Cerramos la bd:
finally:
    conexion.close()