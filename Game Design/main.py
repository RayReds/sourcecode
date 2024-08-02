import time
class Time:
    def Start(self):
        pass
    def Stop(self):
        pass
class Player:
    def __init__(self, names):
        self.name = names
        self.kills = 0
        self.deaths = 0
        self.captures = 0
class Game:
    def __init__(self):
        self.playerList = {}
        self.events = []
    def setup(self):
        for i in range(int(input('How Many Players? > '))):
            playerName = input('Player Name? > ')
            playerTemp = Player(playerName)
            self.playerList[playerName] = playerTemp
    def start(self):
        print('Game Start !!')
        self.events.append('Game Start !!')
    def updateStats(self):
        print('1. Kill'+ '\n'+ '2. Capture')
        temp = self.playerList
        print(temp)
        type = int(input('> '))
        for i in range(len(temp)):
            print(f'{i}. {temp[i]}')
        action = int(input('> '))
        if type == 1:
            print('Players Killed :')
            for i in range(len(temp)):
                print(f'{i}. {temp[i].name}')
            action = int(input('> '))
    def end(self):
        self.events.append('Game End !!')
def Matching(case):
    match case:
        case '1':
            Game.start()
        case '2':
            Game.setup()
        case '3':
            Game.end()
            return 'End'
        case '4':
            Game.updateStats()
Game = Game()
Matching('Start')
inpt = input('> ')
while Matching(inpt) != 'End':
    inpt = input('> ')