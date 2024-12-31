class Task:
    def __init__(self, name) -> None:
        self.name = name
        self.components = {}

    def addComponent(self, number, componentName):
        self.components[componentName] = number + (0 if not (componentName in self.components.keys()) else self.components[componentName])
    def getComponents(self):
        return self.components
    def getName(self):
        return self.name
    def __str__(self) -> str:
        return str(self.name) +" "+str(self.components)
    