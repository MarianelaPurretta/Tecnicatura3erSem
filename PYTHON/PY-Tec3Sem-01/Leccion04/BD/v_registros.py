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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'  # Realizamos la consulta
            # %s : "placeholder"
            entrada = input('Digite los id_persona a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),) #Convertimos la entrada en una tupla separada por comas
            #Colocamos la sentencia que queremos llamar
            cursor.execute(sentencia, llaves_primarias) #Ejecutamos
            registros = cursor.fetchall()  #Recupera todos (all) registros de la sentencia
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrió un error: {e}')
#Cerramos la bd:
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html