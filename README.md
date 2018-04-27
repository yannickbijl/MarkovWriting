# MarkovWriting
A program to write some nonsense text based on a input text. This is done with the use of Markov Chains.

The program uses the modules sys, math, re and the third-party module wx-python 4.0 (Phoenix) WxPython

The executable was made using pyinstaller on Windows 10 Home-edition 64-bit.

In the project folder open the cmd and use the command: pyinstaller -F --icon=MarkovWriting.ico -w MarkovWriting.py

The icon was made in Adobe Illustrator

MarkovWriting.py is the main file, GUI_MArkovInput.py and GUI_MarkovOutput.py are used to generate the user interface, and ESC_MarkovWriting.py does the calculations.
