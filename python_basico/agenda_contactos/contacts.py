import csv


class Contact:
    def __init__(self,name,phone,email):
        super().__init__()
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:
    def __init__(self):
        super().__init__()
        self._contacts = list()
    
    def add(self,name,phone,email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()

    #def add(self,*args):
        #contact = Contact(*args)
        #self._contacts.append(contact)
        #self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('* --- * --- * --- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(contact._name))
        print('Teléfono: {}'.format(contact._phone))
        print('Correo: {}'.format(contact._email))
        print('* --- * --- * --- * --- * --- * --- * --- * --- * ')

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
        print('No existe el contacto en la lista')

    def search(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _not_found(self):
        print('******')
        print('Contacta no encontrado!')
        print('******')

    def _save(self):
        with open('contacts.csv','w',newline='\n',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact._name,contact._phone, contact._email))
            


def run():

    contact_book = ContactBook()

    with open('contacts.csv','r',encoding='utf-8') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            else:
                try:
                    contact_book.add(row[0],row[1],row[2])
                except IndexError:
                    pass

    while True:
        command = str(input('''
            Que deseas hacer?

            [a]gregar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'b':
            name = str(input('Introduzca el nombre de un contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Introduzca el nombre de un contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()