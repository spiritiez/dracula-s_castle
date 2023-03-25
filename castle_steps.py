import json
import time
import random

with open("castle.json") as data:
    
    castle_quest_data = list(json.load(data))
    print('Be sure to read the rules before starting the game.')
    print()
    name_of_player = input('Enter your name, please\n')
    flag = input('would you like to see a demo version of the quest? Enter "yes" if you want and "no" if vice versa\n')
 
    print(castle_quest_data[0])
    print()
    print(f'{name_of_player}, your next action is:\n' + '\n'.join(list(castle_quest_data[1].keys())))
    your_step = castle_quest_data[1]
    
    for i in range(5):
        if flag == 'no':
            step = input()
        else:
            step = random.choice(list(your_step.keys()))
            time.sleep(2)
        if step not in your_step:
            print('O-oh! This action is not available. Try another way')
            step = input()
        your_step = your_step[step]
        
        if your_step == "return to enter":
            your_step = castle_quest_data[1]
            print(castle_quest_data[0])
            print()
            print(f'{name_of_player}, your possible actions are:\n' + '\n'.join(list(castle_quest_data[1].keys())))
            continue
            
        if type(your_step) == str:
            print()
            print(your_step)
            break
            
        print(your_step[0])
        print()
        print(f'{name_of_player}, your next action is:\n' + '\n'.join(list(your_step[1].keys())))
        your_step = your_step[1]  
