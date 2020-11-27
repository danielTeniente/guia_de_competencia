



dias_por_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

#Formula
def clientes_hoy(mes, dia):
    absoluto = dia-15
    if(absoluto<0):
        absoluto *= -1
    return (6-mes)**2 + absoluto


def ganacia_por_dia(num_pacientes, cctv, cstv):
    #pondré el precio de los cuartos de forma global
    global precio_cctv
    global precio_cstv
        
    #pacientes sin televisión, siempre van a preferir sin televisor
    pstv = min(num_pacientes,cstv)
    pctv = min(num_pacientes-pstv,cctv)    
        
    #calcular las ganacias
    return pctv*precio_cctv + pstv*precio_cstv
        

def ganancia_anual(cctv, cstv):
    global dias_por_mes
    
    ganancia = 0
    for mes,num_dias in enumerate(dias_por_mes):
        #se calcula la ganancía día a día
        for dia in range(1,num_dias+1):
            ganancia += ganacia_por_dia(clientes_hoy(mes+1,dia),cctv, cstv)
    
    return ganancia



def minimo_televisores(meta,num_cuartos):
    
    #los límites de búsqueda binaria serán 
    #sin TV, todos con TV
    a = 0
    b = num_cuartos
    
    while(a<b):

        centro = (a+b)//2+1
        
        #cuartos con TV
        cctv = centro
        cstv = num_cuartos - centro
        
        ganancia = ganancia_anual(cctv,cstv)
        
        #La ganancia fue igual o superior a la meta
        if(ganancia>=meta):
            #vamos a comprobar si es el mínimo
            ganancia_menos_unTV = ganancia_anual(cctv-1,cstv+1)
            if(ganancia_menos_unTV<meta):
                #encontramos el mínimo, ya que no alcanza la meta
                #si quitamos un TV
                return cctv
            else:
                #si no, estamos muy arriba
                b = centro-1
            
        else:
            #si no, la meta está más arriba
            a = centro +1
            
    #si no encontró el centro
    return num_cuartos

num_cuartos = int(input())
precios = input().split()
precio_cctv = int(precios[0])
precio_cstv = int(precios[1])
meta = int(input())
print(minimo_televisores(meta,num_cuartos))