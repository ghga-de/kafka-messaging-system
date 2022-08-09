# Copyright 2022 Universität Tübingen, DKFZ and EMBL
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    Kafka consumer
"""

from kafka import KafkaConsumer


def consume():
    """
    consume
    """
    consumer = KafkaConsumer(
        "my-topic", 
        group_id="my-group",
        bootstrap_servers=["my-cluster-kafka-bootstrap:9093"],
        security_protocol='SSL',
        ssl_check_hostname=True,
        ssl_cafile='/data/crt/ca.crt',
        ssl_certfile='/data/usercrt/user.crt',
        ssl_keyfile='/data/usercrt/user.key'
    )

    for message in consumer:
        print(
            f" topic: {message.topic} partition: {message.partition} "
            + f"offset: {message.offset} key: {message.key} value: {message.value} "
        )


if __name__ == "__main__":
    consume()
