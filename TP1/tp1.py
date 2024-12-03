
def q1():
    palavra = "Sítio do pica-pau amarelo \n 2023"
    lista = [string for string in palavra if not string.isspace()]
    print(lista)

q1()
def maior_valor(lista):
    maior_valor = lista[0]
    for item in lista:
        if item > maior_valor:
            maior_valor = item
    print(str(item) + " é o maior valor da array!!!")

maior_valor([1,2,3,4,5,6,7,89])


def quadrado_tabuleiro(numero_graos):
    quadrado = 1
    graos = 1
    while graos < numero_graos:
        quadrado += 1
        graos *= 2 
    print(quadrado )

quadrado_tabuleiro(2)

def bubbleSort(self):                           # Ordenar comparando valores adjs.
      for last in range(self.__nItems-1, 0, -1):  # e subir
         for inner in range(last):                # o loop interno vai até o último
            if self.__a[inner] > self.__a[inner+1]:  # Se o item for menor
               self.swap(inner, inner+1)          # que o item adjacente, trocar


def func1(lista):
    esquerd = 0
    direita = len(lista) - 1
    while esquerd < direita:
        for i in range(esquerd, direita):
            if lista[i] > lista[i + 1]:  
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        direita -= 1  
        for i in range(direita, esquerd, -1):
            if lista[i] < lista[i - 1]: 
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
        esquerd += 1  
    print( lista)
func1(["teste","amora", "banana", "zap"])