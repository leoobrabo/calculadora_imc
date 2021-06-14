import PySimpleGUI as sg

def CalcularImc(altura, peso):
    
    try:
        
        imc = ((int(peso) / int(altura)) / int(altura)) * 10000  
        janela['imc'].update(f'Imc = {round(imc)}', text_color='black')
        
        if imc < 18.5:
            janela['resultado'].update('Abaixo do peso', text_color='yellow')      
        elif imc >= 18.5 and imc < 25:
            janela['resultado'].update('Peso normal', text_color='green')
        elif imc >= 25 and imc < 30:
            janela['resultado'].update('Sobrepeso', text_color='orange')
        elif imc >= 30 and imc < 35:
            janela['resultado'].update('Obesidade grau 1', text_color='red')
        elif imc >= 35 and imc < 40:
            janela['resultado'].update('Obesidade grau 2', text_color='red')
        elif imc >= 40:
            janela['resultado'].update('Obesidade grau 3', text_color='red')
            
    except ValueError:
        sg.Popup('Valor Invalido')

sg.theme('TanBlue')

layout = [  
                [sg.Image(filename='.\imagens\img_center.png', tooltip='Vamos Calcular o imc?', pad=(50, 20))],
                [sg.Text('Vamos descobrir seu Imc?', size=(18,1), pad=(35, 6))],
                [sg.Text('Altura(em centímetros)',size=(18,1), pad=(5, 5)), sg.Input(size=(8,1), pad=(5, 5), tooltip='Digite aqui sua altura', key='altura', border_width=1, text_color='Black')],
                [sg.Text('Peso(em Kg)', size=(18,1), pad=(5, 8)), sg.Input(size=(8,1), pad=(5, 5), tooltip='Digite aqui seu peso', key='peso', border_width=1, text_color='Black')],
                [sg.Text(key='resultado', size=(27,1), justification='center' )], 
                [sg.Text(key='imc', size=(27,1), justification='center', pad=(5, 10))],     
                [sg.Button('Calcular', size=(27,1))]                     
            ]

janela = sg.Window(title= 'Calculadora Imc', layout = layout, icon='.\imagens\icone.ico')

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Calcular':
        CalcularImc(valores['altura'], valores['peso'])
janela.close()
