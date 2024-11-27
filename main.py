# Programmers: Ethan D'Souza & Lucas Podowski
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/27/2024
# Lab Assignment: 11
# Problem Statement: Create a program to convert morse code ciphers back into plain English.
# Data In: Morse Code File
# Data Out: English Translated File

import os

def input_filename(prompt):
    # Prompt the user for a file name and ensure it exists
    filename = input(prompt).strip()
    while not os.path.isfile(filename):
        print(f'Error: The file "{filename}" was not found.')
        filename = input(prompt).strip()
    return filename

def read_file_to_table(filename):
    # Open the Morse code translation file
    file_data = open(filename, 'r')
    m_table = {}
    for row in file_data:
        # Split each row into English character (key) and Morse code (value)
        line = row.strip().split('  ')
        if len(line) == 2:
            # Key: English letter, Value: Morse code
            m_table[line[1].strip()] = line[0].strip()
    file_data.close()
    # Debug: Print the dictionary to ensure it's correct
    print("Morse Code Dictionary:", m_table)
    return m_table


def convert_morse_to_english(input_file, output_file, morse_dict):
    # Convert the file written in Morse code into plain English
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    for line in infile:
        codes = line.strip().split()
        english_translation = ''
        for code in codes:
            translation = morse_dict.get(code, '?')
            print(f"Processing code: {code} -> {translation}")  # Debug: Show each code and result
            english_translation += translation
        outfile.write(english_translation + '\n')
    infile.close()
    outfile.close()

def main():
    # Main function to run the Morse code translator
    print("Welcome to the Morse Code Translator!")

    # Get the Morse code conversion file
    conversion_file = input_filename("Enter the name of the Morse code conversion file (e.g., morsecode.txt): ")
    morse_dict = read_file_to_table(conversion_file)

    # Debug: Print the loaded dictionary
    print("Loaded Dictionary:", morse_dict)

    # Get the input Morse code file
    input_file = input_filename("Enter the name of the input file containing Morse code: ")

    # Debug: Print the input file contents
    infile = open(input_file, 'r')
    print("Input File Content:")
    for line in infile:
        print(line.strip())
    infile.close()

    # Get the output file name
    output_file = input("Enter the name of the output file for the English translation: ").strip()

    # Convert Morse code to English
    convert_morse_to_english(input_file, output_file, morse_dict)
    print(f"Translation complete! English text has been written to {output_file}.")

# Call the main function to execute the program
main()