from users.user import User

class RegularUser(User):
    def user_type(self):
        return "Regular"