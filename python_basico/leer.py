
def run():
    counter = 0
    with open('leer.txt','r') as f:
        for line in f:
            counter += line.count('Lorem')

    print('Lorem se encuentra {} veces en el texto'.format(counter))

if __name__ == '__main__':
    run()