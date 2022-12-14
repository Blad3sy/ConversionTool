import tkinter
import time

class Window:
     
    def __init__(self):
        self.height = None
        self.width = None
        self.title = None
    
    def setDimensions(self, height, width):
        self.height = height
        self.width = width
    
    def setTitle(self, title):
        self.title = title
    
    def GetDimensions(self):
        dimensionsDict = {
            "Height": self.height,
            "Width": self.width
        }

        return dimensionsDict

    def getTitle(self):
        return self.title

    def createWindow(self):
        self.tk = tkinter.Tk()
        self.tk.geometry(f"{self.width}x{self.height}")
        self.tk.title(self.title)
    
    def startWindow(self):
        self.tk.mainloop()

class Button:

    def __init__(self, parent):
        self.height = None
        self.width = None
        self.label = None
        self.xloc = None
        self.yloc = None
        self.parent = parent
        self.command = None
    
    def setDimensions(self, height, width):
        self.height = height
        self.width = width

    def getDimensions(self):
        dimensionsDict = {
            "Height": self.height,
            "Width": self.width
        }

        return dimensionsDict

    def setLocation(self, x, y):
        self.xloc = x
        self.yloc = y

    def getLocation(self):
        locationDict = {
            "X": self.xloc,
            "Y": self.yloc
        }

        return locationDict
    
    def setLabel(self, labelText):
        self.label = labelText
    
    def getLabel(self):
        return self.label      

    def setCommand(self, labelCommand):
        self.command = labelCommand
    
    def getCommand(self):
        return self.command     
   
    def createButton(self):
        self.button = tkinter.Button(self.parent, text=self.label, width=self.width, height=self.height, command=self.command)
        self.button.place(x=self.xloc, y=self.yloc)

class Label:

    def __init__(self, parent):
        self.height = None
        self.width = None
        self.text = None
        self.xloc = None
        self.yloc = None
        self.parent = parent
    
    def setDimensions(self, height, width):
        self.height = height
        self.width = width

    def getDimensions(self):
        dimensionsDict = {
            "Height": self.height,
            "Width": self.width
        }

        return dimensionsDict

    def setLocation(self, x, y):
        self.xloc = x
        self.yloc = y

    def getLocation(self):
        locationDict = {
            "X": self.xloc,
            "Y": self.yloc
        }

        return locationDict
    
    def setText(self, inputText):
        self.text = inputText
    
    def getText(self):
        return self.text

    def createLabel(self):
        self.label = tkinter.Label(self.parent, text=self.text, width=self.width, height=self.height)
        self.label.place(x=self.xloc, y=self.yloc)

class dynamic_Label:

    def __init__(self, parent):
        self.height = None
        self.width = None
        self.text = None
        self.xloc = None
        self.yloc = None
        self.parent = parent
        self.label = tkinter.Label(self.parent, text=self.text, width=self.width, height=self.height)
    
    
    def setDimensions(self, height, width):
        self.height = height
        self.width = width

    def getDimensions(self):
        dimensionsDict = {
            "Height": self.height,
            "Width": self.width
        }

        return dimensionsDict

    def setLocation(self, x, y):
        self.xloc = x
        self.yloc = y

    def getLocation(self):
        locationDict = {
            "X": self.xloc,
            "Y": self.yloc
        }

        return locationDict
    
    def setText(self, inputText):
        self.text = inputText
    
    def getText(self):
        return self.text
    
    def updateDynamicLabel(self, text):
        self.text = text
        self.label.config(text=self.text)
        
    def createDynamicLabel(self):
        self.label.config(text=self.text, width=self.width, height=self.height)
        self.label.place(x=self.xloc, y=self.yloc)