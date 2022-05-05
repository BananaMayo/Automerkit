# Automerkit

## Tsoha - Niklas Nygård

*Sovelluksen avulla voi oppia automerkkejä. Noviisin tulee vastata oikein eri automerkkien 
kohdalla, jotta hän voi siirtyä eteenpäin kysymyksissä. Jokainen käyttäjä on noviisi tai asiantuntija.*

Sovelluksen ominaisuuksia ovat:

- [X] - Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Noviisi näkee miten hän on edistynyt kysymyksissä, kuinka monta oikein ja väärin *(Kesekeneräinen)*
- Noviisi näkee montako kysymystä putkeen hän on vastannut oikein ja saa arvonimen 
  sen mukaan *(Kesekeneräinen)*
- [X] - Asiantuntija voi luoda automerkki kysymyksiä *(Kesekeneräinen)*
- [X] - Asiantuntija voi poistaa luomansa kysymyksen 
- [X] - Asiantuntija näkee vastanneiden tilastot

Sovellusta voi testata [Herokussa](https://automerkit-vierailijat.herokuapp.com/).
  * Tilastot ja poisto eivät jostain syystä toimi Herokussa, eikä myöskään kyselyn luominen.
    Vastaussivu on vielä vaiheessa, toimii kuitenkin Flask runilla muttei Herokusssa 
      * Herokussa seuraavanlainen virhe kun yrittää luoda kyselyä:
        ![image](https://user-images.githubusercontent.com/101586122/166695284-a1b5c098-0bf1-4a65-9fd8-6daeb53f736a.png)

Projektin sivut löytyvät kuvina [täältä](https://github.com/BananaMayo/Automerkit/tree/main/static/Automerkit_sivut).
