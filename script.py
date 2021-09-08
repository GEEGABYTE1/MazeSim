from bfs import bfs 
import time

class Search:

    def __init__(self):
        self.intro()
        playing = True 
        while playing:
            print('\n')
            prompt = str(input('Please input a letter or node you would like to start the search from: '))
            prompt = prompt.strip(" ")
            prompt = prompt.lower()
            check = bfs(prompt, '*')
            if check == None:
                time.sleep(0.4)
                print("That letter does not seem valid")
                time.sleep(0.4)
                print("Please type a letter from 'a' - 'h'")
            else:
                time.sleep(0.4)
                print("Your letter is valid...")
                time.sleep(0.2)
                print("Starting the Search Simulation now...")
                


    def intro(self):
        print('-'*50)
        print('-'*50)
        print('-'*50 + '\n')
        print('\n')
        print("------- Find '*' ! An A-Star Simulation -------")
        print('\n')
        print('-'*50)
        print('-'*50)
        print('-'*50)






search = Search()

print(search)