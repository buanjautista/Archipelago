from typing import TypedDict

class IncludeOptions(TypedDict, total=False):
    trade: bool
    shop: bool
    arena: bool
    chest: bool
    quest: bool
    botanics: bool
