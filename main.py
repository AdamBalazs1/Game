from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother_troll = Troll("Urg")
print(brother_troll)

# ugly_troll.grunt()
# another_troll.grunt()
# brother_troll.grunt()

ugly_troll.take_damage(23)
print(ugly_troll)

another_troll.take_damage(10)
print(another_troll)

first_vampire = Vampire("Sneaky")
print(first_vampire)

second_vampire = Vampire("Sneakier")
print(second_vampire)

while first_vampire._alive:
    first_vampire.take_damage(2)

alucard = VampireKing("Alucard")
print(alucard)

# while alucard._alive:
#     alucard.take_damage(4)
