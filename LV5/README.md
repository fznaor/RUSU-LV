### Opis vježbe
Kroz rješavanje zadataka iz vježbe usvojene su osnovni algoritmi grupiranja podataka kao i njihova evaluacija.
### Opis rješenja zadataka
##### 1. zadatak
Ponovnim pokretanjem kmeans algoritma na istim podacima u nekim slučajevima se dobivaju različiti rezultati jer je kmeans algoritam osjetljiv na početni odabir centroida. Iz izvođenja algoritma na različitim tipovima generiranih podataka moguće je vidjeti kako kmeans ne radi ispravno za clustere nepravilnih (nekonveksnih) oblika, dok podatke grupirane u clustere konveksnih oblika uvijek grupira bez problema.
#####2. zadatak
Primjetljivo je kako za svaki skup podataka vrijednost kriterijske funkcije opada s povećavanjem broja clustera, što je za očekivati jer se smanjuju udaljenosti između podataka i njihovih pripadajućih centroida. Najčešće korištena metoda za određivanje optimalnog broja clustera iz ovakvog tipa grafa je tzv. "metoda lakta" u kojoj se kao optimalan broj clustera uzima ona vrijednost na kojoj dolazi do najveće promjene nagiba grafa kriterijske funkcije u ovisnosti o broju clustera. Primjetljivo je kako metoda lakta daje ispravne rezultate za skupove s konveksnim clusterima, ali ne i za one s nepravilnim clusterima.
#####3. zadatak
Korištenje aglomerativnog grupiranja predstavlja još jedan dobar način za procjenu optimalnog broja clustera. Iz dendrograma se lako može procijeniti koji broj clustera uzeti. Iako različite metode generiranja dendrograma daju različite rezultate, većina ih indicira na istu vrijednost optimalnog broja clustera, no kao najbolja se može istaći metoda `ward`, a kao najgora metoda `single`.
#####4. zadatak
Smanjivanjem broja clustera pogoršava se kvaliteta slike zbog manjeg broja sivih vrijednosti. Međutim, već za vrijednost `k=10` se dobiva slika koja je u velikoj mjeri slična originalnoj (jedino je uočljivo kako je komprimirana slika tamnija od originalne). Korištenjem 10 klustera može se prepoloviti veličina slike jer je dovoljno koristiti 4 bita za opis vrijednosti piksela umjesto dosadašnjih 8.
#####5. zadatak
Rezultati su uvelike slični kao i u prošlom zadatku. `k=10` daje sliku gotovo identičnu originalu (uz male razlike vidljive na nebu i travi), dok daljnje smanjivanje parametra `k` na manje vrijednosti rezultira postupnim pogoršanjem kvalitete komprimirane slike.
#####6. zadatak
Vlastita implementacija algoritma kmeans postiže jednake rezultate kao i ona korištena u ranijim zadatcima. Kao nedostatci vlastite implementacije mogu se istaći brojne `for` petlje i nasumična inicijalizacija centroida (`kmeans++` metoda bi bila puno bolja). Vizualizirani su rezultati grupiranja svih datasetova te su ujedno prikazana kretanja centroida kroz iteracije algoritma. 