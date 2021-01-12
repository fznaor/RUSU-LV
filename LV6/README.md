### Opis vježbe
Kroz rješavanje zadataka iz vježbe usvojena su znanja o algoritmima klasifikacije, odnosno logističke regresije i kNN.
### Opis rješenja zadataka
##### 1. zadatak
Za generiranje trening i testnog skupa bilo je potrebno pozvati funkciju `generate_data` sa željenim brojem objekata.
##### 2. zadatak
Iz vizualizacije je vidljivo da postoje 2 klase, jedna okruglog oblika i druga paraboličnog oblika koja ju okružuje.
##### 3. zadatak
Kako je korišteni model treniran na isključivo linearnim podatcima, dobivena granica odluke je pravac što u ovom slučaju nije točno rješenje.
##### 4. zadatak
Vjerojatnosni prikaz također prikazuje kako je granica odluke dobivena modelom linearna te se vjerojatnost da objekt pripada drugoj klasi linearno smanjuje udaljavanjem od granice odluke.
##### 5. zadatak
Model netočno klasificira 9 podataka iz klase paraboličnog oblika, a točno klasificira sve podatke iz druge klase.
##### 6. zadatak
Dobivena matrica zabune poklapa se s rezultatima iz 5. zadatka. Također, dobivene su vrijednosti ostalih pokazatelja kvalitete klasificiranja. Svi pokazatelji imaju poprilično dobre vrijednosti zbog malog broja pogrešno klasificiranih podataka.
##### 7. zadatak
Uvođenje polinomijalnih članova omogućuje da granica odluke postane nelinearna. U našem slučaju je stupanj `2` dovoljan jer je granica odluke parabola te se dobiva točnost od 100%. Povećavanjem stupnja model počinje overfittati trening podatke te mu se smanjuje točnost na testnom skupu.
##### 8. zadatak 
k-NN daje vrlo dobre rezultate na korištenom skupu podataka jer je također sposoban pronalaziti nelinearne granice između klasa. Povećavanjem parametra `k` točnost se ne mijenja znatno, ali je primjetljivo kako granica odluke poprima sve pravilniji oblik (sličniji paraboli). Povećavanjem `k` iznad 20, točnost počinje opadati. Mana algoritma je dugo vrijeme izvođenja.