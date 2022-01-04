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
    Kafka producer
"""

import json

from kafka import KafkaProducer


def produce():
    """
    produce
    """
    producer = KafkaProducer(
        bootstrap_servers=["10.5.0.1:9092"],
        value_serializer=lambda m: json.dumps(m).encode("ascii"),
    )

    for i in range(100):
        producer.send("my-topic", {i: i})
        print(f"message published {i}")


if __name__ == "__main__":
    produce()
