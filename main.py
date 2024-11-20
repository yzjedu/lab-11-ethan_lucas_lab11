import os

def input_filename():
    filename = input("Enter the name of the file you want to translate: ")
    while not os.path.isfile(filename):
        print(f'Error the file "{filename}" was not fount.')
        filename = input("Enter the name of the file you want to translate: ")
    return filename

def read_file_to_table(filename):
    file_data = open(filename, 'r')
    m_table = {}
    for row in file_data:
        line = row.split()
        m_table[line[1]] = line[0]
    return m_table

