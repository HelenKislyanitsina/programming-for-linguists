import time
fibonacci_numbers = [1, 1]


def general_time_decorator(function):  # Декоратор, показывающий выполнение функции
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = function(*args, **kwargs)
        print("--- %s seconds ---" % (time.perf_counter_ns() - start_time))
        return result
    return wrapper


def main_decorator(function):  # Декоратор с основной информацией по функции
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = function(*args, **kwargs)
        print('Название функции: ', function.__name__)
        print("--- %s seconds ---" % (time.perf_counter_ns() - start_time))
        print('Переменные: ', *args, **kwargs)
        print(result)
        return result
    return wrapper


@main_decorator
@general_time_decorator
def fibonacci_function(first_index, second_index):
    if type(first_index) != int or type(second_index) != int:
        return TypeError('first/ second index should be int')
    elif first_index < 0 or second_index < 0:
        return TypeError('first/ second index should be positive')
    elif (second_index - 1) != 0:
        new_second_index = second_index - 1
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        return fibonacci_function(first_index, new_second_index)  # Та самая рекурсия
    elif (second_index - 1) == 0:
        return fibonacci_numbers[first_index:]


print(fibonacci_function(0, 10))







