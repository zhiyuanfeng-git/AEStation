from .abstract_user import AbstractUserModel

class UserModel(AbstractUserModel):
    """
    Email and password are required. Other fields are optional.
    """