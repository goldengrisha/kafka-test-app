from kafka import KafkaConsumer
from json import loads
from time import sleep


def main():
    try:
        consumer = KafkaConsumer(
            "result",
            bootstrap_servers=["localhost:9092"],
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode("utf-8")),
        )

        for event in consumer:
            event_data = event.value
            # Do whatever you want
            print(event_data)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    # execute only if run as a script
    main()
