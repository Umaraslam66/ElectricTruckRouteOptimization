import pandas as pd

# Load the clean data
data = pd.read_csv('dummy_emission_data.csv')
# Display summary statistics
#summary_stats = data.describe()
#print(summary_stats)

import matplotlib.pyplot as plt

# Histogram of emissions
plt.hist(data['Emissions (kg CO2)'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Emissions (kg CO2)')
plt.ylabel('Frequency')
plt.title('Distribution of Emissions')
plt.show()

# Box plot of emissions by vehicle type
import seaborn as sns

sns.boxplot(x='VehicleType', y='Emissions (kg CO2)', data=data)
plt.xlabel('Vehicle Type')
plt.ylabel('Emissions (kg CO2)')
plt.title('Emissions by Vehicle Type')
plt.show()

# Bar chart of route counts
route_counts = data['Route'].value_counts()
route_counts.plot(kind='bar', color='green', alpha=0.7)
plt.xlabel('Route')
plt.ylabel('Count')
plt.title('Route Distribution')
plt.show()


# Calculate correlation matrix
correlation_matrix = data.corr()

# Visualize the correlation matrix as a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
