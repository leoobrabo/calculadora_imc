import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": [
    "tkinter", "PySimpleGUI"]}
includeFiles = ['.\imagens']
# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Calculadora Imc",
    version="0.1",
    description="Aplicação para o calculo do indice de massa corporal",
    options={"build_exe":{"include_files": includeFiles}},
    executables=[Executable("app.py", base=base)]
)


#comando para gerar build
#python .\setup.py build