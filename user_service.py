class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class UserService:
    def get_user_message(self, user):
        if user.age < 18:
            return "User is a minor"
        else:
            return "User is an adult"

u = User("Rohit", 25)
service = UserService()
print(service.get_user_message(u))
