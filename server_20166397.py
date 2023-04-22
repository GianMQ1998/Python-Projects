#Alumno: Mamani Quispe Gian Carlos
#Codigo: 20166397
import socket
import time
import statistics
import asyncio
import random
import os
#Funcion que genera el equipo con los 5 jugadores con mas minutos jugados.
def get_lista_players(equipo):
        equipo.sort(key=lambda min : float(min[6]))
        equipo.reverse()              
        equipo_filt =[]
        player_equipo = []
        
        for j in range(len(equipo)):
            player_equipo.append(equipo[j][3])

        player_filt = []
        ind_filt = []
        for i in range(len(player_equipo)):
            if player_equipo[i] not in player_filt:
                player_filt.append(player_equipo[i])
                ind_filt.append(i)
        
            
        for k in ind_filt:
            equipo_filt.append(equipo[k])
        while(len(equipo_filt)>5):
            equipo_filt.remove(equipo_filt[-1])
        # Equipo filt contiene los equipos de la competicion 
        return equipo_filt

#Funcion que obtiene la media de puntos por equipo    
def get_media_puntos(equipo):    
    med_pts = []
    for j in range(len(equipo)):
        med_pts.append(int(equipo[j][21]))
    med = statistics.mean(med_pts)
    return med
#Funcion que retorna el score despues de un partido entre dos equipos 
def partido(equipo1, equipo2, score1, score2):
        med0 = get_media_puntos(equipo1)
        med1 = get_media_puntos(equipo2)
        
        if(med0>med1):
            score1+=1
        else:
            score2+=1
            
        return [score1, score2]
#Funcion sincrona que retorna los dos equipos clasificados despues de una fase de grupos
def grupos_sync(score, grupo, grupo_ind):
    [score[0], score[1]] = partido(grupo[0],grupo[1], score[0], score[1])
    time.sleep(0.15)
    [score[0], score[2]] = partido(grupo[0],grupo[2], score[0], score[2])
    time.sleep(0.15)
    [score[0], score[3]] = partido(grupo[0],grupo[3], score[0], score[3])
    time.sleep(0.15)
    [score[1], score[2]] = partido(grupo[1],grupo[2], score[1], score[2])
    time.sleep(0.15)
    [score[1], score[3]] = partido(grupo[1],grupo[3], score[1], score[3])
    time.sleep(0.15)
    [score[2], score[3]] = partido(grupo[2],grupo[3], score[2], score[3])
    time.sleep(0.15)

    total_score = [[score[0],grupo[0], grupo_ind[0]], [score[1],grupo[1], grupo_ind[1]], [score[2],grupo[2], grupo_ind[2]], [score[3],grupo[3], grupo_ind[3]]]
    
    total_score.sort(key=lambda score : score[0])
    
    total_score.reverse()

    clasificados = [total_score[0][2],total_score[1][2]]
    list_clasicados = [total_score[0][1],total_score[1][1]]

    return [clasificados,list_clasicados]

#Funcion asincrona que obtiene los dos equipos clasificados despues de una fase de grupos 
async def grupos_async(score, grupo, grupo_ind):
    [score[0], score[1]] = partido(grupo[0],grupo[1], score[0], score[1])
    await asyncio.sleep(0.15)
    [score[0], score[2]] = partido(grupo[0],grupo[2], score[0], score[2])
    await asyncio.sleep(0.15)
    [score[0], score[3]] = partido(grupo[0],grupo[3], score[0], score[3])
    await asyncio.sleep(0.15)
    [score[1], score[2]] = partido(grupo[1],grupo[2], score[1], score[2])
    await asyncio.sleep(0.15)
    [score[1], score[3]] = partido(grupo[1],grupo[3], score[1], score[3])
    await asyncio.sleep(0.15)
    [score[2], score[3]] = partido(grupo[2],grupo[3], score[2], score[3])
    await asyncio.sleep(0.15)

    total_score_async = [[score[0],grupo[0], grupo_ind[0]], [score[1],grupo[1], grupo_ind[1]], [score[2],grupo[2], grupo_ind[2]], [score[3],grupo[3], grupo_ind[3]]]
    
    total_score_async.sort(key=lambda score : score[0])
    
    total_score_async.reverse()

    clasificados_async = [total_score_async[0][2],total_score_async[1][2]]
    list_clasicados_async = [total_score_async[0][1],total_score_async[1][1]]

    return [clasificados_async,list_clasicados_async]


# Lista con los nombres de los equipos
teams = ["ATL","BOS","BRK","CHA","DAL","DEN","DET","GSW","LAC","LAL","MEM","MIA","NOP","NYK","OKC","ORL","POR","SAC","SAS",
    "SEA","WAS","CHI","CLE","UTA","HOU","IND","MIL","MIN","PHI","PHX","TOR","BOL"]
filename = "players_viernes.csv"
# Funcion que lee el archivo csv y a partir de el obtiene los grupos que contienen a los equipos con sus 5 jugadores 
def get_data(filename,teams):
    
    players_equipo =[]
    data_filt = []
  
    for j in range(len(teams)):
        players_equipo.append([])

    f = open(filename, 'r', encoding="latin1")
    contenido = f.read()
    f.close()
    
    data = contenido.split("\n")

    iter_end = len(data)
    #iter_end = 100

    for idx in range(1,iter_end-1):
        row = data[idx].split(",")
        if row[4] in teams:
            data_filt.append(row)

    
    for j in range(len(data_filt)):
        for k in range(len(players_equipo)):
            if(data_filt[j][4]==teams[k]):
                players_equipo[k].append(data_filt[j])

    #print(players_equipo[0])
    ATL=get_lista_players(players_equipo[0])
    BOS=get_lista_players(players_equipo[1])
    BRK=get_lista_players(players_equipo[2])
    CHA=get_lista_players(players_equipo[3])
    DAL=get_lista_players(players_equipo[4])
    DEN=get_lista_players(players_equipo[5])
    DET=get_lista_players(players_equipo[6])
    GSW=get_lista_players(players_equipo[7])
    LAC=get_lista_players(players_equipo[8])
    LAL=get_lista_players(players_equipo[9])
    MEM=get_lista_players(players_equipo[10])
    MIA=get_lista_players(players_equipo[11])
    NOP=get_lista_players(players_equipo[12])
    NYK=get_lista_players(players_equipo[13])
    OKC=get_lista_players(players_equipo[14])
    ORL=get_lista_players(players_equipo[15])
    POR=get_lista_players(players_equipo[16])
    SAC=get_lista_players(players_equipo[17])
    SAS=get_lista_players(players_equipo[18])
    SEA=get_lista_players(players_equipo[19])
    WAS=get_lista_players(players_equipo[20])
    CHI=get_lista_players(players_equipo[21])
    CLE=get_lista_players(players_equipo[22])
    UTA=get_lista_players(players_equipo[23])
    HOU=get_lista_players(players_equipo[24])
    IND=get_lista_players(players_equipo[25])
    MIL=get_lista_players(players_equipo[26])
    MIN=get_lista_players(players_equipo[27])
    PHI=get_lista_players(players_equipo[28])
    PHX=get_lista_players(players_equipo[29])
    TOR=get_lista_players(players_equipo[30])
    BOL=get_lista_players(players_equipo[31])



    ##Fase de grupos sincrona

    #Grupo A:
    grupoA = [ATL, BOS,BRK, CHA]
    grupoB = [DAL, DEN,DET, GSW]
    grupoC =[LAC,LAL,MEM,MIA]
    grupoD =[NOP,NYK,OKC,ORL]
    grupoE =[POR,SAC,SAS,SEA]
    grupoF =[WAS,CHI,CLE,UTA]
    grupoG =[HOU,IND,MIL,MIN]
    grupoH =[PHI,PHX,TOR,BOL]

    grupos = [grupoA, grupoB, grupoC, grupoD,grupoE, grupoF, grupoG, grupoH]

    return grupos
#Funcion sincrona que retorna los clasificados a semifinales tras las dos fases de grupos
def total_grupos_sync(grupos):
    clasificados =[]
    clasificados_ind = []   
    grupoA = grupos[0]
    grupoB = grupos[1]
    grupoC = grupos[2]
    grupoD = grupos[3]
    grupoE = grupos[4]
    grupoF = grupos[5]
    grupoG = grupos[6]
    grupoH = grupos[7]
    
   
    #GRUPO A    
    grupoAind = teams[0:4]
    scoregrupoA_sync = [0,0,0,0]
    
    class_A_sync = grupos_sync(scoregrupoA_sync, grupoA, grupoAind)
    clasificados.append(class_A_sync[1][0])
    clasificados.append(class_A_sync[1][1])
    clasificados_ind.append(class_A_sync[0][0])
    clasificados_ind.append(class_A_sync[0][1])
    #Grupo B:
    grupoBind = teams[4:8]
    scoregrupoB = [0,0,0,0]
    class_B_sync = grupos_sync(scoregrupoB, grupoB, grupoBind)
    clasificados.append(class_B_sync[1][0])
    clasificados.append(class_B_sync[1][1])
    clasificados_ind.append(class_B_sync[0][0])
    clasificados_ind.append(class_B_sync[0][1])
    #Grupo C:
    grupoCind = teams[8:12]
    scoregrupoC = [0,0,0,0]
    class_C_sync = grupos_sync(scoregrupoC,grupoC,grupoCind)
    clasificados.append(class_C_sync[1][0])
    clasificados.append(class_C_sync[1][1])
    clasificados_ind.append(class_C_sync[0][0])
    clasificados_ind.append(class_C_sync[0][1])
    #Grupo D:
    grupoDind = teams[12:16]
    scoregrupoD = [0,0,0,0]
    class_D_sync = grupos_sync(scoregrupoD,grupoD,grupoDind)
    clasificados.append(class_D_sync[1][0])
    clasificados.append(class_D_sync[1][1])
    clasificados_ind.append(class_D_sync[0][0])
    clasificados_ind.append(class_D_sync[0][1])
    #Grupo E: 
    grupoEind = teams[16:20]
    scoregrupoE = [0,0,0,0]
    class_E_sync = grupos_sync(scoregrupoE,grupoE,grupoEind)
    clasificados.append(class_E_sync[1][0])
    clasificados.append(class_E_sync[1][1])
    clasificados_ind.append(class_E_sync[0][0])
    clasificados_ind.append(class_E_sync[0][1])
    #Grupo F:
    grupoFind = teams[20:24]
    scoregrupoF = [0,0,0,0]
    class_F_sync = grupos_sync(scoregrupoF,grupoF,grupoFind)
    clasificados.append(class_F_sync[1][0])
    clasificados.append(class_F_sync[1][1])
    clasificados_ind.append(class_F_sync[0][0])
    clasificados_ind.append(class_F_sync[0][1])
    #Grupo G:
    grupoGind = teams[24:28]
    scoregrupoG = [0,0,0,0]
    class_G_sync = grupos_sync(scoregrupoG,grupoG,grupoGind)
    clasificados.append(class_G_sync[1][0])
    clasificados.append(class_G_sync[1][1])
    clasificados_ind.append(class_G_sync[0][0])
    clasificados_ind.append(class_G_sync[0][1])
    #Grupo H:
    grupoHind = teams[28:32]
    scoregrupoH = [0,0,0,0]
    class_H_sync = grupos_sync(scoregrupoH,grupoH,grupoHind)
    clasificados.append(class_H_sync[1][0])
    clasificados.append(class_H_sync[1][1])
    clasificados_ind.append(class_H_sync[0][0])
    clasificados_ind.append(class_H_sync[0][1])
    
    #Segunda fase eliminatoria
    grupoI = clasificados[0:4]
    grupoJ = clasificados[4:8]
    grupoK = clasificados[8:12]
    grupoL = clasificados[12:16]
    clasificados_cuartos_de_final = []
    scoregrupoI = [0,0,0,0]
    class_I_sync = grupos_sync(scoregrupoI,grupoI,clasificados_ind[0:4])
    clasificados_cuartos_de_final.append(class_I_sync[0])

    scoregrupoJ = [0,0,0,0]
    class_J_sync = grupos_sync(scoregrupoJ,grupoJ,clasificados_ind[4:8])
    clasificados_cuartos_de_final.append(class_J_sync[0])

    scoregrupoK = [0,0,0,0]
    class_K_sync = grupos_sync(scoregrupoK,grupoK,clasificados_ind[8:12])
    clasificados_cuartos_de_final.append(class_K_sync[0])

    scoregrupoL = [0,0,0,0]
    class_L_sync = grupos_sync(scoregrupoL,grupoL,clasificados_ind[12:16])
    clasificados_cuartos_de_final.append(class_L_sync[0])

    return clasificados_cuartos_de_final

# Funcion sincrona que a partir de la lista de clasificados obtiene el podio de la competicion
def eliminatorias_sync(clasificados):
    lista_semis = []
    lista_semis.append(random.choice([clasificados[0][0],clasificados[1][1]]))
    time.sleep(0.15)
    lista_semis.append(random.choice([clasificados[2][0],clasificados[3][1]]))
    time.sleep(0.15)
    lista_semis.append(random.choice([clasificados[1][0],clasificados[0][1]]))
    time.sleep(0.15)
    lista_semis.append(random.choice([clasificados[3][0],clasificados[2][1]]))
    time.sleep(0.15)
    finalistas = []
    finalistas.append(random.choice([lista_semis[0],lista_semis[1]]))
    time.sleep(0.15)   
    finalistas.append(random.choice([lista_semis[2],lista_semis[3]]))
    time.sleep(0.15)

    third_place = []
    for eq in lista_semis:
        if eq not in finalistas:
            third_place.append(eq)

    campeon = random.choice([finalistas[0],finalistas[1]])
    for part in finalistas:
        if part != campeon:
            subcampeon = part

    tercer_puesto = random.choice([third_place[0],third_place[1]])
    time.sleep(0.15)
    podio = [campeon, subcampeon, tercer_puesto]
    
    return podio

# Funcion asincrona que retorna los clasificados tras las dos fases de grupos 
async def fase_de_grupos_async():
    scoregrupoA_async = [0,0,0,0]
    scoregrupoB_async = [0,0,0,0]
    scoregrupoC_async = [0,0,0,0]
    scoregrupoD_async = [0,0,0,0]
    scoregrupoE_async = [0,0,0,0]
    scoregrupoF_async = [0,0,0,0]
    scoregrupoG_async = [0,0,0,0]
    scoregrupoH_async = [0,0,0,0]
    
    #Fase de grupos
    list_clasif = await asyncio.gather(grupos_async(scoregrupoA_async,grupos[0],teams[0:4]),grupos_async(scoregrupoB_async,grupos[1],teams[4:8]),
    grupos_async(scoregrupoC_async,grupos[2],teams[8:12]),grupos_async(scoregrupoD_async,grupos[3],teams[12:16]),grupos_async(scoregrupoE_async,grupos[4],teams[16:20]),
    grupos_async(scoregrupoF_async,grupos[5],teams[20:24]),grupos_async(scoregrupoG_async,grupos[6],teams[24:28]),grupos_async(scoregrupoH_async,grupos[7],teams[28:32]))
    class_async = []
    class_async_ind = []
    for j in range(len(list_clasif)):
        clasificado = list_clasif[j] 
        class_async.append(clasificado[1][0])
        class_async.append(clasificado[1][1])
        class_async_ind.append(clasificado[0][0])
        class_async_ind.append(clasificado[0][1])
    
    #Segunda fase de grupos
    scoregrupoI_async = [0,0,0,0]
    scoregrupoJ_async = [0,0,0,0]
    scoregrupoK_async = [0,0,0,0]
    scoregrupoL_async = [0,0,0,0]
    
    lista_class_fase2 = await asyncio.gather(grupos_async(scoregrupoI_async,class_async[0:4],class_async_ind[0:4]),grupos_async(scoregrupoJ_async,class_async[4:8],class_async_ind[4:8]),
    grupos_async(scoregrupoK_async,class_async[8:12],class_async_ind[8:12]),grupos_async(scoregrupoL_async,class_async[12:16],class_async_ind[12:16]))

    class_async_fase2 = []

    for j in range(len(lista_class_fase2)):
        clasificado_fase2 = lista_class_fase2[j] 
        class_async_fase2.append(clasificado_fase2[0][0])
        class_async_fase2.append(clasificado_fase2[0][1])

    return class_async_fase2

#Funcion asincrona que recibe los clasificados asincronos y obtiene el podio de la competicion 
async def eliminatorias_async(clasificados):
    lista_semis_async = []
    lista_semis_async.append(random.choice([clasificados[0],clasificados[3]]))
    await asyncio.sleep(0.15)
    lista_semis_async.append(random.choice([clasificados[4],clasificados[7]]))
    await asyncio.sleep(0.15)
    lista_semis_async.append(random.choice([clasificados[2],clasificados[1]]))
    await asyncio.sleep(0.15)
    lista_semis_async.append(random.choice([clasificados[6],clasificados[5]]))
    await asyncio.sleep(0.15)
    finalistas_async = []
    finalistas_async.append(random.choice([lista_semis_async[0],lista_semis_async[1]]))
    await asyncio.sleep(0.15)  
    finalistas_async.append(random.choice([lista_semis_async[2],lista_semis_async[3]]))
    await asyncio.sleep(0.15)

    third_place = []
    for eq in lista_semis_async:
        if eq not in finalistas_async:
            third_place.append(eq)

    campeon = random.choice([finalistas_async[0],finalistas_async[1]])
    for part in finalistas_async:
        if part != campeon:
            subcampeon = part

    tercer_puesto = random.choice([third_place[0],third_place[1]])
    time.sleep(0.15)
    podio_async = [campeon, subcampeon, tercer_puesto]
    
    return podio_async

#Funcion que ejectuta la funcion eliminatorias y obtiene el podio asincrono
async def eliminatorias_async_main():
    podio_async = await asyncio.gather(eliminatorias_async(list_clasif_async))

    return podio_async

#FUNCION PRINCIPAL
if __name__ == "__main__":
    
    grupos = get_data(filename,teams)
    
    incio_sync = time.perf_counter()
    clasificados_sync = total_grupos_sync(grupos)
    podio_sync = eliminatorias_sync(clasificados_sync)
    fin_sync = time.perf_counter()
    #print(f"El tiempo total del torneo sincrono es : {(fin_sync-incio_sync)*1000:0.2f}")
    
    incio_async = time.perf_counter()
    list_clasif_async = asyncio.run(fase_de_grupos_async())
    podio_async = asyncio.run(eliminatorias_async_main())
    fin_async = time.perf_counter()
    #print(f"El tiempo total del torneo asincrono es : {(fin_async-incio_async)*1000:0.2f}") 
    
    SOCK_BUFFER = 65536
    # crea el objeto de socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5020)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    # asociamos la direccion y puerto al objeto socket
    sock.bind(server_address)

    # iniciamos la escucha de conexiones
    sock.listen(5)
    
    #Esperamos conexion del cliente
    print("Esperando conexiones...")
    conn, client_address = sock.accept()
    print(f"Conexion desde {client_address[0]}:{client_address[1]}")
    
    #String vacio que ira guardando los datos enviados al cliente                                     
    msg_save = "" 
    enable = False
    while(enable==False):
        print("Ingresando usuario: ")
        data = conn.recv(SOCK_BUFFER)
        decode = data.decode('utf-8')

        if (decode=="Gian Carlos"):  
            print("Procesando datos..." )
            msg_wel = "Procesando data"
            data_a = msg_wel.encode('utf-8')
            conn.sendall(data_a)
            enable = True
        else:
            msgin = "Usuario incorrecto"
            data_a = msgin.encode('utf-8')
            conn.sendall(data_a)

    while enable:
      
        print("Ingresando comando..." )

        data = conn.recv(SOCK_BUFFER)
        decode = data.decode('utf-8')        
            
        if (decode == "equipos"):
            print("Enviando datos de equipos del torneo")
            inicio_eq = time.perf_counter()
            grupos = get_data(filename,teams)
            fin_eq = time.perf_counter()
            time_eq = f"El tiempo total para obtener los equipos es {(fin_eq - inicio_eq):0.4f} segundos \n"
            msg_equipos ="Los equipos del torneo son: \n"
            for grupo in grupos:
                for j in range(len(grupo)):
                    team = grupo[j]
                    for  k in range(5):
                        msg_equipos+= str(team[k]) + "\n"
                    msg_equipos+="\n"
            msg_save+=msg_equipos
            msg_save+=time_eq
            data_a = msg_equipos.encode('utf-8')
            conn.sendall(data_a)

        elif (decode == "fase de grupos asincrono"):
            print("Enviando los clasificados en una rutina asincrona")
            inicio_grupos_async = time.perf_counter()
            list_clasif_async = asyncio.run(fase_de_grupos_async())
            fin_grupos_async = time.perf_counter()
            time_grupos_async = f"El tiempo total para obtener los equipos clasificados de manera asincrona es {(fin_grupos_async - inicio_grupos_async):0.4f} segundos\n"
            msg_clasificados_async = "Los clasificados para los partidos asincronos son:\n "
            msg_clasificados_async+=str(list_clasif_async) + "\n "
            msg_class_async = msg_clasificados_async
            msg_save+=msg_clasificados_async
            msg_save+=time_grupos_async
            data_a = msg_class_async.encode('utf-8')
            conn.sendall(data_a)

        elif (decode == "fase de grupos sincrono"):
            print("Enviando los clasificados en una rutina sincrona")
            inicio_grupos_sync = time.perf_counter()
            clasificados_sync = total_grupos_sync(grupos) 
            fin_grupos_sync = time.perf_counter()
            time_grupos_sync = f"El tiempo total para obtener los equipos clasificados de manera sincrona es {(fin_grupos_sync - inicio_grupos_sync):0.4f} segundos\n"
            msg_clasificados_sync = "Los clasificados para los partidos asincronos son:\n "
            msg_clasificados_sync+=str(list_clasif_async) + "\n "
            msg_class_sync = msg_clasificados_sync
            msg_save+=msg_clasificados_sync
            msg_save+=time_grupos_sync
            data_a = msg_class_sync.encode('utf-8')
            conn.sendall(data_a)

        elif (decode == "eliminatorias asincrono"):
            print("Enviando los resultados del podio en una rutina asincrona")
            inicio_podio_async = time.perf_counter()
            podio_async = asyncio.run(eliminatorias_async_main())
            fin_podio_async = time.perf_counter()
            time_podio_async = f"El tiempo total para obtener el podio asincrono es {(fin_podio_async - inicio_podio_async):0.4f} segundos\n"
            msg_podio_async = "El podio de los partidos asincronos es:\n "
            msg_podio_async+=  "Campeon: "+str(podio_async[0][0]) + "\n "
            msg_podio_async+=  "Subcampeon: "+str(podio_async[0][1]) + "\n "
            msg_podio_async+=  "Subcampeon: "+str(podio_async[0][2]) + "\n "        
            msg_elim_async = msg_podio_async
            msg_save+=msg_podio_async
            msg_save+=time_podio_async
            data_a = msg_elim_async.encode('utf-8')
            conn.sendall(data_a)

        elif (decode == "eliminatorias sincrono"):
            print("Enviando los resultados del podio en una rutina sincrona")
            inicio_podio_sync = time.perf_counter()
            podio_sync = eliminatorias_sync(clasificados_sync)
            fin_podio_sync = time.perf_counter()
            time_podio_sync = f"El tiempo total para obtener el podio sincrono es {(fin_podio_sync - inicio_podio_sync):0.4f}segundos \n"
            msg_podio_sync = "El podio de los partidos sincronos es:\n "
            msg_podio_sync+=  "Campeon: "+str(podio_sync[0]) + "\n "
            msg_podio_sync+=  "Subcampeon: "+str(podio_sync[1]) + "\n "
            msg_podio_sync+=  "Subcampeon: "+str(podio_sync[2]) + "\n " 
            msg_elim_sync = msg_podio_sync
            msg_save+=msg_podio_sync
            msg_save+=time_podio_sync
            data_a = msg_elim_sync.encode('utf-8')
            conn.sendall(data_a)

        elif (decode == "reporte"):
            print("Generando reporte")
            file = open("/home/gian/Arqui2022/Lab8/Lab_08_reporte.txt", "w")            
            file.write("Reporte de datos (Lab8) - Mamani Quispe Gian Carlos" + os.linesep) 
            file.write(msg_save)
            file.close()
            msg_rep = "Reporte generado"
            data_a = msg_rep.encode('utf-8')
            conn.sendall(data_a)    

        else:
                #En caso no se envie ninguno de los comandos el servidor continuara activo
            msg_c = "Comando incorrecto"                    
            print(msg_c)
            data_3 = msg_c.encode('utf-8')
            conn.sendall(data_3)
            
        

           