import tkinter as tk

window = tk.Tk()
window.title("Jonah's Application")
#frame sets the position of widgets
#frm_name = tk.Frame(master=window, width=100, height=100, bg="red").pack(fill=tk.X)
# (fill=tk.X) will fill the window horizontally, Y will fill vertically, and BOTH will fill both ways
#  tk.FLAT: Has no border effect (the default value).
#  tk.SUNKEN: Creates a sunken effect.
#  tk.RAISED: Creates a raised effect.
#  tk.GROOVE: Creates a grooved border effect.
#  tk.RIDGE: Creates a ridged effect.
lbl_name = tk.Label(window, text = "label is used to print text or pictures").pack()
btn_name = tk.Button(window, text = "Button", bg="blue", fg="black", height=1, width =5).pack()
ent_name = tk.Entry(fg="yellow", bg="blue", width=50).pack()
#  Retrieves text with .get()
#  Deletes text with .delete()
#  Inserts text with .insert()
#Same as entry but larger space
txt_name= tk.Text().pack
#for i in range(3):
#    for j in range(3):
#        frame = tk.Frame(
#            master=window,
#            relief=tk.RAISED,
#            borderwidth=1
#        )
#        frame.grid(row=i, column=j, padx=5, pady=5)
#        btn_name = tk.Button(master=frame, text=f"Row {i}\nColumn {j}").pack()
#window.geometry('350x200') would set window size to 350x200 pixels
window.mainloop()


#  tk.TOP
#  tk.BOTTOM
#  tk.LEFT
#  tk.RIGHT
# To be placed inside pack() function.
# If you don’t set side, then .pack() will automatically use tk.TOP
# and place new widgets at the top of the window, or at the top-most
# portion of the window that isn’t already occupied by a widget.