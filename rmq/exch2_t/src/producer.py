import pika


def main():
    connection_params = pika.ConnectionParameters(host='localhost')

    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        message = "Hello. Test message"

        channel.basic_publish(
            exchange="",
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        print(f"[x] Sent '{message}'")


if __name__ == "__main__":
    main()
