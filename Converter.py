import PySimpleGUI as sg

#I'm sorry but this sourcecode will have a lot of comments because I need to remember everything when I am review the codes

layout= [

    [sg.Input(key= '-INPUT-'), 
    sg.Combo(['km to mile', 'kg to pounds', 'sec to min'], key='-UNITS-'), 
    sg.Button('Convert', key = '-CONVERT-')
    ], 

    [sg.Text('Output', key = '-OUTPUT-')]
]

#Sg.Text only mean there would be a text in the widget
#Sg.Button is a button on the widget
#Sg.Input is input text or number field or both
#Sg.Combo is a dropdown menu on the widget

window = sg.Window('Converter',layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values ['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles'
                case 'kg to pounds':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} secs are {output} minutes'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number not a Text or Symbol')


#Event can be triggered when a certain button or any function on the GUI has been pressed
#Values are the value contained on the input field or any other types of field that has a data inside
#Events are Different from Values.
#In short Events are the work done inside the software
#While Values are the data inside the software
#f'{}' is just a print function that just need {} to input the value so it would be easier to use


###If this sourcecode can be developed more or can be changed more significantly please let me know. So I can learn. 
# Or tell me what should I do to make it better
#Are functions and classes can be used by a sourcecode like this?




window.close()

