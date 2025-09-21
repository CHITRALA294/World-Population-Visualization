import pandas as pd
import matplotlib.pyplot as plt

# READ CSV (Desktop\SCT_DS_1\population_sample.csv)
df = pd.read_csv(r"C:\Users\Acer\Desktop\SCT_DS_1\population_sample.csv")
df.columns = df.columns.str.strip()  # remove any extra spaces in column names

# -------- BAR GRAPH --------
plt.figure(figsize=(10,6))
plt.bar(df["Country"], df["Population"], edgecolor="black")
plt.title("Population by Country")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(r"C:\Users\Acer\Desktop\SCT_DS_1\bargraph.png")
plt.show()

# -------- HISTOGRAM --------
plt.figure(figsize=(8,5))
plt.hist(df["Population"], bins=10, edgecolor="black")
plt.title("Population Distribution")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(r"C:\Users\Acer\Desktop\SCT_DS_1\histogram.png")
plt.show()
