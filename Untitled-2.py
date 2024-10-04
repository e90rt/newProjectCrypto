#Слепая подпись
import math
def inv(a, n):
    for t in range(100):
        a1 = (1 + (n * t)) // a
        if (a * a1) % n == 1:
            return a1

mas = input("Введите сообщение -")
mas = [ord(i.lower()) - 1071 for i in mas if i != ' ']
print("действия стороны Б")
p, q = int(input("введите p -")), int(input("введите q -"))
k0 = int(input("введите k0 -"))

n = p * q
fn = (p - 1)*(q - 1)
if (k0 > 1) and (k0 <= fn) and math.gcd(k0, fn) == 1:
    kc = inv(k0, fn) % fn
print(f"Секретный ключ = {kc}")
print(f"передача пользователю N = {n}, k0 = {k0}")
print("действия стороны A")
m = 0
for i in mas:
    m1 = (m ^ i ** k0 % n) % n
    m = m1
print(f"Хэш равен {m1}")
k = int(input("введите k -"))

if (k > 0 and k < n) and (math.gcd(k, n) == 1):
    k_inv = inv(k, n) % n
print(k_inv)
m2 = (m1 * (k ** k0 % n) % n)
print(f"m' = {m2}")

s1 = m2 ** kc % n 
s = (k_inv * s1) % n
print(f"s' = {s1}, s = {s}")

