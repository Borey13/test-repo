import random


class Warrior:
    def __init__(self, health=100, endurance=100, armor=100):
        self.health = health
        self.endurance = endurance
        self.armor = armor

    def defend_with_armor(self):
        self.health -= random.randint(0, 20)
        self.armor -= random.randint(0, 10)
        if self.armor < 0:
            self.armor = 0
        if self.health < 10:
            self.health = 10

    def defend_without_armor(self):
        self.health -= random.randint(10, 30)
        if self.health < 10:
            self.health = 10

    def two_attack(self):
        self.health -= random.randint(10, 30)
        self.endurance -= 10
        if self.endurance < 0:
            self.endurance = 0
        if self.health < 10:
            self.health = 10

    def one_attack(self):
        self.endurance -= 10
        if self.endurance < 0:
            self.endurance = 0

    def light_attack(self):
        self.health -= random.randint(0, 10)
        if self.health < 10:
            self.health = 10

    @staticmethod
    def get_characteristic():
        print(f'У Макса осталось {maxim.health} hp здоровья, '
              f'{maxim.endurance} pt выносливости, {maxim.armor} pt брони\n'
              f'У Олега осталось {oleg.health} hp здоровья, '
              f'{oleg.endurance} pt выносливости, {oleg.armor} pt брони\n')

    @staticmethod
    def war():
        return random.randint(0, 1)

    @staticmethod
    def life_or_death():
        while True:
            answer = input('Добить проигравшего??? \n')
            if answer.lower() == 'да':
                print('Проигравший погиб...')
                break
            elif answer.lower() == 'нет':
                print('Проигравший будет жить!!!')
                break


oleg = Warrior()
maxim = Warrior()

while oleg.health >= 10 and maxim.health >= 10:
    if oleg.health == 10:
        print('Победил Максим!!!!\n')
        Warrior.life_or_death()
        break
    if maxim.health == 10:
        print('Победил Олег!!!!\n')
        Warrior.life_or_death()
        break
    oleg.war()
    maxim.war()
    if oleg.war() == 1 and maxim.war() == 1:
        if oleg.endurance == 0:
            maxim.light_attack()
        else:
            maxim.two_attack()
        if maxim.endurance == 0:
            oleg.light_attack()
        else:
            oleg.two_attack()
        print('Атаковали оба!')
        Warrior.get_characteristic()
    elif oleg.war() == 1 and maxim.war() == 0:
        if oleg.endurance == 0:
            maxim.light_attack()
        else:
            oleg.one_attack()
            if maxim.armor == 0:
                maxim.defend_without_armor()
            else:
                maxim.defend_with_armor()
        print('Атаковал Олег!')
        Warrior.get_characteristic()
    elif oleg.war() == 0 and maxim.war() == 1:
        if maxim.endurance == 0:
            oleg.light_attack()
        else:
            maxim.one_attack()
            if oleg.armor == 0:
                oleg.defend_without_armor()
            else:
                oleg.defend_with_armor()
        print('Атаковал Максим!')
        Warrior.get_characteristic()
    else:
        print('Оба в защите!!!\n')
