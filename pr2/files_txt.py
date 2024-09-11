def read(file):
    """
    чтение из файла 
    поступает название относительное или полный путь
    """
    with open(file, 'r') as file:
        return file.read()

def write(file,s):
    """
    запись в файл или создание 
    поступает название относительное или полный путь
    """
    with open(file, 'w') as file:
        file.write(s)

def write_plus(file,s):
    """
    дозапись файла или создание
    поступает название относительное или полный путь
    """
    with open(file, 'a') as file:
        file.write(s)

