import varibles

s1 = varibles.s4
costo = varibles.costos
poblacion = varibles.values

#Funcion objetivo a minimizar
def funcionObjetivo(costo, se):
    sum = 0

    for i in range(len(costo)):
        f = (costo[i]*se[i])
        sum = sum + f

    return sum

#Cuenta la cantidad de "1" en el vector
def sumaNvalidos(vector):
    cont_n = 0
    for i in range(len(vector)):
        if(vector[i] == 1):
            cont_n = cont_n+1
        else:
            continue
    return cont_n

#Comprobar si la solucion es factible
def checksSolution(s1, poblacion):
    vectorAux = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    flag = False
    for i in range(len(s1)):
        if(s1[i] == 1):
            for j in range(len(s1)):
                if(poblacion[i][j] == 1 ):
                    vectorAux[j] = 1
                else:
                    if(vectorAux[j] == 1):
                        continue
                    else:
                        vectorAux[j] = 0
                
    nums_1 = sumaNvalidos(vectorAux)           
    # for k in range(len(s1)):                
    #         if(vectorAux[k] == 1):
    #             flag = True
    #         else:
    #             flag = False
    #             break
    # if (flag):
    #     return    
    # else:
    #     print("Solucion no valida")
    return nums_1



def seleccionPadres(solInit,poblacion):
    conjunto_p = solInit
    padres_s = []
    
    for i in range(len(conjunto_p)):
        valor = checksSolution(conjunto_p[i],poblacion)
        padres_s.extend([valor])

    padres_s.sort()
    padres_s.pop(0)
    padres_s.pop(0)
    for i in range(len(conjunto_p)):
        if(padres_s[0] == checksSolution(conjunto_p[i],poblacion)):
            padre1 = conjunto_p[i]
        if(padres_s[1] == checksSolution(conjunto_p[i],poblacion)):
            padre2 = conjunto_p[i]
    print(padres_s)
    padres = [padre1,padre2]
    print(padres)


seleccionPadres(varibles.solInit,poblacion)