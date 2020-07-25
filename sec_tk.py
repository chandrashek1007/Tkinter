import tkinter  as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
label2 = tk.Label(text="Hello, Tkinter", fg="white", bg="red")
label1 = tk.Label(text="Hello, Tkinter", background="#34A2FE")
label3 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=1
)
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="purple"  # Set the background color to black
)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)
text_box = tk.Text()
text_box.pack()
label.pack()
label2.pack()
button.pack()
label3.pack()
label1.pack()
greeting.pack()
entry.pack()
print_text = entry.get()
text_box.get("1.0")
print(print_text)
window.mainloop()