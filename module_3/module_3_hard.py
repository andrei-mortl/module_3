data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

def accountant(*args):
    a = 0
    for i in args:
        if isinstance(i, str):
            a += len(i)
        elif isinstance(i, int):
            a += i
        elif isinstance(i, dict):
            a += accountant(*i.keys())
            a += accountant(*i.values())
        elif isinstance(i, list):
            a += accountant(*i)
        elif isinstance(i, tuple):
            a += accountant(*i)
        elif isinstance(i, set):
            a += accountant(*i)
    return a

result = accountant(data_structure)
print(result)