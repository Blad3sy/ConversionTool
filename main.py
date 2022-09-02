from UIconstruction import Window, Button

background = Window()
button1 = Button()

background.setDimensions(500, 500)
background.setTitle("Test")
background.startWindow()

button1.setDimensions(100, 100)
button1.setLabel("test")
button1.createButton()