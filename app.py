from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("My app")
root.iconbitmap("c:/users/nepul kahandawa/onedrive/pictures/img.ico")
root.geometry("500x500")


def graph():
    house_prices = np.random.normal(200000, 25000, 5)
    plt.pie(house_prices)
    plt.show()

my_button = Button(root, text="Graph", command=graph)
my_button.pack(pady=20)

root.mainloop()
