def test_function():
    def inner_function():
        print('Я в области видимости функции test_function') # ничего не отображает интерпретатор

inner_function() # ошибка NameError: name 'inner_function' is not defined