# Deterministic Finite Automata

def dfa(machine, exp):
    state = 0
    

    for i in exp:
        ismachine = False
        if(len(machine[state]) == 1 and "end" in machine[state]):
            return False
        for j in machine[state]:
            if(i in j[1]):
                print(f"{i} -> {j[0]}")
                ismachine = True
                state = j[0]
        if(not ismachine):
            print(f"{i} -> ?")
            return False

    if(ismachine and ("end" in machine[state])):
        return True
    else:
        return False
