""" Classes for items that appear in the map (except the rover).
    Each class has a getKind() method which returns what sort of 
    item it is as a String.
"""

class SparePart:
    def __init__(self, imageName):
        """Initializes a SparePart from an imageName

        Args:
            imageName (str): the path at which the image is found
        """
        # TODO Part 1
        # Make the following instance fields
        # 1) The image name
        self._imageName = imageName

    def getImageName(self):
        """returns the image's name/path

        Returns:
            str: the filepath for the image
        """
        # TODO Part 1
        # return the image name including the imagepath if any
        return self._imageName
    
    def getName(self):
        return self.getImageName()[len("./Img/"):-4]

    def getKind(self):
        """returns the kind of object this is

        Returns:
            str: part
        """
        return "part"


class ShipPiece:
    def __init__(self, imageName, status):
        """initualizes a ShipPiece from a filepath and part status

        Args:
            imageName (str): the filepath for the image
            status (str): "broken" or "working
        """
        self.status = status
        self._imageName = imageName

    def getImageName(self):
        """returns the image's name/path

        Returns:
            str: the filepath for the image
        """
        # TODO Part 1
        # return the image name including the imagepath if any
        return self._imageName if self.status == "working" else "./Img/"+self.getName()+"_broken.ppm"

    def getKind(self):
        """returns the kind of object this is

        Returns:
            str: ship
        """
        return "ship"
    
    def getStatus(self):
        # TODO Part 1
        # return "broken" or "working"
        return self.status
    
    def setStatus(self, s):
        self.status = s
    
    def getName(self):
        return self._imageName[6:1+min(self._imageName[1:].find("."), self._imageName[1:].find("_")) if self._imageName[1:].find("_") != -1 else self._imageName[1:].find(".")]
    


class Portal:

    def __init__(self, planet = None, location = [0,0]):
        """Initializes a Portal from an imageName

        Args:
            imageName (str): the path at which the image is found
        """
        # TODO Part 1
        # Make the following instance fields
        # 1) The current image name ("./Img/portal.ppm" or "./Img/portal_flashing.ppm")
        self._imageName = "./Img/portal.ppm"
        
        # TODO Part 2
        # Make the following instance fields
        self.planet = planet
        self.location  = location
        self.otherPortal = None
        self.hash = hash(planet)+hash(location[0])+hash(location[1])
        # 1) The map that this portal is on
        # 2) The location [row, column] of this portal on this map
        # 3) The portal at the other end of the wormhole (None if it isn't known yet)


    
    def getImageName(self):
        """returns the image's name/path

        Returns:
            str: the filepath for the image
        """
        # TODO Part 1
        # return the image name including the imagepath if any
        return self._imageName

    def getKind(self):
        """returns the kind of object this is

        Returns:
            str: portal
        """
        return "portal"
    
    def isConnected(self):
        """ Is this portal connected to another portal? True/False """
        print(not self.otherPortal is None)
        return not self.otherPortal is None
    
    def setLocation(self, location):
        """sets location to parameter"""
        self.location = location
    
    def getLocation(self):
        """Returns location"""
        return self.location
    
    def setOtherPortal(self, portal):
        """sets otherPortal to parameter"""
        self.otherPortal = portal
    
    def getOtherPortal(self):
        """Returns otherPortal"""
        return self.otherPortal
    
    def getPlanet(self):
        return self.planet
    
    def setPlanet(self, portal):
        """sets otherPortal to parameter"""
        self.planet = portal
    
    def __str__(self) -> str:
        return str(self.planet.starting)
