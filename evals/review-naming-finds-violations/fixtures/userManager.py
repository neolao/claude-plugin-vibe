class UserManager:
    def __init__(self, users):
        self.users = users

    def checkUser(self, user_id):
        user = self.users.get(user_id)
        return user is not None and user["status"] == "active"

    def process(self, user_id, payload):
        if not self.checkUser(user_id):
            raise ValueError("invalid user")
        with open(f"/data/{user_id}.json", "w") as f:
            f.write(str(payload))
