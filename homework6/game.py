import json
import random

class Persongame(object):
    def __init__(self, word):
        self.word = word

    def replaceword(self):
        check = self.word
        i = 0
        answer = ''
        while i < len(check):
            answer += '_'
            i += 1
        return answer

    def print_viselica(self, mistake):

        HANGMAN = (
            """
            ______
            |     |
            |
            |
            |
            |
            |
            """,
            """
            ______
            |     |
            |     0
            |
            |
            |
            |
            """,
            """
            ______
            |    |
            |    0 |
            | 
            |
            |
            |
            """,
            """
            ______
            |     |
            |     0 |
            |     | 
            | 
            |
            |
            """,
            """
            _______
            |     |
            |     0 |
            |     |
            |    |
            |
            |
            """
,
            """
            _______
            |     |
            |     0 |
            |     |
            |    | |
            |
            |
            """
        )
        return HANGMAN[mistake]


    def is_finished_game(self,check):
        if check == self.word:
            return True

    def makesteps(self, step, answer):
        if step in self.word:
            c = 0
            ans = ''
            while c < len(self.word):
                if step is self.word[c] and answer[c] == '_':
                    ans += step
                elif  step is not self.word[c] and answer[c] != '_':
                    ans += answer[c]
                else:
                    ans += '_'
                c +=1
            return ans
        else:
            return answer

class Computergame(Persongame):
    def is_finished_game(self,check):
        if check == self.word:
            return True



class MainClass(object):
    def random_word(self):
        words = []
        path = 'words.json'
        with open(path, 'r') as f:
            data = json.loads(f.read())
        for i in data['words']['word']:
            words.append(i['value'])
        return random.choice(words)

    def main(self, type):

        if type is 'player':
            s = input('Input word:')
            result = Persongame(s)
        else:
            main = MainClass()
            s = main.random_word()
            result = Computergame(s)
        mistake = 0
        field = result.replaceword()
        while not result.is_finished_game(field) and mistake < 5:
            step = input('Input letter:')
            if field == result.makesteps(step, field):
                mistake += 1
                print('No letter')
                print(result.print_viselica(mistake))
            else:
                field = result.makesteps(step, field)

            print(field)
        if mistake < 5:
            print('You win')
        else:
            print('You lose', result.word)


def main():
    type = int(input('Input type 1 or 2:'))
    game = MainClass()
    if type is 1:

        game.main('player')
    elif type is 2:
        game.main('computer')

main()

