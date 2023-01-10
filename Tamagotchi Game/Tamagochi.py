from Tama import Tamagotchi
command = 'halo'
tamas = {}
names = []
while command:
    command = input('Command: ').split()
    if command:
        if command[0] == 'create' and len(command) == 2:
            if command[1] not in names:
                tamas[command[1]] = Tamagotchi(command[1])
                names.append(command[1])
                print(tamas[command[1]])
            else:
              print('You already have a Tamagotchi called that.')
        elif command[0] == 'feed' and len(command) == 2:
          if command[1] in names:
            tamas[command[1]].feed()
          print(tamas[command[1]])
    else:
      print('No Tamagotchi with that name.')
  elif command[0] == 'play' and len(command) == 2:
    if command[1] in names:
      tamas[command[1]].play()
      print(tamas[command[1]])
    else:
      print('No Tamagotchi with that name.')
  elif command[0] == 'wait':
    for i in names:
      tamas[i].increment_time()
      print(tamas[i])
  else:
    print('Invalid command')
    continue
