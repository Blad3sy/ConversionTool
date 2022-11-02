from UIconstruction import Window, Button, Label, dynamic_Label
import time
import tkinter as tk

root = tk.Tk()
root.geometry(f"{500}x{500}")
root.title("Test")

button1 = Button(root)

button1.setDimensions(5, 10)
button1.setLabel("test")
button1.setLocation(150, 150)

label1 = Label(root)

label1.setDimensions(10, 50)
label1.setText("test")
label1.setLocation(0, 0)

dynamicLabel1 = dynamic_Label(root)
dynamicLabel1.setDimensions(10, 50)
dynamicLabel1.setText("test")
dynamicLabel1.setLocation(0, 0)
dynamicLabel1.createDynamicLabel()

button1.setCommand(lambda : dynamicLabel1.updateDynamicLabel("test2"))

dynamicLabel1.createDynamicLabel()
# label1.createLabel()
button1.createButton()

root.mainloop()