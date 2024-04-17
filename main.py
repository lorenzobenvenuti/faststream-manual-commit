
from typing import Any, Dict
from faststream import FastStream
from faststream.kafka import KafkaBroker
from faststream.kafka.annotations import (
    KafkaMessage,
    Logger
)

broker = KafkaBroker("localhost:9093")
app = FastStream(broker)

@broker.subscriber("source-topic", group_id="foo", auto_commit=False)
async def async_subscriber(body: Dict[str,Any], logger: Logger, msg: KafkaMessage):
    logger.info(body)
    await msg.nack()
