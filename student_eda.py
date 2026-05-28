import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student-por.csv", sep=';')

# -----------------------------
# Basic Information
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Histogram
# -----------------------------
df[['age','absences','G1','G2','G3']].hist(figsize=(10,8))
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))

corr_columns = ['age','Medu','Fedu','traveltime',
                'studytime','failures','absences',
                'G1','G2','G3']

sns.heatmap(
    df[corr_columns].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.savefig('correlation_heatmap.png')
plt.show()

# -----------------------------
# Boxplot (Outlier Analysis)
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(data=df[['G1','G2','G3']])
plt.title("Grade Distribution")
plt.savefig('boxplot.png')
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x='studytime',
    y='G3'
)
plt.title("Study Time vs Final Grade")
plt.savefig('studytime_vs_grade.png')
plt.show()