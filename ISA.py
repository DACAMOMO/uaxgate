import numpy as np

#DATOS
T0 = 288.15 #valor de la temperatura en K a nivel del mar
P0 = 101325 #valor de la presión en Pa a nivel del mar
rho0 = 1.225 #valor de la densidad en kg/m3 a nivel del mar



#CONDICIÓN DE VUELO 0m<h<11000m

T = T0 - (alpha*h)

P = P0 * (1 - ( (h * alpha) / T0))^((g / R * alpha))

rho = rho0 * (1 - ( (h * alpha) / T0))^((g / R * alpha) - 1)



