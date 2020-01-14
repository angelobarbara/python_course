import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1, 6):
        #Obtenemos el contenido de la página xkcd.com
        response = requests.get('https://xkcd.com/{}'.format(i))
        #Parseamos dicho contenido mediante beautifulsoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #Obtenemos el div con id = comic que contiene las imagenes
        image_container = soup.find(id='comic')
        #Obtenemos el contenido del atributo src del elemento cuyo tag es img
        image_url = image_container.find('img')['src']
        #Obtenemos el nombre de la imagen seleccionando el último elemento del array obtenido separando el enlace
        image_name = image_url.split('/')[-1]
        #Guardamos la imagen pasando a la librería urllib como primer parametro la ruta y como segundo el nombre
        #(Anteponemos https: porque en la ruta de la imagen utiliza la notación //... que nos indica que utiliza el mismo trasporte)
        print('Descargando la imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == '__main__':
    run()