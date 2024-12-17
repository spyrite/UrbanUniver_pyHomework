def test_function():
    def inner_function():
        print('Я в области видимости функции tst_function')
    inner_function()

test_function()

# inner_fuction() не вызовется, так как данная функция существует только в пределах функции "test_function"