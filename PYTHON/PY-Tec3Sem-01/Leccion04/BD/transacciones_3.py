import psycopg2 as bd# Conectamos con BD Postgresql
conexion = bd.connect(
    user='postgres',        #Colocamos los datos de la conexion a la bd(var. de entorno)
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
# BUENA PRÁCTICA: con el with
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Juan Carlos', 'Roldan', 'jcroldan@mail.com', 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrió un error, se hizo un rollback: {e}')
#Cerramos la bd:
finally:
    conexion.close()

print('Termina la transaccion')