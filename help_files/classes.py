from marshmallow_dataclass import dataclass

from skills import Skill, HardShot, FuryPunch
@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.9,
    stamina=1.0,
    armor=1.2,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)

HalflingClass = UnitClass(
    name="Полурослик",
    max_health=40.0,
    max_stamina=25.0,
    attack=2.0,
    stamina=1.2,
    armor=2.0,
    skill=HardShot()
)

ElfClass = UnitClass(
    name="Эльф",
    max_health=60.0,
    max_stamina=30.0,
    attack=1.3,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    ElfClass.name: ElfClass,
    HalflingClass.name: HalflingClass
}