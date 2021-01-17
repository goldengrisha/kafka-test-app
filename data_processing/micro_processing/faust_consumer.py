import sys
import os
import faust

sys.path.insert(0, os.path.abspath("./"))
# just a hack

from time import sleep
from shared_function.function_a import list_sum


app = faust.App("worker", broker="kafka://localhost:9092")
buffer_topic = app.topic("buffer")
result_topic = app.topic("result")


@app.agent(buffer_topic)
async def process(transactions):

    # please set timer for retreiving `within is seconds`
    # here it set a limit of 10000 but it can be whatever big
    async for list_transactions in transactions.take(10000, within=10):

        transaction_sum = list_sum(
            list(map(lambda lt: sum(lt["transaction"]), list_transactions))
        )
        print(f"Input data: {transaction_sum}")

        await result_topic.send(value={"transaction_sum": transaction_sum})
        print(f"Data sent to result: {transaction_sum}")


if __name__ == "__main__":
    # run the consumer
    app.main()