import pandas as pd
from pyodide.http import open_url
from js import document


    
url = "https://raw.githubusercontent.com/Einsteintje/Website-test/main/Test.csv"
array = pd.read_csv(open_url(url), sep = ';').to_numpy()
data = array.tolist()

    
colorCodes = {
    'Blue': '#2c72e2',
    'Red': '#e22c2c',
    'Yellow': '#f7d118',
    'Green': '#1ff718'
}
cards = {}

class Card:
    def __init__(self, name, price,colors, image):
        self.name = name
        self.price = price
        self.colors = colors
        self.image = image
        
        colorButtons = ''
        colorImages = '<figure class="image is-3by2">'
        colorFound = False
        fadeState = ' show'
        for color, hex in colorCodes.items():
            if color.lower() in colors.lower():
                colorButtons += f'''<span class="icon" onclick ="runPython('changeColor',[\'{name}\', \'{color}\'])" >
                        <i class="fa-regular fa-circle" style = "color:{hex}"></i>
                        </span>'''
                imgUrl = f"https://raw.githubusercontent.com/Einsteintje/Website-test/main/Images/{color}/{image}"
                colorImages += f'<img class="fadeImage{fadeState}" src="{imgUrl}" alt="Placeholder image" id = "{name} {color}">'
                if not colorFound:
                    colorFound = True
                    fadeState = ''
                    self.activeColor = color
        colorImages += '</figure>'
        
        self.html = f'''
        <div class="column is-2" id = "{name}">
            <div class='card'>
                <div class="card-image">
                    {colorImages}
                </div>
                <div class="card-content ">
                    <div class='content has-text-weight-semibold'>
                        {name}<br>€{price}<br>
                        {colorButtons}
                    </div>
            </div>
        </div>
        '''
        manualDiv = document.getElementById('manual-write')
        manualDiv.innerHTML += self.html

def changeColor(arguments):
    card = cards[arguments[0]]
    if card.activeColor != arguments[1]:
        document.getElementById(f'{arguments[0]} {arguments[1]}').classList.toggle('show')
        document.getElementById(f'{arguments[0]} {card.activeColor}').classList.toggle('show')
        card.activeColor = arguments[1]

def dropDownLabel(label):
    print(label)
    document.getElementById(label).classList.toggle("is-active")
    buttons = document.getElementsByName(label + 'Button')
    for button in buttons:
        button.classList.toggle('show')


def filterColor(color):
    print("color filtered: " + color)

for index, row in enumerate(data):
    cards[row[0]] = Card(row[0], row[1],row[2], row[3])


    

print(data)