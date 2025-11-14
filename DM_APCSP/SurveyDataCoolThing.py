import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"DM_APCSP\NewJollySurvey.csv")
df = pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.info())
'''print(round(df.describe(),1))
print(df['PIE'].value_counts())
print(df.groupby('PIE')['NAP'].mean())'''

df['JOLLY'].value_counts().plot(kind='pie')

plt.title("Jolly-ness of People")
plt.xlabel("Jolly-ness")
plt.ylabel("Number of Responses")
#plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



plt.scatter(df['JOLLY'], df['BELIEF'])

plt.title("Jolly-ness in relation to Belief")
plt.xlabel("Jolly-ness")
plt.ylabel("Belief")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()