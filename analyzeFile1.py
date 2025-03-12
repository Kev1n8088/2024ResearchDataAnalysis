import numpy as np
import matplotlib.pyplot as plt

def analyze_positions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    x_coords = []
    y_coords = []
    
    for line in lines:
        if line.strip():  # Ignore empty lines
            x, y = map(float, line.split(','))
            x_coords.append(x)
            y_coords.append(y)
    
    center_x = np.mean(x_coords)
    center_y = np.mean(y_coords)
    
    x_deviations = np.abs(np.array(x_coords) - center_x)
    y_deviations = np.abs(np.array(y_coords) - center_y)
    
    x_95_percentile = np.percentile(x_deviations, 95)
    y_95_percentile = np.percentile(y_deviations, 95)
    
    return center_x, center_y, x_95_percentile, y_95_percentile, x_deviations, y_deviations

file_path = 'C:/Users/jebid/Desktop/Locations.txt'  # Replace with your file path
center_x, center_y, x_95_percentile, y_95_percentile, x_deviations, y_deviations = analyze_positions(file_path)

print(f"Center X: {center_x}, Center Y: {center_y}")
print(f"95th Percentile X Deviation: {x_95_percentile}, 95th Percentile Y Deviation: {y_95_percentile}")

# Plotting the deviations
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(x_deviations, bins=30, color='blue', alpha=0.7)
plt.axvline(x_95_percentile, color='red', linestyle='dashed', linewidth=1)
plt.title('X Deviations')
plt.xlabel('Deviation')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(y_deviations, bins=30, color='green', alpha=0.7)
plt.axvline(y_95_percentile, color='red', linestyle='dashed', linewidth=1)
plt.title('Y Deviations')
plt.xlabel('Deviation')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()