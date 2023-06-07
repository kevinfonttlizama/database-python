# language=sql


import sqlite3


dbConnection = sqlite3.connect("First_Database")#nos conectamos a la base de datos

myCursor = dbConnection.cursor() #creamos el cursos de la base de datos


# myCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") esta linea de codigo solo la ejecutamos una vez creada la base de datos, si no la invalidamos intentare crear denuevo lo mismo y nos dara error


# myCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")


#esto inserta un solo registro a continuacion se usa una tupla para registrar multiples registros.


myCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=myCursor.fetchall()

for producto in variosProductos:
    print ("Nombre Articulo: ",producto[0], "| Seccion: ",producto[2])




# variosProductos=[

#     ("Camiseta", 10, "Deportes"),
#     ("Jarron", 90, "Ceramica"),
#     ("Camion", 20, "Jugueteria")

# ]

# myCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos) INSERTANDO UN LOTE DE REGISTROS EN LA TABLA, usando una lista y tuplas, usamos el lenguaje sql correspondiente que se traduce en insertar en la tabla productos los valores (?,?,?) <----- esto indica que los parametros o atributos de la tupla donde estamos creando los productos son 3 ya que en la tupla estamos dando 3 parametros


dbConnection.commit()#comando para confirmar los cambios en la base de datos


dbConnection.close()
#se cierra la conexion con la base de datos