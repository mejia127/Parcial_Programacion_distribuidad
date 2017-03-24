import matriz


def matriz_determinante():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    matrizA.matriz_det(a)


def matriz_inver():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    matrizA.matriz_inversa(a)


def transpuesta():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    matrizA.transpuesta()


def matriz_numero():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    matrizA.matriz_numero()


def matriz_elevada():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    matrizA.matriz_elevada()


def matrizSimetrica():
    matrizA = matriz.Matriz()
    matrizA.matrizSimetrica()


def matrizidentica():
    matrizA = matriz.Matriz()
    matrizA.matrizidentica()


def multiplicacionmatriz():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    columnasA = matrizA.getColumnas()
    filasA = matrizA.getFilas()

    matrizB = matriz.Matriz()
    matrizB.crearMatrizA()
    b = matrizB.llenarmatrizA()
    matrizB.imprime_matrizC()

    columnasB = matrizB.getColumnas()
    filasB = matrizB.getFilas()
    matrizA.multiplicacionmatriz(filasA, columnasB, filasB, columnasA, a, b)


def sumamatriz():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    columnasA = matrizA.getColumnas()
    filasA = matrizA.getFilas()

    matrizB = matriz.Matriz()
    matrizB.crearMatrizA()
    b = matrizB.llenarmatrizA()
    matrizB.imprime_matrizC()

    columnasB = matrizB.getColumnas()
    filasB = matrizB.getFilas()
    matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)


def restamatriz():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprime_matriz()
    columnasA = matrizA.getColumnas()
    filasA = matrizA.getFilas()

    matrizB = matriz.Matriz()
    matrizB.crearMatrizA()
    b = matrizB.llenarmatrizA()
    matrizB.imprime_matrizC()

    columnasB = matrizB.getColumnas()
    filasB = matrizB.getFilas()
    matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)
