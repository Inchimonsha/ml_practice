import asyncio
import os
from taskiq_aio_pika import AioPikaBroker

broker_url = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")
broker = AioPikaBroker(broker_url)


@broker.task
async def send_email(email: str, message: str) -> None:
    print(f"Отправка email на {email} с сообщением: {message}")


async def main():
    await broker.startup()
    await send_email.kiq(email="user@example.com", message="Привет от Taskiq!")
    await broker.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
