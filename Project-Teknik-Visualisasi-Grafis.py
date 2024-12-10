import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk menghitung data grafik
def update_graph():
    try:
        battery_capacity = float(entry_battery.get())
        efficiency = float(entry_efficiency.get())
        speed = speed_slider.get()

        # Simulasi hubungan jarak tempuh dan konsumsi daya
        distance = [i for i in range(0, 101)]  # 0-100 km
        power_consumption = [(i / efficiency) + (speed * 0.05) for i in distance]  # Simulasi formula

        # Clear previous plots
        ax.clear()
        ax.plot(distance, power_consumption, label="Konsumsi Daya (kWh)", color="blue")
        ax.set_title("Grafik Jarak Tempuh vs Konsumsi Daya")
        ax.set_xlabel("Jarak Tempuh (km)")
        ax.set_ylabel("Konsumsi Daya (kWh)")
        ax.legend()
        ax.grid(True)

        canvas.draw()
    except ValueError:
        error_label.config(text="Masukkan angka valid untuk semua input!")

# Antarmuka Tkinter
root = tk.Tk()
root.title("Demo Kendaraan Listrik dengan Visualisasi Grafis")

# Frame Input
frame_input = ttk.Frame(root, padding=10)
frame_input.grid(row=0, column=0, sticky="nsew")

# Input Kapasitas Baterai
ttk.Label(frame_input, text="Kapasitas Baterai (kWh):").grid(row=0, column=0, sticky="w")
entry_battery = ttk.Entry(frame_input)
entry_battery.grid(row=0, column=1, sticky="e")

# Input Efisiensi
ttk.Label(frame_input, text="Efisiensi Kendaraan (km/kWh):").grid(row=1, column=0, sticky="w")
entry_efficiency = ttk.Entry(frame_input)
entry_efficiency.grid(row=1, column=1, sticky="e")

# Slider Kecepatan
ttk.Label(frame_input, text="Kecepatan Kendaraan (km/jam):").grid(row=2, column=0, sticky="w")
speed_slider = tk.Scale(frame_input, from_=10, to=120, orient="horizontal")
speed_slider.grid(row=2, column=1, sticky="e")

# Error Label
error_label = tk.Label(frame_input, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2)

# Tombol Update
update_button = ttk.Button(frame_input, text="Update Grafik", command=update_graph)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

# Frame Grafik
frame_graph = ttk.Frame(root, padding=10)
frame_graph.grid(row=1, column=0, sticky="nsew")

# Matplotlib Figure
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack()

# Jalankan Program
root.mainloop()
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk menghitung data grafik
def update_graph():
    try:
        battery_capacity = float(entry_battery.get())
        efficiency = float(entry_efficiency.get())
        speed = speed_slider.get()

        # Simulasi hubungan jarak tempuh dan konsumsi daya
        distance = [i for i in range(0, 101)]  # 0-100 km
        power_consumption = [(i / efficiency) + (speed * 0.05) for i in distance]  # Simulasi formula

        # Clear previous plots
        ax.clear()
        ax.plot(distance, power_consumption, label="Konsumsi Daya (kWh)", color="blue")
        ax.set_title("Grafik Jarak Tempuh vs Konsumsi Daya")
        ax.set_xlabel("Jarak Tempuh (km)")
        ax.set_ylabel("Konsumsi Daya (kWh)")
        ax.legend()
        ax.grid(True)

        canvas.draw()
    except ValueError:
        error_label.config(text="Masukkan angka valid untuk semua input!")

# Antarmuka Tkinter
root = tk.Tk()
root.title("Demo Kendaraan Listrik dengan Visualisasi Grafis")

# Frame Input
frame_input = ttk.Frame(root, padding=10)
frame_input.grid(row=0, column=0, sticky="nsew")

# Input Kapasitas Baterai
ttk.Label(frame_input, text="Kapasitas Baterai (kWh):").grid(row=0, column=0, sticky="w")
entry_battery = ttk.Entry(frame_input)
entry_battery.grid(row=0, column=1, sticky="e")

# Input Efisiensi
ttk.Label(frame_input, text="Efisiensi Kendaraan (km/kWh):").grid(row=1, column=0, sticky="w")
entry_efficiency = ttk.Entry(frame_input)
entry_efficiency.grid(row=1, column=1, sticky="e")

# Slider Kecepatan
ttk.Label(frame_input, text="Kecepatan Kendaraan (km/jam):").grid(row=2, column=0, sticky="w")
speed_slider = tk.Scale(frame_input, from_=10, to=120, orient="horizontal")
speed_slider.grid(row=2, column=1, sticky="e")

# Error Label
error_label = tk.Label(frame_input, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2)

# Tombol Update
update_button = ttk.Button(frame_input, text="Update Grafik", command=update_graph)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

# Frame Grafik
frame_graph = ttk.Frame(root, padding=10)
frame_graph.grid(row=1, column=0, sticky="nsew")

# Matplotlib Figure
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack()

# Jalankan Program
root.mainloop()
