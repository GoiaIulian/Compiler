class Transition:
    def __init__(self, s, a, n):
        self.state = s
        self.alphabet = a
        self.next = n

    def __str__(self):
        return self.state + " " + str(self.alphabet) + " " + self.next
