
# Housing Values in Suburbs of Boston

The  **medv**  variable is the target variable.

### Data description

The Boston data frame has 506 rows and 14 columns.

This data frame contains the following columns:

**_crim_**  
per capita crime rate by town.

**_zn_**  
proportion of residential land zoned for lots over 25,000 sq.ft.

_**indus**_  
proportion of non-retail business acres per town.

_**chas**_  
Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).

_**nox**_  
nitrogen oxides concentration (parts per 10 million).

_**rm**_  
average number of rooms per dwelling.

_**age**_  
proportion of owner-occupied units built prior to 1940.

_**dis**_  
weighted mean of distances to five Boston employment centres.

_**rad**_  
index of accessibility to radial highways.

_**tax**_  
full-value property-tax rate per  $10,000.

_**ptratio**_  
pupil-teacher ratio by town.

_**black**_  
1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.

_**lstat**_  
lower status of the population (percent).

_**medv**_  
median value of owner-occupied homes in  $1000s.

### Source

Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the demand for clean air. J. Environ. Economics and Management 5, 81–102.

Belsley D.A., Kuh, E. and Welsch, R.E. (1980) Regression Diagnostics. Identifying Influential Data and Sources of Collinearity. New York: Wiley.

### Opis vježbe
Kroz rješavanje zadataka iz vježbe usvojene su osnovni postupci linearne i polinomijalne regresije u Pythonu.
### Opis rješenja zadataka
##### 1. zadatak
Tok koda prati način rješavanja regresijskog problema opisan u tekstu vježbe. Učitavaju se podatci, razdvajaju na trening i testni skup te se zatim trenira i evaluira odgovarajući model.
##### 2. zadatak
U zadatku je samostalno implementirano direktno rješenje regresijskog problema koristeći jednadžbu (4-10). Dobiveni koeficijenti jednaki su onima iz prvog zadatka.
##### 3. zadatak
U zadatku je samostalno implementiran iterativni algoritam linearne regresije te testiran za različite vrijednosti stope učenja. Premale vrijednosti stope učenja zahtijevaju vrlo velik broj iteracija za postizanje minimuma kriterijske funkcije, dok previsoke vrijednosti stope učenja rezultiraju divergencijom kriterijske funkcije prema beskonačnosti. Dobiveni rezultati koeficijenata (za odgovarajuće vrijednosti stope učenja poklapaju se s vrijednostima iz prethodnih zadataka).
##### 4. zadatak
Razlika u dobivenim rezultatima je to da model bolje aproksimira zadanu funkciju zahvaljujući većem stupnju polinoma.
##### 5. zadatak
Iz rezultata je vidljivo da povećanje stupnja polinoma rezultira boljim i preciznijim praćenjem zadane funkcije. Međutim, prevelik stupanj polinoma će overfittati podatke što je vidljivo u usporedbi stupnjeva 6 i 15, za zadani dataset stupanj 6 predstavlja najbolji kompromis između točnosti na trening i testnom skupu. Smanjivanje veličine trening skupa pogoršava točnost na testnom skupu, ali isti učinak ima i povećavanje veličine trening skupa na preveliku vrijednost (overfitting).
##### 6. zadatak
U kodu iz prošlog zadatka obična linearna regresija zamijenjena je Ridge regresijom. Povećavanjem regularizacijskog parametra dobiveni model manje vjerno prati trening podatke, no ostvaruje bolje vrijednosti na testnom skupu zbog manjeg overfittinga. Međutim, previsoka vrijednost regularizacijskog parametra rezultira previše nepreciznim (previše jednostavnim) modelom i dovodi do loših rezultata
##### 7. zadatak
U zadatku su prvo učitani podatci iz Boston housing dataseta te je provedena vizualizacija svih dostupnih podataka. Zatim je provedena linearna regresija za razne vrijednosti stupnjeva polinoma i regularizacijskog parametra te je utvrđeno da je najidealniji model za te podatke kvadratni polinom s regularizacijskim parametrom 3000 (polinomi višeg stupnja bi postigli relativno podjednaku točnost pri ekstremno visokim razinama regularizacije pa je stoga izabran jednostavniji model sa sličnom točnošću). Spomenuti model je istreniran te su grafički prikazani odnosi stvarnih cijena kuća te njihovih predviđenih vrijednosti. Iz prikaza je vidljivo da model dobro aproksimira cijene uz poneka veća odstupanja. 
##### Dodatni zadatak
Lasso regularizacija daje podjednake rezultate kao i Ridge regularizacija. Mana joj je potreba za vrlo velikim brojem iteracija kako bi postigla točnost na razini one koju postiže Ridge. Kao i kod Ridge regularizacije, povećavanje regularizacijskog parametra rezultira pojednostavljivanjem modela i izbjegavanjem overfittinga. Koeficijenti dobiveni Lasso metodom su manji od onih dobivenih Ridge metodom, te su neki koeficijenti jednaki nuli, što nije bio slučaj kod Ridge regularizacije.