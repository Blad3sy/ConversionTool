from ConversionTool.UIconstruction import Label
from UIconstruction import Window, Button

background = Window()

background.setDimensions(500, 500)
background.setTitle("Test")
background.createWindow()

button1 = Button(background.tk)

button1.setDimensions(5, 10)
button1.setLabel("test")
button1.setLocation(150, 150)
button1.createButton()

label1 = Label(background.tk)

label1.setDimensions(10, 50)
label1.setText("test")
label1.setLocation(0, 0)
label1.createLabel()

background.startWindow()