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
        Window.tk = tkinter.Tk()
        Window.tk.geometry(f"{self.width}x{self.height}")
        Window.tk.title(self.title)
        Window.tk.mainloop()

class Button:

    def __init__(self):
        self.height = None
        self.width = None
        self.label = None
        self.container = None
    
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
        button = tkinter.Button(text = self.label, width = self.width, height = self.height)