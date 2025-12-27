import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

print("\n🔍 DATA PREVIEW")
print(df.head())

print("\nℹ️ DATA INFO")
print(df.info())

print("\n📊 STATISTICAL SUMMARY")
print(df.describe())

# Average marks per subject

avg_marks = df[["Maths", "Science", "English"]].mean()
print("\n📈 AVERAGE MARKS PER SUBJECT")
print(avg_marks)

# Highest scorer

df["Total"] = df["Maths"] + df["Science"] + df["English"]
topper = df.loc[df["Total"].idxmax()]
print("\n🏆 TOP PERFORMER")
print(topper)

# ---------------- VISUALIZATIONS ---------------- #

# Bar chart for student-wise performance
df.set_index("Name")[["Maths", "Science", "English"]].plot(kind="bar")
plt.title("Student Performance Comparison")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.tight_layout()
plt.show()

# Average marks bar chart

avg_marks.plot(kind="bar", color=["blue", "green", "red"])
plt.title("Average Marks per Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Correlation heatmap

plt.figure(figsize=(6,4))
sns.heatmap(df[["Maths", "Science", "English"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Subjects")
plt.tight_layout()
plt.show()

print("\n✅ EDA Completed Successfully!")
