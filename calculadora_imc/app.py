import PySimpleGUI as sg

sg.theme('TanBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  
                [sg.Titlebar(
                    title = "Teste", icon = None,
                    text_color = None,
                    background_color = None,
                    font = None,
                    key = None,
                    k = None
                                )
                 ],
                [sg.Image(filename='.\imagens\img_center (1).png', tooltip='Vamos Calcular o imc?', pad=((14, 20),(30,32)))],
                [sg.Text('Vamos descobrir seu Imc?', pad=((14, 20),(30,32)))],
                [sg.Text('Altura(em centímetros)', pad=((14, 20),(30,32))), sg.Input(tooltip='digite aqui sua altura', border_width=1, text_color='Black')],
                [sg.Text('Peso(em Kilos)', pad=((14, 20),(30,32))), sg.Input(tooltip='digite aqui seu peso', border_width=1, text_color='Black')],
                [sg.Text('')], 
                [sg.Text('')],
                [sg.Button('Calcular', pad=((14, 20),(30,32)))] 
                
                
            ]

# Create the Window
window = sg.Window('Calculadora de Imc', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
