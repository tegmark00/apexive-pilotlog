from rest_framework.exceptions import ValidationError


class FileExtensionValidator:
    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions

    def __call__(self, value):
        if value.name.split(".")[-1] not in self.allowed_extensions:
            raise ValidationError(
                f"File extension not allowed."
                f"Allowed extensions are {self.allowed_extensions}"
            )
        return value
