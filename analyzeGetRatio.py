import numpy as np
import scipy.stats as stats


def fieller_confidence_interval(sample1, sample2, confidence=0.95):
    """Computes the confidence interval for the ratio of means using Fieller’s Theorem."""
    n1, n2 = len(sample1), len(sample2)
    mean1, mean2 = np.mean(sample1), np.mean(sample2)
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)

    if mean2 == 0:
        raise ValueError("Mean of the second sample is zero, ratio is undefined.")

    t_crit = stats.t.ppf(1 - (1 - confidence) / 2, df=n1 + n2 - 2)

    s1_sq = var1 / n1
    s2_sq = var2 / n2
    covariance = 0  # Assuming independence of samples
    numerator = (mean1 / mean2) ** 2 * s2_sq + s1_sq - 2 * (mean1 / mean2) * covariance
    denominator = mean2 ** 2 - t_crit ** 2 * s2_sq

    if denominator <= 0:
        return float('-inf'), float('inf')  # Fieller’s method suggests unbounded interval

    root_term = np.sqrt(t_crit**2 * numerator / denominator)
    lower = mean1 / mean2 - root_term
    upper = mean1 / mean2 + root_term

    return lower, upper

def bootstrap_confidence_interval(sample1, sample2, confidence=0.95, n_bootstrap=10000):
    """Computes the bootstrap confidence interval for the ratio of means."""
    means_ratios = []
    n1, n2 = len(sample1), len(sample2)

    for _ in range(n_bootstrap):
        sample1_boot = np.random.choice(sample1, n1, replace=True)
        sample2_boot = np.random.choice(sample2, n2, replace=True)

        mean1_boot, mean2_boot = np.mean(sample1_boot), np.mean(sample2_boot)
        if mean2_boot != 0:
            means_ratios.append(mean1_boot / mean2_boot)

    lower = np.percentile(means_ratios, (1 - confidence) / 2 * 100)
    upper = np.percentile(means_ratios, (1 + confidence) / 2 * 100)
    
    return lower, upper


def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    a_counts = []
    for line in lines:

        a_count = line.count('A')
        a_counts.append(a_count)
    
    return a_counts

file_path1 = 'Data/M864Noisy.txt'  # Replace with your file path
file_path2 = 'Data/M795PDNoisy.txt'  # Replace with your file path

sample1 = analyze_file(file_path1)
sample2 = analyze_file(file_path2)


fieller_ci = fieller_confidence_interval(sample1, sample2)
bootstrap_ci = bootstrap_confidence_interval(sample1, sample2)

print(f"Fieller's Theorem CI: {fieller_ci}")
print(f"Bootstrap CI: {bootstrap_ci}")


#print(analyze_file(file_path1))