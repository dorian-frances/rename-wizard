import enum


class CasingTypeEnum(str, enum.Enum):
    snake_case = "snake_case"
    kebab_case = "kebab_case"
    camel_case = "camel_case"
    pascal_case = "pascal_case"
