import psycopg2 # Conectamos con BD Postgresql
conexion = psycopg2.connect(
    user='postgres',        #Colocamos los datos de la conexion a la bd(var. de entorno)
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
#Creamos un objeto tipo cursor
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 12),
                ('Romina', 'Ayala', 'ayalar@mail.com', 13)) #Una tupla de tuplas
            cursor.executemany(sentencia, valores) #Ejecutamos
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
#Cerramos la bd:
finally:
    conexion.close()


#FILE --RESET LAYOUT-- SI DEJA DE VERSE EL OUT EN PS