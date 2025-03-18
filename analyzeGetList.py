import numpy as np

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    a_counts = []
    for line in lines:

        a_count = line.count('A')
        a_counts.append(a_count)
    
    return a_counts

file_path = 'Data/M795PDProneNoisy.txt'  # Replace with your file path

a = analyze_file(file_path)

print(a)

b = []

for data in a:
    b.append(str(data))

c = " ".join(b)
print(c)