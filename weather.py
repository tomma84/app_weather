import requests
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

api_key = "a051396e946a1309fa43f950786cf903"

def cerca_cap(evento=None):
    try:
        api_key = "a051396e946a1309fa43f950786cf903"
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" + cap.get() + ",it&appid=" + api_key + '&units=metric'
        response = requests.get(url)
        data = json.loads(response.text)
        
        icona = "icons/" + data['weather'][0]['icon'] + "@2x.png"
        render = ImageTk.PhotoImage(Image.open(icona))
        immagine.create_image(50, 50, image=render)
        immagine.image = render
        
        var_localita.set(data['name'])
        var_temperatura.set('Attuale: ' + str(data['main']['temp']) + ' °C')
        var_temperatura_min.set('Min: ' + str(data['main']['temp_min']) + ' °C')
        var_temperatura_max.set('Max: ' + str(data['main']['temp_max']) + ' °C')
    except:
        messagebox.showerror("Errore", "Non hai inserito un CAP valido")


root = Tk()
root.title('Meteo')
root.resizable(width=False, height=False)

contenitore = Frame(root, padx=10, pady=10)

etichetta = Label(contenitore, text='CAP Località')

cap = StringVar()
cap_entry = Entry(contenitore, textvariable=cap)
cap_entry.bind('<Return>', cerca_cap)

cerca = Button(contenitore, text='Cerca', command=cerca_cap)

contenitore.grid(column=0, row=0)

etichetta.grid(column=0, row=0)
cap_entry.grid(column=1, row=0, padx=5)
cerca.grid(column=2, row=0)

immagine = Canvas(contenitore, bg='#8ad0ff', height=100, width=100)
immagine.grid(column=0, row=1, pady=(7,0))

cornice_dati = LabelFrame(contenitore, text='Oggi')
cornice_dati.grid(column=1, row=1, columnspan=2, sticky='EW')

var_localita = StringVar()
var_temperatura = StringVar()
var_temperatura_min = StringVar()
var_temperatura_max = StringVar()

localita = Label(cornice_dati, textvariable=var_localita)
temperatura = Label(cornice_dati, textvariable=var_temperatura)
temperatura_min = Label(cornice_dati, textvariable=var_temperatura_min)
temperatura_max = Label(cornice_dati, textvariable=var_temperatura_max)

localita.pack()
temperatura.pack()
temperatura_min.pack()
temperatura_max.pack()

root.mainloop()