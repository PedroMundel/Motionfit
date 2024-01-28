from enum import Enum

class MuscleRegion(Enum):
    SUPERIOR_CORPO = "Superior do Corpo" # upper body
    INFERIOR_CORPO = "Inferior do Corpo" # lower body
    CORE = "Núcleo" # core

class Muscle:
    def __init__(self, name, region):
        self.name = name
        self.region = MuscleRegion(region)
