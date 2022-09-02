from posixpath import dirname
import tkinter

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

    def startWindow(self):
        root = tkinter.Tk()
        root.geometry(f"{self.width}x{self.height}")
        root.title = self.title
        root.mainloop()

class Button:

    def __init__(self):
        self.height = None
        self.width = None
        self.label = None
    
    def setDimensions(self, height, width):
        self.height = height
        self.width = width

    def GetDimensions(self):
        dimensionsDict = {
            "Height": self.height,
            "Width": self.width
        }

        return dimensionsDict
    
    def setLabel(self, labelText):
        self.label = labelText
    
    def getLabel(self):
        return self.label
    
    def createButton(self):
        button = Button(text = self.label, height = self.height, width = self.width)
        button.mainloop()