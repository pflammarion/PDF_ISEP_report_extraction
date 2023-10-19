import os
import re

import PyPDF2
import pandas as pd

path_to_directory = 'input'

files = os.listdir(path_to_directory)


for file in files:
    if file.endswith('.pdf'):
        file_path = os.path.join(path_to_directory, file)

        pdf_file = open(file_path, 'rb')

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        page = pdf_reader.pages[0]
        text = page.extract_text()

        pdf_file.close()

        lines = text.split('\n')

        headers = ['Destination', 'Choix 1', 'Choix 2', 'Choix 3', 'Choix 4', 'Choix 5', 'Quota', 'Affectation']

        lines = lines[1:]

        data = []
        for line in lines:
            elements = re.split(r'(\d+)', line)
            elements = [elem for elem in elements if elem.strip()]
            if len(elements) == 8:
                data.append(elements)

        df = pd.DataFrame(data, columns=headers)

        df.to_csv('output/' + file + '.csv', index=False)