

class UserM():

    users_m = []

    def check_user(self, user):
        if user in self.users_m:
            return True
        return False
    
    def add_user(self, user):
        self.users_m.append(user)
        if len(self.users_m) > 100:
            self.users_m.pop(0)

