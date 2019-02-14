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
    print_slowly2(('Description: ' + map[player.location][Description]))
    print('\n')


def command():  # Main menu for commands
    print('\n')
    print_slowly('What you want to do?\n')
    prompt = input('> ')
    permitted_prompt = ['go', 'move', 'look', 'describe', 'examine', 'mission', 'missions', 'complete the mission', 'complete mission', 'contact with nasa', 'contact', 'wait', 'get ready', 'exit']
    while prompt.lower() not in permitted_prompt:
        print_slowly('''Enter valid command:
go, describe, examine, mission, complete the mission.\n''')
        prompt = input('> ')
    if prompt.lower() == 'exit':
        sys.exit()
    elif prompt.lower() in ['go', 'move']:
        player_movement()
    elif prompt.lower() in ['look', 'describe']:
        player_description()
    elif prompt.lower() in ['examine']:
        player_examine()
    elif prompt.lower() in ['mission', 'missions']:
        current_mission()
    elif prompt.lower() == ['complete the mission', 'complete mission']:
        if player.completed_missions == 0:
            mission_01()
        elif player.completed_missions == 1:
            mission_02()
    elif prompt.lower() in ['contact with nasa', 'contact']:
        if player.completed_missions == 0:
            mission_01()
    elif prompt.lower() == ['wait', 'get ready']:
        if player.completed_missions == 1:
            mission_02()


def current_mission():  # Def for printing actual mission
    if player.completed_missions == 0:
        print_slowly('Try to contact with NASA.')
        command()
    if player.completed_missions == 1:
        print_slowly('Get ready for the storm.')
        command()
    # if player.misja_wyknane == 2:
    # print_wolno((''))


def player_movement():  # Def for player movement
    question = 'Where do you want to go?\n'
    place = input(question)
    if place in ['up', 'north']:
        destination = map[player.location][up]
        ruch(destination)
    elif place in ['left', 'west']:
        destination = map[player.location][left]
        ruch(destination)
    elif place in ['right', 'east']:
        destination = map[player.location][right]
        ruch(destination)
    elif place in ['down', 'south']:
        destination = map[player.location][down]
        ruch(destination)


def ruch(destination):
    loading()
    print('\n' + "You moved to: " + destination + '.')
    player.location = destination
    print_location()
    command()


def player_description():  # Def for "opisz", in english: 'review' or 'description'
    print_slowly((map[player.location][Description]))
    time.sleep(1)
    command()


def player_examine():  # Def for "zbadaj", in english: "examine"
    if player.completed_missions == 0:
        print_slowly('Looking around everything that is in the base, you notice a new message from NASA on the monitor.')
        command()
    elif player.completed_missions == 1:
        print_slowly('No.')
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
        Name: "Sector A1",
        Description: 'Nothing, but rocks and a lot of sand.',
        Badanie: 'Nothing new.',
        up: '',
        down: 'a2',
        left: '',
        right: 'b1',
    },
    'a2': {
        Name: "Parking for rovers",
        Description: 'All rovers should be here.',
        Badanie: 'Everything is unchanged.',
        up: 'a1',
        down: 'a3',
        left: '',
        right: 'b2',
    },
    'a3': {
        Name: "Sector A3",
        Description: 'Nothing, but rocks and a lot of sand.',
        Badanie: 'Nothing interesting.',
        up: 'a2',
        down: '',
        left: '',
        right: 'b3',
    },
    'b1': {
        Name: "MAV - Mars Ascent Vehicle",
        Description: 'A place near the base where the MAV is located.',
        Badanie: 'Everything looks like always.',
        up: '',
        down: 'b2',
        left: 'a1',
        right: 'c1',
    },
    'b2': {
        Name: "Hab",
        Description: 'This is your main base, the only safe place on this planet.',
        Badanie: 'Nothing extraordinary, no news.',
        up: 'b1',
        down: 'b3',
        left: 'a2',
        right: 'c2',
    },
    'b3': {
        Name: "A place to manage.",
        Description: 'An ordinary square prepared for future constructions.',
        Badanie: 'Looks normal.',
        up: 'b2',
        down: '',
        left: 'a3',
        right: 'c3',
    },
    'c1': {
        Name: "Sector C1",
        Description: 'Nothing, but rocks and a lot of sand.',
        Badanie: 'It looks like always.',
        up: '',
        down: 'c2',
        left: 'b1',
        right: '',
    },
    'c2': {
        Name: "Solar panels",
        Description: 'Here you will find all the solar panels that need to feed the base.',
        Badanie: 'Everything looks invariably.',
        up: 'c1',
        down: 'c3',
        left: 'b2',
        right: '',
    },
    'c3': {
        Name: "Sector C3",
        Description: 'Nothing, but rocks and a lot of sand.',
        Badanie: 'Nothing new.',
        up: 'c2',
        down: '',
        left: 'b3',
        right: '',
    },

}


# - Menu - #
def main_menu_choose():  # Main menu
    choice = input("> ")
    if choice == "play":
        start_scene()
    elif choice.lower() == "help":
        menu_help()
    elif choice.lower() == "exit":
        sys.exit()
    while choice.lower() not in ['play', 'help', 'exit']:
        print('Please enter valid command.')
        choice = input("> ")
        if choice == "play":
            command()
        elif choice.lower() == "help":
            menu_help()
        elif choice.lower() == "exit":
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
    print('###########################')
    print('#Welcome to the text game!#')
    print('#         - Play -        #')
    print('#         - Help -        #')
    print('#         - Exit -        #')
    print('###########################')
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
    print_slowly('You have completed the game, at least this path of history.')
    time.sleep(2)
    sys.exit()


def mission_01():  # First mission, contacting with NASA
    if player.location not in 'b2':
        print('To contact NASA, you must be in the Hab.')
        command()
    else:
        print_slowly2('You are communicating with NASA')
        loading()
        print_slowly2('Bravo! You have made contact.\n')
        print_slowly2(('''NASA:--> Information has come to us that a sandstorm is heading towards your location.
It does not pose a threat to the mission, but outside work must be discontinued until further notice.'''))
        player.completed_missions = player.completed_missions + 1
        command()


def mission_02():  # Second mission, waiting for storm
    if player.location in 'b2':
        print_slowly('You are preparing for the storm.\n')
        mission_03()
    else:
        print_slowly('To wait out the storm you have to be in the Hab.\n')
        command()


def mission_03():  # Third mission, storm gets dangerous
    print_slowly(('''NASA:--> The storm located in your location reaches speeds that can be dangerous
for the proper operation of the base and MAV.
The decision to cancel the mission is yours.\n'''))
    decision_01()


def decision_01():  # First decission about story
    print_slowly('Enter "stay" if you want to stay or "cancel" if you want to cancel the mission.\n')
    decision_01_choose = input('> ')
    if decision_01_choose in ['stay']:
        print_slowly('You chose to stay on Mars.\n')
        time.sleep(1)
        command()
    if decision_01_choose in ['cancel']:
        print_slowly('You have chosen to cancel the mission.\n')
        game_over()
    else:
        print_slowly('PPlease choose the correct command.\n')


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
