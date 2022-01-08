from .Scene import Scene
from .Vector import Vector2
from .Loader import read
import pygame
from sys import modules
import time



class Screen():
    def __init__(self, filepath:str) -> None:
        self.attributesJson = read(filepath)
        # reading the data inside the screen file
        self.dimensions = Vector2(int(self.attributesJson["dimensions"]["x"]), int(self.attributesJson["dimensions"]["y"]))
        # getting the dimensions of the screen as a Vector2 
        self.title = self.attributesJson["title"]
        # getting the title of the window 
        self.screen = pygame.display.set_mode((self.dimensions.x, self.dimensions.y))
        # setting up the screen 
        pygame.display.set_caption(self.title)
        # setting the title of the window 
        self.running = True
        # true when the screen is running 
        self.currentScene = Scene(self.attributesJson["defaultScene"])
        self.run()
        # running the window  

    def run(self):
        previousFrame = time.time()
        # tracking the time of the previous frame

        modules["__main__"].start(self, time.time()-previousFrame, pygame)
        # running the start function

        while self.running:
            pygame.display.update()
            deltaTime = (time.time() - previousFrame) * 60
            # updating the deltaTime 
            previousFrame = time.time()
            # updating the previous frame 
            
            modules["__main__"].main(self, deltaTime, pygame)
            # running the main function 
            """
            The main function has to be imported by the __main__ file in order to run custom scripts
            """

            if self.currentScene != None:
                self.currentScene.run(self, deltaTime, pygame)
            # running the current scene 


            for event in pygame.event.get():
                """
                Event Listener
                """
                if event.type == pygame.QUIT:
                    self.running = False
                    # quitting the game when 'x' is pressed 

        pygame.quit()
        # quitting the game 

    def loadScene(self, scene:Scene):
        self.currentScene = scene