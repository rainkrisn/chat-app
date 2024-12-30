from tkinter import *

root = Tk()
root.geometry("1500x700")
root.title("BanranApp")

root.overrideredirect(True)

#root.attributes('-alpha', 0.99)

#root.wm_attributes('-transparentcolor', 'white')


main_frame = Frame(root, bg='#f0f0f0', highlightthickness=2)
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

close_button = Button(main_frame, text='X', command=root.destroy, 
                     bg='#f0f0f0', bd=0, padx=10,
                     font=('Arial', 14),
                     width=3, height=1)
close_button.pack(anchor='ne')

welcome = Label(root, text="Rainy", font=('Source Code Pro',20,'italic'))
welcome.place(x=10, y=10)

root.mainloop()

