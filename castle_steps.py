import json

with open("/Users/Ekaterina/Desktop/mypr/castle.json") as data:
    
    castle_quest_data = list(json.load(data))
    print(castle_quest_data[0])
    print('Your actions:\n' + '\n'.join(list(castle_quest_data[1].keys())))
    your_step = castle_quest_data[1]
    
    for i in range(5):
        
        step = input()
        your_step = your_step[step]
        
        if your_step == "return to enter":
            your_step = castle_quest_data[1]
            print(castle_quest_data[0])
            print('Your actions:\n' + '\n'.join(list(your_step[1].keys())))
            continue
            
        if type(your_step) == str:
            print(your_step)
            break
            
        print(your_step[0])
        print('Your actions:\n' + '\n'.join(list(your_step[1].keys())))
        your_step = your_step[1]  
