import matplotlib.pyplot as plt
import numpy as np

# The height of bar is the mean value;
# The black plot is the standard deviation.

x = np.array([1, 2, 3, 4, 5])
normal = np.array([0.38, 0.25, 0.32, 0.27, 0.25, 0.81, 0.24, 0.27, 0.41, 0.25, 0.26, 0.92, 0.91, 0.26,
                   0.25, 0.96, 0.57, 0.71, 0.25, 0.24, 0.72, 0.45, 0.7, 0.37, 0.31, 1.02, 0.56, 0.38,
                   0.85, 0.24, 0.26, 0.25, 0.66, 0.26, 0.45, 0.35, 0.41, 0.32, 0.27, 0.51, 0.26, 0.26,
                   0.37, 0.25, 0.31, 0.27, 0.24, 0.25, 0.5, 0.25, 0.26, 0.28, 0.26, 0.25, 0.27, 0.27,
                   0.27, 0.27, 0.26, 0.27, 0.24, 0.54, 0.25, 0.74, 0.24, 0.31, 0.33, 0.26, 0.26, 0.25,
                   0.24, 0.27, 0.26, 0.25, 0.26, 0.26, 0.26, 0.25, 0.54, 0.56, 0.56, 0.73, 0.24, 0.25,
                   0.31, 0.25, 0.6, 0.49, 0.27, 0.26, 0.25, 0.25, 0.25, 0.26, 0.26, 0.26, 0.27, 0.25,
                   0.26, 0.26, 0.25, 0.25, 0.54, 0.25, 0.24, 0.25, 0.24, 0.26, 0.27, 0.25, 0.3, 0.25,
                   0.25, 0.25, 0.25, 0.26, 0.26, 0.25, 0.26, 0.27, 0.25, 0.26, 0.25, 0.88, 0.24, 0.28,
                   0.24, 0.24, 0.3, 0.26, 0.25, 0.26]
)
mutant_sep1_V = np.array([0.38, 0.71, 0.97, 0.98, 1.02, 1.0, 0.8, 0.47, 0.44, 0.5, 0.91, 0.83, 1.01, 0.86, 0.84])
mutant_sep2_C = np.array([0.97, 0.98, 0.94, 0.97, 0.79, 0.97, 0.98, 0.97, 0.97, 1.01, 0.99, 0.99, 0.98, 0.98, 0.9, 1.0, 0.95, 0.99, 0.98, 1.03, 0.95, 0.95, 0.99, 0.99, 0.99, 1.05, 0.9, 1.01, 0.98, 0.97, 0.98, 0.98, 0.99])
mutant_sep2_V = np.array([0.79, 0.99, 1.02, 1.0, 0.98, 0.93, 1.01, 0.96, 1.01, 1.0, 0.96, 1.0, 0.98, 0.97, 0.97, 0.98, 1.02, 0.98, 1.05, 1.0, 0.98, 0.97, 0.98, 0.97, 1.01, 0.98, 0.97, 0.99, 1.0, 0.93])
mutant_sep3_V = np.array([0.76, 1.21, 0.58, 0.86, 0.96, 0.87, 0.99, 0.57, 0.87, 0.36, 0.81, 0.82, 0.32, 0.77, 0.84, 0.87, 0.97, 0.81, 0.53, 0.75, 0.37, 0.63, 0.59, 1.19, 0.88, 1.19])
mutant_sep4_V = np.array([0.34, 0.93, 0.97, 0.53, 0.84, 0.96, 0.86, 0.95, 0.88, 0.89, 0.79, 0.34, 0.87, 0.83])

# Get the average
normal_mean = np.mean(normal)
sep1_V_mean = np.mean(mutant_sep1_V)
sep2_C_mean = np.mean(mutant_sep2_C)
sep2_V_mean = np.mean(mutant_sep2_V)
sep3_V_mean = np.mean(mutant_sep3_V)
sep4_V_mean = np.mean(mutant_sep4_V)

# Get the standard deviation
normal_std = np.std(normal)
sep1_V_std = np.std(mutant_sep1_V)
sep2_C_std = np.std(mutant_sep2_C)
sep2_V_std = np.std(mutant_sep2_V)
sep3_V_std = np.std(mutant_sep3_V)
sep4_V_std = np.std(mutant_sep4_V)

materials = ['normal', 'sep1-V', 'sep2-C', 'sep2-V', 'sep3-V', 'sep4-V']
x_pos = np.arange(len(materials))
ave = [normal_mean, sep1_V_mean, sep2_C_mean, sep2_V_mean, sep3_V_mean, sep4_V_mean]
error = [normal_std, sep1_V_std, sep2_C_std, sep2_V_std, sep3_V_std, sep4_V_std]
print(ave)

# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, ave, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()