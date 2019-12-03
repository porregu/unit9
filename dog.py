class Dog:

    def __init__(self, dogs_name):
        self.dogs_name = dogs_name
        self.trick_list = []
        if self.trick_list == 0:
            "the dog didnt realize any trick"
        elif self.trick_list == 1:
            "the dog realize this tricks "
        for x in self.trick_list:
            self.trick_list.append(self.trick_list)


    def get_name(self):
        return self.dogs_name

    def print_name(self):
        print(self.dogs_name)

    def sit(self):
        print(self.dogs_name + " sits" )
        self.trick_list.append("sits")

    def lay_down(self):
        print(self.dogs_name + " lay down" )
        self.trick_list.append("lay down")

    def roll(self):
        print(self.dogs_name + " rolls")
        self.trick_list.append("roll")

