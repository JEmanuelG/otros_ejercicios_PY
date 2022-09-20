'''
A partir de una lista de números del 1 al 10,
obtener una nueva lista con los elementos incrementados en 10 unidades
'''

num_list = [1,2,3,4,5,6,7,8,9,10]

nums_mas_10 = list( map( (lambda numero: numero + 10), num_list))

print(nums_mas_10)