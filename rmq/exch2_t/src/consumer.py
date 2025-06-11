import time
import pika


def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")

    time.sleep(2)
    print("[x] Done processing")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection_params = pika.ConnectionParameters(host='localhost')

    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        channel.basic_qos(prefetch_count=1)

        channel.basic_consume(
            queue='task_queue',
            on_message_callback=callback
        )
        print("[*] Waiting for messages")

        channel.start_consuming()


if __name__ == "__main__":
    main()
