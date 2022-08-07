<!--
 Copyright 2022 Universität Tübingen, DKFZ and EMBL
 for the German Human Genome-Phenome Archive (GHGA)

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

# kafka-messaging-system

This project demonstrates some features of the Apache Kafka system. It is implemented using the kafka-python library for python.


To start a producer, open a new terminal


    cd src/
    python producer.py


To start a consumer, in another terminal


    cd src/
    python consumer.py
    
To run producer and consumer in k8s


    kubectl -n data-portal run kafka-messaging-system -ti --image=docker.io/ghga/kafka-messaging-system:0.0.0-8-6b17b45-main --rm=true --restart=Never -- python ../../service/src/producer.py 
    kubectl -n data-portal run kafka-messaging-system -ti --image=docker.io/ghga/kafka-messaging-system:0.0.0-8-6b17b45-main --rm=true --restart=Never -- python ../../service/src/consumer.py
    
    
    
    
