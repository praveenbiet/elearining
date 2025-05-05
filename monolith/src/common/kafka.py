from typing import Any, Dict, Optional

from confluent_kafka import Consumer, Producer
from pydantic import BaseModel

from .config import get_settings
from .logger import get_logger

settings = get_settings()
logger = get_logger(__name__)


class KafkaProducer:
    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
        })

    def produce(self, topic: str, key: str, value: Dict[str, Any]) -> None:
        """Produce message to Kafka topic."""
        try:
            self.producer.produce(
                topic=f"{settings.KAFKA_TOPIC_PREFIX}.{topic}",
                key=key,
                value=str(value),
                callback=self._delivery_report,
            )
            self.producer.flush()
        except Exception as e:
            logger.error(
                "Failed to produce message",
                extra={
                    "topic": topic,
                    "key": key,
                    "error": str(e),
                },
            )
            raise

    @staticmethod
    def _delivery_report(err, msg):
        """Handle delivery report."""
        if err is not None:
            logger.error(
                "Message delivery failed",
                extra={
                    "error": str(err),
                },
            )
        else:
            logger.debug(
                "Message delivered",
                extra={
                    "topic": msg.topic(),
                    "partition": msg.partition(),
                    "offset": msg.offset(),
                },
            )


class KafkaConsumer:
    def __init__(self, group_id: str):
        self.consumer = Consumer({
            'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': group_id,
            'auto.offset.reset': 'earliest',
        })

    def subscribe(self, topics: list[str]) -> None:
        """Subscribe to Kafka topics."""
        self.consumer.subscribe([f"{settings.KAFKA_TOPIC_PREFIX}.{topic}" for topic in topics])

    def consume(self, timeout: float = 1.0) -> Optional[Dict[str, Any]]:
        """Consume message from Kafka topic."""
        try:
            msg = self.consumer.poll(timeout)
            if msg is None:
                return None
            if msg.error():
                logger.error(
                    "Consumer error",
                    extra={
                        "error": msg.error(),
                    },
                )
                return None
            return {
                "topic": msg.topic(),
                "key": msg.key().decode('utf-8'),
                "value": msg.value().decode('utf-8'),
            }
        except Exception as e:
            logger.error(
                "Failed to consume message",
                extra={
                    "error": str(e),
                },
            )
            raise

    def close(self) -> None:
        """Close consumer."""
        self.consumer.close()


class Event(BaseModel):
    """Base event model."""
    event_type: str
    event_id: str
    timestamp: str
    data: Dict[str, Any] 