### mtcars.csv

Motor Trend Car Road Tests

The data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models)
* mpg - Miles/(US) gallon
* cyl - Number of cylinders
* disp - Displacement (cu.in.)
* hp - Gross horsepower
* drat - Rear axle ratio
* wt - Weight (lb/1000)
* qsec - 1/4 mile time
* vs - V/S
* am - Transmission (0 = automatic, 1 = manual)
* gear - Number of forward gears
* carb - Number of carburetors

Source: R built in dataset



### AirQualityRH.py

Skripta za dohvaćanje podataka o kvaliteti zraka pomocu REST API

### Opis vježbe
Kroz rješavanje zadataka iz vježbe usvojene su osnove korištenja biblioteke Pandas te osnovni postupci eksplorativne analize podataka.
### Opis rješenja zadataka
##### 1. zadatak
Za dobivanje potrebnih informacija iz dataseta mtcars korištena je biblioteka *Pandas*. Za sortiranje vrijednosti korištena je metoda `sort_values`, a za prebrojavanje određenih vrijednosti metoda `len`. Dohvaćanje određenog broja vrijednosti ostvareno je pomoću naredbe `head`, a za kombiniranje više uvjeta korišteni su logički operatori and i or. Preračunavanje mase u kilograme ostvareno je dodavanjem novog stupca u DataFrame koristeći već postojeći stupac s masom u lbs. Za računanje prosječne vrijednosti korištena je metoda `mean`.
##### 2. zadatak
Prikaz ovisnosti potrošnje o broju cilindara automobila prikazan je pomoću bar plota koristeći naredbe `groupby` (kako bi grupirali aute ovisno o broju cilindara) i `plot.bar`. Distribucije mase u ovisnosti o cilindrima i potrošnje u ovisnosti o vrsti mjenjača prikazani su naredbom `boxplot`. Rezultat naredbe je dijagram koji prikazuje distribuciju dobivenih vrijednosti, kao i neke specifične veličine (medijan, kvartili i sl.). Odnos ubrzanja auta s ručnim i automatskim mjenjačem prikazan je pomoću scatter plota, a vrsta mjenjača prikazana je bojom točke na grafu.
##### 3. zadatak
Učitavanje podataka ostvareno je sa zadane web-stranice. Ispis 3 dana s najvećom koncentracijom čestica ostvareno je sortiranjem DataFramea po koncentraciji čestica i ispisom 3 najvećih vrijednosti. Bar plot nedostajućih mjerenja napravljen je tako što je od broja dani u mjesecu oduzet broj mjerenja ostvaren u tom mjerenju te prikazom dobivenih rezultata. Distribucije mjerenja u ovisnosti o mjesecu i radnom danu/vikendu prikazane su naredbom `boxplot`. Za dobivanje dvaju mjeseca korišteno je izdvajanje pomoću logičke operacije 'ili', a za izdvajanje radnih dana dodan je novi stupac koji provjerava je li dan radni ili ne. Iz rezultata je vidljivo da je koncentracija čestica viša po zimi te neznatno viša u radnim danima.