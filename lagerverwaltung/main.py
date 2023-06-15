import tkinter as tk
from warehouse import *
from tkinter import messagebox


# Anmerkung:
#
# Dieser Code wurde größtenteils automatisch generiert.
# Er erzeugt eine einfache und schlichte GUI für das Projekt
# und stellt die Schnittstelle zwischen Benutzer und der Klasse 
# Warehouse her.

def handle_inbound():
    sku = sku_entry.get()
    location = location_entry.get()
    try:
        warehouse.store(sku, location)
        messagebox.showinfo("Artikel erfolgreich eingebucht!", "Artikel erfolgreich eingebucht!")
    except Exception as e:
        messagebox.showerror("Artikel kann nicht eingelagert werden!", str(e))
    update_overview()


def handle_search():
    sku = sku_entry2.get()
    try:
        location = warehouse.find(sku)
        if location == "0":
            messagebox.showwarning("Artikel nicht gefunden!", "Artikel wurde nicht gefunden.")
        else:
            messagebox.showinfo("Artikel gefunden!", "Artikel " + sku + " ist in " + location + ".")
    except Exception as e:
        messagebox.showerror("Artikel nicht gefunden!", str(e))


def handle_outbound():
    sku = sku_entry3.get()
    try:
        warehouse.retrieve(sku)
        messagebox.showinfo("Artikel erfolgreich ausgebucht!", "Artikel erfolgreich ausgebucht!")
    except Exception as e:
        messagebox.showerror("Artikel kann nicht ausgelagert werden!", str(e))
    update_overview()


def update_overview():
    warehouse_overview_text.delete(1.0, tk.END)
    warehouse_overview_text.insert(tk.END, warehouse.getOverview())


if __name__ == "__main__":
    # Create our warehouse
    warehouse = Warehouse()

    # Create the main window
    root = tk.Tk()
    root.title("Lagerverwaltung")

    # --- Title label ---
    title_label = tk.Label(root, text="Lagerverwaltung", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # --- Inbound Section ---
    inbound_frame = tk.LabelFrame(root, text="Einbuchen")
    inbound_frame.pack(padx=10, pady=5, fill="both")

    sku_label = tk.Label(inbound_frame, text="SKU:")
    sku_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    sku_entry = tk.Entry(inbound_frame, bg="white")
    sku_entry.grid(row=0, column=1, padx=5, pady=5)

    location_label = tk.Label(inbound_frame, text="Lagerplatz:")
    location_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    location_entry = tk.Entry(inbound_frame, bg="white")
    location_entry.grid(row=1, column=1, padx=5, pady=5)

    inbound_button = tk.Button(inbound_frame, text="Einbuchen", command=handle_inbound)
    inbound_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # --- Search Section ---
    search_frame = tk.LabelFrame(root, text="Suchen")
    search_frame.pack(padx=10, pady=5, fill="both")

    sku_label2 = tk.Label(search_frame, text="SKU:")
    sku_label2.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    sku_entry2 = tk.Entry(search_frame, bg="white")
    sku_entry2.grid(row=0, column=1, padx=5, pady=5)
    search_button = tk.Button(search_frame, text="Suchen", command=handle_search)
    search_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # --- Outbound Section ---
    outbound_frame = tk.LabelFrame(root, text="Ausbuchen")
    outbound_frame.pack(padx=10, pady=5, fill="both")

    sku_label3 = tk.Label(outbound_frame, text="SKU:")
    sku_label3.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    sku_entry3 = tk.Entry(outbound_frame, bg="white")
    sku_entry3.grid(row=0, column=1, padx=5, pady=5)

    outbound_button = tk.Button(outbound_frame, text="Ausbuchen", command=handle_outbound)
    outbound_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # --- Warehouse Overview ---
    warehouse_overview_label = tk.Label(root, text="Lagerplatzübersicht", font=("Arial", 14, "bold"))
    warehouse_overview_label.pack(pady=10)

    warehouse_overview_frame = tk.Frame(root)
    warehouse_overview_frame.pack(padx=10, pady=5, fill="both")

    warehouse_overview_text = tk.Text(warehouse_overview_frame)
    warehouse_overview_text.pack(side=tk.LEFT, padx=5, pady=5, fill="both", expand=True)

    update_button = tk.Button(warehouse_overview_frame, text="Aktualisieren", command=update_overview)
    update_button.pack(side=tk.RIGHT, padx=5, pady=5)

    # Start the main event loop
    root.mainloop()
