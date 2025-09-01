print("SISTEMA DE RESERVA DE PELICULAS S.A")


#Información de la película 1 guardada 

dias_p1= ("martes", "jueves", "viernes")
horas_martes_p1= (18:00, 12:00, 13:00) 
horas_jueves_p1= (18:30, 15:00, 14:00) 
horas_viernes_p1= (11:00, 8:00, 7:30)
salas= (1,2,3)
asientos_p1_martes_18_00= [1, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 18, 20, 21, 22, 25, 29, 32, 34, 38, 40, 41, 43, 47, 50]
asientos_p1_martes_12_00=[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 19, 27, 33, 39, 48]
asientos_p1_martes_13_00=[1, 2, 4, 7, 8, 10, 13, 14, 15, 17, 18, 19, 21, 24, 25, 28, 29, 31, 32, 34, 35, 38, 45, 46]
asientos_p1_jueves_18_30=[1, 4, 5, 7, 8, 9, 11, 12, 13, 15, 17, 20, 21, 22, 23, 28, 30, 31, 36, 44, 49]
asientos_p1_jueves_15_00=[3, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 28, 29, 32, 33, 39, 40, 44]
asientos_p1_jueves_14_00=






pelicula_1= {"nombre de la pelicula":"Encantada",
            "dias disponibles": dias_p1,
            "horas de la pelicula martes": horas_martes_p1,
            "horas de la pelicula jueves": horas_jueves_p1, 
            "horas de la peliculas viernes": horas_viernes_p1,
            "sala martes 18:00":salas[1],
            "sala martes 12:00":salas[0],
            "sala martes 13:00":salas[2],
            "sala jueves 18:30":salas[1],
            "sala jueves 15:00":salas[0],
            "sala jueves 14:00":salas[2],
            "sala viernes 11:00":salas[1],
            "sala viernes 11:00":salas[0],
            "sala viernes 8:00":salas[2],
            "sala viernes 7:30":salas[1],
            "asientos disponibles martes 18:00": asientos_p1_martes_18_00}

dias_p2= ("lunes", "miercoles, viernes")
horas_lunes_p2= (20:00, 18:00, 15:00) 
horas_miercoles_p2= (17:30, 12:00, 11:00) 
horas_viernes_p2= (18:00, 12:00, 13:00) 
salas_p2= (1,2,3)
asientos_p2_lunes_20_00=(12, 35, 7, 22, 49, 5, 28, 41)
asientos_p2_lunes_18_00=( 3, 30, 1, 46, 23, 9, 18, 36)
asientos_p2_lunes_15_00= (47, 17, 50, 33, 43, 39, 14, 44)
asientos_p2_miercoles_17_30= (2, 24, 38, 13, 4, 8, 34, 32)
asientos_p2_miercoles_12_00= (19, 31, 48, 21, 10, 42, 6, 27)
asientos_p2_miercoles_11_00=( 16, 15, 25, 29, 11, 26, 37, 20)
asientos_p2_viernes_18_00=(21, 3, 43, 13, 5, 41, 23, 19)
asientos_p2_viernes_12_00= (37, 26, 39, 49, 35, 16, 14, 7)
asientos_p2_viernes_13_00= (9, 33, 1, 27, 44, 24, 15, 25)

pelicula_2= {"nombre de la pelicula":"HUNTRIX",
            "dias disponibles": dias_p2,
            "horas de la pelicula lunes": horas_lunes_p2,
            "horas de la pelicula jueves": horas_miercoles_p2,
            "horas de la pelicula viernes": horas_viernes_p2,
            "sala lunes 20:00":salas_p2[1],
            "sala lunes 18:00":salas_p2[0],
            "sala lunes 15:00":salas_p2[2],
            "sala miercoles 18:30":salas_p2[1],
            "sala miercoles 15:00":salas_p2[0],
            "sala miercoles 14:00":salas_p2[2],
            "sala viernes 18:00":salas_p2[1],
            "sala viernes 12:00":salas_p2[0],
            "sala viernes 13:00":salas_p2[2],
            "asientos disponibles lunes20:00": asientos_p2_lunes_20_00,
            "asientos disponibles lunes18:00": asientos_p2_lunes_18_00,
            "asientos disponibles lunes15:00": asientos_p2_lunes_15_00,
            "asientos disponibles lunes18:00": asientos_p2_miercoles_17_30,
            "asientos disponibles lunes18:00": asientos_p2_miercoles_12_00,
            "asientos disponibles lunes18:00": asientos_p2_miercoles_11_00,
            "asientos disponibles lunes18:00": asientos_p2_viernes_12_00,
            "asientos disponibles lunes18:00": asientos_p2_viernes_13_00,
              }

             
dias_p3= ("martes","jueves","viernes")
horas_martes_p3= (13:00,17:00,20:00)
horas_jueves_p3= (12:00,15:00,20:00)
horas_viernes_p3= (12:00,16:00,20:00)
salas_p3= (1,2,3)
asientos_p3_martes_13:00= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50.) 
asientos_p3_martes_17:00= ()            
=00:91,00:613 ,00:21"" ,00:21""():3p_setram_s
             
=00:91,00:613 ,00:21"" ,00:21""():3p_setram_s
             
=00:91,00:613 ,00:21"" ,00:21""():3p_setram_s
             



pelicula_3= {"nombre de la pelicula":"Spiderman",
             "dias disponibles"}


