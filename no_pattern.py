import numpy as np

def input_matrices():
    size = int(input("Введите размер матриц: "))

    def read_matrix():
        return np.array([list(map(int, input().split())) for _ in range(size)])

    print("Введите элементы первой матрицы:")
    matrix1 = read_matrix()
    if any(len(row) != size for row in matrix1):
        print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
        return None, None

    print("Введите элементы второй матрицы:")
    matrix2 = read_matrix()
    if any(len(row) != size for row in matrix2):
        print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
        return None, None

    return matrix1, matrix2

def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def main_menu():
    matrix1 = matrix2 = None
    result_matrix = None
    determinant_matrix1 = None
    determinant_matrix2 = None

    while True:
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '4':
            break
        elif choice == '1':
            matrix1, matrix2 = input_matrices()
            if matrix1 is None or matrix2 is None:
                print("Ошибка ввода матриц. Попробуйте снова.")
        elif choice == '2':
            if matrix1 is not None and matrix2 is not None:
                result_matrix = add_matrices(matrix1, matrix2)
                determinant_matrix1 = calculate_determinant(matrix1)
                determinant_matrix2 = calculate_determinant(matrix2)
            else:
                print("Сначала введите матрицы.")
        elif choice == '3':
            if result_matrix is not None:
                print("Сумма матриц:\n", result_matrix)
                print("Определитель первой матрицы:", determinant_matrix1)
                print("Определитель второй матрицы:", determinant_matrix2)
            else:
                print("Сначала выполните алгоритм.")

if __name__ == "__main__":
    main_menu()
