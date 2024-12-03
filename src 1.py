import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'South_Asian_dataset_new.csv'  # Adjust path if necessary
data = pd.read_csv("./dataset/South_Asian_dataset new.csv")

# Data Cleaning
# Convert GDP and related columns to numeric after removing non-numeric characters
numeric_columns = [
    'GDP (current US$)',
    'GDP growth (annual %)',
    'GDP per capita (current US$)',
    'Population growth (annual %)'
]

for col in numeric_columns:
    data[col] = pd.to_numeric(data[col].str.replace('[^\d.]', '', regex=True), errors='coerce')

# Visualization 1: Line Plot (GDP over the years for a selected country)
def plot_gdp_over_years(country_name):
    country_data = data[data['Country'] == country_name]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['GDP (current US$)'], marker='o', label='GDP (current US$)')
    plt.title(f'GDP Over the Years for {country_name}')
    plt.xlabel('Year')
    plt.ylabel('GDP (current US$)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Visualization 2: Bar Chart (GDP per capita comparison across countries in a specific year)
def plot_gdp_per_capita(year):
    year_data = data[data['Year'] == year]
    plt.figure(figsize=(12, 8))
    plt.bar(year_data['Country'], year_data['GDP per capita (current US$)'], color='skyblue')
    plt.title(f'GDP per Capita in {year}')
    plt.xlabel('Country')
    plt.ylabel('GDP per Capita (current US$)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Visualization 3: Scatter Plot (Life Expectancy vs Infant Mortality)
def plot_life_expectancy_vs_infant_mortality():
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Life expectancy at birth, total (years)'],
                data['Mortality rate, infant (per 1,000 live births)'],
                alpha=0.7, color='coral')
    plt.title('Life Expectancy vs Infant Mortality')
    plt.xlabel('Life Expectancy at Birth (years)')
    plt.ylabel('Infant Mortality Rate (per 1,000 live births)')
    plt.grid(True)
    plt.show()

# Run Visualizations
plot_gdp_over_years('India')  # Example: GDP of India over the years
plot_gdp_per_capita(2000)     # Example: GDP per capita in 2000
plot_life_expectancy_vs_infant_mortality()  # Life expectancy vs infant mortality
