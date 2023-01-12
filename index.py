set_countries = {'col','mex','bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,3,4,5,6,7}
print(set_numbers)

set_Types= {1, "Hola", False, 12.12}
print(set_Types)

# con set() no duplica y tira en pantalla las unicas
set_from_string = set('holacomotas ss')
print(set_from_string)

set_from_tuples = set(('abc', 'aei', 'uno-dos-tres', 'abc'))
print(set_from_tuples)

set_from_list = [1,2,3,1,2,3,5]
# devuelve los numeros unicos
set_numbers = set(set_from_list)
print(set_numbers)
unique_nums = list(set_numbers)
print(unique_nums)