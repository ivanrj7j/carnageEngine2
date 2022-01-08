from .Loader import read


class Scene:
    def __init__(self, filepath:str) -> None:
        self.attributesJson = read(filepath)
        # reading the attributes 
        self.name = self.attributesJson["Name"]
        self.objects = self.attributesJson["Objects"]
        self.defaultBackground = (self.attributesJson["defaultBG"][0], self.attributesJson["defaultBG"][1], self.attributesJson["defaultBG"][2])

    def run(self, screen, deltaTime:float, pygame):
        screen.screen.fill(self.defaultBackground)
        if len(self.objects) > 0:
            for obj in self.objects:
                obj.run(screen, deltaTime, pygame)
                # running each and every object in the scene 