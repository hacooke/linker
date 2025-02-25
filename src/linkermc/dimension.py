import enum

class Dimension(enum.Enum):
    overworld = 1
    nether = 2

    @classmethod
    def validate(cls, obj, context):
        if not isinstance(obj, cls):
            raise ValueError(f"Invalid dimension in {context}")
