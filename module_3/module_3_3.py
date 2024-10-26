# ______________________1________________________

def print_params(a=1, b='stroka',c=True):
    print(a,b,c)
print_params()
print_params('123')
print_params(b = 25)
print_params(c = [1,2,3])

# ______________________2________________________

values_list = [True, 'str',78]
values_dict = {'Петя': 40, 'Саша': '50', 'Коля': 60}
print_params( * values_list)
print_params( ** values_dict)

# ______________________3________________________

values_list_2 = [600.1, True]
print_params(*values_list_2, 42)