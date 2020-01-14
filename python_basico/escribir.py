
def run():
    #Usando el context manager with no es necesario cerrar el archivo(f.close())
    with open('numeros.txt','w') as f:
        for i in range(10):
            f.write(str(i))
    
    #Sin utilizar el content manager with
    # try:
    #     f = open('numeros.txt','w')
    # finally:
    #     f.close()

if __name__ == '__main__':
    run()