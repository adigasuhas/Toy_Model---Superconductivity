#------------------------------------------------------------------------------------------------------------------#
# Name : Suhas Adiga
# Project : Toy model to explain Cooper pair formation in superconductors  
# Code : GUI Integration - 2D System
# Date : 05-10-2024
#------------------------------------------------------------------------------------------------------------------#

# Importing the necessary libraries 

import numpy as np 
import matplotlib.pyplot as plt 
import tkinter as tk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#------------------------------------------------------------------------------------------------------------------#
# Declaring Global constants 

k = 8.99e9
e = -1.6e-19

# Function to generate position of lattice points

def generate_positions(m, a, x):
    if m == 3:
        positions = {
            "A": (a, 0),
            "B": (0, 0),
            "L1": (-a / 2, a / 2),
            "L2": (-a / 2, -a / 2),
            "L3": (a - x / np.sqrt(2), x / np.sqrt(2)),
            "L4": (a - x / np.sqrt(2), -x / np.sqrt(2)),
            "L5": (a + x / np.sqrt(2), x / np.sqrt(2)),
            "L6": (a + x / np.sqrt(2), -x / np.sqrt(2)),
        }
    else:
        positions = {
            "A": (a, 0),
            "B": (-a, 0),
            "L1": (-a / 2, a / 2),
            "L2": (-a / 2, -a / 2),
            "L3": (a - x / np.sqrt(2), x / np.sqrt(2)),
            "L4": (a - x / np.sqrt(2), -x / np.sqrt(2)),
            "L5": (a + x / np.sqrt(2), x / np.sqrt(2)),
            "L6": (a + x / np.sqrt(2), -x / np.sqrt(2)),
        }
    for i in range(1, m):
        positions[f"L7_m{i}"] = (-a * (2 * i - 1) / 2, a / 2)
        positions[f"L8_m{i}"] = (-a * (2 * i - 1) / 2, -a / 2)

    return positions

# Function to plot the distribution

def graph_plot():
    m = int(entry_1.get())  
    a = float(entry_2.get())  
    x = float(entry_4.get())  
    n = int(entry_3.get())  

    # Evaluating force to the left 
    Fleft=0
    for i in range(1,int((m+3)/2)):
    	Fleft=Fleft + ((2*k*n*e**2)*((2*i-1)*a)/2)/(((((2*i-1)*a)/2)**2)\
    		+(a/2)**2)**(3/2)
    #Evaluating net forces to right 
    Fright=0
    for i in range(1,int((m-1)/2)):
    	Fright=Fright+((2*k*n*e**2)*((2*i-1)*a)/2)/(((((2*i-1)*a)/2)**2)\
    		+(a/2)**2)**(3/2)

    # Evaluating force between two electrons 
    Fee=(k*e**2)/(((m-1)*a)/2)**2

    # Function to calculate net force 

    def f(x):
    		return -1*(-1*Fleft + Fright + (2*k*n*e**2/((((m-1)*a)/2 + \
    			(x/np.sqrt(2)))**2 +(x/np.sqrt(2))**2)**(3/2))*(((m-1)*a)/2 + \
    		(x/np.sqrt(2))) +(2*k*n*e**2/((((m-1)*a)/2 - (x/np.sqrt(2)))**2 \
    			+(x/np.sqrt(2))**2)**(3/2))*(((m-1)*a)/2 - (x/np.sqrt(2))) + -1*Fee)

    result = f(x)
    plt.figure(fig1.number, figsize=(10,6))  
    plt.clf()  
    
    positions = generate_positions(m, a, x)
    for label, (x_pos, y_pos) in positions.items():
        if label.startswith("L"):
            color = 'magenta' if "7" in label or "8" in label else 'blue' if "1" in label or "2" else 'green' if "5" in label or "6" else 'red'
            plt.plot(x_pos, y_pos, 'o', color=color, markersize=10)
    plt.plot(positions['A'][0], positions['A'][1], 'ko', markersize=5)
    plt.plot(positions['B'][0], positions['B'][1], 'ko', markersize=5)
    plt.axis('off')
    plt.text(-0.2,-0.2,"electron -A ",color='green',fontweight='bold')
    plt.text(a-0.2,-0.2,"electron -B ",color='green',fontweight='bold')
    plt.text(-0.8,-0.7,"Lattice Ion (+Ne) ",color='navy',fontweight='bold')
    plt.title(f"Distorted {m}x1 Unit Cell Lattice (2-D)", fontweight = 'bold', fontsize = 15, color = 'red')
    canvas1.draw()  

    plt.figure(fig2.number,figsize=(10,6))  
    plt.clf()  


    def y(x):
        return 0 * x
    
    x = np.linspace(0.2*a, 2 * a, 1000)
    plt.plot(x, y(x), linestyle='--', color='grey')
    color_1 = ['limegreen', 'blue', 'darkgreen', 'red' ]
    for N in range(n,n+4):
    	Fleft=0
    	for i in range(1,int((m+3)/2)):
    		Fleft=Fleft + ((2*k*N*e**2)*((2*i-1)*a)/2)/(((((2*i-1)*a)/2)**2)\
    		+(a/2)**2)**(3/2)
    		
    	Fright=0
    	for i in range(1,int((m-1)/2)):
    		Fright=Fright+((2*k*N*e**2)*((2*i-1)*a)/2)/(((((2*i-1)*a)/2)**2)\
    			+(a/2)**2)**(3/2)
    	Fee=(k*e**2)/(((m-1)*a)/2)**2
    	def f(x):
    		return -1*(-1*Fleft + Fright + (2*k*N*e**2/((((m-1)*a)/2 + \
    			(x/np.sqrt(2)))**2 +(x/np.sqrt(2))**2)**(3/2))*(((m-1)*a)/2 + \
    		(x/np.sqrt(2))) +(2*k*N*e**2/((((m-1)*a)/2 - (x/np.sqrt(2)))**2 \
    			+(x/np.sqrt(2))**2)**(3/2))*(((m-1)*a)/2 - (x/np.sqrt(2))) + -1*Fee)
    	plt.plot(x, f(x), color=color_1[(N - n) % len(color_1)], label=f'N={N}')
    	plt.legend(loc= 'best')
    	plt.title('$F_{res}$ v/S ($\lambda$/a)(2-D)', fontsize = 15 )
    	#plt.text(0.72,-1,"Attractive Force",color='green',fontweight='bold')
    	plt.text(0.72,0.03e-10*((a**2)),"Repulsive Force",color='red',fontweight='bold')
    	plt.yticks([])
    plt.ylabel('$F_{res}$', fontsize = 16)
    plt.xlabel('$\lambda$/a',fontsize = 16)


    canvas2.draw()  

    result_label.config(text=f"The net resultant force on electron - A is: {result} N")

#------------------------------------------------------------------------------------------------------------------#

root = tk.Tk()
#root.config(width = 800, height = 800)
root.title('Toy Model to explain Cooper Pair Formation in Superconductors (2D)')
root.geometry("1600x1200")  


input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


label_1 = tk.Label(input_frame, text='Enter the number of unit cells required (m): ', font=("helv15", 14))
label_1.grid(row=0, column=0, sticky='w', pady=5)

entry_1 = tk.Entry(input_frame, font=("helv15", 14))
entry_1.grid(row=0, column=1, pady=5)

label_2 = tk.Label(input_frame, text='Enter the lattice parameter (a) (in SI units) :', font=("helv15", 14))
label_2.grid(row=1, column=0, sticky='w', pady=5)

entry_2 = tk.Entry(input_frame, font=("helv15", 14))
entry_2.grid(row=1, column=1, pady=5)

label_3 = tk.Label(input_frame, text='Enter the Atomic Number (N):', font=("helv15", 14))
label_3.grid(row=2, column=0, sticky='w', pady=5)

entry_3 = tk.Entry(input_frame, font=("helv15", 14))
entry_3.grid(row=2, column=1, pady=5)

label_4 = tk.Label(input_frame, text='Enter the displacement along the diagonal (λ) (in SI units) :', font=("helv15", 14))
label_4.grid(row=3, column=0, sticky='w', pady=5)

entry_4 = tk.Entry(input_frame, font=("helv15", 15))
entry_4.grid(row=3, column=1, pady=5)

plot_button = tk.Button(input_frame, text='Plot', command=graph_plot, font=("Arial", 12), bg='blue', fg='white')
plot_button.grid(row=4, columnspan=2, pady=10)

label_5 = tk.Label(input_frame, text='Note: The value of K = 8.99e9 (in SI) and e = -1.6021e-19 C ', font=("helv15", 16))
label_5.grid(row = 2, column = 3 , pady = 5)

label_6 = tk.Label(input_frame, text='Note: Net force = +ve implies repulsive force and -ve implies attractive force ', font=("helv15", 15))
label_6.grid(row = 5, column = 3 , pady = 5)

result_label = tk.Label(input_frame, text="The net resultant force on electron- A is:", font=("helv15", 16))
result_label.grid(row=5, columnspan=2, pady=10)


fig1 = plt.figure(figsize=(8, 6))
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas_widget1 = canvas1.get_tk_widget()
canvas_widget1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

fig2 = plt.figure(figsize=(8, 6))
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas_widget2 = canvas2.get_tk_widget()
canvas_widget2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()