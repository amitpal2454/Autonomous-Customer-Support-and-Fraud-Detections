# Auto-generated
def to_str(value):
    if value is None:
        return None
    if hasattr(value, "value"):   # Enum case
        return value.value
    return value                 # already string