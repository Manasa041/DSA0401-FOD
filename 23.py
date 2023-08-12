import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Simulated data for the control group (placebo) and treatment group (new drug)
np.random.seed(42)  # For reproducibility
control_group = np.random.normal(loc=50, scale=10, size=100)
treatment_group = np.random.normal(loc=55, scale=10, size=100)

# Perform two-sample t-test for independent samples
t_statistic, p_value = stats.ttest_ind(treatment_group, control_group)

# Visualization
plt.figure(figsize=(8, 6))
plt.hist(control_group, bins=20, alpha=0.5, label='Control Group (Placebo)')
plt.hist(treatment_group, bins=20, alpha=0.5, label='Treatment Group (New Drug)')
plt.axvline(x=np.mean(control_group), color='blue', linestyle='dashed', linewidth=2, label='Control Mean')
plt.axvline(x=np.mean(treatment_group), color='orange', linestyle='dashed', linewidth=2, label='Treatment Mean')
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Distribution of Outcomes in Control and Treatment Groups')
plt.legend()
plt.show()

# Print the results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

if p_value < 0.05:
    print("The new treatment has a statistically significant effect.")
else:
    print("There is no statistically significant effect of the new treatment.")
