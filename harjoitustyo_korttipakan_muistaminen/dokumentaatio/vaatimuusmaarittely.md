# Vaatimusmäärittely #
## Sovelluksen tarkoitus ##
Sovellus on peli jonka avulla voi harjoitella muistamista. Sovelluksessa näytetään korttipakan kortteja satunnaisessa järjestyksessä ja pelaajan tehtävä on lopuksi valita oikea järjestys missä kortit juuri näytettiin. 


## Perusversion toiminnallisuus ##

### Pelin aloittaminen ###
* Ennen pelin alkua tulee lomake missä kysytään seuraavat asiat:
    * Näytetäänkö koko pakka vai vähemmän kortteja 
        * Kysytään kokonaislukua korttien määrästä 
* Lomakkeen lopussa on nappi aloita peli ja peli alkaa käyttäjän antamilla asetuksilla 
### Pelaaminen ###
* Haluttu määrä kortteja näytetään ruudulla 
    * ruudun alapuolella näytetään monesko kortti on menossa (esim 4/52)
* Kun kaikki kortit on näytetty avautuu seuraava näkymä jossa kerätään vastaukset. 
    * Näkymässä näytetään myös monesko kortti on menossa ja monta on jäljellä esim (5/52)
    * Näkymässä on myös seuraava/"lukitse vastaus" nappi jossa käyttäjä lukitsee kortin ja siirtyy valitsemaan seuraavaa 
    * Näkymässä on myös anna periksi nappi missä peli päättyy 
* Pelaaja valitsee kortin minkä muistaa tulleen ensimmäiseksi ja painaa sitten seuraava nappia. Tämän jälkeen hän valitsee muistamansa toisen kortin ja niin edespäin. 
* Kun pelaaja on valinnut kaikki kortit peli päättyy ja päästään tuloksiin. 
### Tulokset ###
* Pelin päätteeksi päästään tulokset sivulle 
* Tässä näytetään kuinka monta korttia sai oikein 
* Mitkä kortit meni oikein ja mitkä väärin 
* Voi verrata omia vastauksia oikeisiin vastauksiin 

## Jatkokehitysideoita ##
* hienot animaatiot
* Kortit näytetään automaattisesti mikäli pelaaja niin valitsee
* toisenlainen helppo muistamispeli
