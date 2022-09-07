import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/siddhantagarwal/Downloads/chart.csv")
print(df.shape)

print(df.head())

x = df['DateTime']
y = df["XBOX"]

plt.plot(x,y)
plt.show()

