import time
import logging
import pika


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def callback(ch, method, properties, body):
    message = body.decode()
    logging.info(f"[x] Received: '{message}'")

    try:
        time.sleep(2)
        logging.info("[x] Done processing")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logging.error(f"Error: {e}")


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
        logging.info("[*] Waiting for messages")

        channel.start_consuming()


if __name__ == "__main__":
    main()
