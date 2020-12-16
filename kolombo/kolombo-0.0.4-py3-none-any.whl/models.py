from typing import List

from ormar import Boolean, Integer, Model, String

from kolombo.resources import database, metadata


class Domain(Model):
    class Meta:
        tablename = "domains"
        metadata = metadata
        database = database

    id: int = Integer(primary_key=True)
    #: Domain that is specified in DNS MX record, like mail.example.org
    mx: str = String(max_length=255)
    #: Domain that is actually used in email, like example.org
    actual: str = String(max_length=255)
    #: Whether this domain is active
    active: bool = Boolean(default=True)

    @classmethod
    async def all_active(cls) -> List["Domain"]:
        return await cls.objects.filter(active=True).all()  # type: ignore[return-value]


class User(Model):
    class Meta:
        tablename = "users"
        metadata = metadata
        database = database

    id: int = Integer(primary_key=True)
    #: Domain that user is associated with (part of email after @)
    domain: str = String(max_length=255)
    #: Email like user@domain.org
    email: str = String(max_length=255, unique=True)
    #: Password will be 32 bytes hash base64 encoded, so 44 symbols (+1 just in case)
    password: str = String(max_length=45)
    #: Whether this user is active
    active: bool = Boolean(default=True)

    @classmethod
    async def all_active(cls) -> List["User"]:
        return await cls.objects.filter(active=True).all()  # type: ignore[return-value]
