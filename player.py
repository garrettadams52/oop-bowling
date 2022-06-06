import random

class Player:
    def __init__(self, player, scores = None):
        self.player = player
        self.scores = []
    
    def calc(self):
        lst = [x for xs in self.scores for x in xs]
        print(lst)
        for i, x in enumerate(lst):
            if x == 'spare':
                if len(lst)-1 == i:
                    check = lst.append(random.randint(0,10))
                    if check == 10:
                        lst.append('strike')
                if type(lst[i+1]) == int:
                    lst[i] = lst[i+1]
                else:
                    lst[i] = 10
                i = 0
            elif x == 'strike':
                if type(lst[i+1]) == int and type(lst[i+2]) == int:
                    lst[i] = lst[i+1] + lst[i+2] 
                elif type(lst[i+1]) != int and type(lst[i+2]) == int:
                    lst[i] = 10 + lst[i+2] 
                elif type(lst[i+1]) == int and type(lst[i+2]) != int:
                    lst[i] = 10 + lst[i+1] 
                elif type(lst[i+1]) != int and type(lst[i+2]) != int:
                    lst[i] = 10 + 10

                i = 0

        print(lst)
        ans = sum(lst)
        return ans