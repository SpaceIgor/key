from django.core.exceptions import ValidationError


def validate_non_negative_price(value):
    if value < 0:
        raise ValidationError("Ціна не може бути від'ємною.")


def validate_category_nesting_level(value):
    if value and value.level > 10:
        raise ValidationError("Максимальний рівень вкладеності категорій - 10.")
