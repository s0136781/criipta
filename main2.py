#Реализовать программный продукт
#нахождения множества
#квадратичных вычетов и множества квадратичных невычетов по заданному
#простому модулю .
#Квадратичный вычет, понятие теории чисел. К. в. по модулю m — число а,
#для которого сравнение x2 º а (mod m) имеет решение: при некотором целом х число x2—a
#делится на m; если это сравнение не имеет решений, то а называют квадратичным невычетом.
#Например, если m = 11, то число 3 будет К. в., так как сравнение x2 º 3 (mod 11)
#имеет решения х = 5, х = 6, а число 2 будет невычетом, т.к. не существует чисел х,
#удовлетворяющих сравнению x2 º 2 (mod 11).



class QuadraticResidues:
    def __init__(self, prime_mod):
        self.prime_mod = prime_mod

    def calculate_quadratic_residues(self):
        residues = []  # Список квадратичных вычетов
        non_residues = []  # Список квадратичных невычетов

        # Находим квадратичные вычеты и невычеты по модулю
        for num in range(1, self.prime_mod):
            residue = (num ** 2) % self.prime_mod  # Вычисляем квадрат числа по модулю
            if residue not in residues:
                residues.append(residue)  # Добавляем в список квадратичных вычетов
            print(f"Вычисляем квадрат числа {num} по модулю {self.prime_mod}: результат - {residue}")

        residues.sort()  # Сортируем список квадратичных вычетов
        print(f"Квадратичные вычеты по модулю {self.prime_mod}: {residues}")

        for num in range(1, self.prime_mod):
            if num not in residues:
                non_residues.append(num)  # Добавляем в список квадратичных невычетов
        print(f"Квадратичные невычеты по модулю {self.prime_mod}: {non_residues}")

        return residues, non_residues

# Пример использования:
prime_mod = 17  # Простое модуль
qr = QuadraticResidues(prime_mod)
residues, non_residues = qr.calculate_quadratic_residues()

print(f"Множество квадратичных вычетов по модулю {prime_mod}: {residues}")
print(f"Множество квадратичных невычетов по модулю {prime_mod}: {non_residues}")