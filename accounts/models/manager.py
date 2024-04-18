from django.contrib.auth.models import BaseUserManager

class UserModelManager(BaseUserManager):
    """
    Customize the user model manager
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email address, password
        """

        if not email:
            raise ValueError("The given email must be set.")
        
        if not password:
            raise ValueError("The password must be set.")
        
        email = self.normalize_email(email)
        userModel = self.model(email=email, **extra_fields)
        userModel.set_password(password)
        userModel.save(using=self._db)
        return userModel
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})