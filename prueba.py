
def prueba(email,first_name,last_name,password,is_admin):
    print(email)

def prueba2(**kwargs):
    print(kwargs['email'])

def prueba3(*args):
    print(args)

def prueba4(args):
    print(args)

users = {
    'email': 'cvander@platzi.com',
    'first_name': 'Christian',
    'last_name': 'Van der Henst',
    'password': '1234567',
    'is_admin': True
}

users2 = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True
    },
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True
    }
]


prueba(**users)
prueba2(**users)
prueba3(users2)
prueba4(users2)

