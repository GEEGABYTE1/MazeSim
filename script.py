from bfs import bfs 
from a_star import a_star
from nodes import objects
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
            final_obj_object = self.star_object_finder()
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
                prompt_object = self.prompt_object_finder(prompt)
                a_star_sim = a_star(prompt_object, final_obj_object)

    
    def prompt_object_finder(self, prompt):
        prompt_obj = None 
        for vertex in objects:
            if vertex.value == prompt:
                prompt_obj = vertex 
                break 

        return prompt_obj

    def star_object_finder(self):
        final_obj = None 
        for vertex in objects:
            if vertex.value == '*':
                final_obj = vertex 
                break  

        return final_obj           


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