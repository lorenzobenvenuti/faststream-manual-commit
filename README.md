# faststream-manual-commit

Reproducer for [this issue](https://github.com/airtai/faststream/issues/1001#issuecomment-2060454302)

Steps to reproduce the issue:

- Start Kafka
  ```
  docker-compose -f docker-compose.yaml up
  ```
- Start the application
  ```
  faststream run main:app
  ```
- Send messages:
  ```
  ./send.sh
  ```

Expected behavior: the application consumes the same message again and again.
\
Actual behavior: the application consumes all the messages.
