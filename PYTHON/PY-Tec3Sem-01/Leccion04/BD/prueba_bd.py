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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Realizamos la consulta
            # %s : "placeholder"
            id_persona = input('Digite un número para el id_persona: ')
            #Colocamos la sentencia que queremos llamar
            cursor.execute(sentencia, (id_persona,)) #Ejecutamos
            registros = cursor.fetchone()  #Recupera todos (all) registros de la sentencia
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
#Cerramos la bd:
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html