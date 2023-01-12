#Curso de Python: Comprehensions, Funciones y Manejo de Errores

set_countries = {'mex', 'arg','col'}

size = len(set_countries)
print(size)
print(set_countries)

print('cOl' in set_countries)
print('bol' in set_countries)

# add | no repite string
set_countries.add('pe')
print(set_countries)
set_countries.add('ven')
print(set_countries)

#update | varios add
set_countries.update({'esp', 'ec', 'br'})
print(set_countries)

#remove 
set_countries.remove('arg')
print(set_countries)
set_countries.discard('ecua')
print(set_countries)