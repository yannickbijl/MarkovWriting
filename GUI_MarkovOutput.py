import wx

class GUI_MarkovOutput(wx.Panel):
    def __init__(self, bb_parent):            
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.text = wx.TextCtrl(self, value="", style=wx.TE_MULTILINE)
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.prev = wx.Button(self, label="Previous")
        
        # Placing of items in frame
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.prev, 1, wx.EXPAND | wx.ALL)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.text, 3, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_MarkovOutput"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(800, 600))
            panel = wx.Panel(self)
            panel1 = GUI_MarkovOutput(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()
