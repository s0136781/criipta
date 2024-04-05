#Реализовать решение квадратичного сравнения по составному модулю.
def extended_gcd(a, b):  #реализует расширенный алгоритм Евклида для нахождения наибольшего общего делителя и коэффициентов x и y таких, что ax + by = gcd(a, b).
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):  #Использует расширенный алгоритм Евклида для нахождения обратного элемента a по модулю m. Если обратного элемента не существует, возвращает None.
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Обратного элемента не существует
    return x % m


def solve_quadratic_congruence(a, b, c, n):
    # Решение квадратичного сравнения ax^2 + bx + c ≡ 0 (mod n)

    # 1. Находим дискриминант
    D = (b ** 2 - 4 * a * c) % n

    # 2. Проверяем, является ли D квадратом по модулю n
    for x in range(1, n):
        if (x ** 2) % n == D:
            break
    else:
        return None  # Квадратный корень не найден

    # 3. Находим обратный элемент для 2a
    a_inv = mod_inverse(2 * a, n)

    if a_inv is None:
        return None

    # 4. Вычисляем первое решение x1
    x1 = (-b + x) * a_inv % n

    # 5. Вычисляем второе решение x2
    x2 = (-b - x) * a_inv % n

    return x1, x2



a = 2
b = 5
c = 2
n = 17  # модуль

solutions = solve_quadratic_congruence(a, b, c, n)

if solutions is not None:
    print(f"Решения квадратичного сравнения по модулю {n}: {solutions}")
else:
    print("Решения не найдены.")