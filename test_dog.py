import dog
import pack
my_dog = dog.Dog("Gaspar")
print(my_dog.trick_list)
my_dog.print_name()
my_dog.sit()
my_dog.roll()
print(my_dog.trick_list)
my_dog.lay_down()
my_dog.print_trick_list()
my_pack = pack.Pack(my_dog)
print(my_pack.get_leader_name())
print(my_pack.print_pack())