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

background.startWindow()