import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file

def lennard_jones_potential(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# Bokeh grafiğini tarayıcıda göstermek için
output_file("lennard_jones_potential.html")

# Parametreleri tanımlayın
epsilon = 0.0103  # kJ/mol
sigma = 0.340  # nm
r_min = 0.9 * sigma
r_max = 2.5 * sigma
n_points = 500

# r değerlerini ve potansiyel değerlerini hesaplayın
r_values = np.linspace(r_min, r_max, n_points)
potential_values = lennard_jones_potential(r_values, epsilon, sigma)

# Grafiği oluşturun
p = figure(title="Lennard-Jones Potential", x_axis_label='r (nm)', y_axis_label='V(r) (kJ/mol)')
p.line(r_values, potential_values, line_width=2)

# Grafiği gösterin
show(p)