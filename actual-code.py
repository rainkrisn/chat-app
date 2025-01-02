import customtkinter as ctk

# Create a CTk instance
root = ctk.CTk()
root.geometry("1500x700")
root.title("BanranApp")

# Remove the title bar
root.overrideredirect(True)

# Main frame using CTkFrame
main_frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#f0f0f0", border_width=2)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Close button using CTkButton
close_button = ctk.CTkButton(
    main_frame,
    text="X",
    command=root.destroy,
    fg_color="#f0f0f0",
    hover_color="#e0e0e0",
    text_color="black",
    font=("Arial", 14),
    width=50,
    height=30
)
close_button.pack(anchor="ne")

# Welcome label using CTkLabel
welcome = ctk.CTkLabel(root, text="Rainy", font=("Source Code Pro", 30, "bold"))
welcome.place(x=10, y=10)

# Input Entry and Array
TextArray = []

# Add a variable to track the current y-position for messages
message_y_position = 100

def submit_text():
    text = entry.get()
    if text:  # Check if the entry is not empty
        TextArray.append(text)
        print(f"Submitted: {text}")
        entry.delete(0, 'end')  # Clear the entry

entry = ctk.CTkEntry(
    master=root,
    placeholder_text="Write your message here...",
    font=("Source Code Pro", 30, "italic"),
    width=500,
    height=25,
    border_width=2,
    corner_radius=10
)
entry.place(x=500, y=600)

# Add an upward arrow button
def on_arrow_click(event=None):
    global message_y_position
    text = entry.get()
    if text:  # Only create label if there's text
        # Create label with root as parent and entry text as the display text
        label = ctk.CTkLabel(
            root, 
            text=text,
            font=("Trade Gothic", 20),
        )

        # Place the label at the current y-position
        label.place(x=90
                    , y=message_y_position)
        
        # Move the position up for the next message
        message_y_position -= 30  # Adjust this value to control spacing between messages
        
        # Clear the entry field
        entry.delete(0, 'end')

root.bind("<Return>", on_arrow_click)

arrow_button = ctk.CTkButton(
    root,
    text="↑",  # Unicode for upward arrow
    command=on_arrow_click,
    font=("Arial", 15, "bold"),
    fg_color="#000000",
    text_color="White",
    hover_color="#d3d3d3",
    corner_radius=30,
    width=40,
    height=50
)
arrow_button.place(x=1000, y=600)

# Start the main loop
root.mainloop()
