import sys
import time
import random
import cmd
import textwrap
import os

##### - Class - #####
class gracz: #Filozofia
    def __init__(self):
        self.lokalizacja = 'b2'
        self.misje_wykonane = 0
gracz = gracz()


##### - Interaction - #####

def print_lokalizacja():      # Def for printing players location
    print('\n')
    print_wolno2(('Aktualna lokalizacja: ' + mapa[gracz.lokalizacja][Nazwa]))
    print('\n')
    print_wolno2(('Opis: ' + mapa[gracz.lokalizacja][Opis]))
    print('\n')

def komenda():      # Main menu for commands
    print('\n')
    print_wolno(('Co chciałbyś zrobić?\n'))
    polecenie = input('> ')
    dozwolone_polecenia = ['idź', 'badaj', 'zbadaj', 'wyjdź', 'popatrz', 'rusz się', 'biegnij', 'opisz', 'misje', 'misja', 'wykonaj misje', 'skontaktuj się z nasa', 'skontaktuj', 'przygotuj', '']
    while polecenie.lower() not in dozwolone_polecenia:
        print_wolno('''Proszę wpisać poprawną komendę: idź, zbadaj, opisz, misje, wykonaj misje (lub poprostu czynność np: skontaktuj),
         \n''')
        polecenie = input('> ')
    if polecenie.lower() == 'wyjdź':
        sys.exit()
    elif polecenie.lower() in ['idź', 'rusz się', 'biegnij']:
        gracz_ruch(polecenie.lower())
    elif polecenie.lower() in ['popatrz', 'opisz']:
        gracz_opis(polecenie.lower())
    elif polecenie.lower() in ['badaj', 'zbadaj']:
        gracz_badanie(polecenie.lower())
    elif polecenie.lower() in ['misje', 'misja']:
        aktualna_misja(polecenie.lower())
    elif polecenie.lower() == 'wykonaj misje':
        if gracz.misje_wykonane == 0:
            misja_01()
        elif gracz.misje_wykonane == 1:
            misja_02()
    elif polecenie.lower() in ['skontaktuj się z nasa', 'skontaktuj']:
        if gracz.misje_wykonane == 0:
            misja_01()
    elif polecenie.lower() == 'przygotuj':
        if gracz.misje_wykonane == 1:
            misja_02()

def aktualna_misja(polecenie):    # Def for printing actual mission
    if gracz.misje_wykonane == 0:
        print_wolno(('Spróbuj skontaktować się z NASA za pomocą komputera.'))
        komenda()
    if gracz.misje_wykonane == 1:
        print_wolno(('Przygotuj się na przyjście burzy'))
        komenda()
    #if gracz.misja_wyknane == 2:
        #print_wolno((''))

def gracz_ruch(polecenie):      # Def for player movement
    pytanie = 'Gdzie chciałbyś pójść?\n'
    miejsce = input(pytanie)
    if miejsce in ['góra', 'północ']:
        miejsce_docelowe = mapa[gracz.lokalizacja][góra]
        ruch(miejsce_docelowe)
    elif miejsce in ['lewo', 'zachód']:
        miejsce_docelowe = mapa[gracz.lokalizacja][lewo]
        ruch(miejsce_docelowe)
    elif miejsce in ['prawo', 'wschód']:
        miejsce_docelowe = mapa[gracz.lokalizacja][prawo]
        ruch(miejsce_docelowe)
    elif miejsce in ['dół', 'południe']:
        miejsce_docelowe = mapa[gracz.lokalizacja][dół]
        ruch(miejsce_docelowe)

def ruch(miejsce_docelowe):
    ładowanie()
    print('\n' + "Poruszyłeś się do " + miejsce_docelowe + '.')
    gracz.lokalizacja = miejsce_docelowe
    print_lokalizacja()
    komenda()

def gracz_opis(polecenie):    # Def for "opisz", in english: 'review' or 'description'
    print_wolno((mapa[gracz.lokalizacja][Opis]))
    time.sleep(1)
    komenda()

def gracz_badanie(polecenie):     # Def for "zbadaj", in english: "examine"
    if gracz.misje_wykonane == 0:
        print_wolno(('Rozglądając się po wszystkim co jest w bazie, spostrzegasz na monitorze nową wiadomość od NASA.'))
        komenda()
    elif gracz.misje_wykonane == 1:
        print_wolno(('Narazie niema drugiej misji, poczekaj na update.'))
        komenda()
    else:
        print(mapa[gracz.lokalizacja][Badanie])
        time.sleep(1)
        komenda()


##### - Map - #####

# a b c
#| |m| | 1
#|ł|b|p| 2
#| |ś| | 3
#-------

Nazwa = ''
Opis = 'opis'
Badanie = 'zbadaj'
góra = 'góra', 'północ'
dół = 'dół', 'południe'
lewo = 'lewo', 'zachód'
prawo = 'prawo', 'wschód'

mapa = {
    'a1': {
        Nazwa: "Sektor A1",
        Opis: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Nic nowego.',
        góra: '',
        dół: 'a2',
        lewo: '',
        prawo: 'b1',
    },
    'a2': {
        Nazwa: "Parking dla łaźików",
        Opis: 'Tutaj powinny znajdować się wszystkie łaźiki.',
        Badanie: 'Wszystko jest bez zmian.',
        góra: 'a1',
        dół: 'a3',
        lewo: '',
        prawo: 'b2',
    },
    'a3': {
        Nazwa: "Sektor A3",
        Opis: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Nic ciekawego.',
        góra: 'a2',
        dół: '',
        lewo: '',
        prawo: 'b3',
    }, 
    'b1': {
        Nazwa: "MAV - Mars Ascent Vehicle",
        Opis: 'Miejsce nieopodal bazy, gdzie znajduje się MAV.',
        Badanie: 'Wszystko wygląda tak jak zawsze.',
        góra: '',
        dół: 'b2',
        lewo: 'a1',
        prawo: 'c1',
    },   
    'b2': {
        Nazwa: "Baza",
        Opis: 'To jest twoja główna baza, jedyne bezpieczne miejsce na tej planecie.',
        Badanie: 'Nic nadzwyczajnego, żadnych nowości.',
        góra: 'b1',
        dół: 'b3',
        lewo: 'a2',
        prawo: 'c2',
    },   
    'b3': {
        Nazwa: "Miejsce do zagospodarowania.",
        Opis: 'Zwykły plac przygotowany na przyszłe konstrukcje.',
        Badanie: 'Wygląda w normie.',
        góra: 'b2',
        dół: '',
        lewo: 'a3',
        prawo: 'c3',
    },   
    'c1': {
        Nazwa: "Sektor C1",
        Opis: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Wygląda jak zawsze.',
        góra: '',
        dół: 'c2',
        lewo: 'b1',
        prawo: '',
    },   
    'c2': {
        Nazwa: "Panele słoneczne",
        Opis: 'Tutaj znajdują się wszystkie potrzebne panele słoneczne, które zasilają bazę.',
        Badanie: 'Wszystko wygląda niezmiennie.',
        góra: 'c1',
        dół: 'c3',
        lewo: 'b2',
        prawo: '',
    },   
    'c3': {
        Nazwa: "Sektor C3",
        Opis: 'Teren blisko bazy na którym narazie niema nic ciekawego, tylko piach i kamienie.',
        Badanie: 'Nic nowego.',
        góra: 'c2',
        dół: '',
        lewo: 'b3',
        prawo: '',
    },   

}


##### - Menu - #####
def glowne_menu_wybory():    # Main menu
    wybor = input("> ")
    if wybor == ("start"):
        start_scena()
    elif wybor.lower() == ("pomoc"):
        pomoc_menu()
    elif wybor.lower() == ("wyjdź"):
        sys.exit()
    while wybor.lower() not in ['start', 'pomoc', 'wyjdź']:
        print ('Proszę wpisać poprawną komendę.')
        option = input("> ")
        if wybor == ("start"):
           komenda()
        elif wybor.lower() == ("pomoc"):
            pomoc_menu()
        elif wybor.lower() == ("wyjdź"):
            sys.exit()

def pomoc_menu():   # Def for "pomoc" in main menu, english: "help"
    print('''Jest to gra tekstowa, w której sterujesz historią postaci za pomocą wpisywania komend.
W każdym miejscu możesz zakończyć grę wpisując "wyjdź". Podstawowe komendy to: "Idź", "Zbadaj", "Opisz", "Misje"
Aby wykonać misje, wpisz "Wykonaj zadanie".
Polecam uruchomić grę w normalnym CMD w pełnym oknie!
Aby się poruszać, trzeba wpisać "Idź", a następnie kierunek: "Prawo", "lewo". itd.
Wybrane opcje wpływają na historię.
Game created by: Jakub "Adikad" Skrzypczak.\n''')
    glowne_menu_wybory()

def glowne_menu():    # Main menu, visual condition
    os.system('cls')
    print('#########################')
    print('#Witaj w grze tekstowej!#')
    print('#       - Start -       #')
    print('#       - Pomoc -       #')
    print('#       - Wyjdź -       #')
    print('#########################')
    glowne_menu_wybory()


##### - Funkcje - #####

def print_wolno(str):     # Def for text speech effect 1
    for gracz in str:
        sys.stdout.write(gracz)
        sys.stdout.flush()
        time.sleep(0.0)
def print_wolno2(str):     # Def for text speech effect 2 - slower
    for gracz in str:
        sys.stdout.write(gracz)
        sys.stdout.flush()
        time.sleep(0.0)


def ładowanie():    # Def for "loading"
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


##### - Scenes - #####

def koniec_gry():    # Def for game over
    print_wolno(('Ukończyłeś grę, a przynajmniej tą ścieżkę historii'))
    time.sleep(2)
    sys.exit()

def misja_01():       # First mission, contacting with NASA
    if gracz.lokalizacja not in 'b2':
        print('Aby skontaktować się z NASA, musisz znajdować się w bazie głównej.')
        komenda()
    else:
        print_wolno2(('Komunikujesz się z NASA'))
        ładowanie()
        print_wolno2(('Brawo! Udało Ci się nawiązać kontakt.\n'))
        print_wolno2(('''NASA:--> Przyszyły do nas informacje, iż w kierunku Twojej lokalizacji zmierza burza piaskowa.
Nie stanowi zagrożenia dla misji, lecz prace na zewnątrz muszą być przerwane do odwołania.'''))
        gracz.misje_wykonane = gracz.misje_wykonane + 1
        komenda()

def misja_02():   # Second mission, waiting for storm
    if gracz.lokalizacja in 'b2':
        print_wolno(('Przygotowywujesz się na burzę.\n'))
        misja_03()
    else:
        print_wolno(('Aby przeczekać burzę musisz być w bazie.\n'))
        komenda()

def misja_03():  # Third mission, storm gets dangerous
    print_wolno(('''NASA:--> Burza znajdująca się w Twojej lokalizacji osiąga prędkości które mogą być niebezpieczne prawidłowego funkcjonowania bazy i MAV.
Decyzja o anulowaniu misji należy do Ciebie.\n'''))
    decyzja_01()



def decyzja_01():   # First decission about story
    decyzja_01_dozwolone_wybory = ['zostań', 'zostan', 'anuluj']
    print_wolno(('Wpisz "zostań", jeśli chcesz zostać, lub "anuluj", jeśli chcesz anulować misję.\n'))
    decyzja_01_wybor = input('> ')
    if decyzja_01_wybor in ['zostań', 'zostan']:
        print_wolno(('Wybrałeś aby zostać na Marsie.\n'))
        time.sleep(1)
        komenda()
    if decyzja_01_wybor in ['anuluj']:
        print_wolno(('Wybrałeś aby anulować misję.\n'))
        koniec_gry()
    else:
        print_wolno(('Proszę wybrać poprawną komendę.\n'))



def start_scena():     # First scene, this is where game begins
    os.system('cls')
    print('''Jest to gra tekstowa, w której sterujesz historią postaci za pomocą wpisywania komend.
W każdym miejscu możesz zakończyć grę wpisując "wyjdź". Podstawowe komendy to: "Idź", "Zbadaj", "Opisz", "Misje"
Aby wykonać misje, wpisz "Wykonaj zadanie".
Polecam uruchomić grę w normalnym CMD w pełnym oknie!
Aby się poruszać, trzeba wpisać "Idź", a następnie kierunek: "Prawo", "lewo". itd.
Wybrane opcje wpływają na historię.\n''')
    print('\n')
    print_wolno(('''Nazywasz się Elon, pracujesz jako astronauta w Nasa, jako jeden z wielu astronautów NASA zostałeś wybrany do lotu testowego na planetę Mars.
Miesiące mijały na ciężkich treningach i symulacjach. Misja "New Horizon" w której uczestniczysz przewiduje wysłanie jednego członka załogi na okres 31 dni.
Jego cel to przetestowanie w ekstremalnych warunkach wszystkich systemów podtrzymujących życia, jak i pobranie próbek gruntu, a następnie wykonanie kilku eksperymentów.
Podróż na planetę Mars miała wyglądać w następujący sposób: Uzyskanie orbity Ziemi, na orbicie statek zostanie zatankowany przez dodatkowe pojazdy, które nastepnie wylądują na Ziemi,
Następnie zostanie rozpoczęta faktyczna podróż na orbitę Marsa. Po kilku miesiącach, uzyskałeś orbitę czerwonej planety. Znajdujesz się na "Statku matce" o nazie "Hermes", używasz
pojazdu MDV (Mars Descent Vehicle, służy do wylądowania na powierzchni planety.) do lądowania. Po bezpiecznym lądowaniu rozkładasz główną bazę, a następnie do niech wchodzisz...'''))
    print('\n' * 2)
    print_lokalizacja()
    komenda()
    
##### - Game - #####

glowne_menu()
