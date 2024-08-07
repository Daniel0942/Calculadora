import PySimpleGUI as sg

# Definindo o tema da interface
sg.theme('Black')

# Layout da calculadora
layout = [
    [sg.Input(size=(20, 1), key='-DISPLAY-')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
    [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('/')]
]

# Criando a janela
window = sg.Window('Calculadora', layout, grab_anywhere=False, size=(130, 170))

# Loop de eventos para capturar inputs do usuário
operation = ''
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event in '0123456789':
        operation += event
        window['-DISPLAY-'].update(operation)
    elif event in '+-*/':
        if operation[-1] not in '+-*/' and operation != '':
            operation += event
            window['-DISPLAY-'].update(operation)
    elif event == 'C':
        operation = ''
        window['-DISPLAY-'].update(operation)
    elif event == '=':
        try:
            result = eval(operation)
            window['-DISPLAY-'].update(result)
            operation = str(result)
        except:
            window['-DISPLAY-'].update('Erro')
            operation = ''

# Fechando a janela
window.close()