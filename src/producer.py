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
from time import sleep

from kafka import KafkaProducer


def produce():
    """
    produce
    """     
    try:

        producer = KafkaProducer(
            bootstrap_servers=["my-cluster-kafka-bootstrap:9093"],
            value_serializer=lambda m: json.dumps(m).encode("ascii"),
            security_protocol='SSL',
            ssl_check_hostname=True,
            ssl_cafile='/data/crt/ca.crt',
            ssl_certfile='/data/usercrt/user.crt',
            ssl_keyfile='/data/usercrt/user.key'
        )
        for i in range(100):        
         producer.send("my-topic", {i: i})
         print('message published {0}'.format(i))       

    except Exception as e:
        # ... PRINT THE ERROR MESSAGE ... #
         print(e)     


if __name__ == "__main__":
    while True:        
        produce()
        sleep(60)