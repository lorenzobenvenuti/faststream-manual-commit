#!/bin/bash

for i in $(seq 1 10); do echo "${i}:{\"index\":\"${i}\"}" | kafka-console-producer.sh --bootstrap-server localhost:9093  --topic source-topic --property parse.key=true --property key.separator=:; done

