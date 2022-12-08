from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    is_dungeon_master: bool
    hit_points: int = field(default=1)
    experience: int = field(default=0)
    spell_points: dict = field(default_factory=dict)
    items: list = field(default_factory=list)
    spells: list = field(default_factory=list)
    features: list = field(default_factory=list)
    
    @property
    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item


@dataclass
class Item:
    name: str
    description: str
    value: int
    quantity: int = field(default=1)


@dataclass
class Spell:
    name: str
    casting_time: int
    range: int
    duration: int
    description: str
    components: tuple = field(default_factory=tuple)


@dataclass
class Feature:
    name: str
    description: str

