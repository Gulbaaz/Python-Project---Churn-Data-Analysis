import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Customer Churn.csv')
print(df.info())

# Replacing blanks with 0 as tenure is 0 and no total charges are recorded
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
df["TotalCharges"] = df["TotalCharges"].astype("float")

print(df.describe())
print(df["customerID"].duplicated().sum())

# Converting SeniorCitizen from 0 and 1 to No and Yes. To make it more understandable
def conv(value):
    if value == 1:
        return "Yes"
    else:
        return "No"
    
df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
print(df.head())

ax = sns.countplot(x = df["Churn"], data = df)
ax.bar_label(ax.containers[0])
plt.title("Churn Count")
plt.show()
gb = df.groupby("Churn").agg({'Churn':'count'})
plt.pie(gb["Churn"], labels=gb.index, autopct='%1.2f%%')
plt.title("Churn Distribution")
plt.show()
# Here we can conclude that 26.54% of customers have churned out

sns.countplot(x = df["gender"], data = df, hue=df["Churn"])
plt.title("Gender vs Churn")
plt.show()

sns.countplot(x = df["SeniorCitizen"], data = df, hue=df["Churn"])
plt.title("Senior Citizen vs Churn")
plt.show()
# Comparitivelt a greater percentage of people in senior citizen category have churned.

plt.figure(figsize=(9,4))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.show()
# Customers with low tenure are more likely to churn

plt.figure(figsize=(4,4))
ax = sns.countplot(x = "Contract", data = df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract Type")
plt.show()
# Customers with month-to-month contracts are more likely to churn

columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))
axes = axes.flatten()
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])
plt.tight_layout()
plt.show()
# The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL), and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably higher when these services are not used or are unavailable.

plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)
plt.show()
