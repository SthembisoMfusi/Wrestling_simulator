class Wrestler:
    statList = ["name","gender", "strength","speed", "agility","health", "power", "grapple", "stamina"] 
    genders = ['male','female']
    def __init__(self,name:str, gender:str,strength:int,speed:int,agility:int,health:int,power:int,grapple:int,stamina:int):
        self.name = name
        self.gender = gender
        self.strength = strength # how much strength they have to use to grapple and escape grapples
        self.speed = speed# how fast they move
        self.agility = agility # how well they can perform reversals, how confident they are at using the top rope 
        self.health = health# how much damage they can sustain
        self.power = power# how strong their attacks are
        self.grapple = grapple # how well they know how to grapple
        self.stamina = stamina# how long they can perform a combination of abilities within a short time period
        def __setattr__(self,name,value):
            match name:
                case "name":
                    if (not isinstance(value,str)):
                        raise ValueError("name must be a string value")
                case "gender":
                    if (not isinstance(value,str)) or value not in self.genders:
                        raise ValueError("gender must be a str value and should be either 'male' or 'female' ")
                case "strength":
                    if (not isinstance(value,int)) or value < 40 or value >100:
                        raise ValueError("Strength value is invalid, it should be between 40 and 100")
                case "speed":
                    if (not isinstance(value,int)) or value < 30 or value >100:
                        raise ValueError("Speed value is invalid, it should be between 30 and 100")
                case "agility":
                    if (not isinstance(value,int)) or value < 10 or value >100:
                        raise ValueError("Agility value is invalid, it should be between 10 and 100")
                case "health":
                    if (not isinstance(value,int)) or value < 80 or value >200:
                        raise ValueError("Health value is invalid, it should be between 80 and 200")
                case "power":
                    if (not isinstance(value,int)) or value < 50 or value >100:
                        raise ValueError("Power value is invalid, it should be between 50 and 100")
                case "grapple":
                    if (not isinstance(value,int)) or value < 1 or value >20:
                        raise ValueError("Grapple value is invalid, it should be between 1 and 20")
                case "stamina":
                    if (not isinstance(value,int)) or value < 30 or value >100:
                        raise ValueError("Stamina value is invalid, it should be between 30 and 100")
            if name not in self.statList:
                raise ValueError(f"only these stats can be changed : {self.statList}")
            self.__dict__[name] = value
    def __str__(self):
        return f"name: {self.name}, gender: {self.gender}, strength: {self.strength},speed: {self.speed},agility: {self.agility}, health: {self.health},power: {self.power}, grapple: {self.grapple}, stamina: {self.stamina}"

    def __repr__(self):
        return str(self)
p = Wrestler('John Cena',"male",60,70,48,167,54,7,78)
print(p)