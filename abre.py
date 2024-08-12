import os
from tkinter import filedialog

# Open file dialog to select a specific file
file_path = filedialog.askopenfilename(title='Selecciona el archivo SQL', filetypes=[('SQL files', '*.sql')])

# Open directory dialog to select a folder
file_mainpath = filedialog.askdirectory(title='Selecciona la carpeta principal')
encoding_option = "latin1"
try: 
    with open(file_path,"r",encoding=encoding_option) as file:
        content = file.read()
except FileNotFoundError:
    print("Archivo no encontrado")

file_pathosdatabase=os.path.join(file_mainpath,"base_datos.txt")

try:
    with open(file_pathosdatabase,'w',encoding=encoding_option) as database:
        database.write(content)
        print("Base de datos en txt escrita satisfactoriamente")
except FileNotFoundError:
    pass


