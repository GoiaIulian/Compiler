from ve.Utils.Transition import Transition


class Repo:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.final_states = []
        self.initial_state = ""

    def initialize(self):
        l = 1
        file = open("FA.txt", "r")
        for line in file:
            if line[0] == "/":
                continue
            else:
                if (l == 1) or (l == 2) or (l == 3):
                    l += 1
                    a = line.strip('\n').split(",")
                    for el in a:
                        self.alphabet.append(el)
                elif l == 4:
                    l += 1
                    a = line.strip('\n').split(",")
                    for el in a:
                        self.states.append(el)
                elif l == 5:
                    l += 1
                    self.initial_state = line
                elif l == 6:
                    l += 1
                    a = line.strip('\n').split(",")
                    for el in a:
                        self.final_states.append(el)
                else:
                    a = line.strip('\n').split("=")
                    nex = a[1]
                    a[0] = a[0].replace('(', '')
                    a[0] = a[0].replace(')', '')
                    b = a[0].split(",")
                    self.transitions.append(Transition(b[0], b[1:], nex))
        file.close()

    def write(self):
        print(self.alphabet)
        print(self.states)
        print(self.initial_state)
        print(self.final_states)
        for el in self.transitions:
            print(el)
