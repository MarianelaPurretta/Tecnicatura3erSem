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
    conexion.autocommit = False   # Inicia la transaccion
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Jorge', 'Prol', 'jprol@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan Carlos', 'Perez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit() #Se cierra la transaccion
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
#Cerramos la bd:
finally:
    conexion.close()