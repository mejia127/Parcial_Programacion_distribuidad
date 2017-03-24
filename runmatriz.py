import matriz
import threading
import funciones_hilos


def main():

    M = False
    while M!=True:

            mi_menu = matriz.Menu()
            a=mi_menu.loop()

            if a == 1:
                hilo1 = threading.Thread(target=funciones_hilos.matriz_determinante, args=())
                hilo1.start()
                hilo1.join()

            if a == 2:
                hilo2 = threading.Thread(target=funciones_hilos.matriz_inver, args=())
                hilo2.start()
                hilo2.join()

            if a == 3:
                hilo3 = threading.Thread(target=funciones_hilos.transpuesta, args=())
                hilo3.start()
                hilo3.join()

            if a == 4:
                hilo4 = threading.Thread(target=funciones_hilos.matriz_numero, args=())
                hilo4.start()
                hilo4.join()

            if a == 5:
                hilo5 = threading.Thread(target=funciones_hilos.matriz_elevada, args=())
                hilo5.start()
                hilo5.join()

            if a == 6:
                hilo6 = threading.Thread(target=funciones_hilos.matrizSimetrica(), args=())
                hilo6.start()
                hilo6.join()

            if a == 7:
                hilo7 = threading.Thread(target=funciones_hilos.matrizidentica(), args=())
                hilo7.start()
                hilo7.join()

            if a == 8:
                hilo8 = threading.Thread(target=funciones_hilos.multiplicacionmatriz(), args=())
                hilo8.start()
                hilo8.join()

            if a == 9:
                hilo9 = threading.Thread(target=funciones_hilos.sumamatriz(), args=())
                hilo9.start()
                hilo9.join()

            if a == 10:
                hilo10 = threading.Thread(target=funciones_hilos.restamatriz(), args=())
                hilo10.start()
                hilo10.join()

            if a == 11:
                print "Hasta Luego "
                M = True
            else:
                b = raw_input("Presione enter para volver al menu")
                M = False














if __name__ == '__main__':
    main()
