vertebras = input('')
classe = input('')
dieta = input('')

animal = {
    'vertebrado':{
        'ave':{
            'carnivoro':'aguia',
            'onivoro':'pomba'
            },
        'mamifero':{
            'onivoro':'homem',
            'herbivoro':'vaca'
            }
        },

    'invertebrado':{
        'inseto':{
            'hematofago':'pulga',
            'herbivoro':'lagarta'
            },
        'anelideo':{
            'hematofago':'sanguessuga',
            'onivoro':'minhoca'
            }
        }
    }

print(animal[vertebras][classe][dieta])