'''
Desarrolle un programa en el lenguaje C++ en donde se obtenga
el valor máximo y mínimo de una lista utilizando una aproximación
de divide y venceras. Tome como ejemplo las siguientes ejecuciones
del programa:
A) Lista de números: [3,1,4,1,5,9,2,6,5,3,5]
Valor mínimo: 1
Valor máximo: 9

B) Lista de números: [9,8,7,6,5,4,3,2,1]
Valor mínimo: 1
Valor máximo: 9
'''

def max_min(lista):
     if len(lista) == 1:
         return lista[0],lista[0]
     else:
         mitad = len(lista) // 2
         return max(max_min(lista[:mitad]), max_min(lista[mitad:])), min(max_min(lista[:mitad]), max_min(lista[mitad:]))
     
print(max_min([3,1,4,1,5,9,2,6,5,3,5]))