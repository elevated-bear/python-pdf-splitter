import os
import PySimpleGUI as sg

sg.theme('LightTeal')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Select the pdf to split up'), sg.Input(), sg.FileBrowse()],
            [sg.Text('Pages per chunck'), sg.Spin(values=('05','06','07','08','09','10','11','12','13','14','15'), initial_value= 10)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Welcome to PDF Splitter', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    
    pathToFile = values[0]
    if (pathToFile.endswith(".pdf")):
        fileFolderName = os.path.basename(pathToFile)[:-4] # lazy way to shave last 4 chars
        path = pathToFile[:-4]
        if os.path.isdir(path) is False: #create if dir doesn't exist
            try:
                os.mkdir(path)
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                print ("Successfully created the directory %s " % path)

        print('Thanks for the pdf')
    else:
        print('This is not a pdf')
        values.clear()
    # print('You entered ', values[0])

window.close()