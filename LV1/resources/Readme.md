Ovaj repozitorij sadrži python skriptu koja broji koliko puta se pojedina riječ pojavljuje u tekstualnoj datatoteci. Rezultat bi trebao biti dictionary gdje uz svaku riječ (key) stoji broj ponavljanja riječi (value). Međutim, skripta ima bugove i ne radi kako je zamišljeno.

Izmjene:<br/>
-u 3. liniji raw_input promijenjen u input<br/>
-u 5. liniji fnamex promijenjeno u fname<br/>
-u 7. liniji dodane zagrade za print<br/>
-u 18. liniji + promijenjen u +=<br/>
-u 20. liniji dodane zagrade za print

1. zadatak je riješen ispisom dvaju unesenih realnih vrijednosti (sati i cijena).

U 2. zadatku se prvo provjerava je li unešen broj. Ukoliko nije, ispisuje se poruka o grešci i izlazi iz programa. Zatim se provjerava je li broj u intervalu [0,1] te ako nije se ispisuje odgovarajuća poruka, dok se u suprotnome preko if i elif naredbi određuje ocjena.

U 3. zadatku je dodana funkcija total_kn koja prima sate i cijenu te vraća njihov produkt. U ispisu je pozvana kreirana funkcija.

U 4. zadatku se u beskonačnoj petlji od korisnika traži unos broja. Ako je unesen string 'Done' prekida se izvođenje petlje. Ako nije unesen broj, ispisuje se odgovarajuća poruka te se prelazi na sljedeću iteraciju petlje. Ako je unesen broj, uspoređuje se s dosad najvećim i najmanjim brojem te se te varijable ažuriraju ako je došlo do promjene. Varijabla suma sadrži sumu svih unesenih brojeva, a varijabla n broj unesenih brojeva.

U 5. zadatku se od korisnika traži unos imena datoteke. Ako odabrana datoteka ne postoji, ispisuje se poruka o grešci. Za svaku liniju u datoteci se gleda počinje li ona s 'X-DSPAM-Confidence: ' te ukoliko počinje se varijabli suma pribraja realni broj u toj liniji koji je dobiven naredbom split. Naredba split liniju razdvaja na dio 'X-DSPAM-Confidence:' i dio s brojem.

U 6. zadatku je proces učitavanja datoteke jednak kao u 5. zadatku. Ukoliko linija počinje s 'From: ', u listu emails dodaje dio linije iza razmaka (email adresu), a u dictionary domains sprema dio adrese iza znaka '@' zajedno s njegovim dotadašnjim brojem ponavljanja. Za oba izdvajanja koristi se naredba split. Naposlijetku se ispisuje svaka 5. email adresa i sadržaj dictionaryja.