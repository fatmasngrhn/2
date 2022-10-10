from araba import Araba
from flask import Flask
from flask.templating import render_template


app = Flask (__name__)


mercedes=Araba()
mercedes.id=1
mercedes.beygir=70
mercedes.icerik="güzel araba"
mercedes.model=2015
mercedes.renk="siyah"
mercedes.resimyolu="mercedes.jpg"
mercedes.marka="Mercedes Benz"
mercedes.uretilenUlkeAdi="Arjantin"

audi=Araba()
audi.id=2
audi.beygir=90
audi.icerik="güzel araba"
audi.model=2013
audi.renk="sarı"
audi.resimyolu="audi.jpg"
audi.marka="Audi"
audi.uretilenUlkeAdi="Bavyera"

ford=Araba()
ford.id=3
ford.beygir=90
ford.icerik="güzel araba"
ford.model=2019
ford.renk="mavi"
ford.resimyolu="ford.jpg"
ford.marka="Ford Focus"
ford.uretilenUlkeAdi="Michigan"

opel=Araba()
opel.id=4
opel.beygir=80
opel.icerik="güzel araba"
opel.model=2004
opel.renk="kırmızı"
opel.resimyolu="opel.jpg"
opel.marka="Opel Astra"
opel.uretilenUlkeAdi="Almanya"

arabaListesi=[mercedes, audi, ford, opel]


@app.route("/")
def anasayfa():
    return render_template ("index.html", araclar=arabaListesi)
    


if __name__ == "__main__":
    app.run(debug=True)