import psycopg2  # Conectamos con BD Postgresql

conexion = psycopg2.connect(
    user='postgres',  #Colocamos los datos de la conexion a la bd(var. de entorno)
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
#Creamos un objeto tipo cursor
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los números de registros a eliminar: ')
            valores = (tuple(entrada.split(', ')),)  #Es una tupla de tuplas
            cursor.execute(sentencia, valores)  #Ejecutamos
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
#Cerramos la bd:
finally:
    conexion.close()
