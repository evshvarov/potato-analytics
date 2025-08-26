#!/usr/bin/env python3
"""
Add potato consumption data to the CSV file
Based on typical per capita consumption patterns and population estimates
"""

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(123)
random.seed(123)

# Read the existing CSV file
df = pd.read_csv('/Users/eshvarov/Github/potato-analytics/data/potato_sales_template_2000_2022.csv')

# Country consumption characteristics
# Based on per capita consumption (kg/person/year) and estimated population
country_consumption_characteristics = {
    # High consumption countries (kg per person per year)
    'Belarus': {'per_capita': 180, 'population_2000': 10000000, 'growth': 0.001},
    'Ukraine': {'per_capita': 140, 'population_2000': 48000000, 'growth': -0.005},
    'Russia': {'per_capita': 130, 'population_2000': 146000000, 'growth': 0.002},
    'Poland': {'per_capita': 125, 'population_2000': 38000000, 'growth': 0.001},
    'Lithuania': {'per_capita': 120, 'population_2000': 3500000, 'growth': -0.003},
    'Latvia': {'per_capita': 115, 'population_2000': 2400000, 'growth': -0.005},
    'Estonia': {'per_capita': 110, 'population_2000': 1400000, 'growth': 0.002},
    'Kazakhstan': {'per_capita': 105, 'population_2000': 15000000, 'growth': 0.008},
    'Ireland': {'per_capita': 100, 'population_2000': 3800000, 'growth': 0.012},
    'Kyrgyzstan': {'per_capita': 95, 'population_2000': 5000000, 'growth': 0.015},
    
    # Medium-high consumption
    'United Kingdom': {'per_capita': 85, 'population_2000': 59000000, 'growth': 0.006},
    'Germany': {'per_capita': 80, 'population_2000': 82000000, 'growth': 0.001},
    'Netherlands': {'per_capita': 78, 'population_2000': 16000000, 'growth': 0.005},
    'Belgium': {'per_capita': 75, 'population_2000': 10200000, 'growth': 0.003},
    'United States': {'per_capita': 73, 'population_2000': 282000000, 'growth': 0.008},
    'Canada': {'per_capita': 70, 'population_2000': 31000000, 'growth': 0.009},
    'Norway': {'per_capita': 68, 'population_2000': 4500000, 'growth': 0.008},
    'Australia': {'per_capita': 65, 'population_2000': 19000000, 'growth': 0.012},
    'Denmark': {'per_capita': 63, 'population_2000': 5300000, 'growth': 0.004},
    'Finland': {'per_capita': 60, 'population_2000': 5200000, 'growth': 0.003},
    
    # Medium consumption
    'France': {'per_capita': 58, 'population_2000': 59000000, 'growth': 0.004},
    'Sweden': {'per_capita': 55, 'population_2000': 8900000, 'growth': 0.006},
    'Switzerland': {'per_capita': 53, 'population_2000': 7200000, 'growth': 0.007},
    'Austria': {'per_capita': 50, 'population_2000': 8100000, 'growth': 0.004},
    'Czechia': {'per_capita': 48, 'population_2000': 10300000, 'growth': 0.002},
    'Slovakia': {'per_capita': 45, 'population_2000': 5400000, 'growth': 0.001},
    'Hungary': {'per_capita': 43, 'population_2000': 10000000, 'growth': -0.002},
    'New Zealand': {'per_capita': 40, 'population_2000': 3900000, 'growth': 0.010},
    'Slovenia': {'per_capita': 38, 'population_2000': 2000000, 'growth': 0.002},
    'Croatia': {'per_capita': 35, 'population_2000': 4500000, 'growth': -0.003},
    
    # Lower-medium consumption
    'Spain': {'per_capita': 33, 'population_2000': 40000000, 'growth': 0.008},
    'Italy': {'per_capita': 30, 'population_2000': 57000000, 'growth': 0.001},
    'Portugal': {'per_capita': 28, 'population_2000': 10300000, 'growth': 0.002},
    'Greece': {'per_capita': 25, 'population_2000': 11000000, 'growth': 0.003},
    'Japan': {'per_capita': 23, 'population_2000': 127000000, 'growth': -0.001},
    'South Korea': {'per_capita': 20, 'population_2000': 47000000, 'growth': 0.004},
    'Israel': {'per_capita': 18, 'population_2000': 6000000, 'growth': 0.018},
    'Turkey': {'per_capita': 15, 'population_2000': 64000000, 'growth': 0.012},
    'Chile': {'per_capita': 13, 'population_2000': 15000000, 'growth': 0.009},
    'Argentina': {'per_capita': 12, 'population_2000': 37000000, 'growth': 0.009},
    
    # Low consumption
    'Brazil': {'per_capita': 10, 'population_2000': 176000000, 'growth': 0.010},
    'Mexico': {'per_capita': 8, 'population_2000': 98000000, 'growth': 0.011},
    'China': {'per_capita': 7, 'population_2000': 1280000000, 'growth': 0.006},
    'India': {'per_capita': 5, 'population_2000': 1050000000, 'growth': 0.013},
    'South Africa': {'per_capita': 4, 'population_2000': 45000000, 'growth': 0.015},
    'Egypt': {'per_capita': 3, 'population_2000': 68000000, 'growth': 0.018},
    'Nigeria': {'per_capita': 2, 'population_2000': 123000000, 'growth': 0.025},
    'Indonesia': {'per_capita': 1.5, 'population_2000': 212000000, 'growth': 0.012},
    'Philippines': {'per_capita': 1, 'population_2000': 76000000, 'growth': 0.018},
    'Vietnam': {'per_capita': 0.8, 'population_2000': 79000000, 'growth': 0.011},
    
    # Very low consumption (tropical/rice-based diets)
    'Thailand': {'per_capita': 0.5, 'population_2000': 63000000, 'growth': 0.005},
    'Malaysia': {'per_capita': 0.3, 'population_2000': 23000000, 'growth': 0.018},
    'Singapore': {'per_capita': 0.2, 'population_2000': 4000000, 'growth': 0.015},
    'Bangladesh': {'per_capita': 0.1, 'population_2000': 131000000, 'growth': 0.012},
}

def generate_consumption_data(country, year, characteristics):
    """Generate realistic potato consumption data for a country and year"""
    if country not in characteristics:
        # Default for countries not in the list - estimate based on development level
        if country in ['Luxembourg', 'Monaco', 'Malta', 'Cyprus', 'Iceland']:
            per_capita = random.uniform(40, 70)  # Developed small countries
            population = random.randint(300000, 2000000)
            growth = random.uniform(0.002, 0.008)
        elif country in ['Qatar', 'UAE', 'Kuwait', 'Bahrain', 'Saudi Arabia', 'Oman']:
            per_capita = random.uniform(5, 25)  # Gulf countries
            population = random.randint(1000000, 10000000)
            growth = random.uniform(0.015, 0.025)
        elif country in ['Romania', 'Bulgaria', 'Serbia', 'Bosnia and Herzegovina', 'Albania', 'North Macedonia', 'Moldova']:
            per_capita = random.uniform(30, 60)  # Eastern Europe
            population = random.randint(2000000, 20000000)
            growth = random.uniform(-0.005, 0.005)
        else:
            per_capita = random.uniform(1, 30)  # Other developing countries
            population = random.randint(5000000, 50000000)
            growth = random.uniform(0.005, 0.020)
    else:
        per_capita = characteristics[country]['per_capita']
        population = characteristics[country]['population_2000']
        growth = characteristics[country]['growth']
    
    # Calculate years since 2000
    years_passed = year - 2000
    
    # Population growth
    current_population = population * (1 + growth) ** years_passed
    
    # Base consumption
    base_consumption = per_capita * current_population
    
    # Add some random variation (±15%)
    random_factor = 1 + np.random.normal(0, 0.15)
    
    # Apply economic and dietary trend factors
    dietary_trend = 1.0
    if year >= 2010:  # Health trends reducing potato consumption in developed countries
        if per_capita > 50:  # Developed countries
            dietary_trend *= 0.98 ** (year - 2010)
    
    # Economic shocks
    if year in [2008, 2009]:  # Financial crisis - people eat more potatoes (cheaper food)
        if per_capita > 30:
            dietary_trend *= 1.05
    elif year in [2020, 2021]:  # COVID-19 - home cooking increased
        dietary_trend *= 1.08
    
    final_value = base_consumption * random_factor * dietary_trend
    
    # Ensure positive values and round to nearest tonne
    return max(0, round(final_value))

# Generate consumption data for all rows
print("Generating potato consumption data...")
potato_consumption = []

for _, row in df.iterrows():
    country = row['Country']
    year = row['Year']
    
    consumption_value = generate_consumption_data(country, year, country_consumption_characteristics)
    potato_consumption.append(consumption_value)

# Add the consumption data to the dataframe
df['Potato_consumption_tonnes'] = potato_consumption

# Save the updated CSV
output_file = '/Users/eshvarov/Github/potato-analytics/data/potato_sales_template_2000_2022.csv'
df.to_csv(output_file, index=False)

print(f"Updated CSV file saved: {output_file}")
print(f"Generated consumption data for {len(df)} rows")
print("\nSample of generated data:")
print(df.head(10)[['Country', 'Year', 'Potato_import_tonnes', 'Potato_consumption_tonnes']])

# Generate some statistics
print(f"\nStatistics for 2022:")
df_2022 = df[df['Year'] == 2022]
print(f"Total global consumption in 2022: {df_2022['Potato_consumption_tonnes'].sum():,} tonnes")
print(f"Total global imports in 2022: {df_2022['Potato_import_tonnes'].sum():,} tonnes")
print(f"Import/Consumption ratio: {df_2022['Potato_import_tonnes'].sum() / df_2022['Potato_consumption_tonnes'].sum():.2%}")

print(f"\nTop 5 consuming countries in 2022:")
top_consumers = df_2022.nlargest(5, 'Potato_consumption_tonnes')[['Country', 'Potato_consumption_tonnes']]
for _, row in top_consumers.iterrows():
    print(f"  {row['Country']}: {row['Potato_consumption_tonnes']:,} tonnes")

print(f"\nTop 5 per capita consumption in 2022 (estimated):")
# Calculate rough per capita for display
df_2022_copy = df_2022.copy()
population_estimates_2022 = {
    'Belarus': 9400000, 'Ukraine': 44000000, 'Russia': 146000000, 'Poland': 38000000,
    'Lithuania': 2800000, 'Latvia': 1900000, 'Estonia': 1300000, 'Ireland': 5000000
}
for country, pop in population_estimates_2022.items():
    if country in df_2022_copy['Country'].values:
        consumption = df_2022_copy[df_2022_copy['Country'] == country]['Potato_consumption_tonnes'].iloc[0]
        per_capita = consumption * 1000 / pop  # Convert tonnes to kg
        print(f"  {country}: {per_capita:.1f} kg/person/year")
