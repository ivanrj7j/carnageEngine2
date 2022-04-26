from .Object_ import Object_
from .Loader import read


class Scene:
    def __init__(self, filepath:str) -> None:
        self.attributesJson = read(filepath)
        # reading the attributes 
        self.name = self.attributesJson["Name"]
        self.objects = self.attributesJson["Objects"]
        self.defaultBackground = (self.attributesJson["defaultBG"][0], self.attributesJson["defaultBG"][1], self.attributesJson["defaultBG"][2])
        self.attributePath = list(filepath.split("/")).pop(0)
        attrbpath = ""
        for i in range(len(self.attributePath)):
            if i == 0:
                attrbpath += self.attributePath[i]
            elif i > 0:
                attrbpath += "/"
                attrbpath += self.attributePath[i]
        self.attributePath = attrbpath
        print("Attributes", self.attributePath)

    def run(self, screen, deltaTime:float, pygame):
        screen.screen.fill(self.defaultBackground)
        if len(self.objects) > 0:
            for obj in self.objects:
                Object_(screen, deltaTime, pygame, read(self.attributePath+obj))
                # running each and every object in the scene 