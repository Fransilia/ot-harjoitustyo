# Ot-harjoitustyö
### Korttipakan muistaminen
Sovelluksen avulla voi harjoitella korttipakan ulkoa muistamista.

### Dokumentaatio
[Käyttöohje](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/vaatimuusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/testausdokumentti.md)

[Työaikakirjanpito](https://github.com/Fransilia/ot-harjoitustyo/blob/master/harjoitustyo_korttipakan_muistaminen/dokumentaatio/tyoaikakirjanpito.md)

### Asennus
[Viimeisin Release](https://github.com/Fransilia/ot-harjoitustyo/releases/tag/Viikko7)

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