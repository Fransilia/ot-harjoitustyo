# Vaatimusmäärittely #
## Sovelluksen tarkoitus ##
Sovellus on peli jonka avulla voi harjoitella muistamista. Sovelluksessa näytetään korttipakan kortteja satunnaisessa järjestyksessä ja pelaajan tehtävä on lopuksi valita oikea järjestys missä kortit juuri näytettiin. 
## Käyttäjät ##
* Sovelluksessa on vain normaalit käyttäjät ja käyttäjät jotka eivät ole rekisteröitynyt.
* Sovelluksessa on mahdollista nähdä omaa tilastoa (esim. montako korttia on muistanut oikein) mikäli käyttää sovellusta rekisteröitynä käyttäjänä. 
* Sovellukseen saatetaan lisätä pääkäyttäjä jolla on enemmän oikeuksia kuin normaalilla käyttäjällä

## Perusversion toiminnallisuus ##
### Kirjautuminen ###
* Käyttäjä voi luoda sovellukseen käyttäjätunnuksen 
    * Mahdollisuus käyttää ilman 
    * Käyttäjätunnus tulee olla uniikki ja pituudeltaan vähintään 5 merkkiä
    * Kaikilla käyttäjillä tulee olla salasana pituudeltaan vähintään 8 merkkiä
* Käyttäjä voi kirjautua
    * Toimii kirjautumislomakkeella
    * Mikäli jokin virhe ilmenee kirjautuessa tästä ilmoitetaan ja pyydetään kokeilemaan uudestaan
* Käyttäjä voi myös olla kirjautumatta
    * Mahdollisuudesta ilmoitetaan ja kerrotaan mitsä jää paitsi jos ei kirjaudu
    * Saatetaan lisätä rajoite monta kertaa peliä voi pelata kirjautumatta *mikäli se on mahdollista tehdä*
### Pelin aloittaminen ###
* Ennen pelin alkua tulee lomake missä kysytään seuraavat asiat:
    * Näytetäänkö koko pakka vai vähemmän kortteja
        * mikäli koko pakka niin voi valita kuinka monta pakkaa *mietin tätä vielä*
        * mikäli vähemmän kortteja käyttäjä syöttää määrän (esim 10 korttia)
    * Kuinka monta sekunttia yksi kortti näytetään ruudulla ennen seuraavaan siirtymistä 
    * Ilmoitetaanko heti virheestä vai vasta pelin lopussa tulokset sivulla
* Lomakkeen lopussa on nappi aloita peli ja peli alkaa käyttäjän antamilla asetuksilla
### Pelaaminen ###
* Haluttu määrä kortteja näytetään ruudulla
    * kukin kortti näkyy niin kauan kun on pelin aloituslomakkeessa sanottu
    * ruudun alapuolella näytetään monesko kortti on menossa (esim 4/52)
* Kun kaikki kortit on näytetty avautuu seuraava näkymä jossa on kaikki korttipakan kortit näkyvissä.
    * Näkymässä näytetään myös monesko kortti on menossa ja monta on jäljellä esim (5/52)
    * Näkymässä on myös seuraava/"lukitse vastaus" nappi jossa käyttäjä lukitsee kortin ja siirtyy valitsemaan seuraavaa
    * Näkymässä on myös anna periksi nappi missä peli päättyy
* Pelaaja valitsee kortin minkä muistaa tulleen ensimmäiseksi ja painaa sitten seuraava nappia. Tämän jälkeen hän valitsee muistamansa toisen kortin ja niin edespäin. 
* Kun pelaaja on valinnut kaikki kortit peli päättyy ja päästään tuloksiin. 
### Tulokset ###
* Pelin päätteeksi päästään tulokset sivulle 
* Tässä näytetään kuinka monta korttia sai oikein
* Voi verrata omia vastauksia oikeisiin vastauksiin
* Mikäli on rekisteröitynyt käyttäjä voi verrata aikaisempia tuloksia tämän pelin tulokseen. 
* Näkyy myös millä asetuksilla juuri pelasi 

## Jatkokehitysideoita ##
* hienot animaatiot
* lisää tilastoja 
* toisenlainen peli helppo peli muoto? 
