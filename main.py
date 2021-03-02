from pikepdf import Pdf # pip install pikepdf
from os import listdir
from os.path import isfile, join
import sys

DEC_PATH = sys.argv[1] if len(sys.argv) >= 2 else ''

def decrypt_pdf(input_path, output_path, v_password):
    with Pdf.open(input_path,password=v_password) as pdf:
        pdf.save(output_path)

def get_files_to_decrypt():
    return [f for f in listdir(DEC_PATH) if isfile(join(DEC_PATH, f))]

if __name__ == '__main__':
    # example usage:
    # decrypt_pdf('encrypted.pdf', 'decrypted.pdf', 'secret_password')

    all_files = get_files_to_decrypt()
    for fl in all_files:
        decrypt_pdf(f'{DEC_PATH}/{fl}', f'{DEC_PATH}/dec_{fl}', 'secret_password')

