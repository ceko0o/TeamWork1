class Spell:
    def __init__(self,name, damage, required_mana):
        self.damage = damage
        self.name = name
        self.required_mana = required_mana

class Weapon:
    def __init__(self,name, damage):
        self.damage = damage
        self.name = name

class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def __equip__(self, weapon):
        self.weapon = weapon

    def __learn__(self, spell):
        self.spell = spell

    def __known_as__(self):
        return "{} the {}".format(self.name, self.title)

    def __is_alive__(self):
        return self.health > 0

    def __get_health__(self):
        return self.health

    def __get_mana__(self):
        return self.mana

    def __can_cast__(self):
        if self.spell.required_mana > self.mana:
            return False
        else:
            return True

    def __take_damage__(self,damage_points):
        reduced_health = self.health - damage_points
        if reduced_health < 0:
            self.health = 0
        else:
            self.health = reduced_health

    def __take_healing__(self,healing_points):
        new_healh = self.health + healing_points

        if is_alive():
            if new_health > 100:
                self.health = 100
            else:
                self.health = new_health
            return True
        else:
            return False

    def __take_mana__(self, mana_points = 0):
        new_mana = self.mana + mana_points + mana_regeneration_rate

        if new_mana > 100:
            self.mana = 100
        else:
            self.mana = new_mana


    def __attack__(self, by=""):
        if by == "magic":
            return self.spell.damage
        elif by == "weapon":
            return self.weapon.damage
        else:
            return 0

w = Weapon("sabq", 10)
s = Spell("sab",25, 20)
h = Hero("ivan", "kralq", 100, 100, 2)


