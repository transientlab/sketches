import numpy as np
import matplotlib.pyplot as plt
import math
# miesiące pracy
l = 48
# liczba dni pracy
l1 = 20
# liczba godzin pracy w dniu
l2 = 6

x = 0
s = 0

# Definiowanie funkcji
def func(x):
    return int(162 * (1 / (1 + math.exp(-0.0000000007 * pow((0.2 * x - 78), 5)))) - 1)


# stawka za godzinę w kolejnym dniu pracy
print('m\t h\t d\t m\t s\t avg')
for m in range(1,l+1):
    for d in range(1,l1+1):
        i = m * d
        y = func(i)
        d = y*l2
        k = d*l1
    s += k
    avg = int(s/m)
    
    print('{} \t {} \t {} \t {} \t {} \t {}'.format(m, y, d, k, s, avg))



# Zakres wartości x do wykresu
x_values = np.linspace(0, 1200, 500)
y_values = [func(x) for x in x_values]

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Funkcja: y = 160*(1/(1+exp(-0.000000000008*(0.1*x-78)^5)))')
plt.title('Wykres funkcji')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Wyświetlenie wykresu
# plt.show()