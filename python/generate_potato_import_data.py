#!/usr/bin/env python3
"""
Generate realistic potato import data for countries in the CSV file
Based on typical agricultural trade patterns and country characteristics
"""

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Read the existing CSV file
df = pd.read_csv('/Users/eshvarov/Github/potato-analytics/data/potato_sales_template_2000_2022.csv')

# Country characteristics for generating realistic import data
# Based on typical potato import patterns and economic factors
country_import_characteristics = {
    # Major potato importers (high import volumes)
    'United States': {'base': 800000, 'growth': 0.02, 'volatility': 0.15},
    'Germany': {'base': 650000, 'growth': 0.015, 'volatility': 0.12},
    'United Kingdom': {'base': 500000, 'growth': 0.01, 'volatility': 0.18},
    'Netherlands': {'base': 450000, 'growth': 0.025, 'volatility': 0.20},
    'Belgium': {'base': 380000, 'growth': 0.02, 'volatility': 0.16},
    'France': {'base': 350000, 'growth': 0.01, 'volatility': 0.14},
    'Japan': {'base': 320000, 'growth': 0.005, 'volatility': 0.13},
    'Italy': {'base': 280000, 'growth': 0.015, 'volatility': 0.17},
    'Canada': {'base': 250000, 'growth': 0.02, 'volatility': 0.15},
    'Spain': {'base': 220000, 'growth': 0.018, 'volatility': 0.16},
    
    # Medium importers
    'Brazil': {'base': 180000, 'growth': 0.03, 'volatility': 0.25},
    'Russia': {'base': 160000, 'growth': 0.01, 'volatility': 0.30},
    'South Korea': {'base': 140000, 'growth': 0.025, 'volatility': 0.18},
    'Australia': {'base': 120000, 'growth': 0.015, 'volatility': 0.20},
    'China': {'base': 100000, 'growth': 0.05, 'volatility': 0.25},  # Growing rapidly
    'India': {'base': 80000, 'growth': 0.04, 'volatility': 0.30},
    'Mexico': {'base': 75000, 'growth': 0.03, 'volatility': 0.22},
    'Poland': {'base': 70000, 'growth': 0.02, 'volatility': 0.18},
    'Turkey': {'base': 65000, 'growth': 0.025, 'volatility': 0.25},
    'Argentina': {'base': 60000, 'growth': 0.02, 'volatility': 0.28},
    
    # Smaller importers
    'South Africa': {'base': 45000, 'growth': 0.025, 'volatility': 0.30},
    'Chile': {'base': 40000, 'growth': 0.02, 'volatility': 0.25},
    'Norway': {'base': 35000, 'growth': 0.01, 'volatility': 0.15},
    'Sweden': {'base': 32000, 'growth': 0.012, 'volatility': 0.14},
    'Denmark': {'base': 30000, 'growth': 0.015, 'volatility': 0.16},
    'Finland': {'base': 28000, 'growth': 0.01, 'volatility': 0.15},
    'Switzerland': {'base': 25000, 'growth': 0.008, 'volatility': 0.12},
    'Austria': {'base': 22000, 'growth': 0.012, 'volatility': 0.14},
    'Portugal': {'base': 20000, 'growth': 0.015, 'volatility': 0.18},
    'Greece': {'base': 18000, 'growth': 0.01, 'volatility': 0.20},
    
    # Very small importers or self-sufficient countries
    'Ireland': {'base': 15000, 'growth': 0.01, 'volatility': 0.16},
    'New Zealand': {'base': 12000, 'growth': 0.015, 'volatility': 0.18},
    'Israel': {'base': 10000, 'growth': 0.02, 'volatility': 0.22},
    'Singapore': {'base': 8000, 'growth': 0.025, 'volatility': 0.20},
    'Hong Kong': {'base': 7000, 'growth': 0.02, 'volatility': 0.18},
    'UAE': {'base': 6000, 'growth': 0.03, 'volatility': 0.25},
    'Saudi Arabia': {'base': 5500, 'growth': 0.025, 'volatility': 0.30},
    'Kuwait': {'base': 3000, 'growth': 0.02, 'volatility': 0.25},
    'Qatar': {'base': 2000, 'growth': 0.03, 'volatility': 0.22},
    'Bahrain': {'base': 1500, 'growth': 0.02, 'volatility': 0.20},
}

def generate_import_data(country, year, characteristics):
    """Generate realistic potato import data for a country and year"""
    if country not in characteristics:
        # Default for countries not in the list
        base = random.randint(1000, 50000)
        growth = random.uniform(0.005, 0.03)
        volatility = random.uniform(0.15, 0.35)
    else:
        base = characteristics[country]['base']
        growth = characteristics[country]['growth']
        volatility = characteristics[country]['volatility']
    
    # Calculate years since 2000
    years_passed = year - 2000
    
    # Base trend with growth
    trend_value = base * (1 + growth) ** years_passed
    
    # Add some random variation
    random_factor = 1 + np.random.normal(0, volatility)
    
    # Apply economic shocks for certain years
    if year in [2008, 2009]:  # Financial crisis
        random_factor *= 0.85
    elif year in [2020, 2021]:  # COVID-19 impact
        random_factor *= 0.92
    elif year in [2014, 2015]:  # Various economic issues
        random_factor *= 0.95
    
    final_value = trend_value * random_factor
    
    # Ensure positive values and round to nearest tonne
    return max(0, round(final_value))

# Generate import data for all rows
print("Generating potato import data...")
potato_imports = []

for _, row in df.iterrows():
    country = row['Country']
    year = row['Year']
    
    import_value = generate_import_data(country, year, country_import_characteristics)
    potato_imports.append(import_value)

# Add the import data to the dataframe
df['Potato_Sales_Tonnes'] = potato_imports

# Save the updated CSV
output_file = '/Users/eshvarov/Github/potato-analytics/data/potato_sales_template_2000_2022.csv'
df.to_csv(output_file, index=False)

print(f"Updated CSV file saved: {output_file}")
print(f"Generated import data for {len(df)} rows")
print("\nSample of generated data:")
print(df.head(10)[['Country', 'Year', 'Potato_Sales_Tonnes']])

# Generate some statistics
print(f"\nStatistics:")
print(f"Total imports in 2022: {df[df['Year'] == 2022]['Potato_Sales_Tonnes'].sum():,} tonnes")
print(f"Average annual imports per country: {df['Potato_Sales_Tonnes'].mean():,.0f} tonnes")
print(f"Top 5 importing countries in 2022:")
top_2022 = df[df['Year'] == 2022].nlargest(5, 'Potato_Sales_Tonnes')[['Country', 'Potato_Sales_Tonnes']]
for _, row in top_2022.iterrows():
    print(f"  {row['Country']}: {row['Potato_Sales_Tonnes']:,} tonnes")
