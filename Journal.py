
import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime


## "The Last Bookmark" — Journal Edition


quotes = [
    "What a privilege it is to feel discomfort in the pursuit of a goal I chose to pursue.",
    "No reason to stay is a good reason to go.",
    "What goes around comes back around.",
    "Always the poet, never the poem.",
    "What a privilege to be tired from the work you once begged the universe for.",
    "What a privilege to feel overwhelmed by the growth you used to dream about.",
    "What a privilege to be challenged by a life you created on purpose.",
    "How lovely is the silence of growing things.",
    "In the graveyard of the sea, there is nothing but eternity.",
    "Everyone you idolize wakes up scared to be themselves sometimes.",
    "Some people are so poor, all they have is money.",
    "Whoever gives nothing has nothing.",
    "The greatest misfortune is not to be unloved, but not to love.",
    "Can a man possessing consciousness ever really respect himself?",
    "The habit of despair is worse than despair itself.",
    "Forgive me for not answering your eyes.",
    "Everything you love will be gone one day — but love will return in another way.",
    "We’re all broken; that’s how the light gets in.",
    "You don’t need revenge.",
    "You need faith — God rebuilds you in front of the people who broke you.",
    "When the roots are deep, there is no reason to fear the wind.",
    "Where did all the years go?",
    "Home is where the heart is.",
    "The deeper the grief, the closer is God.",
    "A heart rich in goodness will always find contentment."
]

# ----------------------------
# Functions
# ----------------------------
def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

def save_entry():
    text = entry_box.get("1.0", tk.END).strip()
    if text:
        with open("journal_entries.txt", "a", encoding="utf-8") as f:
            f.write(f"\n\n{datetime.now().strftime('%d %B %Y, %I:%M %p')}\n{text}")
        messagebox.showinfo("Saved", "Your thought has been saved to 'journal_entries.txt'.")
        entry_box.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty", "Please write something before saving.")

def open_pages():
    try:
        with open("journal_entries.txt", "r", encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            content = "No saved pages yet. Start writing your first thought today!"
    except FileNotFoundError:
        content = "No saved pages yet. Start writing your first thought today!"
    
    # New window for saved pages
    pages_window = tk.Toplevel(root)
    pages_window.title("My Pages — The Last Bookmark")
    pages_window.geometry("700x500")
    pages_window.configure(bg="#f4e9d8")

    tk.Label(
        pages_window,
        text="My Pages",
        font=("Book Antiqua", 22, "bold italic"),
        bg="#f4e9d8",
        fg="#5b4636"
    ).pack(pady=10)

    text_widget = tk.Text(
        pages_window,
        wrap="word",
        font=("Georgia", 12),
        bg="#fdf8f1",
        fg="#3e3227",
        padx=10,
        pady=10
    )
    text_widget.insert("1.0", content)
    text_widget.config(state="disabled")
    text_widget.pack(expand=True, fill="both", padx=20, pady=10)

# ----------------------------
# GUI Setup
# ----------------------------
root = tk.Tk()
root.title("The Last Bookmark — Journal Edition")
root.geometry("750x650")
root.configure(bg="#f4e9d8")  # warm parchment background

# Header
title_label = tk.Label(
    root,
    text="The Last Bookmark",
    font=("Book Antiqua", 28, "bold italic"),
    bg="#f4e9d8",
    fg="#5b4636"
)
title_label.pack(pady=(20, 10))

# Quote
quote_label = tk.Label(
    root,
    text="Click below to reveal a quote...",
    wraplength=650,
    justify="center",
    font=("Georgia", 14, "italic"),
    bg="#f4e9d8",
    fg="#3e3227",
    padx=20,
    pady=20
)
quote_label.pack(pady=10)

next_button = tk.Button(
    root,
    text="Next Quote ✨",
    command=show_quote,
    font=("Book Antiqua", 12, "bold"),
    bg="#d1bfa7",
    fg="#3e3227",
    relief="flat",
    padx=20,
    pady=8
)
next_button.pack()

# Divider line
divider = tk.Frame(root, height=2, bg="#cdb79e", bd=0)
divider.pack(fill="x", pady=20)

# Journal Section
tk.Label(
    root,
    text="Write Today's Thought:",
    font=("Book Antiqua", 16, "bold italic"),
    bg="#f4e9d8",
    fg="#5b4636"
).pack()

entry_box = tk.Text(
    root,
    height=6,
    width=70,
    wrap="word",
    font=("Georgia", 12),
    bg="#fdf8f1",
    fg="#3e3227",
    relief="flat",
    padx=10,
    pady=10
)
entry_box.pack(pady=10)

# Buttons (Save + My Pages)
button_frame = tk.Frame(root, bg="#f4e9d8")
button_frame.pack(pady=5)

save_button = tk.Button(
    button_frame,
    text="Save Entry 🕯️",
    command=save_entry,
    font=("Book Antiqua", 12, "bold"),
    bg="#d1bfa7",
    fg="#3e3227",
    relief="flat",
    padx=15,
    pady=8
)
save_button.grid(row=0, column=0, padx=10)

pages_button = tk.Button(
    button_frame,
    text="My Pages 📖",
    command=open_pages,
    font=("Book Antiqua", 12, "bold"),
    bg="#d1bfa7",
    fg="#3e3227",
    relief="flat",
    padx=15,
    pady=8
)
pages_button.grid(row=0, column=1, padx=10)

# Footer
footer_label = tk.Label(
    root,
    text="“The lesson that shall always reside in my life.”",
    font=("Georgia", 10, "italic"),
    bg="#f4e9d8",
    fg="#7c6a56"
)
footer_label.pack(side="bottom", pady=15)

root.mainloop()
