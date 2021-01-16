from time import sleep
from json import dumps
from kafka import KafkaProducer


def main():
    try:
        producer = KafkaProducer(
            bootstrap_servers=["localhost:9092"],
            value_serializer=lambda x: dumps(x).encode("utf-8"),
        )
        credit_transactions = [
            [
                12.8,
                0.029,
                0.48,
                0.98,
                6.2,
                29.1,
                3.33,
                1.2,
                0.39,
                75.1,
                0.66,
                11.2,
                1.3,
                0.2,
                12.8,
                0.029,
                0.45,
                0.98,
                6.2,
                29,
                3.33,
                1.2,
                0.39,
                75.3,
                0.3,
                2.2,
                1.3,
                2.2,
                1.01,
            ],
            [
                0.8,
                0.2,
                0.32,
                0.1,
                5.2,
                29.1,
                3.4,
                1.2,
                0.4,
                75.1,
                0.77,
                1.2,
                1.3,
                1.2,
                11.8,
                0.002,
                0.48,
                0.99,
                6.2,
                4,
                3.33,
                1.2,
                0.2,
                75.3,
                0.4,
                1.2,
                1.3,
                2.2,
                2.01,
            ],
            [
                11.2,
                20,
                0.1,
                0.98,
                6.2,
                29.1,
                3.23,
                1.2,
                0.7,
                75.1,
                0.88,
                1.22,
                1.4,
                2.2,
                3.8,
                0.003,
                0.45,
                0.1,
                6.2,
                29,
                3.8,
                1.2,
                0.39,
                75.3,
                0.5,
                1.6,
                1.3,
                3.2,
                3.001,
            ],
            [
                2.1,
                0.34,
                0.34,
                0.2,
                4.2,
                29.1,
                3.1,
                1.2,
                0.2,
                75.1,
                0.99,
                1.32,
                1.5,
                3.2,
                0.8,
                0.02,
                0.48,
                0.2,
                6.2,
                6,
                3.33,
                1.2,
                0.3,
                75.3,
                0.6,
                0.2,
                1.3,
                5.2,
                5.2,
            ],
            [
                0.08,
                0.22,
                0.1,
                0.98,
                6.2,
                29.1,
                3.33,
                1.2,
                0.56,
                75.1,
                0.1,
                1.42,
                1.6,
                4.2,
                0.8,
                0.1,
                0.45,
                0.3,
                6.2,
                29,
                3.7,
                1.2,
                0.39,
                75.3,
                0.7,
                1.2,
                1.3,
                7.2,
                1.21,
            ],
        ]
        for j in range(len(credit_transactions)):
            print("Iteration", j)
            data = {"transaction": credit_transactions[j]}
            producer.send("buffer", value=data)
            # sleep(0.5)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    # execute only if run as a script
    main()