from dataclasses import dataclass
from opt.obj.accessType import AccessType

@dataclass
class MemoryAccess:
    address: int
    operation: AccessType
    value: int | None