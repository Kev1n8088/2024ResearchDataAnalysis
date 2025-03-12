import numpy as np

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    a_counts = []
    for line in lines:

        a_count = line.count('A')
        a_counts.append(a_count)
    
    return a_counts

file_path = 'Data/M864UncoveredTest.txt'  # Replace with your file path
print(analyze_file(file_path))