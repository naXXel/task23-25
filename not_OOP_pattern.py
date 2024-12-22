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

def command_input_matrices(state):
    state['matrix1'], state['matrix2'] = input_matrices()
    if state['matrix1'] is None or state['matrix2'] is None:
        print("Ошибка ввода матриц. Попробуйте снова.")

def command_execute_algorithm(state):
    if state['matrix1'] is not None and state['matrix2'] is not None:
        state['result_matrix'] = add_matrices(state['matrix1'], state['matrix2'])
        state['determinant_matrix1'] = calculate_determinant(state['matrix1'])
        state['determinant_matrix2'] = calculate_determinant(state['matrix2'])
    else:
        print("Сначала введите матрицы.")

def command_display_results(state):
    if state['result_matrix'] is not None:
        print("Сумма матриц:\n", state['result_matrix'])
        print("Определитель первой матрицы:", state['determinant_matrix1'])
        print("Определитель второй матрицы:", state['determinant_matrix2'])
    else:
        print("Сначала выполните алгоритм.")

def main_menu():
    state = {
        'matrix1': None,
        'matrix2': None,
        'result_matrix': None,
        'determinant_matrix1': None,
        'determinant_matrix2': None
    }

    commands = {
        '1': command_input_matrices,
        '2': command_execute_algorithm,
        '3': command_display_results
    }

    while True:
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '4':
            break
        elif choice in commands:
            commands[choice](state)
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
