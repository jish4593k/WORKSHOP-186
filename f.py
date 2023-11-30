import tkinter as tk
from tkinter import filedialog
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

def swap_file_data():
    # GUI for selecting files
    root = tk.Tk()
    root.withdraw()

    file1_path = filedialog.askopenfilename(title="Select the first file")
    file2_path = filedialog.askopenfilename(title="Select the second file")

    # Read data from file1
    with open(file1_path, 'r') as file1_handle:
        data_file1 = file1_handle.read()

    # Read data from file2
    with open(file2_path, 'r') as file2_handle:
        data_file2 = file2_handle.read()

    # Write data_file2 to file1
    with open(file1_path, 'w') as file1_handle:
        file1_handle.write(data_file2)

    # Write data_file1 to file2
    with open(file2_path, 'w') as file2_handle:
        file2_handle.write(data_file1)

    print("File data swapped successfully!")

    # Perform linear regression on the length of file content
    perform_regression_analysis([len(data_file1), len(data_file2)])

def perform_regression_analysis(data_lengths):
    # Generate some dummy data for illustration
    x_values = list(range(1, len(data_lengths) + 1))

    # Perform linear regression
    regression_model = LinearRegression()
    x_values_reshaped = [[x] for x in x_values]
    regression_model.fit(x_values_reshaped, data_lengths)
    predicted_lengths = regression_model.predict(x_values_reshaped)

    # Plot the trend
    plot_regression_trend(x_values, data_lengths, predicted_lengths)

def plot_regression_trend(x_values, actual_values, predicted_values):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_values, y=actual_values, label='Actual Lengths')
    sns.lineplot(x=x_values, y=predicted_values, label='Predicted Lengths', linestyle='dashed')
    plt.title('Regression Analysis of File Data Lengths')
    plt.xlabel('File Number')
    plt.ylabel('Data Length')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    swap_file_data()
