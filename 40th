import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:/Users/admin/Documents/house.csv")

top_goal_scorers = df.nlargest(5, "goals")
top_salary_players = df.nlargest(5, "salary")
average_age = df["age"].mean()
above_average_age_players = df[df["age"] > average_age]
position_counts = df["position"].value_counts()

plt.figure(figsize=(10, 6))
position_counts.plot(kind="bar", color="skyblue")
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.show()

print("Top 5 Goal Scorers:")
print(top_goal_scorers)

print("\nTop 5 Highest Salary Players:")
print(top_salary_players)

print(f"\nAverage Age of Players: {average_age:.2f}")

print("\nPlayers Above Average Age:")
print(above_average_age_players)
