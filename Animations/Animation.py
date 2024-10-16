import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

# Load the COVID-19 data
covid_data = pd.read_csv('Dataset/day_wise.csv')

# Convert 'Date' column to datetime
covid_data['Date'] = pd.to_datetime(covid_data['Date'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize the plot with empty data
def init():
    ax.clear()
    ax.set_xlim(covid_data['Date'].min(), covid_data['Date'].max())
    ax.set_ylim(0, covid_data['Confirmed'].max())
    ax.set_title('Spread of COVID-19 Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed Cases')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())

# Update function for each frame of the animation
def update(day):
    ax.clear()
    ax.plot(covid_data['Date'][:day], covid_data['Confirmed'][:day], label='Confirmed Cases', color='blue')
    ax.plot(covid_data['Date'][:day], covid_data['Deaths'][:day], label='Deaths', color='red')
    ax.set_xlim(covid_data['Date'].min(), covid_data['Date'].max())
    ax.set_ylim(0, covid_data['Confirmed'].max())
    ax.set_title('Spread of COVID-19 Over Time (2020)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cases')
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())

# Create the animation
ani = FuncAnimation(fig, update, frames=len(covid_data), init_func=init, interval=100, repeat=True)

# Create a PillowWriter object with looping metadata
pillow_writer = PillowWriter(fps=10)

# Save the animation as a GIF (looping metadata is set automatically for GIFs)
ani.save('Animation/covid_spread_animation.gif', writer=pillow_writer)

plt.show()