"""Django standard Apps file."""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """CoreConfig function."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
