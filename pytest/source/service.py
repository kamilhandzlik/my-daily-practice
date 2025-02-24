database = {1: "Alicja", 2: "Weronika", 3: "Oliwia"}


def get_user_from_db(user_id):
    return database.get(user_id)
