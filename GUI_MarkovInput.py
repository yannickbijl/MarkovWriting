import wx

class GUI_MarkovInput(wx.Panel):
    def __init__(self, bb_parent):
        
        def explain1():
            text = ("Order: The number of unique words to be generated in " +
                    " sequence. 2 would mean that 'the the' cannot happen. " +
                    "The minimum order is 1 and the maximum is 10.")
            return text
        
        def explain2():
            text = ("Length: The length of the text to be generated. " +
                    "The minimum length is 1 and the maximum is 300 words")
            return text
        
        def explain3():
            text = ("File: The text that is used to train the generator. " +
                    "It should be in plain text.")
            return text
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.order = wx.SpinCtrl(self, min=1, max=10, initial=1)
        self.length = wx.SpinCtrl(self, min=1, max=300, initial=20)
        self.filename = wx.FilePickerCtrl(self, path="") 
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.next = wx.Button(self, label="Next")
        
        # Text
        self.explain1 = wx.StaticText(self, label=explain1())
        self.explain2 = wx.StaticText(self, label=explain2())
        self.explain3 = wx.StaticText(self, label=explain3())
        
        # Placing of items in frame
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.next, 1, wx.EXPAND | wx.ALL)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.explain1, 1, wx.EXPAND | wx.ALL)
        box.Add(self.order, 1, wx.EXPAND | wx.ALL)
        box.Add(self.explain2, 1, wx.EXPAND | wx.ALL)
        box.Add(self.length, 1, wx.EXPAND | wx.ALL)
        box.Add(self.explain3, 1, wx.EXPAND | wx.ALL)
        box.Add(self.filename, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_MarkovInput"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(800, 600))
            panel = wx.Panel(self)
            panel1 = GUI_MarkovInput(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()
