import tkinter as tk
from tkinter import ttk, messagebox
import requests
from sarvamai import SarvamAI
from config import SARVAM_API_KEY
client = SarvamAI(api_subscription_key="SARVAM_API_KEY")

LANGUAGES = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Kannada": "kn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Malayalam": "ml-IN",
    "Bengali": "bn-IN",
    "Marathi": "mr-IN",
    "Gujarati":"gu-IN"
}
def translate_text():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = LANGUAGES[source_language.get()]
    target = LANGUAGES[target_language.get()]

    try:
        response = client.text.translate(
            input=text,
            source_language_code=source,
            target_language_code=target,
            model="sarvam-translate:v1",
            mode="formal"
        )

        result = response.translated_text

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except Exception as error:
        messagebox.showerror("Translation Error", str(error))

def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

def copy_translation():
    text = output_box.get("1.0", tk.END).strip()

    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Translation copied!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy.")
        
root = tk.Tk()
root.title("Language Translator")
root.geometry("400x600")

title = tk.Label(
    root,
    text="Language Translator",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Enter text:").pack()

input_box = tk.Text(root, height=7, width=42)
input_box.pack(pady=8)

source_language = ttk.Combobox(
    root,
    values=list(LANGUAGES.keys()),
    state="readonly"
)
source_language.set("English")
source_language.pack(pady=5)

target_language = ttk.Combobox(
    root,
    values=list(LANGUAGES.keys()),
    state="readonly"
)
target_language.set("Kannada")
target_language.pack(pady=5)

translate_button = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold")
)
translate_button.pack(pady=12)

tk.Label(root, text="Translation:").pack()

output_box = tk.Text(root, height=7, width=42)
output_box.pack(pady=8)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_text
)
clear_button.pack(pady=10)
copy_button = tk.Button(
    root,
    text="Copy Translation",
    command=copy_translation
)
copy_button.pack(pady=5)

root.mainloop()