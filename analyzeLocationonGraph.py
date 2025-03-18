import matplotlib.pyplot as plt

def read_locations(file_path):
    locations = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            locations.append((x, y))
    return locations

def calculate_average(locations):
    avg_x = sum(x for x, y in locations) / len(locations)
    avg_y = sum(y for x, y in locations) / len(locations)
    return avg_x, avg_y

def adjust_locations(locations, avg_x, avg_y):
    adjusted_locations = [(x - avg_x, y - avg_y) for x, y in locations]
    return adjusted_locations

def plot_locations(locations):
    x_vals = [x for x, y in locations]
    y_vals = [y for x, y in locations]

    plt.scatter(x_vals, y_vals, label='Locations')
    plt.scatter(0, 0, color='red', label='Average Location')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Locations on X/Y Plot with Average as Origin')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

def main():
    file_path = 'Data/legacy/Locations.txt'  # Replace with your file path
    locations = read_locations(file_path)
    avg_x, avg_y = calculate_average(locations)
    adjusted_locations = adjust_locations(locations, avg_x, avg_y)
    plot_locations(adjusted_locations)

main()