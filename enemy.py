class Enemy(object):

    def __init__(self, name="enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._base_hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        remaining_damage = damage
        while remaining_damage > 0:
            if remaining_points > 0:
                self._hit_points = remaining_points
                remaining_damage -= self._hit_points
            else:
                remaining_damage -= self._hit_points
                self._take_lives()

        if self._alive:
            print(f"{self._name} took {damage} points of damage and have {self._lives}"
                  f" lives left and {self._hit_points} hit points left.")
        else:
            print(f"{self._name} took {damage} points of damage and lost all their lives and died")

    def _take_lives(self):
        remaining_lives = self._lives - 1
        if remaining_lives > 0:
            self._lives -= 1
            self._hit_points = self._base_hit_points
            print(f"I lost a life and have {self._lives} remaining.")
        else:
            self._lives = 0
            self._hit_points = 0
            self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23) # This works
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)  # This also works
        super().__init__(name=name, lives=1, hit_points=23)  # This also also works but use this!

    def grunt(self):
        print(f"Me {self._name}. {self._name} stomp you")


class Vampire(Enemy):

    def __init__(self, name):
        # self._hit_points = hit_points
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        import random
        if random.randint(1, 3) == 3:
            print("{0._name} dodges".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)
