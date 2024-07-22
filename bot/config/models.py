from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class AioRedis:
    host: str
    port: int


@dataclass
class Geoapify:
    token: str

@dataclass
class Nats:
    servers: list[str]

@dataclass
class DbConfig:
    dsn: str
