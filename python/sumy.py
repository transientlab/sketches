import timeit

TESTS_COUNT = 10
TEST_VALUE  = 1000000

def sumuj(x):
    return sum(range(0,x+1))


def hipoteza(x):
    return x*(x+1)/2


def testuj(zakres):
    for i in range(0, zakres):
        if hipoteza(i) == sumuj(i):
            pass
        else:
            return False
    return True, hipoteza(zakres), sumuj(zakres)


result1 = timeit.timeit(stmt='sumuj(TEST_VALUE)', globals=globals(), number=TESTS_COUNT)
result2 = timeit.timeit(stmt='hipoteza(TEST_VALUE)', globals=globals(), number=TESTS_COUNT)

print(result1/result2)