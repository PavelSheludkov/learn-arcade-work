class Monster():

    def __init__(self, monster_name, monster_health):
        self.name = monster_name
        self.health = monster_health

    def decrease_health(self, decrease_amount):
        self.health = self.health - decrease_amount
        if self.health < 0:
            print("Monster " + self.name + " is DEAD")

def main():
    my_monster = Monster("Diablo", 90)
    my_monster.decrease_health(int(input("For how much? ")))

main()