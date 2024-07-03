categories = ("Elektronika", "Do domu", "Do ogrodu", "Sport i turystyka", "Motoryzacja", "Zdrowie i uroda",
              "Dla dzieci", "Rolnictwo", "Nieruchomości", "Moda", "Kultura i rozrywka", "Oddam za darmo")

states = ("Nowe", "Używane", "Uszkodzone")

backend_url = "http://127.0.0.1:5000"
# backend_url = "http://mrgrzechu96.pythonanywhere.com"

days = tuple(str(day) for day in range(1, 32))

months = ("Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień",
          "Październik", "Listopad", "Grudzień")

years = tuple(str(year) for year in range(1910, 2024))
