#------------------------------------------------------------------------------------------------------------------#
# Name : Suhas Adiga
# Project : Toy model to explain Cooper pair formation in superconductors  
# Code : GUI Integration - 3D System
# Date : 08-10-2024
#------------------------------------------------------------------------------------------------------------------#

# Importing the necessary libraries 

import numpy as np 
import matplotlib.pyplot as plt 
import tkinter as tk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#------------------------------------------------------------------------------------------------------------------#
# Declaring global constants

K = 8.99e9
e = -1.6e-19
#------------------------------------------------------------------------------------------------------------------#
# Defining a function to plot the curve 

def graph_plot():
    m = int(entry_1.get())  
    a = float(entry_2.get())  
    x = float(entry_4.get())  
    n = int(entry_3.get()) 
    # Trigonometric ratios 

    D=np.sqrt(2/3) 
    E=np.sqrt(1/2)

    # Force to left 
    Fl=0
    for i in range(1,int(0.5*m+1.5)):
        Fl=Fl+ (16*K*n*e**2*((2*i-1)/(((2*i-1)**2 + 2)*(np.sqrt((2*i-1)\
            **2 + 2)))))/a**2
    
    # Force to right
    Fr=0
    for i in range(1,int(0.5*m-0.5)):
        Fr=Fr+ (16*K*n*e**2*(2*i-1)/(((2*i-1)**2 + 2)*(np.sqrt((2*i-1)\
            **2 + 2))))/a**2

    # Force between two electrons
    F12=K*e**2/(((m-1)/2)*a)**2

    # Function to calculate net force 
    def f(x):
        return -1*(Fr - Fl - F12 + (((K*n*e**2)/((np.sqrt((0.5*(m-1)*a \
            - x*D*E)**2+ 2*((x*D*E)**2))**3)))*(4*(0.5*(m-1)*a-x*D*E)) \
        + ((K*n*e**2)/((np.sqrt((0.5*(m-1)*a + x*D*E)**2 + 2*((x*D*E)**2))\
            **3)))*(4*(0.5*(m-1)*a+x*D*E))))

    result = f(x)
   
    plt.figure(fig2.number,figsize=(10,6))  
    plt.clf()  

    def y(x):
        return 0 * x
    
    x = np.linspace(0.2*a, 2 * a, 1000)
    plt.plot(x, y(x), linestyle='--', color='grey')
    color_1 = ['limegreen', 'blue', 'darkgreen', 'red' ]
    for N in range(n,n+4):
        Fl=0
        for i in range(1,int(0.5*m+1.5)):
            Fl=Fl+ (16*K*N*e**2*((2*i-1)/(((2*i-1)**2 + 2)*(np.sqrt((2*i-1)\
                **2 + 2)))))/a**2
        Fr=0
        for i in range(1,int(0.5*m-0.5)):
            Fr=Fr+ (16*K*N*e**2*(2*i-1)/(((2*i-1)**2 + 2)*(np.sqrt((2*i-1)\
                **2 + 2))))/a**2
        F12=K*e**2/(((m-1)/2)*a)**2
        def f(x):
            return -1*(Fr - Fl - F12 + (((K*N*e**2)/((np.sqrt((0.5*(m-1)*a \
                - x*D*E)**2+ 2*((x*D*E)**2))**3)))*(4*(0.5*(m-1)*a-x*D*E)) \
            + ((K*N*e**2)/((np.sqrt((0.5*(m-1)*a + x*D*E)**2 + 2*((x*D*E)**2))\
                **3)))*(4*(0.5*(m-1)*a+x*D*E))))
        plt.plot(x, f(x), color=color_1[(N - n) % len(color_1)], label=f'N={N}')
        plt.legend(loc= 'best')
        plt.title('$F_{res}$ v/S ($\lambda$/a)(3-D)', fontsize = 15 )
        #plt.text(0.72,-1,"Attractive Force",color='green',fontweight='bold')
        plt.text(1.25,0.02e-29,"Repulsive Force",color='red',fontweight='bold')
        plt.yticks([])
    plt.ylabel('$F_{res}$', fontsize = 16)
    plt.xlabel('$\lambda$/a',fontsize = 16)
    canvas2.draw()  
    result_label.config(text=f"The net resultant force on electron - A is: {result} N")

#------------------------------------------------------------------------------------------------------------------#
# Tkinter GUI Part 

root = tk.Tk()
#root.config(width = 800, height = 800)
root.title('Toy Model to explain Cooper Pair Formation in Superconductors (3D)')
root.geometry("1600x1200")  

input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


label_1 = tk.Label(input_frame, text='Enter the number of unit cells required in 3-Dimension (m): ', font=("helv15", 14))
label_1.grid(row=0, column=0, sticky='w', pady=5)

entry_1 = tk.Entry(input_frame, font=("helv15", 14))
entry_1.grid(row=0, column=1, pady=5)

label_2 = tk.Label(input_frame, text='Enter the lattice parameter (a) (in SI) :', font=("helv15", 14))
label_2.grid(row=1, column=0, sticky='w', pady=5)

entry_2 = tk.Entry(input_frame, font=("helv15", 14))
entry_2.grid(row=1, column=1, pady=5)

label_3 = tk.Label(input_frame, text='Enter the Atomic Number (N):', font=("helv15", 14))
label_3.grid(row=2, column=0, sticky='w', pady=5)

entry_3 = tk.Entry(input_frame, font=("helv15", 14))
entry_3.grid(row=2, column=1, pady=5)

label_4 = tk.Label(input_frame, text='Enter the displacement along the diagonal (λ) (in SI) :', font=("helv15", 14))
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


fig2 = plt.figure(figsize=(10, 6))
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas_widget2 = canvas2.get_tk_widget()
canvas_widget2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()