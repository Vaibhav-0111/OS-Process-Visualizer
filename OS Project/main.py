#I have  integrated different files to ensure compatibility across various environments for seamless operation

from gui_module import ProcessVirtualizationGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessVirtualizationGUI(root)
    root.mainloop()
