

import matplotlib.pyplot as plt

days = ["Ponedeljak", "Utorak", "Sreda", "Četvrtak", "Petak", "Subota", "Nedelja"]
temperatures = [25, 27, 26, 24, 28, 27, 26]

plt.plot(days, temperatures, marker='o')

max_temp = max(temperatures)
max_index = temperatures.index(max_temp)

plt.scatter(days[max_index], max_temp, s=100, zorder=5, color="red")
plt.annotate("Najtopliji dan", xy=(days[max_index], max_temp), zorder=6)


plt.show()