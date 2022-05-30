def multiply(a, b):
    return a*b

def myitmes():
    return {
        'NRW':'Duesseldorf',
        'BWU':'Stuttgart',
        'Bavaria':'Munich',
        'Hessen':'Frankfurt'
    }

def mylists():
    return ['Batman', 'Superman', 'The Flash', 'Wonder Woman']

if __name__=="__main__":
    print ("call multiplier")
    print (multiply(2,3))
    
    print('call dictionary')
    
    states = myitmes()
    print("loop through items")
    for item in states.items():
        print(item)
    
    print("loop through keys")
    for key in states.keys():
        print(key)
        
    print("loop through values")
    for value in states.values():
        print(value)
    
    print("loop through key and value")
    for key, value in states.items():
        print(key,'->',value)


    superheroes = mylists()
    superheroes.append('Green Lantern')
    
    for hero in superheroes:
        print(hero)
    
    