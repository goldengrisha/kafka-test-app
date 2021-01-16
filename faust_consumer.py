import faust


app = faust.App("worker", broker="kafka://localhost:9092")

buffer_topic = app.topic("buffer")
result_topic = app.topic("result")


@app.agent(buffer_topic)
async def process(transactions):
    async for value in transactions:
        transaction_sum = sum(value["transaction"])
        print(f"Input data: {transaction_sum}")
        await result_topic.send(value={"transaction_sum": transaction_sum})
        print(f"Data sent to result")


# @app.timer(interval=1.0)
# async def example_sender(app):
#     print("Input data: ")


if __name__ == "__main__":
    # run the consumer
    app.main()