from matplotlib import pyplot as plt

# Pie-chart, where the slices will be ordered
# and plotted counter-clockwise:

Players = 'Ronaldo', 'Messi', 'Neymar', 'Lewandowski'

Score = [45, 30, 15, 10]

explode = (0.1, 0, 0, 0)   # it's "explode" the 1st slice

fig1, ax1 = plt.subpllots()

ax1.pie(Score, explode=explode, labels=Players, autopct='%1.1f%%',
	shadow=True, startangle=90)

ax1.ais('equal')   # Equal aspect ratio ensures that pie is drawn as a circle

plt.show()

