from model.user_request import UserRequest


class User(UserRequest):
    id: int
    is_registered: bool
