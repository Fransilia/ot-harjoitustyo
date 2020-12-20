# Käyttöohje #
Lataa projektin viimeisimmän releasen lähdekoodi.

## Ohjelman käynnistäminen ##
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```
python3 -m pipenv install
```
Käynnistä sovellus komennolla:
```
python3 -m pipenv run start
```

## Pelin aloitus ##
Ensimmäisessä näkymässä on kaksi nappia. Aloita nappia (ylin) painamalla pääsee aloittamaan pelin. Alin nappi "tietoja" avaa ruudun missä on lyhyt kuvaus pelistä ja sen tarkoituksesta. 

**Paina aloita nappia** aloittaaksesi pelin. Pääset tästä näkymään mistä voit valita pelisi asetukset.

## Pelin asetuksien valitseminen ##
Aloita napin painamisen jälkeen sovellus kysyy montako korttia pelaaja tahtoo koittaa muistaa. Kirjoita tähän kokonaisluku. 

Kun olet valinnut pelin asetukset paina aloita nappia.

## Pelaaminen ##
Kortteja näytetään yksitellen niin monta kun olet valinnut. Paina seuraava nappia nähdäksesi seuraavan kortin. Koita muistaa kortit ja oikea järjestys!! 

**Kun kaikki kortit on näytetty** pelaaja siirtyy täyttämään vastaukset hänen muistamassaan järjestyksessä. Aina kun valitset kortin **muista painaa lukitse vastaus** päästäksesi valitsemaan seuraavaa korttia. Alhaalta näet monesko kortti on menossa.

Kun olet täyttänyt kaikki vastaukset peli loppuu ja pääset tulokset sivulle. Tässä näet miten hyvin pärjäsit.

Tulokset näkymästä voi aloittaa uuden pelin tai palata päävalikkoon. 
