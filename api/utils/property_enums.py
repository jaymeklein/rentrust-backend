import enum


class PropertyTypes(enum.Enum):
    # Residential
    HOUSE = 1
    APARTMENT = 2
    CONDO = 3
    TOWNHOUSE = 4
    VILLA = 5
    BUNGALOW = 6
    STUDIO = 7
    LOFT = 8
    DUPLEX = 9
    TRIPLEX = 10
    PENTHOUSE = 11
    FARMHOUSE = 12
    CABIN = 13
    COTTAGE = 14
    MANSION = 15
    RANCH = 16

    # Non-Residential
    SHED = 17
    GARAGE = 18
    BARN = 19
    WAREHOUSE = 20
    WORKSHOP = 21
    GREENHOUSE = 22
    POOL_HOUSE = 23
    GUEST_HOUSE = 24
    BOATHOUSE = 25
    CARPORT = 26
    SILO = 27
    STABLE = 28
    GUARD_HOUSE = 29
    OTHER = 30


class PropertyStatuses(enum.Enum):
    FOR_RENT = 1
    OCCUPIED = 2
    UNDER_MAINTENANCE = 3
    FOR_SALE = 4
    SOLD = 5
    PENDING = 6
    OFF_MARKET = 7
    DELISTED = 8
    VACANT = 9
    RENTED = 10
    LEASED = 11
    EXPIRED = 12
    HOLD = 13
    ARCHIVED = 14
    DRAFT = 15
    INACTIVE = 16
    RENOVATION = 17
    PRE_MARKET = 18
    RESERVED = 19
    AUCTION = 20
