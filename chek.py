def digit_check():
    try:
        input_number = int(input('Введите число: \n'))
        return input_number
    except ValueError:
        print('Введите пожалуйста число\n')
        return digit_check()