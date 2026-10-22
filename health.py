import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(
    [
        (
            f"C_{i}",
            y,
            70 + y * 0.2 + np.random.normal(),
            1000 + y * 150 + np.random.normal(),
        )
        for i in range(10)
        for y in range(20)
    ],
    columns=["Country", "Year", "Life_Exp", "Spending"],
)
df.loc[df.sample(frac=0.05).index, "Life_Exp"] = np.nan

# FIXED: Uses a direct lambda function to avoid the string mean error
df["Life_Exp"] = df.groupby("Country")["Life_Exp"].transform(
    lambda x: x.fillna(x.mean())
)

print(df["Spending"].corr(df["Life_Exp"]))
yl = df.groupby("Year").mean(numeric_only=True).reset_index()
t = np.poly1d(np.polyfit(yl["Year"], yl["Life_Exp"], 2))(yl["Year"])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4), facecolor="white")
for a in (ax1, ax2):
    a.set_facecolor("white")

ax1.scatter(df["Spending"], df["Life_Exp"], alpha=0.5, c="blue")
ax2.plot(yl["Year"], yl["Life_Exp"], "o", yl["Year"], t, "-")
ax2.axhline(df["Life_Exp"].mean(), color="r", linestyle=":")

plt.tight_layout()
plt.savefig("global_health_snapshot.png", facecolor="white")
plt.show()


