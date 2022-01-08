import json
from . import Screen

class Loader:
    def __init__(self, filePath:str) -> None:
        typeNotations = {"0": Screen.Screen,"1": "Camera","2": "Entity","3": "UI","-1": "Notations"}
        type_ = typeNotations[str(read(filePath)["type"])]
        type_(filePath)

    
def read(filepath:str):
    with open(filepath, "r") as file:
        return json.loads(file.read())