import numpy as np

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    a_counts = []
    for line in lines:
        a_count = line.count('A') 
        a_counts.append(a_count)
    
    mean = np.mean(a_counts)
    std_dev = np.std(a_counts)
    sample_size = len(a_counts)
    
    return mean, std_dev, sample_size

file_path = 'Data/M795PDUncoveredTest.txt'  # Replace with your file path
mean, std_dev, sample_size = analyze_file(file_path)
print(file_path)
print(f"Mean: {mean}, Standard Deviation: {std_dev}, Sample Size: {sample_size}")