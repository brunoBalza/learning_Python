def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_info(name='Bruno', age=34, city='Mendoza')
print_info(name='Rocio', age=35, city='Mendoza')