import nats
from nats.aio.client import Client as NATSClient
from nats.js import JetStreamContext


async def connect_to_nats(servers: list[str]) -> tuple[NATSClient, JetStreamContext]:
    nc = await nats.connect(servers)
    js = nc.jetstream()
    return nc, js
