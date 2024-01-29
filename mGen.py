import tkinter as tk
from tkinter import filedialog, messagebox
import json
import random
import os

def add_trait():
    frame = tk.Frame(window)
    frame.pack(fill='x', padx=10, pady=5)

    entry_label = tk.Label(frame, text=f"Trait Type {len(trait_frames) + 1}:")
    entry_label.pack(side='left')

    entry = tk.Entry(frame, width=30)
    entry.pack(side='left', padx=5)

    # Pass the actual index of the trait entry
    button = tk.Button(frame, text='Select File', command=lambda index=len(trait_entries): select_file(index))
    button.pack(side='left', padx=5)

    trait_frames.append(frame)
    trait_entries.append(entry)
    trait_file_buttons.append(button)

def select_file(index):
    filename = filedialog.askopenfilename()
    if filename:  # Only add if a file was selected
        trait_files[index] = filename
        print(f"File selected for trait {index}: {filename}")  # Debug print

def generate_metadata():
    collection = collection_name_entry.get()
    description = description_entry.get()
    quantity = int(quantity_entry.get())
    output_folder = 'json'
    os.makedirs(output_folder, exist_ok=True)
    traits = {}

    # Check if a file has been selected for each trait type and load traits
    for i in range(len(trait_entries)):
        trait_name = trait_entries[i].get()
        if not trait_name:
            messagebox.showerror("Error", f"Trait type name missing for trait {i+1}.")
            return

        # Check if a file has been selected for this trait type
        if i not in trait_files:
            messagebox.showerror("Error", f"Please select a file for trait type '{trait_name}'.")
            return

        # Load traits from file
        try:
            with open(trait_files[i], 'r') as f:
                traits[trait_name] = f.read().splitlines()
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file for trait '{trait_name}': {e}")
            return

    # Generate metadata
    for i in range(quantity):
        metadata = {
            "name": f"{collection} #{i}",
            "description": description,
            "attributes": [{"trait_type": trait, "value": random.choice(values)} for trait, values in traits.items() if values]
        }
        with open(os.path.join(output_folder, f'{i}.json'), 'w') as f:
            json.dump(metadata, f, indent=4)


window = tk.Tk()
window.title("mGen")
window.geometry('500x600')

collection_frame = tk.Frame(window)
collection_frame.pack(fill='x', padx=10, pady=5)
collection_label = tk.Label(collection_frame, text="Collection Name:")
collection_label.pack(side='left')
collection_name_entry = tk.Entry(collection_frame)
collection_name_entry.pack(fill='x', expand=True, padx=5)

description_frame = tk.Frame(window)
description_frame.pack(fill='x', padx=10, pady=5)
description_label = tk.Label(description_frame, text="Description:")
description_label.pack(side='left')
description_entry = tk.Entry(description_frame)
description_entry.pack(fill='x', expand=True, padx=5)

quantity_frame = tk.Frame(window)
quantity_frame.pack(fill='x', padx=10, pady=5)
quantity_label = tk.Label(quantity_frame, text="Quantity:")
quantity_label.pack(side='left')
quantity_entry = tk.Entry(quantity_frame)
quantity_entry.pack(fill='x', expand=True, padx=5)

trait_frames = []
trait_entries = []
trait_file_buttons = []
trait_files = {}
add_trait()

add_trait_button = tk.Button(window, text='+ Add Another Trait Type', command=add_trait)
add_trait_button.pack(fill='x', padx=10, pady=5)

generate_button = tk.Button(window, text='Generate Metadata', command=generate_metadata)
generate_button.pack(side='bottom', fill='x', padx=10, pady=10)

window.mainloop()
