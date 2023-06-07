import sqlite3 

miConexion=sqlite3.connect("gestionProductos")

miCursor=miConexion.cursor()


#las tres comillas son cuando la instruccion es muy larga y queremos dividirla en varias lineas esto solo funciona con las 3 comillas.
# miCursor.execute('''

#      CREATE TABLE PRODUCTOS(
#      ID INTEGER PRIMARY KEY AUTOINCREMENT,
#      NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#      PRECIO INTEGER,
#      SECCION VARCHAR(20))
#  ''')

#UNIQUE SIRVE PARA EVITAR QUE LOS DATOS SE REPITAN/EVITA QUE SE REPIA LA INFORMACION EN LA BASE DE DATOS

#ID INTEGER PRIMARY KEY AUTOINCREMENT SIRVE PARA AUTOMATIZAR EL CAMPO DE ID HACIENDO QUE SE AUTOINCREMENTE AUTOMATICAMENTE CADA PRODUCTO



#---- OPERACION C R U D ------------------------

#CREATE

# productos=[ <---- CREATE

#      ("PELOTA", 20, "JUGUETERiA"),
#      ("PANTALON", 15, "CONFECCION"),
#      ("DESTORNILLADOR", 25, "FERRETERIA"),
#      ("JARRON", 45, "CERAMICA"),
#  ]


# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



#READ

#--------------- READ ----------------------------

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='CONFECCION'")  <--- LEYENDO LA INFORMACION

# productos=miCursor.fetchall() <---- METODO FETCH 

# print(productos) <--- IMPRIMIR PARA LEER POR CONSOLA


#UPDATE

#--------------------- UPDATE ---------------------

# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='PELOTA'")

#NOS ACTUALIZA EL VALOR DE PRECIO DE PELOTA A 35 




#DELETE

#--------------------- DELETE ---------------------



# miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

#CON ESTO HEMOS BORRADO EL ARTICULO CON EL ID 4 QUE ERA JARRON (ID 4)

#NUNCA OLVIDAR EL WHERE EN UNA CLAUSULA DELETE O ELIMANAREMOS TODA LA INFORMACION DE LA TABLA DE LA BASE DE DATOS (MUY IMPORTANTE) 

miConexion.commit()

miConexion.close()