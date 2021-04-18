def sumaTodos(limitTo):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado +=1
    return resultado
print(sumaTodos(100))

def sumaTodosLosCuadrados(limitTo):
    resultado=0
    for i in range(limitTo):
        resultado += i*i
        
    return resultado
print(sumaTodosLosCuadrados(4))
        