import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
np.random.seed(42)
n_control = 1000
clicks_control = np.random.binomial(n=n_control, p=0.10)
ctr_control = clicks_control / n_control
n_variant = 1000
clicks_variant = np.random.binomial(n=n_variant, p=0.12)
ctr_variant = clicks_variant / n_variant  
ctr_control = np.nan_to_num(ctr_control)
ctr_variant = np.nan_to_num(ctr_variant)
t_stat, p_value = stats.ttest_ind_from_stats(mean1=np.mean(ctr_control), std1=np.std(ctr_control), nobs1=n_control,
                                             mean2=np.mean(ctr_variant), std2=np.std(ctr_variant), nobs2=n_variant)
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
alpha = 0.05
if p_value < alpha:
    print("Statistically significant difference detected between control and variant groups.")
else:
    print("No statistically significant difference detected between control and variant groups.")
plt.figure(figsize=(10, 6))
plt.hist(ctr_control, bins=30, alpha=0.5, label='Control Group')
plt.hist(ctr_variant, bins=30, alpha=0.5, label='Variant Group')
plt.xlabel('Click-through Rate')
plt.ylabel('Frequency')
plt.title('Distribution of Click-through Rates')
plt.legend()
plt.show()
