from django.db import models
from django.core.exceptions import ValidationError
from .dataclasses import TodoData


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ---------- VALIDATION ----------
    @staticmethod
    def validate(data: TodoData):
        if not data.title:
            raise ValidationError("Title is required")

        if len(data.title) > 200:
            raise ValidationError("Title must be <= 200 characters")

        if not data.description:
            raise ValidationError("Description is required")

    # ---------- CREATE ----------
    @classmethod
    def create_todo(cls, data: TodoData):
        cls.validate(data)
        return cls.objects.create(
            title=data.title,
            description=data.description,
            is_completed=data.is_completed,
        )

    # ---------- UPDATE ----------
    def update_todo(self, data: TodoData):
        self.validate(data)
        self.title = data.title
        self.description = data.description
        self.is_completed = data.is_completed
        self.save()
        return self

    def __str__(self):
        return self.title
