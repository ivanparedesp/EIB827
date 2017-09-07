def miFuncion():
    print "hola mundo"

if __name__ == "__main__":
    print "Soy el programa principal. El valor de __name__ es: " + __name__
    miFuncion()
else:
    print "He sido importado. El valor de __name__ es: " + __name__