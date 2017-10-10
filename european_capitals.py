import random
european_capitals = {
            'Albania': 'Tirana',
            'Andorra': 'Andorra la Vella',
            'Armenia': 'Yerevan',
            'Austria': 'Vienna',
            'Azerbaijan': 'Baku',
            'Belarus': 'Minsk',
            'Belgium': 'Brussels',
            'Bosnia and Herzegovina': 'Sarajevo',
            'Bulgaria': 'Sofia',
            'Croatia': 'Zagreb',
            'Cyprus': 'Nicosia',
            'Czech Republic': 'Prague',
            'Denmark': 'Copenhagen',
            'Estonia': 'Tallinn',
            'Finland': 'Helsinki',
            'France': 'Paris',
            'Georgia': 'Tbilisi',
            'Germany': 'Berlin',
            'Greece': 'Athens',
            'Hungary': 'Budapest',
            'Iceland': 'Reykjavik',
            'Ireland': 'Dublin',
            'Italy': 'Rome',
            'Kazakhstan': 'Astana',
            'Kosovo': 'Pristina',
            'Latvia': 'Riga',
            'Liechtenstein': 'Vaduz',
            'Lithuania': 'Vilnius',
            'Luxembourg': 'Luxembourg',
            'Macedonia (FYROM)': 'Skopje',
            'Malta': 'Valletta',
            'Moldova': 'Chisinau',
            'Monaco': 'Monaco',
            'Montenegro': 'Podgorica',
            'Netherlands': 'Amsterdam',
            'Norway': 'Oslo',
            'Poland': 'Warsaw',
            'Portugal': 'Lisbon',
            'Romania': 'Bucharest',
            'Russia': 'Moscow',
            'San Marino': 'San Marino',
            'Serbia': 'Belgrade',
            'Slovakia': 'Bratislava',
            'Slovenia': 'Ljubljana',
            'Spain': 'Madrid',
            'Sweden': 'Stockholm',
            'Switzerland': 'Bern',
            'Turkey': 'Ankara',
            'Ukraine': 'Kiev',
            'United Kingdom': 'London',
            'Vatican City': 'Vatican City'
            }

def main():
    generator = random.choice(list(european_capitals.items()))
    while True:
        guess = raw_input("Guess the capital of " + (generator[0]) + ": ")
        if guess == generator[1]:
            print "WOOHOOO, that's right!"
            break
        else:
            print "WRONG! Guess again: "

if __name__ == "__main__":
    another_game = "y"
    while another_game.lower() == "y":
        main()
        another_game = raw_input("Wanna play again?    Y / N  :")
