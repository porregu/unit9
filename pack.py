class Pack:
    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0
        self.members.append(self.dog)

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()


    def add_member(self, dog):
        self.members.append(dog)

    def print_pack(self, dog):
        dog1 = "sport"
        dog2 = "fidu"
        dog3 = "rover"
        self.members.append(dog1, dog, dog2, dog3)

    def new_leader(self):


