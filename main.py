#Nguyễn Phước Nhã - 43.01.104.118
from tkinter import *
def calculate(event):
 tx1=int(tx_1.get());
 value1 = (2 * tx1) * 3.14
 value2 = tx1 * tx1 * 3.14
 print(value1)
 print(value2)
 updateDisplay1(value1);
 updateDisplay2(value2);
	
def updateDisplay1(myString):
	displayVariable1.set(myString)

def updateDisplay2(myString):
	displayVariable2.set(myString)

root=Tk()
root.geometry("800x400")
root.title("Chu Vi - Diện Tích Hình Tròn")
root.grid()

lbl1=Label(root, text="Nhập bán kính", font=("TimeNewRoman",20))
lbl1.pack()
tx_1= Entry(root, width=30, font=("TimeNewRoman",20))
tx_1.pack()

button_1 = Button(root, text="Tính toán", font=("TimeNewRoman",30,"bold"), bg="cyan", fg="red") 
button_1.bind("<Button-1>", calculate)
button_1.pack()

lbl2=Label(root, text="Chu vi", font=("TimeNewRoman",20))
lbl2.pack()

displayVariable1 = StringVar()
displayLabel1 = Label(root, textvariable=displayVariable1, font=("TimeNewRoman",20))
displayLabel1.pack()

lbl2=Label(root, text="Diện tích", font=("TimeNewRoman",20))
lbl2.pack()

displayVariable2 = StringVar()
displayLabel2 = Label(root, textvariable=displayVariable2, font=("TimeNewRoman",20))
displayLabel2.pack()

root.mainloop()