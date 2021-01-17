# kafka-test-app

### run tests: `pytest tests`

### run docker: `docker-compose up`

### run async processing:

1.  Before you have run producer: `python ./data_processing/micro_processing/producer.py`
2.  Async processing: `python ./data_processing/micro_processing/faust_consumer.py worker`
