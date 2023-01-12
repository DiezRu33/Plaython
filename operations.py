set_a = {'col','bol','mex'}
set_b = {'pa','gua','mex'}

# union 
set_c = set_a.union(set_b)
print(set_c)
#    el piola
print(set_a | set_b)

# lanza el elemento en comun
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)