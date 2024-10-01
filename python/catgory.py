class nowaklasa():
    a = 5

def identity(any):
    return any

# print(identity(1))
# print(identity('string'))
# print(identity(nowaklasa))

def func1(a):
    return a + a

def func2(a):
    return a*a

def func3(a):
    return a^a

def compose_functions(func1, func2):
    return lambda x : func1(func2(x))

# c = compose_functions(func1, func2)(3)
# print(c)

def test_composition_identity():
    return identity == compose_functions(identity, identity)(identity)

class memoize():
    arg_list = []
    res_list = []
    # if 


# def functiones(*argos, **kwargons):
#     print(*argos)
#     for key, item in kwargons.items():
#         print('key: ' + key + ' value: ' + str(item))

# functiones(1, 2, 3, argumentos=6)

def main():
    print('identity test result:', test_composition_identity())



if __name__=='__main__':
    main()


