#ORDENACIONES ASCENDENTES Y DESCENDENTES DE LISTAS DE OBJETOs

lista = [2, 5, 4, 5, 1, 9, 10, 23, 25, 70, 45, 34, 12, 11, 8, 7, 6, 3, 0]

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j].lista < lista[j+1].lista: #lista[j].lista > lista[j+1].lista: ASC
                lista[j], lista[j+1] = lista[j+1], lista[j]

def insertion_sort(lista):
    for step in range(1, len(lista)):
        key = lista[step]
        j = step - 1 
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key > lista[j]: #j >= 0 and key < lista[j]: ASC
            lista[j + 1] = lista[j]
            j = j - 1
        # Ubicar el valor rescatado justo por delante del valor menor a este
        lista[j + 1] = key

# Función para determinar el pivot
def partition(lista, low, high):#siempre recibe el array completo
  # seleccionar el último elemento del array como pivot
  pivot = lista[high]
  # esta variable la usaremos para señalar elementos mas grandes que el pivot
  i = low - 1
  # Buscar todos los elementos menores al pivot y reubicarlos
  for j in range(low, high):
    if lista[j] >= pivot: #lista[j] <= pivot: ASC
      # Si hay un element menor que el pivot intercamabiarlos por el de la position i
      i = i + 1
      (lista[i], lista[j]) = (lista[j], lista[i])
  # finalmente, intercamabiar el pivot por el contenido del sigueinte lugar de i
  (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
  # Retornar la posición dónde se partió
  #print("semiprocesado: ", end='')
  #print(array)
  return i + 1

def quickSort(lista, low, high):#HIGH es el largo del array y LOW vale 0 que es largo del array
  if low < high:
    pi = partition(lista, low, high)
    # ordenar a la izq del punto particionado
    quickSort(lista, low, pi - 1)
    #Ordena desde el pivot menos 1 hacia el inicio del array. osea el sub array izquierdp
    # ordenar a la derecha del punto particionado
    quickSort(lista, pi + 1, high)
    #Ordena desde el pivot mas 1 hacia el final del array. osea el sub array derecho

def mergeSort(lista):
    if len(lista) > 1:
        #FASE de dividir el array en 2 partes 
        # middle es el puntero donde el array es dividido en 2 subarrays
        middle = len(lista) // 2
        L = lista[:middle] #mitad izquierda
        R = lista[middle:] #mitad derecha
        # Ordenar las 2 mitades
        mergeSort(L)
        mergeSort(R)
        #FASE de hacer el merge de los subarrays
        # necesitamos 3 punteros:
        # 2 para para ir señalando elementos en los subarrays (mitades)
        # y un 3ro para usar con el el array combinado resultante
        i = j = k = 0
        # Recorrer tanto el subarrays L como M hasta alcanzar el final de alguno
        # de ellos. Compara el elemento de L contra el de M y reubicar en el
        # array general
        while i < len(L) and j < len(R):
            if L[i] > R[j]: #L[i] < R[j]: ASC 
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        # Pasamos los restantes elemenos de L al array general 
        # (en el caso que M tenga menos elementos que L)
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        # Lo mismo que lo anterior pero si M tenía más elementos que L
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

print('Personas Antes Ordenación:')
print(*lista, sep='\n')
print("")

ordenar_burbuja(lista)
print('Personas Después Ordenación BURBUJA:')
print(*lista, sep='\n')

insertion_sort(lista)
print("\nPersonas Después Ordenación INSERTION: ")
print(*lista, sep='\n')

quickSort(lista, 0, len(lista) - 1)
print('\nPersonas Después Ordenación QUICKSORT:')
print(*lista, sep='\n')

mergeSort(lista)
print("\nPersonas Después Ordenación MERGESORT:")
for i in range(len(lista)):
    print(lista[i], sep='\n')


