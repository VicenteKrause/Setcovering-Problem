import variables
import random
import numpy as np


s1 = variables.s4
costo = variables.costos
poblacion = variables.values


#Funcion objetivo a minimizar
def calculoPrecio(costo, se):
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
                
    sumnums = sumaNvalidos(vectorAux)
    if(sumnums != 36):
        sumnums=0
    precio = calculoPrecio(costo,s1)   
    prom = sumnums/precio  
    return prom

def checksSolutionNvalidos(s1, poblacion):
    vectorAux = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                
    sumnums = sumaNvalidos(vectorAux)
    return sumnums

#Funcion que selecciona los mejores padres
def seleccionPadres(solInit,poblacion):
    padres_s = []
    
    for i in range(len(solInit)):
        valor = checksSolution(solInit[i],poblacion)
        padres_s.extend([valor])
    padres_s.sort()
    padres_s.pop(0)
    padres_s.pop(0)   

    for i in range(len(solInit)):
        if(padres_s[0] == checksSolution(solInit[i],poblacion)):
            padre1 = solInit[i]
        if(padres_s[1] == checksSolution(solInit[i],poblacion)):
            padre2 = solInit[i]

    padres = [padre1 , padre2]
    return padres

#Cruzamiento de los padres
def cruzamiento(padres):
    size = len(padres[0])/2
    padre1 = padres[0]
    padre2 = padres[1]

    hijo1 = []
    hijo2 = []

    for i in range(len(padres[0])):
        if(i<size):
            hijo1.extend([padre1[i]])
            hijo2.extend([padre2[i]])
        else:
            hijo1.extend([padre2[i]])
            hijo2.extend([padre1[i]])

    for i in range(len(hijo1)):
        ran = random.uniform(0, 1)
        if(ran<variables.fm):
            if(hijo1[i] == 0):
                hijo1[i] = 1
            else:
                hijo1[i] = 0
        else:
            continue

    for i in range(len(hijo2)):
        ran = random.uniform(0, 1)
        if(ran<variables.fm):
            if(hijo2[i] == 0):
                hijo2[i] = 1
            else:
                hijo2[i] = 0
        else:
            continue
    
    hijos =[ hijo1 , hijo2 ]
    return hijos

# Comprueba la solucion
def comunaConAntena(indice, solution):
    if solution[indice] == 1:
        return True
    else:
        for i in range(len(solution)):
            if poblacion[indice ][i] == 1 and solution[i] == 1:
                return True
    return False
def regionConAtena(solution):
    for i in range(len(solution)):
        if comunaConAntena(i, solution) == False:
            return False
    return True

#Genera soluciones iniciales
def generarSoluciones():
    solution = [0] * len(poblacion)
    while regionConAtena(solution) == False:
        solution[random.randint(0, len(solution)-1)] = 1
    return solution

def main():
    conjuntoS = [[],[],[],[]]
    conjDesv = []
    for i in range(4):
        conjuntoS[i].extend(generarSoluciones())
    
    cont = 1
    best = conjuntoS[0]
    sumCost=0

    while cont <= 1000:
        print("Iteracion :", cont)
        padres = seleccionPadres(conjuntoS,variables.values)
        if(calculoPrecio(costo,padres[0]) < calculoPrecio(costo,padres[1]) and checksSolutionNvalidos(padres[0],poblacion)==36):
            best = padres[0]
        if(calculoPrecio(costo,padres[0]) > calculoPrecio(costo,padres[1]) and checksSolutionNvalidos(padres[1],poblacion)==36):
            best = padres[1]
        
        print("Padre 1:",padres[0] )
        print("Costo:", calculoPrecio(costo,padres[0]))
        print("Padre 2:",padres[1] )
        print("Costo:", calculoPrecio(costo,padres[1]))
        hijos = cruzamiento(padres)
        print("Hijo 1:",hijos[0] )
        print("Costo:", calculoPrecio(costo,hijos[0]))
        print("Hijo 2:",hijos[1] )
        print("Hijo:", calculoPrecio(costo,hijos[1]))
        conjuntoS = [hijos[0],hijos[1],padres[0],padres[1]]
        besth = best
        if(calculoPrecio(costo,best)>calculoPrecio(costo,hijos[0]) and checksSolutionNvalidos(hijos[0],poblacion)==36):
            besth = hijos[0]
        if(calculoPrecio(costo,best)>calculoPrecio(costo,hijos[1]) and checksSolutionNvalidos(hijos[1],poblacion)==36):
            besth = hijos[1]
        sumCost = calculoPrecio(costo,hijos[0])+calculoPrecio(costo,hijos[1])+calculoPrecio(costo,padres[0])+calculoPrecio(costo,padres[1]) + sumCost
        best=besth
        conjDesv.extend([conjuntoS])
        cont +=1
        print("---------------------------------------------------------------------------------------------------------------------------------")
    sumDesv = []
    desvEst = 0
    for i in range(len(conjDesv)):
        desSum = conjDesv[i]
        for j in range(len(desSum)):        
            sumDesv.extend([calculoPrecio(costo,desSum[j])])
    desvEst = np.std(sumDesv)

    print("Mejor Solucion:",best)
    print("Costo:", calculoPrecio(costo,best))
    print("Promedio costos:", sumCost/(4*cont))
    print("Desviacion Estandar:", desvEst)

main()