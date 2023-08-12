import pandas as pd
import numpy as np
from scipy.stats import t
data = pd.read_csv("C:/Users/Acer/Desktop/FOD/customer_reviews.csv")
ratings = data["rating"]
confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
sample_size = len(ratings)
sample_mean = np.mean(ratings)
sample_std = np.std(ratings, ddof=1)
degrees_of_freedom = sample_size - 1
t_score = t.ppf(1 - (1 - confidence_level) / 2, df=degrees_of_freedom)
margin_of_error = t_score * (sample_std / np.sqrt(sample_size))
confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error
print("\nAnalysis of Customer Reviews:")
print("Sample Size:", sample_size)
print("Sample Mean Rating:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print(f"Confidence Interval ({confidence_level*100}%): {confidence_interval_lower} - {confidence_interval_upper}")
