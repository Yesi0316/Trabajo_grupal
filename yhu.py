dias={0:"Lunes",1:"Martes",2:"Miercoles",3:"Jueves",4:"Viernes",5:"Sabado",6:"Domingo"}

#sala
sala1={}
for a in range(1,51):
    sala1[a]=True
sala_1=[sala1.copy(),sala1.copy(),sala1.copy(),sala1.copy(),sala1.copy(),sala1.copy()]
sala_2=[sala1.copy(),sala1.copy(),sala1.copy(),sala1.copy(),sala1.copy(),sala1.copy()]

#peliculas
pelicula1=("Avengers","tipos con superpoderes",(6,8,10,12,14,16,18,20,22),(0,1,2))
peliculas=[pelicula1]
print(f"nombre: {pelicula1[0]} \n sinopsis: {pelicula1[1]} \n horarios: {pelicula1[2]} \n dias: {[dias[i] for i in pelicula1[3]]}")

#opciones
pp=input("Ingrese la pelicula que va a ver: ")
if pp in [i for i in peliculas[0]]:
    
    print(f"Los dias que se proyecta son: {[dias[i] for i in pelicula1[3]]}")
    print(f"en estos horarios: {pelicula1[2]}")
    da=input("Ingrese el dia que va a ir: ")
    if dias[da] in peliculas[peliculas.index(pp)][3]:
        ho=input("Ingrese el horario que va a ir: ")
        if ho in peliculas[peliculas.index(pp)][2]:
            print("Estos son los asientos disponibles")
            for silla in sala_1[da]:
                if sala_1[da][silla]==True:
                    print(silla,end=", ")
            asien=int(input("\nIngrese el asiento que desea: "))
            if sala_1[da][asien]==True:
                sala_1[da][asien]=False
                print("Su asiento ha sido reservado")
            else:
                print("El asiento no esta disponible")
        else:
            print("El horario no es valido")