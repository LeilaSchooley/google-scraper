import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Text('Input path to wasabi passphrases')],
                                                  [sg.InputText(sg.user_settings_get_entry('-dmfile-', ''),
                                                                key="DMAccounts"), sg.FileBrowse()],  [sg.Text('Log')],

        [sg.Multiline(size=(83, 10), key='logs')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break


window.close()