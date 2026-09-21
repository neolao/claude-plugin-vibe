class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):
        return self.db.get(user_id)

    def deactivate_user(self, user_id):
        user = self.db.get(user_id)
        if user is None:
            raise ValueError("user not found")
        user["active"] = False
        return user
