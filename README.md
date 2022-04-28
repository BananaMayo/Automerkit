# Automerkit

## Tsoha - Niklas Nygård

*Sovelluksen avulla voi oppia automerkkejä. Noviisin tulee vastata oikein eri automerkkien 
kohdalla, jotta hän voi siirtyä eteenpäin kysymyksissä. Jokainen käyttäjä on noviisi tai asiantuntija.*

Sovelluksen ominaisuuksia ovat:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Noviisi näkee miten hän on edistynyt kysymyksissä, kuinka monta oikein ja väärin *(Kesekeneräinen)*
- Noviisi näkee montako kysymystä putkeen hän on vastannut oikein ja saa arvonimen 
  sen mukaan *(Kesekeneräinen)*
- Asiantuntija voi luoda automerkki kysymyksiä *(Kesekeneräinen)*
- Asiantuntija voi poistaa luomansa kysymyksen 
- Asiantuntija näkee vastanneiden tilastot

Sovellusta voi testata [Herokussa](https://automerkit-vierailijat.herokuapp.com/).
  * Tilastot ja poisto eivät jostain syystä toimi Herokussa, mutta Flask runilla ne toimii. Kyselyn luoiminen on
  vielä vaiheessa, toimii kuitenkin Flask runilla muttei Herokusssa; kuvan lataamiselle tulee vielä muutoksia 
  jotta sen saa jokaisen kysymyksen kohdalle näkyväksi. 
