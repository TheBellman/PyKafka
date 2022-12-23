# PyKafka
Simple Python code to demonstrate working with Kafka and Avro

## Prerequisites
This project assumes that:

- git is installed and available in the command path.
- To be completed

It also pretty well assumes you have a schema registry and Kafka cluster available for use. The easiest way to achieve that is to use the [confluentinc/cp-all-in-one](https://github.com/confluentinc/cp-all-in-one) project with Docker (yes, you will need Docker as well) which can run up an ensemble including Kafka and the Confluent schema registry on your desktop. Use of this project is also discussed at [Confluent](https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html)

Finally, this assumes that you have a topic in your target cluster called `pykafka` - you can create it with something akin to this:

```shell
./kafka-topics.sh --bootstrap-server localhost:9092 \
    --create \
    --replication-factor 1 \
    --partitions 1 \ 
    --topic names
```

## Test and Build
T.B.C.

## Usage
Executing with `--help`, or with no options, the toy will report its usage.

```shell
% PyKafka --help
Usage: PyKafka [OPTIONS] COMMAND [ARGS]...

  Simple demonstration of using Kafka producers/consumers.

Options:
  --bootstrap-server TEXT  Where to find kafka, assumed to be host:port
  --topic TEXT             The target topic to use
  --help                   Show this message and exit.

Commands:
  consume
  produce
```

The commands also have help:
```shell
% PyKafka consume --help
Usage: PyKafka consume [OPTIONS]

Options:
  --help  Show this message and exit.


% PyKafka produce --help
Usage: PyKafka produce [OPTIONS]

Options:
  --count INTEGER  Number of messages to produce
  --help           Show this message and exit.
```
T.B.C.

## ToDo
Next steps for enhancement are:

- setup a data source
- create the Producer
- create the Consumer
- provide the target topic on the command line, optionally
- try to create a topic if it doesn't already exist
- convert to using Avro
- provide the Schema Registry URL on the command line, optionally
- finish this README

### Notes
To build : `python -m build . --wheel`
which presumes: `pip install build`
for testing and dev ` pip install --editable .`
to test: pytest

## License

Copyright 2022 Little Dog Digital

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
