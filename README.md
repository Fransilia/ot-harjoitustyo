# Ot-harjoitustyö
### Korttipakan muistaminen
Sovelluksen avulla voi harjoitella korttipakan muistamista.

### Tämänhetkinen toiminta
Perusprojektirakenne toimii. Alkuruudussa aloita nappia painamalla pääsee valitsemaan korttien määrän. Väärillä syötteillä ohjelma ilmoittaa virheen. Kun oikea syöte on laitettu niin peli alkaa. Näytetään yksitellen haluttu määrä kortteja. Seuraavaan pääsee seuraava nappia painamalla. Kun kaikki on näytetty päästään näkymään missä käyttäjä laittaa vastaukset muistamassaan järjestyksessä. Kun kaikki on laitettu päästään tulos sivulle. Tulos sivulla näytetään montako arvausta meni oikein. Näytetään myös oikeat vastaukset ja jos käyttäjä muisti oikein vai väärin kyseisen kortin. Tulossivulta voi aloittaa uuden pelin.

### Dokumentaatio
[Työaikakirjanpito](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/tyoaikakirjanpito.md)

[Vaatimusmäärittely](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/vaatimuusmaarittely.md)

[Arkkitehtuuri](https://github.com/Fransilia/ot-harjoitustyo/blob/41148b8e3d566ece72ad9407172c8cc6369052e1/harjoitustyo_korttipakan_muistaminen/dokumentaatio/arkkitehtuuri.md)

### Asennus
1. Asenna riippuvuudet komennolla:
```
python3 -m pipenv install
```
2. Käynnistä sovellus komennolla:
```
python3 -m pipenv run start
```
3. Testaus komennoilla:
```
python3 -m pipenv run test
```
4. Testikattavuus:
```
python3 -m pipenv run coverage
```
```
python3 -m pipenv run coverage-report
```
5. Pylint
```
python3 -m pipenv run lint
```