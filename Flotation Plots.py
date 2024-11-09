import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file and strip any leading/trailing whitespace in the column names
file_path = r'J:\Mill\Metallurgy\Coop Students\Devin Sutton\Coop_Project_Data_1.csv'
df = pd.read_csv(file_path)

# Strip the whitespace from column names
df.columns = df.columns.str.strip()

# Display the first few rows to ensure it loaded correctly
print(df.head())
print(df.columns)  # Check the actual column names

# Elements to plot
elements = ['Au', 'Ag', 'S', 'C']

# Define the promoter types (one promoter per plot)
promoter_types = df['Promoter_Type'].unique()

# Define the conditions based on PAX concentrations for each promoter
conditions = {
    'Aero 8045 - 0': {'PAX': 90, 'Promoter': 0, 'Frother': 30},
    'Aero 8045 - 30': {'PAX': 60, 'Promoter': 30, 'Frother': 30},
    'Aero 8045 - 60': {'PAX': 30, 'Promoter': 60, 'Frother': 30},
    'Aero 8045 - 90': {'PAX': 0, 'Promoter': 90, 'Frother': 30}
}

# Plot for each promoter and element combination
for promoter in promoter_types:
    promoter_data = df[df['Promoter_Type'] == promoter]

    # Plot for each element (Au, Ag, S, C)
    for element in elements:
        plt.figure(figsize=(10, 6))

        # Define the recovery and grade column names dynamically based on the element
        recovery_col = f'{element} Recovery'
        grade_col = f'{element} Grade'

        # Plot the data for each condition
        for label, condition in conditions.items():
            # Filter the data based on the conditions
            condition_data = promoter_data[(promoter_data['PAX'] == condition['PAX']) &
                                           (promoter_data['Promoter'] == condition['Promoter']) &
                                           (promoter_data['Frother'] == condition['Frother'])]

            # Plot the curve for this condition if data exists
            if not condition_data.empty:
                plt.plot(condition_data[grade_col], condition_data[recovery_col], marker='o', label=label)

        # Set labels, title, and custom legend
        plt.xlabel(f'{element} Grade g/t')
        plt.ylabel(f'{element} Recovery (%)')
        plt.title(f'{promoter} - {element} Recovery vs Grade')
        plt.legend(title="Conditions")
        plt.grid(True)

        # Show the plot for the current element
        plt.show()
