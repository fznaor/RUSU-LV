### Opis dataseta mtcars
Motor Trend Car Road Tests

The data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models
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

### Opis vježbe
Kroz rješavanje zadataka iz vježbe usvojene su osnove korištenja regularnih izraza u Pythonu, kao i biblioteka Numpy i Matplotlib.

### Opis rješenja zadataka
##### 1. zadatak
Rad s datotekama je ostvaren na isti način kao i na prošloj vježbi. Regularni izraz za pronalaženje validne e-mail adrese provjerava sadrži li e-mail adresa znak *@* te sadrži li lijevo i desno od tog znaka dopuštene znakove (alfanumeričke znakove te znakove *.* i *_*). Iz svake validne e-mail adrese je izdvojen početni dio pomoću naredbe `split` te je spremljen u listu koja je naposlijetku ispisana.
##### 2. zadatak
Parsiranje početnih dijelova validnih e-mail adresa odrađeno je na isti način kao u prvom zadatku. Zatim je nad listom koja sadrži sve početne dijelove mailova upotrebljen svaki od 5 zadanih regularnih izraza koristeći naredbu `filter` koja predani prekompajlirani regularni izraz traži zasebno u svakom elementu liste te u rezultat sprema samo one elemente koji zadovoljavaju regularni izraz. Rezultat naredbe `filter` potrebno je eksplicitno pretvoriti u listu.
##### 3. zadatak
Za kreiranje polja nasumičnih brojeva 0 i 1 korištena je funkcija `np.random.randint`, dok je za polje visina prvo kreirano polje nula koje je zatim popunjeno s visinama iz dvaju normalnih razdioba. Kako bi se odredilo koju razdiobu treba koristiti za koji element polja *visine*, korišteno je pridruživanje oblika `visine[spol == 0]`, koje odmah pridružuje vrijednosti svim elementima polja *visine* koji se nalaze na indeksima koji u polju spol sadrže vrijednost 0. Za vizualizaciju visina korištena je metoda `plt.scatter`. Računanje prosječne visine ostvareno je pomoću naredbe `np.dot`. Naime, skalarni produkt polja *visine* i *spol* kao rezultat daje zbroj visina svih muškaraca, dok skalarni produkt polja *visine* i *spol - 1* daje negativni zbroj visina svih žena (jer njihov indeks tad postane -1). Za prikaz prosječnih visina korištena je naredba `plt.axhline`
##### 4. zadatak
Polje *throws* inicijalizirano je kao polje od 100 nasumičnih vrijednosti između 1 i 6 uključivo. Za to polje je nacrtan histogram. Vrijednost `bins = 20` postavljena je radi bolje preglednosti dobivenog grafa.
##### 5. zadatak
Za jednostavno učitavanje i rad s podatcima iz datoteke korištena je biblioteka *Pandas* i njezina metoda `read_csv`. Ovisnost potrošnje o konjskim snagama prikazana je naredbom `plt.scatter`, dok je boja točaka na grafu proporcionalna njihovoj masi. Uz graf je dodana i legenda (*colorbar*) koji prikazuje koja boja odgovara kojoj masi. Minimalna, maksimalna i prosječna vrijednost potrošnje izračunate su metodama `min`, `max` i `mean`.
##### 6. zadatak
Slika je učitana pomoću metode `matplotlib.image.imread`. Kako su RGB vrijednosti učitane slike zapisane u intervalu [0,1], a niti jedna vrijednost nije prelazila 0.75, sve vrijednosti u matrici povećane su za 0.25, što je posvijetlilo sliku.
##### Dodatni zadatak
Rješenje dodatnog zadatka nalik je rješenju 4. zadatka, jedino je postupak "bacanja" kocaka stavljen u petlju od 1000, odnosno 10000 ponavljanja. Iz rezultata je vidljivo da povećanjem broja izvođenja pokusa (bacanja 30 kocaka) razdioba srednjih vrijednosti sve više teži ka Gaussovoj razdiobi sa srednjom vrijednošću 3.5 i standardnom devijacijom ~0.31.