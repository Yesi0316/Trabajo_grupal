# ---------------- SISTEMA DE RESERVA DE PELÍCULAS ----------------------------------------------------

# Mensaje de bienvenida inicial

print("SISTEMA DE RESERVA DE PELICULAS S.A")#titulol

sala={} #diccionario de salas que se encuenta vacio.
for a in range(1,51):#guardamos los asientos disponibles en el diccionario 'sala' (range==rango genio, aprende ingles):9, la i va a tomar valores del 1-50 (antes del 51) y los vamos a almacenar en el diccionario 
    sala[a]=True #le damos el valor a verdadero a cada número 

# Diccionario con los horarios de una sala para cada día de la semana Cada horario contiene una copia de los asientos disponibles

sala1={"lunes":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()},"Martes":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()},"miercoles":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()},"jueves":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()},"viernes":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()},"sabado":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()},"domingo":{"8":sala.copy(),"11":sala.copy(),"14":sala.copy(),"17":sala.copy(),"20":sala.copy()}}
#se crea un diccionarío dondee nse guarda toda la inmformación de la sala1

# Se crean copias de la sala1 para las demás películas

sala2=sala1.copy()
sala3=sala1.copy()
sala4=sala1.copy()
sala5=sala1.copy()
sala6=sala1.copy()
sala7=sala1.copy()
sala8=sala1.copy()

# ---------------------- PELÍCULAS ---------------------- #
# Cada película es una tupla: (nombre, sinopsis, duración, horarios)

#pelicula_1 guardada en una tupla
pelicula_1=("Encantada","La bella princesa Giselle es transportada por un hechizo de la malvada reina Narissa desde su mágico mundo a la moderna y caótica Manhattan actual.Inmersa en un entorno que desconoce,Giselle deambula por un mundo desorganizado.","1h 47m",sala1) 

#pelicula_2 guardada en una tupla
pelicula_2=("Las guerreras del k-pop","Un supergrupo de k-pop usa sus poderes secretos para proteger a sus fans de amenazas sobrenaturales y de una banda rival de chicos decididos a robar corazones y mentes.","1h 36m",sala2)

#pelicula_3 guardada en una tupla
pelicula_3=("spiderman","Luego de sufrir la picadura de una araña genéticamente modificada, un estudiante de secundaria tímido y torpe adquiere increíbles capacidades como arácnido. Pronto comprenderá que su misión es utilizarlas para luchar contra el mal y defender a sus vecinos.","2h 6m",sala3)

#pelicula_4 guardada en una tupla
pelicula_4=("Intensa-Mente","Riley acaba de nacer y en el centro de control de su pequeña mente sólo hay sitio para Alegría. Poco después aparece Tristeza y, más tarde, Ira, Miedo y Asco. Las cinco emociones tendrán que ayudar a la niña cuando, ya con 11 años, su familia se mude desde su idílico pueblo del Medio Oeste estadounidense a la enorme e intimidante ciudad de San Francisco. Tras una serie de acontecimientos, Alegría y Tristeza tendrán que trabajar juntas para salvar a Riley.","1h 35m",sala4)

#pelicula_5 guardada en una tupla
pelicula_5=("Barbie","Después de ser expulsada de Barbieland por no ser una muñeca de aspecto perfecto, Barbie parte hacia el mundo humano para encontrar la verdadera felicidad.","1h 54m",sala5) 

#pelicula_6 guardada en una tupla
pelicula_6=("Cómo entrenar a tu dragón 3","El joven vikingo Hipo parece haber conseguido que dragones y humanos convivan en paz. Sin embargo, su sueño y el de los demás habitantes de la isla de Mema no es compartido por otros vikingos, especialmente por los brutales cazadores de dragones.","1h 44m",sala6)

#pelicula_7 guardada en una tupla
pelicula_7=("Hotel Transylvania","El nuevo y misterioso invento de Van Helsing transforma a Drac y sus amigos en humanos, y a Johnny en un monstruo. Con sus nuevos cuerpos, Drac y la manada deben encontrar la manera de revertirlo antes de que se se vuelva permanente.","1h 27m",sala7)

#pelicula_8 guardada en una tupla
pelicula_8=("turning red","Mei Lee, una niña de 13 años un poco rara pero segura de sí misma, que se debate entre seguir siendo la hija obediente que su madre quiere que sea y el caos de la adolescencia.","1h 40m",sala8)

# Lista con todas las películas

peliculas=[pelicula_1,pelicula_2,pelicula_3,pelicula_4,pelicula_5,pelicula_6,pelicula_7,pelicula_8]

opcion="null" # Variable para controlar la opción del menú principal, ayuda a que tenga un valor nulo fuera del bucle

# ------------------ VARIABLES DE USUARIO Y RESERVAS -------------------------------------------------------------

cuentas= {"yesi@gmail.com":"123"}#Diccionario con las cuentas registradas (correo,contraseña)
nombres_usuarios={"yesi@gmail.com":"Yesi"} # Diccionario para asociar correo con el nombre del usuario
boleta_valor=10000  # ps el valor genio
descuento=0.10 #10% de descuento si la compra es mayor a 4 entradas
asiento_revervados=[] # Lista para almacenar reservas
comprobante=False # Variable para controlar si el usuario inició sesión

# ------------------- FLUJO PRINCIPAL DEL PROGRAMA ------------------------------------------

reservas=[] #lista de reservas
while True:
    print("BIENVENIDO A LA PÁGINA DEL CINE MUNDO S.A")
    n=1 #Contador de intentos
    pregunta= input("1.Registrarse \n2.Ingresar\n\nIngresé su opción: ").lower()#Le preguntamos al usuario si quiere registrarse po ingresar .lower para convertir a minusculas

    contador= 1

# ------------------- INGRESO A LA CUENTA ------------------- -----------------------------------------------------


    if pregunta=="2":
        while n<=3:#si el numero de intentos faliidos es mayor a 3 sera un error
            try:
                usuario= input("Ingresé su usuario (correo electronico): ") #ps ingrese y ya
                contraseña= input("Ingresé su contraseña: ") #ps ingrese y ya
                if contraseña==cuentas[usuario]:
                    print(f"Bienvenido a su cuenta {nombres_usuarios[usuario]}") # se te da la bienvenida y te muestra tu mombre 
                    comprobante=True #comprueba q el uisuario esta en su cuenta
                    break
                elif contraseña!=cuentas[usuario]: #si la contraseña es diferente a la del diccionario
                    print("Contraseña incorrecto")
                else:
                    print("No se pudo ingresar a su cuenta")
                n+=1 #se le suma un intento a la cuenta
            except KeyError: #se arroja el keyerror ya q ingreso el correo mal ya q esla clave de un diccionario de una cuenta
                if n<3:
                    print("Correo incorrecto") #se da un mensaje de correo incorrecto
                    n+=1 #se le suma un intento a la cuenta
                else:
                    print("No se pudo ingresar a su cuenta") #sorry
                    break

#se le lleva a la parte de incio y ps si ya

# ------------------- REGISTRO DE NUEVA CUENTA -------------------------------------------------------------------------

    elif pregunta=="1":
        while True:
            nombre=input("Ingrese un apodo o su nombre (Por este se le llamará): ") #ingrese y ya
            usuario= input("Ingresé un correo electronico será su usuario : ") #ingrese y ya
            # Validación del correo
            if "@gmail.com" in usuario or "@hotmail.com" in usuario or "@yahoo.com"  in usuario: #correo si o si
                if usuario in cuentas:
                    print("Error, el correo ya esta registrado") #ps y lo esta, la bien
                    continue #vuelve al inicio del while
                else:
                    pass #pasa a la siguiente linea del codigo 
            else:
                print("Error, el correo no es valido") #pailas
                continue #vuelve al inicio del while
            contraseña= input("Ingresé una contraseña: ") #ingrese
            cuentas[usuario]=contraseña #guardamos la cuenta en el diccionario
            nombres_usuarios[usuario]=nombre #guardamos el nombre del usuario en el diccionario
            print(f"\nFELICIDADES, su cuenta a sido creada con éxito,{nombres_usuarios[usuario]}  \n Volvera a la página de ingreso donde beberá ingresar su usuario y contraseña")
            break #Volvemos al inicio del while para que ingrese a su cuenta

    else:
        print("Error, opción no valida")

# Si el usuario ingresó correctamente, mostrar menú principal

    if comprobante:
        while True:
            print("MENU PRINCIPAL CINE MUNDO S.A")
            print("Opciones disponibles: \n\n1.Ver cartelera \n2.Reservar entradas \n3.Ver asientos disponibles  \n4.Ver mis reservas \n5.Salir") #Menu principal para el usuario 
            opcion=input("Ingresé su opción: ") #ps ingrese y ya

# ----------- Ver cartelera ---------------------------------------------------------------

            if opcion=="1":
                print("CARTELERA DE PELICULAS DISPONIBLES")
                for i in range(len(peliculas)): #Recorremos la lista de peliculas
                    print("-".center(100,"-"))
                    print(f"{peliculas[i][0]} \n\nsinopsis: \n{peliculas[i][1]} \n\nDuración: {peliculas[i][2]}") #Mostramos el nombre, sinopsis y duración de la pelicula la i es una variable que va desde 0 hasta la cantida de pelicula
                    print("-".center(100,"-")) #Linea decorativa

# ----------- Reservar entradas ------------------------------------------------------------------------

            elif opcion=="2":
                print("RESERVA DE ENTRADAS") 
                while True:
                    print("Peliculas disponibles para reservar entradas:")
                    for i in range(len(peliculas)): #Recorremos la lista de peliculas
                        print(f"{peliculas[i][0]}") #Mostramos las peliculas disponibles solpo los npombres
                        print("-".center(100,"-"))
                    pelicula_reservar=input("Ingresé el nombre de la pelicula que desea reservar: ").lower()# Se le pregunta al usuario que pelicula deseas ver.lower para convertir a minusculas
                    j=[i[0].lower() for i in peliculas] #Lista para convertir a minusculas los nombres de las peliculas Y guardarlas en la variable j para luego compararlas 
                    if pelicula_reservar in j: #Si la pelicula ingresada por el usuario esta en la lista de peliculas
                        pelicula=peliculas[j.index(pelicula_reservar)] #Guardamos la pelicula seleccionada en una variable
                        while True:
                            dia=input("Ingresé el día que desea ver la pelicula (lunes,martes,miércoles,jueves,viernes,sábado,domingo): ").lower()#.lower para convertir a minusculas
                            if dia in ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]:
                                while True:
                                    hora=input("Ingresé la hora que desea ver la pelicula (8,11,14,17,20): ") #ps ingrese la hora
                                    if hora in ["8","11","14","17","20"]:
                                        while True:
                                            asientos=[]
                                            asientoss=[i for i in pelicula[3][dia][hora].keys()]#Guardamos los asientos disponibles en una variable
                                            for i in range(len(asientoss)): #Recorremos el diccionario de asientos de la pelicula seleccionada
                                                if pelicula[3][dia][hora][i+1]==True: #Si el asiento esta disponible
                                                    asientos.append(asientoss[i])#Mostramos los asientos disponibles
                                            print(f"Asientos disponibles: \n{asientos}")

                                            # Inicia un bucle infinito para permitir al usuario ingresar correctamente
# la cantidad de asientos que desea reservar.
                                            while True:
                                                try:
                                                    asiento_cantidad=int(input(f"Ingresé la cantidad de asiento que desea reservar (1-{len(asientos)}):  "))  # Solicita al usuario que ingrese la cantidad de asientos que quiere reservar

                                                    # Valida si la cantidad solicitada es mayor o igual al total de asientos disponibles. Si lo es, muestra un mensaje de error y vuelve a pedir el dato.
                                                    if asiento_cantidad>=len(asientos):
                                                        print("Error, cantidad de asientos no disponibles")

                                                        continue # Regresa al inicio del bucle para que el usuario intente de nuevo.

                                                    else:
                                                        print("Número de ascientos aceptado") # Si la cantidad ingresada es válida, informa al usuario.

                                                        asientos_revervados=[]# Lista vacía para guardar los asientos que el usuario reservará

                                                        for i in range(asiento_cantidad): # Repite el proceso tantas veces como asientos haya solicitado.

                                                            reserva= int(input(f"Ingresé el número del asiento {i+1} que desea reservar: ")) # Pide al usuario que ingrese el número del asiento que quiere reservar

                                                            # Verifica si el asiento ingresado está en la lista de asientos disponibles.
                                                            if reserva in asientos:
                                                                asientos_revervados.append(reserva)  # Si está disponible, lo agrega a la lista de reservados

                                                             # Marca el asiento como no disponible en la estructura de datos pelicula
                                                                pelicula[3][dia][hora][reserva]=False
                                                            else:
                                                                print("Error, asiento no disponible") # Si el asiento no está disponible, muestra un error y continúa con el siguiente.
                                                                continue

# Si el usuario reservó 4 o más asientos, se aplica un descuento del 10%.

                                                        if len(asientos_revervados)>=4:
                                                            total_compra=(boleta_valor*asiento_cantidad)-(boleta_valor*asiento_cantidad*descuento)
                                                            print(f"Se le a aplicado un descuento del 10% por comprar más de 4 entradas")
                                                        else:
                                                            total_compra=boleta_valor*asiento_cantidad  # Si no cumple el requisito del descuento, paga el valor normal.

                                                        reservas.append((nombres_usuarios[usuario],pelicula[0],dia,hora,asientos_revervados,total_compra)) # Guarda la reserva en la lista reservas con toda la información necesaria: no
 
                                                        print(f"Los asientos reservados fueron: {asientos_revervados} \n para la pelicula: {pelicula[0]} \n el día: {dia} \n a la hora: {hora} \n el valor total a pagar es de: ${total_compra}") # Muestra un resumen de la reserva al usuario

                                                        break # Sale del bucle principal al completar la reserva correctamente.
                                                                    
                                                except ValueError:
                                                    print("Error, ingrese un número") # Si el usuario ingresa un valor que no es número entero, muestra un mensaje de error

                                                    continue # Permite que el usuario intente de nuevo

                                            break # Este break final está fuera del try/except y asegura que, una vez realizada la reserva correctamente, el programa salga completamente del bucle principal.
                                            
                                                
                                    else:
                                        print("Error, hora incorrecta")
                                        continue #vuelve al inicio del while
                                    break
                            else:
                                print("Error, dia incorrecto")
                                continue
                            break
                            
                    else:
                        print("Error, pelicula no disponible")
                        continue
                    break
            elif opcion=="3":
                print("ASIENTOS DISPONIBLES")
                while True:
                    print("Peliculas disponibles para reservar entradas:")
                    for i in range(len(peliculas)): #Recorremos la lista de peliculas
                        print("-".center(100,"-"))
                        print(f"{peliculas[i][0]}") #Mostramos las peliculas disponibles solpo los npombres
                        print("-".center(100,"-"))
                    pelicula_reservar=input("Ingresé el nombre de la pelicula que desea revisar: ").lower()# Se le pregunta al usuario que pelicula deseas ver.lower para convertir a minusculas
                    j=[i[0].lower() for i in peliculas]
                    if pelicula_reservar in j:
                        pelicula=peliculas[j.index(pelicula_reservar)] #Guardamos la pelicula seleccionada en una variable
                        while True:
                            dia=input("Ingresé el día que desearevisar de la pelicula la pelicula (lunes,martes,miércoles,jueves,viernes,sábado,domingo): ").lower()#.lower para convertir a minusculas
                            if dia in ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]:
                                while True:
                                    hora=input("Ingresé la hora que desea revisar de la pelicula (8,11,14,17,20): ") 
                                    if hora in ["8","11","14","17","20"]:
                                        while True:
                                            asientos=[]
                                            asientoss=[i for i in pelicula[3][dia][hora].keys()]#Guardamos los asientos disponibles en una variable
                                            for i in range(len(asientoss)): #Recorremos el diccionario de asientos de la pelicula seleccionada
                                                if pelicula[3][dia][hora][i+1]==True: #Si el asiento esta disponible
                                                    asientos.append(asientoss[i])#Mostramos los asientos disponibles
                                            print(f"Asientos disponibles: \n{asientos}")
                                            break
                                    else:
                                        print("Error, hora incorrecta")
                                        continue
                                    break
                            else:
                                print("Error, dia incorrecto")
                                continue
                            break
                            
                    else:
                        print("Error, pelicula no disponible")
                        continue
                    break
            elif opcion=="4":
                print("MIS RESERVAS")
                reservass=[]
                for i in range(len(reservas)):
                    if reservas[i][0]==nombres_usuarios[usuario]: #Si el nombre del usuario es igual al nombre de la reserva
                        reservass.append(reservas[i]) #Se agrega la reserva a la lista de reservas del usuario
                if len(reservass)==0:
                    print("No tiene reservas")
                else:
                    for i in range(len(reservass)): #Recorremos la lista de peliculas
                        print("-".center(100,"-")) 
                        print(f"Reserva {i+1}: \nNombre: {reservass[i][0]} \nPelicula: {reservass[i] [1]} \nDía: {reservass[i][2]} \nHora: {reservass[i][3]} \nAsientos: {reservass[i][4]} \nValor total pagado: ${reservass[i][5]}") #Mostramos el nombre, sinopsis y duración de la pelicula la i es una variable que va desde 0 hasta 6 guardado dentro de una tupla dentro de una lista pasada a una lista especial con el nombre del usuario
                        print("-".center(100,"-"))
            elif opcion=="5":
                print("Gracias por usar el sistema de reservas del cine mundo S.A")
                comprobante=False #se cierra la sesion
                break
            else:
                print("Error, opción no valida")
    if opcion=="5": #final del programa
          break #sale del while True principal y finaliza el programa