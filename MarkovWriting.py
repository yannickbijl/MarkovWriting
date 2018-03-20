import sys
import random

import wx

from ESC_MarkovWriting import ESC_MarkovWriting
from GUI_MarkovInput import GUI_MarkovInput
from GUI_MarkovOutput import GUI_MarkovOutput

class MarkovWriting(wx.Frame):
    def __init__(self, s_parent, s_title="MarkovWriting"):
        wx.Frame.__init__(self, s_parent, title=s_title, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
        box = wx.BoxSizer()
        self.frames()
        self.hiding()
        self.panel.SetSizer(self.box2)
        self.dic['A'].Show()
        self.binder()
        self.Show(True)
        self.Centre()
        self.SetSize((400, 400))
        box.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def frames(self):
        def dic_make():
            self.dic = {}
            self.dic['A'] = self.markovinput
            self.dic['B'] = self.markovoutput

        self.markovinput = GUI_MarkovInput(self.panel)
        self.markovoutput = GUI_MarkovOutput(self.panel)
        dic_make()
        self.box2 = wx.BoxSizer()
        for x in self.dic:
            self.box2.Add(self.dic[x], 1, wx.ALL | wx.EXPAND)

    def hiding(self):
        for x in self.dic:
            self.dic[x].Hide()

    def binder(self):
        def stop_buttons():
            for x in self.dic:
                self.dic[x].stop.Bind(wx.EVT_BUTTON, self.quitting)

        def other_buttons():
            self.markovinput.next.Bind(wx.EVT_BUTTON, self.next_frame)
            self.markovoutput.prev.Bind(wx.EVT_BUTTON, self.prev_frame)

        stop_buttons()
        other_buttons()

    def quitting(self, event):
        sys.exit()

    def next_frame(self, event):
        def get_text():
            writing = ESC_MarkovWriting(self.markovinput.order.GetValue())
            writing.train(self.markovinput.filename.GetPath())
            return writing.generate(self.markovinput.length.GetValue())
        
        try:
            self.markovoutput.text.SetValue(get_text())
        except:
            pass
        else:
            self.hiding()
            self.dic['B'].Show()
            self.Layout()
            self.Centre()
    
    def prev_frame(self, event):
        def set_values():
            self.markovinput.order.SetValue(1)
            self.markovinput.length.SetValue(20)
            self.markovinput.filename.SetPath("")
        
        set_values()
        self.hiding()
        self.dic['A'].Show()
        self.Layout()
        self.Centre()


# Is called when this script is used as the MAIN.
if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            frame = MarkovWriting(None)
            frame.Show(True)
            frame.Centre()
            self.SetTopWindow(frame)
            return True

    # The application-loop
    app = MyApp(0)
    app.MainLoop()
