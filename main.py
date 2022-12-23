import PySimpleGUI as sg
import mymath

sg.theme('Dark')

layout = [  [sg.Text('Рівняння (знак степеня **): ', size=(30,2)), sg.Multiline(key='-FUNCTION-', size=(30,2))],
            [sg.Text('Початкове значення X0: ', size=(30,2)), sg.InputText(key='-X0-', size=(30,2))],
            [sg.Text('Кількість знаків після коми (напр., 3): ', size=(30,2)), sg.InputText(key='-EPSILON-', size=(30,2))],
            [sg.Text('Кількість ітерацій: ', size=(30,2)), sg.InputText(key='-ITERATIONS-', size=(30,2))],
            [sg.Button('Розвязати', key='-CONVERT-'), sg.Button('Exit')],
            [sg.Text('f(x)=0; x=', size=(15,0))],
            [sg.Output(size=(65,30), key='-RESULT-')]]

window = sg.Window('Метод дотичних', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-CONVERT-':
        fun = str(values['-FUNCTION-'])
        x1 = float(values['-X0-'])
        epsilon = int(values['-EPSILON-'])
        iterations = int(values['-ITERATIONS-'])
        result = mymath.calculation(fun=fun, x1=x1, epsilon=epsilon, iterations=iterations)
        window['-RESULT-'].update(result)

window.close()