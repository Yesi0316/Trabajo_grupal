print("SISTEMA DE RESERVA DE PELICULAS S.A")



peliculas=[]
def pelicula_crear (nombre, sinopsis, duracion, horario):
    peliculas.append(({"nombre de la pelicula": nombre,
            "sinopsis":sinopsis,
            "duracion": duracion, 
            "horarios":horario
}))
horarios_pelicula_1= {
    "martes": {
        "18:00": {"sala": 1, "asientos":[1]},
        "12:00": {"sala": 1, "asientos": sala_1 },
        "13:00": {"sala": 1, "asientos":[1, 2, 4, 7, 8, 10, 13, 14, 15, 17, 18, 19, 21, 24, 25, 28, 29, 31, 32, 34, 35, 38, 45, 46]}
    },
    "jueves": {
        "18:30": {"sala": 1, "asientos": [1, 4, 5, 7, 8, 9, 11, 12, 13, 15, 17, 20, 21, 22, 23, 28, 30, 31, 36, 44, 49]},
         "15:00": {"sala": 1, "asientos":[3, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 28, 29, 32, 33, 39, 40, 44]},
          "14:00": {"sala": 1, "asientos": [1, 2, 4, 6, 8, 9, 11, 12, 14, 16, 19, 21, 24, 27, 31, 33, 38, 41, 49]}
    },
    "viernes": {
        "11:00": {"sala": 1, "asientos": [2, 3, 5, 7, 8, 10, 13, 14, 15, 17, 19, 20, 22, 24, 28, 30, 32, 34, 35, 39, 43, 46] },
        "18:00": {"sala": 1, "asientos":[1, 3, 5, 6, 7, 9, 10, 11, 13, 15, 16, 18, 19, 21, 23, 25, 27, 29, 30, 33, 36, 40, 42, 44, 48]},
        "17:30": {"sala": 1, "asientos": [4, 6, 8, 9, 12, 14, 18, 20, 22, 25, 28, 31, 34, 37, 40, 45, 50]}
    }
}

pelicula_1= pelicula_crear ("encantada", "La bella princesa Giselle es transportada por un hechizo de la malvada reina Narissa desde su mágico mundo a la moderna y caótica Manhattan actual.Inmersaen un entorno que desconoce,Giselle deambula por un mundo desorganizado.", "1h 47m", horarios_pelicula_1)

print(pelicula_1)

horarios_pelicula_2= {
    "martes": {
        "18:00": {"sala": 2, "asientos": [1, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 18, 20, 21, 22, 25, 29, 32, 34, 38, 40, 41, 43, 47, 50] },
        "12:00": {"sala": 2, "asientos":[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 27, 33, 39, 48]},
        "13:00": {"sala": 2, "asientos":[1, 2, 4, 7, 8, 10, 13, 14, 15, 17, 18, 19, 21, 24, 25, 28, 29, 31, 32, 34, 35, 38, 45, 46]}
    },
    "jueves": {
        "18:30": {"sala": 2, "asientos": [1, 4, 5, 7, 8, 9, 11, 12, 13, 15, 17, 20, 21, 22, 23, 28, 30, 31, 36, 44, 49]},
         "15:00": {"sala": 2, "asientos":[3, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 28, 29, 32, 33, 39, 40, 44]},
          "14:00": {"sala": 2, "asientos": [1, 2, 4, 6, 8, 9, 11, 12, 14, 16, 19, 21, 24, 27, 31, 33, 38, 41, 49]}
    },
    "viernes": {
        "11:00": {"sala": 2, "asientos": [2, 3, 5, 7, 8, 10, 13, 14, 15, 17, 19, 20, 22, 24, 28, 30, 32, 34, 35, 39, 43, 46] },
        "18:00": {"sala": 2, "asientos":[1, 3, 5, 6, 7, 9, 10, 11, 13, 15, 16, 18, 19, 21, 23, 25, 27, 29, 30, 33, 36, 40, 42, 44, 48]},
        "17:30": {"sala": 2, "asientos": [4, 6, 8, 9, 12, 14, 18, 20, 22, 25, 28, 31, 34, 37, 40, 45, 50]}
    }
}

dias_p2= ("lunes", "miercoles", "viernes") #dias donde se pueden ver unicamente, del resto pilas
horas_lunes_p2= ("20:00", "18:00", "15:00") #horas habiles para el dia lunes
horas_miercoles_p2= ("17:30", "12:00", "11:00") #horas habiles para el dia miercoles
horas_viernes_p2= ("18:00", "12:00", "13:00") #horas habiles para el dia viernes
salas_p2= (1,2,3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p2_lunes_20_00=[12, 35, 7, 22, 49, 5, 28, 41]
asientos_p2_lunes_18_00=[3, 30, 1, 46, 23, 9, 18, 36]
asientos_p2_lunes_15_00= [47, 17, 50, 33, 43, 39, 14, 44]
asientos_p2_miercoles_17_30=[2, 24, 38, 13, 4, 8, 34, 32]
asientos_p2_miercoles_12_00=[19, 31, 48, 21, 10, 42, 6, 27]
asientos_p2_miercoles_11_00=[16, 15, 25, 29, 11, 26, 37, 20]
asientos_p2_viernes_18_00=[21, 3, 43, 13, 5, 41, 23, 19]
asientos_p2_viernes_12_00= [37, 26, 39, 49, 35, 16, 14, 7]
asientos_p2_viernes_13_00= [9, 33, 1, 27, 44, 24, 15, 25]

# diccionario donde se muestra las horas y salas de todos los dias disponibles

pelicula_2= {"nombre de la pelicula":"huntrix", #nombre de la pelicula
             "sinopsis":"""Un supergrupo de k-pop usa sus poderes secretos para proteger a sus fans de amenazassobrenaturales y de una banda rival de chicos decididos a robar corazones y mentes. """, #aqui se muestra la sinopsis de la pelicula
            "duracion": "1h 31m", #duracion de la peli
            "dias disponibles": dias_p2, #dias disponibles de la peli
            #horas de las peliculas
            "horas de la pelicula lunes": horas_lunes_p2,
            "horas de la pelicula miercoles": horas_miercoles_p2,
            "horas de la pelicula viernes": horas_viernes_p2,
            #salas correspondientes con el dia y la hora respectivamente
            "sala lunes 20:00":salas_p2[1],
            "sala lunes 18:00":salas_p2[0],
            "sala lunes 15:00":salas_p2[2],
            "sala miercoles 17:30":salas_p2[1],
            "sala miercoles 12:00":salas_p2[0],
            "sala miercoles 11:00":salas_p2[2],
            "sala viernes 18:00":salas_p2[1],
            "sala viernes 12:00":salas_p2[0],
            "sala viernes 13:00":salas_p2[2],
            #aqui se muestran los asintos disponibles de los dias con las horas
            "asientos disponibles lunes 20:00": asientos_p2_lunes_20_00,
            "asientos disponibles lunes 18:00": asientos_p2_lunes_18_00,
            "asientos disponibles lunes 15:00": asientos_p2_lunes_15_00,
            "asientos disponibles miercoles 17:30": asientos_p2_miercoles_17_30,
            "asientos disponibles miercoles 12:00": asientos_p2_miercoles_12_00,
            "asientos disponibles miercoles 11:00": asientos_p2_miercoles_11_00,
            "asientos disponibles viernes 18:00": asientos_p2_viernes_18_00,
            "asientos disponibles viernes 12:00": asientos_p2_viernes_12_00,
            "asientos disponibles viernes 13:00": asientos_p2_viernes_13_00,
              }
#informacion de la pelicula 3
             
dias_p3= ("martes","jueves","viernes")#dias donde se pueden ver unicamente, del resto pilas
horas_martes_p3= ("13:00","17:00","20:00") #horas habiles para el dia martes
horas_jueves_p3= ("12:00","15:00","20:00") #horas habiles para el dia jueves
horas_viernes_p3= ("12:00","16:00","20:00") #horas habiles para el dia viernes
salas_p3= (1,2,3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p3_martes_13_00= [1,2,3,4,5,6,7,8] #asientos disponibles con la hora del dia martes
asientos_p3_martes_17_00= [2,5,8,11,14,17,20,23] #asientos disponibles con la hora del dia martes
asientos_p3_martes_20_00= [1,2,3,4,5,6,7,8] #asientos disponibles con la hora del dia martes
asientos_p3_jueves_12_00= [3,5,7,9,11,13,15,17] #asientos disponibles con la hora del dia jueves
asientos_p3_jueves_15_00= [1,2,4,6,8,10,12,14]  #asientos disponibles con la hora del dia jueves
asientos_p3_jueves_20_00= [1,5,6,7,8,9,10,12] #asientos disponibles con la hora del dia jueves
asientos_p3_viernes_12_00= [7,42,15,48,3,21,29,46]   #asientos disponibles con la hora del dia viernes
asientos_p3_viernes_16_00= [17,3,45,28,12,39,6,21]  #asientos disponibles con la hora del dia viernes
asientos_p3_viernes_20_00= [12,27,43,6,21,38,2,49] #asientos disponibles con la hora del dia viernes

# diccionario donde se muestra las horas y salas de todos los dias disponibles

pelicula_3= {"nombre de la pelicula":"spiderman", #nombre de la pelicula
             "sinopsis":"""Luego de sufrir la picadura de una araña genéticamente modificada, un estudiante de secundaria tímido y torpe adquiere increíbles capacidades como arácnido. Pronto comprenderá que su misión es utilizarlas para luchar contrael mal y defender a sus vecinos.""", #aqui se muestra la sinopsis de la pelicula
            "duracion": "2h 6m", #duraciond de la peli
            "dias disponibles":dias_p3, #dias disponibles de la peli
            #horas de las peliculas
            "horas de la pelicula martes":horas_martes_p3,
            "horas de la pelicula jueves":horas_jueves_p3,
            "horas de la pelicula viernes":horas_viernes_p3,
            #salas disponibles de la pelicula de las horas de la peli
            "sala martes 13:00":salas_p3[1],
            "sala martes 17:00":salas_p3[2],
            "sala martes 20:00":salas_p3[0],
            "sala jueves 12:00":salas_p3[1],
            "sala jueves 15:00":salas_p3[2],
            "sala jueves 20:00":salas_p3[0],
            "sala viernes 12:00":salas_p3[1],
            "sala viernes 16:00":salas_p3[2],
            "sala viernes 20:00":salas_p3[0],
            #aqui se muestran los asintos disponibles de los dias con las horas
            "asientos disponibles martes 13:00":asientos_p3_martes_13_00,
            "asientos disponibles martes 17:00":asientos_p3_martes_17_00,
            "asientos disponibles martes 20:00":asientos_p3_martes_20_00,
            "asientos disponibles jueves 12:00":asientos_p3_jueves_12_00,
            "asientos disponibles jueves 15:00":asientos_p3_jueves_15_00,
            "asientos disponibles jueves 20:00":asientos_p3_jueves_20_00,
            "asientos disponibles viernes 12:00":asientos_p3_viernes_12_00,
            "asientos disponibles viernes 16:00":asientos_p3_viernes_16_00,
            "asientos disponibles viernes 20:00":asientos_p3_viernes_20_00}




#Información de la película 4 guardada 

dias_p4 = ("lunes", "miercoles", "viernes")#dias donde se pueden ver unicamente, del resto pilas
horas_lunes_p4 = ("14:00", "16:00", "19:00") #horas habiles para el dia lunes
horas_miercoles_p4 = ("11:30", "13:00", "17:00") #horas habiles para el dia miercoles
horas_viernes_p4 = ("10:00", "15:00", "20:00") #horas habiles para el dia viernes
salas_p4 = (1, 2, 3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p4_lunes_14_00 = [3, 12, 25, 38, 44, 7, 29, 50] #asientos disponibles con la hora del dia lunes
asientos_p4_lunes_16_00 = [5, 16, 23, 42, 9, 31, 18, 36] #asientos disponibles con la hora del dia luness
asientos_p4_lunes_19_00 = [48, 21, 33, 10, 14, 41, 26] #asientos disponibles con la hora del dia lunes
asientos_p4_miercoles_11_30 = [8, 2, 17, 34, 45, 6, 28, 24] #asientos disponibles con la hora del dia miercoles
asientos_p4_miercoles_13_00 = [19, 4, 11, 27, 46, 35, 15, 22] #asientos disponibles con la hora del dia miercoles
asientos_p4_miercoles_17_00 = [30, 47, 13, 37, 20, 32, 39, 43] #asientos disponibles con la hora del dia miercoles
asientos_p4_viernes_10_00 = [40, 49, 5, 12, 33, 18, 6, 22] #asientos disponibles con la hora del dia viernes
asientos_p4_viernes_15_00 = [7, 26, 24, 1, 29, 9, 35, 14] #asientos disponibles con la hora del dia viernes
asientos_p4_viernes_20_00 = [3, 11, 20, 38, 44, 27, 16, 42] #asientos disponibles con la hora del dia viernes

# diccionario donde se muestra las horas y salas de todos los dias disponibles

pelicula_4 = {
    "nombre de la pelicula": "intensamente", #nombre de la pelicula
    "sinopsis":"""Riley acaba de nacer y en el centro de control de su pequeña mente sólo hay sitio
    para Alegría. Poco después aparece Tristeza y, más tarde, Ira, Miedo y Asco.
    Las cinco emociones tendrán que ayudar a la niña cuando, ya con 11 años, su familia
    se mude desde su idílico pueblo del Medio Oeste estadounidense a la enorme e intimidante ciudad de San Francisco.
    Tras una serie de acontecimientos, Alegría y Tristeza tendrán que trabajar juntas para salvar a Riley.""", #aqui se muestra la sinopsis de la pelicula
    "duracion": "1h 35m", #duracion de la peli
    "dias disponibles":dias_p4, #dias disponibles de la peli
    #horas de las peliculas
    "horas de la pelicula lunes": horas_lunes_p4,
    "horas de la pelicula miercoles": horas_miercoles_p4,
    "horas de la pelicula viernes": horas_viernes_p4,
    #salas disponibles de la pelicula de las horas de la peli
    "sala lunes 14:00": salas_p4[0],
    "sala lunes 16:00": salas_p4[1],
    "sala lunes 19:00": salas_p4[2],
    "sala miercoles 11:30": salas_p4[2],
    "sala miercoles 13:00": salas_p4[1],
    "sala miercoles 17:00": salas_p4[0],
    "sala viernes 10:00": salas_p4[1],
    "sala viernes 15:00": salas_p4[2],
    "sala viernes 20:00": salas_p4[0],
    #aqui se muestran los asintos disponibles de los dias con las horas
    "asientos disponibles lunes 14:00": asientos_p4_lunes_14_00,
    "asientos disponibles lunes 16:00": asientos_p4_lunes_16_00,
    "asientos disponibles lunes 19:00": asientos_p4_lunes_19_00,
    "asientos disponibles miercoles 11:30": asientos_p4_miercoles_11_30,
    "asientos disponibles miercoles 13:00": asientos_p4_miercoles_13_00,
    "asientos disponibles miercoles 17:00": asientos_p4_miercoles_17_00,
    "asientos disponibles viernes 10:00": asientos_p4_viernes_10_00,
    "asientos disponibles viernes 15:00": asientos_p4_viernes_15_00,
    "asientos disponibles viernes 20:00": asientos_p4_viernes_20_00,
}

#Información de la película 5 guardada 

dias_p5 = ("martes", "jueves", "sabado") #dias donde se pueden ver unicamente, del resto pilas
horas_martes_p5 = ("13:00", "16:30", "19:30") #horas habiles para el dia martes
horas_jueves_p5 = ("10:00", "12:45", "17:15") #horas habiles para el dia jueves
horas_sabado_p5 = ("11:00", "14:30", "20:00") #horas habiles para el dia sabado
salas_p5 = (1, 2, 3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p5_martes_13_00 = [4, 17, 22, 35, 48, 6, 31, 13] #asientos disponibles con la hora del dia martes
asientos_p5_martes_16_30 = [11, 28, 2, 36, 7, 44, 25, 49] #asientos disponibles con la hora del dia martes
asientos_p5_martes_19_30 = [12, 1, 39, 26, 21, 19, 32, 8] #asientos disponibles con la hora del dia martes
asientos_p5_jueves_10_00 = [5, 14, 46, 24, 3, 10, 33, 42] #asientos disponibles con la hora del dia jueves
asientos_p5_jueves_12_45 = [40, 18, 23, 9, 38, 15, 50, 30]#asientos disponibles con la hora del dia jueves 
asientos_p5_jueves_17_15 = [16, 29, 43, 41, 34, 27, 20, 45] #asientos disponibles con la hora del dia jueves
asientos_p5_sabado_11_00 = [47, 37, 6, 22, 11, 14, 29, 33] #asientos disponibles con la hora del dia sabado
asientos_p5_sabado_14_30 = [2, 8, 19, 5, 10, 17, 31, 40] #asientos disponibles con la hora del dia sabado
asientos_p5_sabado_20_00 = [9, 26, 13, 15, 30, 44, 39, 24] #asientos disponibles con la hora del dia sabado

# diccionario donde se muestra las horas y salas de todos los dias disponibles

pelicula_5 = {
    "nombre de la pelicula": "barbie", #nombre de la pelicula
    "sinopsis":"""Después de ser expulsada de Barbieland por no ser una muñeca de aspecto perfecto, Barbie parte hacia el mundo humano para encontrar la verdadera felicidad.""",#aqui se muestra la sinopsis de la pelicula
    "duracion": "1h 54m", #duracion de la peli
    "dias disponibles": dias_p5, #dias disponibles de la peli
    #horas de las peliculas
    "horas de la pelicula martes": horas_martes_p5,
    "horas de la pelicula jueves": horas_jueves_p5,
    "horas de la pelicula sabado": horas_sabado_p5,
    #salas disponibles de la pelicula de las horas de la peli
    "sala martes 13:00": salas_p5[0],
    "sala martes 16:30": salas_p5[1],
    "sala martes 19:30": salas_p5[2],
    "sala jueves 10:00": salas_p5[1],
    "sala jueves 12:45": salas_p5[0],
    "sala jueves 17:15": salas_p5[2],
    "sala sabado 11:00": salas_p5[2],
    "sala sabado 14:30": salas_p5[0],
    "sala sabado 20:00": salas_p5[1],
    #aqui se muestran los asintos disponibles de los dias con las horas
    "asientos disponibles martes 13:00": asientos_p5_martes_13_00,
    "asientos disponibles martes 16:30": asientos_p5_martes_16_30,
    "asientos disponibles martes 19:30": asientos_p5_martes_19_30,
    "asientos disponibles jueves 10:00": asientos_p5_jueves_10_00,
    "asientos disponibles jueves 12:45": asientos_p5_jueves_12_45,
    "asientos disponibles jueves 17:15": asientos_p5_jueves_17_15,
    "asientos disponibles sabado 11:00": asientos_p5_sabado_11_00,
    "asientos disponibles sabado 14:30": asientos_p5_sabado_14_30,
    "asientos disponibles sabado 20:00": asientos_p5_sabado_20_00,
}

#información de la pelicula 6 guardada

dias_p6 = ("lunes", "miercoles", "viernes")#dias donde se pueden ver unicamente, del resto pilas
horas_lunes_p6 = ("13:15", "16:00", "18:45") #horas habiles para el dia lunes
horas_miercoles_p6 = ("11:00", "14:20", "19:00") #horas habiles para el dia miercoles
horas_viernes_p6 = ("10:30", "15:00", "21:00") #horas habiles para el dia viernes
salas_p6 = (1, 2, 3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p6_lunes_13_15 = [14, 38, 2, 47, 26, 9, 44, 21]  #asientos disponibles con la hora del dialunes
asientos_p6_lunes_16_00 = [3, 16, 35, 8, 22, 11, 46, 29] #asientos disponibles con la hora del dia lunes
asientos_p6_lunes_18_45 = [1, 31, 5, 40, 19, 6, 27, 33] #asientos disponibles con la hora del dia lunes
asientos_p6_miercoles_11_00 = [10, 24, 45, 13, 7, 37, 12, 41] #asientos disponibles con la hora del dia miercoles
asientos_p6_miercoles_14_20 = [18, 36, 48, 4, 32, 15, 20, 28] #asientos disponibles con la hora del dia mercoles
asientos_p6_miercoles_19_00 = [30, 23, 17, 42, 43, 39, 34, 25] #asientos disponibles con la hora del dia miercoles
asientos_p6_viernes_10_30 = [49, 14, 38, 19, 6, 3, 24, 13] #asientos disponibles con la hora del dia viernes
asientos_p6_viernes_15_00 = [9, 45, 22, 33, 7, 29, 2, 47] #asientos disponibles con la hora del dia viernes
asientos_p6_viernes_21_00 = [11, 31, 1, 40, 26, 35, 8, 5] #asientos disponibles con la hora del dia viernes

# diccionario donde se muestra las horas y salas de todos los dias disponibles

pelicula_6 = {
    "nombre de la pelicula": "como entrenar a tu dragón 3", #nombre de la pelicula
  "sinopsis":"""El joven vikingo Hipo parece haber conseguido que dragones y humanos convivan en paz.  
  Sin embargo, su sueño y el de los demás habitantes de la, isla de Mema no es compartido por otros vikingos,
  especialmente por los brutales cazadores de dragones.""", #aqui se muestra la sinopsis de la pelicula
    "duracion": "1h 47m", #duracion de la peli
    "dias disponibles": dias_p6, #dias disponibles
    #horas de las peliculas
    "horas de la pelicula lunes": horas_lunes_p6,
    "horas de la pelicula miercoles": horas_miercoles_p6,
    "horas de la pelicula viernes": horas_viernes_p6,
    #salas disponibles de la pelicula de las horas de la peli
    "sala lunes 13:15": salas_p6[0],
    "sala lunes 16:00": salas_p6[1],
    "sala lunes 18:45": salas_p6[2],
    "sala miercoles 11:00": salas_p6[1],
    "sala miercoles 14:20": salas_p6[0],
    "sala miercoles 19:00": salas_p6[2],
    "sala viernes 10:30": salas_p6[2],
    "sala viernes 15:00": salas_p6[0],
    "sala viernes 21:00": salas_p6[1], 
    #aqui se muestran los asintos disponibles de los dias con las horas
    "asientos disponibles lunes 13:15": asientos_p6_lunes_13_15,
    "asientos disponibles lunes 16:00": asientos_p6_lunes_16_00,
    "asientos disponibles lunes 18:45": asientos_p6_lunes_18_45,
    "asientos disponibles miercoles 11:00": asientos_p6_miercoles_11_00,
    "asientos disponibles miercoles 14:20": asientos_p6_miercoles_14_20,
    "asientos disponibles miercoles 19:00": asientos_p6_miercoles_19_00,
    "asientos disponibles viernes 10:30": asientos_p6_viernes_10_30,
    "asientos disponibles viernes 15:00": asientos_p6_viernes_15_00,
    "asientos disponibles viernes 21:00": asientos_p6_viernes_21_00,
}
#información de la pelicula 7 guardada

dias_p7 = ("lunes", "miercoles", "viernes")#dias donde se pueden ver unicamente, del resto pilas
horas_lunes_p7 = ("12:00", "15:30", "19:00") #horas habiles para el dia lunes
horas_miercoles_p7 = ("10:15", "13:45", "18:20") #horas habiles para el dia miercoles
horas_viernes_p7 = ("11:30", "16:10", "20:40")#horas habiles para el dia viernes
salas_p7 = (1, 2, 3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p7_lunes_12_00 = [5, 18, 22, 37, 40, 11, 29, 44] #asientos disponibles con la hora del dia jueves
asientos_p7_lunes_15_30 = [2, 13, 26, 33, 7, 19, 46, 28] #asientos disponibles con la hora del dia jueves
asientos_p7_lunes_19_00 = [9, 15, 30, 41, 6, 23, 39, 48] #asientos disponibles con la hora del dia jueves
asientos_p7_miercoles_10_15 = [3, 17, 35, 21, 14, 47, 25, 42] #asientos disponibles con la hora del dia miercoles
asientos_p7_miercoles_13_45 = [8, 20, 36, 4, 27, 12, 31, 45] #asientos disponibles con la hora del dia miercoles
asientos_p7_miercoles_18_20 = [16, 32, 50, 1, 28, 34, 10, 43] #asientos disponibles con la hora del dia miercoles
asientos_p7_viernes_11_30 = [22, 37, 5, 49, 18, 9, 40, 14] #asientos disponibles con la hora del dia viernes
asientos_p7_viernes_16_10 = [33, 46, 2, 7, 26, 13, 19, 28] #asientos disponibles con la hora del dia viernes
asientos_p7_viernes_20_40 = [6, 41, 15, 9, 30, 48, 39, 23] #asientos disponibles con la hora del dia viernes

# diccionario donde se muestra las horas y salas de todos los dias disponibles

pelicula_7={  "nombre de la pelicula": "hotel transilvania 3", #nombre de la pelicula
    "sinopsis":"""Drácula y su familia se embarcan en un lujoso crucero para monstruos. Lo que empieza como unas vacaciones tranquilas se complica cuando Drácula se enamora de la misteriosa capitana del barco, sin saber que ella es descendiente de Van Helsing y tiene un plan secreto para acabar con todos los monstruos.""", #aqui se muestra la sinopsis de la pelicula
    "dias disponibles": dias_p7, #dias disponibles de la peli
    "duracion": "1h 37m",  #duracion de la peli
    #horas de las peliculas
    "horas de la pelicula lunes": horas_lunes_p7,
    "horas de la pelicula miercoles": horas_miercoles_p7, 
    "horas de la pelicula viernes": horas_viernes_p7,
    #salas disponibles de la pelicula de las horas de la peli
    "sala lunes 12:00": salas_p7[0],
    "sala lunes 15:30": salas_p7[1],
    "sala lunes 19:00": salas_p7[2],
    "sala miercoles 10:15": salas_p7[1],
    "sala miercoles 13:45": salas_p7[0],
    "sala miercoles 18:20": salas_p7[2],
    "sala viernes 11:30": salas_p7[2],
    "sala viernes 16:10": salas_p7[0],
    "sala viernes 20:40": salas_p7[1],
    #aqui se muestran los asintos disponibles de los dias con las horas
    "asientos disponibles lunes 12:00": asientos_p7_lunes_12_00,
    "asientos disponibles lunes 15:30": asientos_p7_lunes_15_30,
    "asientos disponibles lunes 19:00": asientos_p7_lunes_19_00,
    "asientos disponibles miercoles 10:15": asientos_p7_miercoles_10_15,
    "asientos disponibles miercoles 13:45": asientos_p7_miercoles_13_45,
    "asientos disponibles miercoles 18:20": asientos_p7_miercoles_18_20,
    "asientos disponibles viernes 11:30": asientos_p7_viernes_11_30,
    "asientos disponibles viernes 16:10": asientos_p7_viernes_16_10,
    "asientos disponibles viernes 20:40": asientos_p7_viernes_20_40,
}

#información de la pelicula 8 guardada

dias_p8 = ("martes", "jueves", "sabado")#dias donde se pueden ver unicamente, del resto pilas
horas_martes_p8 = ("11:00", "14:30", "18:10")#horas habiles para el dia martes
horas_jueves_p8 = ("12:15", "16:00", "20:20")#horas habiles para el dia jueves
horas_sabado_p8 = ("10:45", "15:30", "21:15")#horas habiles para el dia sabado
salas_p8 = (1, 2, 3) #salas disponibles
#asiesntos disponibles de los dias y las horas
asientos_p8_martes_11_00 = [7, 22, 35, 48, 12, 40, 29, 18] #asientos disponibles con la hora del dia martes
asientos_p8_martes_14_30 = [4, 17, 33, 26, 45, 10, 21, 39] #asientos disponibles con la hora del dia martes
asientos_p8_martes_18_10 = [6, 31, 50, 3, 28, 14, 42, 23] #asientos disponibles con la hora del dia martes
asientos_p8_jueves_12_15 = [11, 27, 46, 19, 5, 37, 20, 44] #asientos disponibles con la hora del dia jueves
asientos_p8_jueves_16_00 = [8, 25, 32, 15, 2, 36, 49, 41] #asientos disponibles con la hora del dia jueves
asientos_p8_jueves_20_20 = [9, 30, 47, 13, 34, 6, 22, 16] #asientos disponibles con la hora del dia jueves
asientos_p8_sabado_10_45 = [1, 24, 38, 7, 29, 43, 12, 40] #asientos disponibles con la hora del dia sabado
asientos_p8_sabado_15_30 = [18, 33, 46, 9, 27, 4, 50, 25] #asientos disponibles con la hora del dia sabado 
asientos_p8_sabado_21_15 = [14, 35, 48, 20, 31, 2, 37, 11]  #asientos disponibles con la hora del dia sabado

# diccionario donde se muestra las horas y salas de todos los dias disponibles
pelicula_8 = {
    "nombre de la pelicula": "turning red", #nombre de la pelicula
    "dias disponibles": dias_p8, #dias disponibles de la peli
    "duracion": "1h 40m",  #duracion de la peli
    "sinopsis":"NO TABA",
    #horas de las peliculas
    "horas de la pelicula martes": horas_martes_p8,
    "horas de la pelicula jueves": horas_jueves_p8,
    "horas de la pelicula sabado": horas_sabado_p8,
    #salas disponibles de la pelicula de las horas de la peli
    "sala martes 11:00": salas_p8[0],
    "sala martes 14:30": salas_p8[1],
    "sala martes 18:10": salas_p8[2],
    "sala jueves 12:15": salas_p8[1],
    "sala jueves 16:00": salas_p8[0],
    "sala jueves 20:20": salas_p8[2],
    "sala sabado 10:45": salas_p8[2],
    "sala sabado 15:30": salas_p8[0],
    "sala sabado 21:15": salas_p8[1],
    #aqui se muestran los asintos disponibles de los dias con las horas
    "asientos disponibles martes11:00": asientos_p8_martes_11_00,
    "asientos disponibles martes14:30": asientos_p8_martes_14_30,
    "asientos disponibles martes18:10": asientos_p8_martes_18_10,
    "asientos disponibles jueves12:15": asientos_p8_jueves_12_15,
    "asientos disponibles jueves16:00": asientos_p8_jueves_16_00,
    "asientos disponibles jueves20:20": asientos_p8_jueves_20_20,
    "asientos disponibles sabado10:45": asientos_p8_sabado_10_45,
    "asientos disponibles sabado15:30": asientos_p8_sabado_15_30,
    "asientos disponibles sabado21:15": asientos_p8_sabado_21_15,
}


cuentas= {"yesickrivera@gmail.com":"123"}#Diccionario con las cuentas registradas (correo,contraseña)
nombres_usuarios={"yesickrivera@gmail.com":"Yesi"}
boleta_valor=10000 
asiento_revervados=[]
contador= 1
descuento= boleta_valor*0.10

cartelera=f" Las películas disponibles son: \n {pelicula_1['nombre de la pelicula']} \n duración: {pelicula_1['duracion']} \n Sinopsis: {pelicula_1['sinopsis']} \n {pelicula_2['nombre de la pelicula']} \n duración: {pelicula_2['duracion']} \n Sinopsis: {pelicula_2['sinopsis']} \n {pelicula_3['nombre de la pelicula']} \n duración: {pelicula_3['duracion']} \n Sinopsis: {pelicula_3['sinopsis']} \n {pelicula_4['nombre de la pelicula']} \n duración: {pelicula_4['duracion']} \n Sinopsis: {pelicula_4['sinopsis']} \n {pelicula_5['nombre de la pelicula']} \n duración: {pelicula_5['duracion']} \n Sinopsis: {pelicula_5['sinopsis']} \n {pelicula_6['nombre de la pelicula']} \n duración: {pelicula_6['duracion']} \n Sinopsis: {pelicula_6['sinopsis']} \n {pelicula_7['nombre de la pelicula']} \n duración: {pelicula_7['duracion']} \n Sinopsis: {pelicula_7['sinopsis']} \n {pelicula_8['nombre de la pelicula']} \n duración: {pelicula_8['duracion']} \n Sinopsis: {pelicula_8['sinopsis']}"
                           
while True:
    print("1.Ver cartelera \n 2.Hacer reserva \n 3.Consultar sillas disponibles \n 4.Salir")
    pregunta_2= input("Ingresé el número correspondiente de la acción que desea realizar: ")
    if pregunta_2=="1":
           print(cartelera)
    elif pregunta_2=="2":
        print(f"RESERVAR \n Las películas disponibles son:{cartelera}")
        pregunta_3=input("Ingresé el nombre de la película que desea ver: ").lower()
        if pregunta_3==pelicula_1["nombre de la pelicula"]:
            print(f"Los días disponibles para ver la pelicula son: {pelicula_1['dias disponibles']}")
            pregunta_4= input("¿Qué día desea ver la película?: ").lower()
            if pregunta_4=="viernes":
                print(f"Las horas disponibles para ver la pelicula el viernes son: {pelicula_1['horas de la peliculas viernes']}")
                pregunta_5=input("Ingresé la hora a la que desea ver la pelicula: ")
                if pregunta_5=="11:00":
                    print(f"Los asientos disponibles son:{pelicula_1['asientos disponibles viernes 11:00']}")
                    pregunta_6=int(input("Ingresé el número del ascientos a reservar (Este no es un número del asiento sino cuantos asientos va a querer): "))
                    while pregunta_6>=contador:
                        asiento_reservado=float(input("Ingresé el número de asciento a reservar:"))
                        if asiento_reservado in pelicula_1["asientos disponibles viernes 11:00"]:
                            print("El asiento se encuentra en la lista")
                            asiento_revervados.append(asiento_reservado)
                            asientos_p1_viernes_11_00.remove(asiento_reservado)
                            contador+=1
                            if len(asiento_revervados)>=4:
                                factura=boleta_valor*contador-(descuento*contador)
                                print(f"El costo de su compra es {factura}")
                                print(f"FACTURA \n película: {pelicula_1['nombre de la pelicula']} \n Día:viernes \n Hora:11:00 \n Sala: {pelicula_1['sala viernes 11:00']} \n Boletas: {len(asiento_revervados)} \n Nùmero de asientos: {asiento_revervados} ")
                                asiento_reservado.clear
                        else:
                            print("El asiento no esta")
    elif pregunta_2=="3":
       pregunta_3=input("Ingresé el nombre de la película que desea ver los asientos disponibles: ").lower()
       if pregunta_3==pelicula_1["nombre de la pelicula"]:
            print(f"Los días disponibles para ver la pelicula son: {pelicula_1['dias disponibles']}")
            pregunta_4= input("¿Qué día desea ver la película?: ").lower()
            if pregunta_4=="viernes":
                print(f"Las horas disponibles para ver la pelicula el viernes son: {pelicula_1['horas de la peliculas viernes']}")
                pregunta_5=input("Ingresé la hora a la que desea ver la pelicula: ")
                if pregunta_5=="11:00":
                    print(f"Los asientos disponibles son:{pelicula_1['asientos disponibles viernes 11:00']}")
    elif pregunta_2=="4":
        print("Gracias por visitar nuestra página, HASTA LUEGO :)")
        break    