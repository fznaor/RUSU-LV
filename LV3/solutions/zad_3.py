import urllib
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# url that contains valid xml file:
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=4&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017.'

airQualityHR = urllib.request.urlopen(url).read()
root = ET.fromstring(airQualityHR)

df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

i = 0
while True:
    
    try:
        obj = root.getchildren()[i].getchildren()
    except:
        break
    
    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
    df.mjerenje[i] = float(df.mjerenje[i])
    i = i + 1

df.vrijeme = pd.to_datetime(df.vrijeme, utc = True)
df.plot(y='mjerenje', x='vrijeme');

# add date month and day designator
df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek

#3 dana s najvećom koncentracijom čestica
print(df.sort_values(['mjerenje'], ascending = False).head(3).vrijeme.dt.date)

plt.figure(2)
missing = [31,28,31,30,31,30,31,31,30,31,30,31] - df.groupby('month').mjerenje.count()
missing.plot.bar()
plt.xlabel('Mjesec')
plt.ylabel('Izostala mjerenja')

mjeseci = df[(df.month == 1) | (df.month == 8)]
mjeseci.boxplot(column = ['mjerenje'], by = 'month')
plt.xticks([1, 2], ['Siječanj', 'Kolovoz'])
plt.xlabel('Mjesec')
plt.ylabel('Koncentracija čestica')
plt.title("")
plt.suptitle("")

plt.figure(4)
df['vikend'] = (df.dayOfweek >= 5) & (df.dayOfweek <= 6)
df.boxplot(column = ['mjerenje'], by = 'vikend')
plt.xticks([1, 2], ['Radni dan', 'Vikend'])
plt.xlabel('Dan')
plt.ylabel('Koncentracija čestica')
plt.title("")
plt.suptitle("")