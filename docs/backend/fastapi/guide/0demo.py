from enum import Enum, StrEnum


class STATUS(Enum):
    PENDING = "pending"
    RESOLVED = "resolved"
    REJECTED = "rejected"


print(STATUS.PENDING)
print(STATUS.PENDING.name)
print(STATUS.PENDING.value)
print('--------------------------------')
print(STATUS["PENDING"].value)
print(STATUS["PENDING"].name)