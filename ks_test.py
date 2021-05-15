import pandas 
from scipy import stats

#данные измерений массы грузов в граммах
d = [4.51, 4.49, 4.42, 4.46, 4.16, 4.45,
     4.42, 4.47, 4.40, 4.71, 4.52, 4.38,
     4.48, 4.48, 4.53, 4.525]

df = pandas.DataFrame(data={'mass': d})
data = df['mass']

print(stats.kstest(data, 'norm', (data.mean(), data.std())))
