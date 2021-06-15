from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Utworzenie kości typu D6
die1 = Die()
die2 = Die(10)

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

#Analiza wyników
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Wizualizacja wyników
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania kośćmi D6 i D10 50000 tysięcy razy',
                   xaxis=x_axis_config, yaxis =y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d6_d10.html')