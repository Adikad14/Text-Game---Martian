import sys
import time
import os


#filozofia
# -Class- #
class Player:
    def __init__(self):
        self.location = 'b2'
        self.completed_missions = 0


player = Player()

# - Interaction - #


def print_location():  # Def for printing players location
    print('\n')
    print_slowly2(('Location: ' + map[player.location][Name]))
    print('\n')
    print_slowly2(('De: ' + map[player.location][Description]))
    print('\n')


def command():  # Main menu for commands
    print('\n')
    print_slowly('Co chciałbyś zrobić?\n')
    prompt = input('> ')
    permitted_prompt = ['idź', 'badaj', 'zbadaj', 'wyjdź', 'popatrz', 'rusz się', 'biegnij', 'opisz', 'misje',
                           'misja', 'wykonaj misje', 'skontaktuj się z nasa', 'skontaktuj', 'przygotuj', ]
    while prompt.lower() not in permitted_prompt:
        print_slowly('''Proszę wpisać poprawną komendę:
idź, zbadaj, opisz, misje, wykonaj misje (lub czynność np: skontaktuj)\n''')
        prompt = input('> ')
    if prompt.lower() == 'wyjdź':
        sys.exit()
    elif prompt.lower() in ['idź', 'rusz się', 'biegnij']:
        player_movement()
    elif prompt.lower() in ['popatrz', 'opisz']:
        player_description()
    elif prompt.lower() in ['badaj', 'zbadaj']:
        player_examine()
    elif prompt.lower() in ['misje', 'misja']:
        current_mission()
    elif prompt.lower() == 'wykonaj misje':
        if player.completed_missions == 0:
            mission_01()
        elif player.completed_missions == 1:
            mission_02()
    elif prompt.lower() in ['skontaktuj się z nasa', 'skontaktuj']:
        if player.completed_missions == 0:
            mission_01()
    elif prompt.lower() == 'przygotuj':
        if player.completed_missions == 1:
            mission_02()


def current_mission():  # Def for printing actual mission
    if player.completed_missions == 0:
        print_slowly('Spróbuj skontaktować się z NASA za pomocą komputera.')
        command()
    if player.completed_missions == 1:
        print_slowly('Przygotuj się na przyjście burzy')
        command()
    # if player.misja_wyknane == 2:
    # print_wolno((''))


def player_movement():  # Def for player movement
    question = 'Gdzie chciałbyś pójść?\n'
    place = input(question)
    if place in ['up', 'północ']:
        destination = map[player.location][up]
        ruch(destination)
    elif place in ['left', 'zachód']:
        destination = map[player.location][left]
        ruch(destination)
    elif place in ['right', 'wschód']:
        destination = map[player.location][right]
        ruch(destination)
    elif place in ['down', 'południe']:
        destination = map[player.location][down]
        ruch(destination)


def ruch(destination):
    loading()
    print('\n' + "Poruszyłeś się do " + destination + '.')
    player.location = destination
    print_location()
    command()


def player_description():  # Def for "opisz", in english: 'review' or 'description'
    print_slowly((map[player.location][Description]))
    time.sleep(1)
    command()


def player_examine():  # Def for "zbadaj", in english: "examine"
    if player.completed_missions == 0:
        print_slowly('Rozglądając się po wszystkim co jest w bazie, spostrzegasz na monitorze nową wiadomość od NASA.')
        command()
    elif player.completed_missions == 1:
        print_slowly('Narazie niema drugiej misji, poczekaj na update.')
        command()
    else:
        print(map[player.location][Badanie])
        time.sleep(1)
        command()


# - Map - #

Name = ''
Description = 'description'
Badanie = 'examine'
up = 'up', 'north'
down = 'down', 'south'
left = 'left', 'west'
right = 'right', 'east'

map = {
    'a1': {
        Name: "Sektor A1",
        Description: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Nic nowego.',
        up: '',
        down: 'a2',
        left: '',
        right: 'b1',
    },
    'a2': {
        Name: "Parking dla łaźików",
        Description: 'Tutaj powinny znajdować się wszystkie łaźiki.',
        Badanie: 'Wszystko jest bez zmian.',
        up: 'a1',
        down: 'a3',
        left: '',
        right: 'b2',
    },
    'a3': {
        Name: "Sektor A3",
        Description: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Nic ciekawego.',
        up: 'a2',
        down: '',
        left: '',
        right: 'b3',
    },
    'b1': {
        Name: "MAV - Mars Ascent Vehicle",
        Description: 'Miejsce nieopodal bazy, gdzie znajduje się MAV.',
        Badanie: 'Wszystko wygląda tak jak zawsze.',
        up: '',
        down: 'b2',
        left: 'a1',
        right: 'c1',
    },
    'b2': {
        Name: "Baza",
        Description: 'To jest twoja główna baza, jedyne bezpieczne miejsce na tej planecie.',
        Badanie: 'Nic nadzwyczajnego, żadnych nowości.',
        up: 'b1',
        down: 'b3',
        left: 'a2',
        right: 'c2',
    },
    'b3': {
        Name: "Miejsce do zagospodarowania.",
        Description: 'Zwykły plac przygotowany na przyszłe konstrukcje.',
        Badanie: 'Wygląda w normie.',
        up: 'b2',
        down: '',
        left: 'a3',
        right: 'c3',
    },
    'c1': {
        Name: "Sektor C1",
        Description: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Wygląda jak zawsze.',
        up: '',
        down: 'c2',
        left: 'b1',
        right: '',
    },
    'c2': {
        Name: "Panele słoneczne",
        Description: 'Tutaj znajdują się wszystkie potrzebne panele słoneczne, które zasilają bazę.',
        Badanie: 'Wszystko wygląda niezmiennie.',
        up: 'c1',
        down: 'c3',
        left: 'b2',
        right: '',
    },
    'c3': {
        Name: "Sektor C3",
        Description: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Nic nowego.',
        up: 'c2',
        down: '',
        left: 'b3',
        right: '',
    },

}


# - Menu - #
def main_menu_choose():  # Main menu
    choice = input("> ")
    if choice == "start":
        start_scene()
    elif choice.lower() == "pomoc":
        menu_help()
    elif choice.lower() == "wyjdź":
        sys.exit()
    while choice.lower() not in ['start', 'pomoc', 'wyjdź']:
        print('Proszę wpisać poprawną komendę.')
        choice = input("> ")
        if choice == "start":
            command()
        elif choice.lower() == "pomoc":
            menu_help()
        elif choice.lower() == "wyjdź":
            sys.exit()


def menu_help():  # Def for "pomoc" in main menu, english: "help"
    print('''It is a text game in which you control the character's history by entering commands.
You can end the game in any place by typing "exit". The basic commands are: "Go", "Examine", "Describe", "Missions"
To complete the missions, enter "Complete the task".
I recommend running the game in a normal CMD in full window!
To move, you must enter "Go" and then the direction: "Right", "left". e.t.c.
The selected options affect the history.
Game created by: Jakub "Adikad" Skrzypczak.\n''')
    main_menu_choose()


def main_menu():  # Main menu, visual condition
    os.system('cls')
    print('#########################')
    print('#Witaj w grze tekstowej!#')
    print('#       - Start -       #')
    print('#       - Pomoc -       #')
    print('#       - Wyjdź -       #')
    print('#########################')
    main_menu_choose()


# - Funkcje - #

def print_slowly(str):  # Def for text speech effect 1
    for player in str:
        sys.stdout.write(player)
        sys.stdout.flush()
        time.sleep(0.0)


def print_slowly2(str):  # Def for text speech effect 2 - slower
    for player in str:
        sys.stdout.write(player)
        sys.stdout.flush()
        time.sleep(0.0)


def loading():  # Def for "loading"
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)


# - Scenes - #

def game_over():  # Def for game over
    print_slowly('Ukończyłeś grę, a przynajmniej tę ścieżkę historii')
    time.sleep(2)
    sys.exit()


def mission_01():  # First mission, contacting with NASA
    if player.location not in 'b2':
        print('Aby skontaktować się z NASA, musisz znajdować się w bazie głównej.')
        command()
    else:
        print_slowly2('Komunikujesz się z NASA')
        loading()
        print_slowly2('Brawo! Udało Ci się nawiązać kontakt.\n')
        print_slowly2(('''NASA:--> Przyszyły do nas informacje, iż w kierunku Twojej lokalizacji zmierza burza piaskowa.
Nie stanowi zagrożenia dla misji, lecz prace na zewnątrz muszą być przerwane do odwołania.'''))
        player.completed_missions = player.completed_missions + 1
        command()


def mission_02():  # Second mission, waiting for storm
    if player.location in 'b2':
        print_slowly('Przygotowywujesz się na burzę.\n')
        mission_03()
    else:
        print_slowly('Aby przeczekać burzę musisz być w bazie.\n')
        command()


def mission_03():  # Third mission, storm gets dangerous
    print_slowly(('''NASA:--> Burza znajdująca się w Twojej lokalizacji osiąga prędkości które mogą być niebezpieczne prawidłowego funkcjonowania bazy i MAV.
Decyzja o anulowaniu misji należy do Ciebie.\n'''))
    decision_01()


def decision_01():  # First decission about story
    print_slowly('Wpisz "zostań", jeśli chcesz zostać, lub "anuluj", jeśli chcesz anulować misję.\n')
    decision_01_choose = input('> ')
    if decision_01_choose in ['zostań', 'zostan']:
        print_slowly('Wybrałeś aby zostać na Marsie.\n')
        time.sleep(1)
        command()
    if decision_01_choose in ['anuluj']:
        print_slowly('Wybrałeś aby anulować misję.\n')
        game_over()
    else:
        print_slowly('Proszę wybrać poprawną komendę.\n')


def start_scene():  # First scene, this is where game begins
    os.system('cls')
    print('''It is a text game in which you control the character's history by entering commands.
You can end the game in any place by typing "exit". The basic commands are: "Go", "Examine", "Describe", "Missions"
To complete the missions, enter "Complete the task".
I recommend running the game in a normal CMD in full window!
To move, you must enter "Go" and then the direction: "Right", "left". e.t.c.
The selected options affect the history.\n''')
    print('\n')
    print_slowly(('''Your name is Elon, you work as an astronaut in Nasa,
As one of many NASA astronauts you have been selected for a test flight to the planet Mars.
The months went by in hard training and simulations.
The "New Horizon" mission in which you participate provides for sending one crew member for a period of 31 days.
Its goal is to test in the extreme conditions of all life support systems,
as well as taking soil samples and then performing several experiments.
The trip to the planet Mars was to look as follows: Obtaining the Earth's orbit,
in orbit the ship will be refueled by additional vehicles, which will then land on Earth,
Then, the actual journey into Mars's orbit will begin. After a few months, you obtained the orbit of the red planet.
You are on the "Mother ship", its called: "Hermes",
you use MDV vehicle (Mars Descent Vehicle, used to land on the surface of the planet.) for landing.
After a safe landing, you decide to set up a base, and then enter it...'''))
    print('\n' * 2)
    print_location()
    command()


# - Game - #

main_menu()
