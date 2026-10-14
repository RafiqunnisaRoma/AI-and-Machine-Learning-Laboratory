# Simple Reflex Vacuum Agent
def vaccum_agent(location, env):
    if env["A"]=='Clean' and env["B"]=='Clean':
        return "NoOp"
    if env [location]=='Dirty':
        return "Suck"
    if location =="A":
        return "Right"
    else:
        return "Left"

environment= {"A":"Dirty","B":"Clean"}
location= "B"
print('\nInitial State:',location)
print('\nInitial Environment:',environment)
print('\n Percept- Action Pairs :')
step=1
while True:
    percept= (location,environment[location])
    action=vaccum_agent(location,environment)
    print(f"Step: {step} Percept: {percept} Action: {action}")
    if action == "NoOp":
        break
    elif action == "Suck":
        environment[location]="Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"
    step +=1
print ('\nFInal environment: ',environment)
print('\nFinal location : ',location)
print('Agent stopped')
