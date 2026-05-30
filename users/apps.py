<<<<<<< HEAD
from django.apps import AppConfig

class UsersConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'users'

    def ready(self):

=======
from django.apps import AppConfig

class UsersConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'users'

    def ready(self):

>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
        import users.signals