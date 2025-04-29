import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', label='original data', alpha=.5)


    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, _, _, _ = linregress(x, y)
    
    def myfunc(x):
        return slope * x + intercept 
    
    mymodel = list(map(myfunc, range(1880, 2051, 1)))
    plt.plot(range(1880, 2051, 1), mymodel, label='fitted line', color='red')

    # Create second line of best fit
    mask = df['Year'] >= 2000
    x2 = df[mask]['Year']
    y2 = df[mask]['CSIRO Adjusted Sea Level']
    slope2, intercept2, _, _, _ = linregress(x2, y2)
    
    def myfunc2(x):
        return slope2 * x + intercept2 

    mymodel2 = list(map(myfunc2, range(2000, 2051, 1)))
    plt.plot(range(2000, 2051, 1), mymodel2, label='fitted line 2', color='green')
    plt.legend()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()