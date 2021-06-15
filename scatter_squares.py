import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-deep')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c=(y_values), cmap='turbo', s=10)

#Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet.
ax.tick_params(axis='both', which='major', labelsize=14)
ax.ticklabel_format(useOffset=False, style='plain')

#Zdefininowanie zakresu dla każdej osi.
ax.axis([0, 1100, 0, 1100000])
plt.show()
#Zapis do pliku, bbox_inches='tight' powoduje usunięcie białych znaków dookoła wykresu
#plt.savefig('squares_plot2.png', bbox_inches='tight')