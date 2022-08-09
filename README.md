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

# Dependencies
## Requirments 

Requires Python 3 and pip3

### install packages 
```
pip install -r requirements.txt
```

To start a producer, open a new terminal


    cd src/
    python producer.py


To start a consumer, in another terminal


    cd src/
    python consumer.py
    
To run producer and consumer in k8s

apiVersion: v1
kind: Pod
metadata:
  labels:
    purpose: kafka-producer
  name: kafka-producer
spec:
     containers:
     - name: kafka-producer
       image: ghga/kafka-messaging-system:0.0.0-18-da3bc2c-main     
       volumeMounts:
       - name: secret-volume
         mountPath: /data/crt  
       - name: user-secret-volume
         mountPath: /data/usercrt      
       command: ["python"]
       args: ["/service/src/producer.py"]
       restartPolicy: OnFailure
     volumes:
     - name: secret-volume
       secret:
         secretName: my-cluster-cluster-ca-cert
     - name: user-secret-volume
       secret:
         secretName: my-user
    
    
To run consumer in k8s

apiVersion: v1
kind: Pod
metadata:
  labels:
    purpose: kafka-consumer
  name: kafka-consumer
spec:
     containers:
     - name: kafka-producer
       image: ghga/kafka-messaging-system:0.0.0-18-da3bc2c-main     
       volumeMounts:
       - name: secret-volume
         mountPath: /data/crt  
       - name: user-secret-volume
         mountPath: /data/usercrt      
       command: ["python"]
       args: ["/service/src/consumer.py"]
       restartPolicy: OnFailure
     volumes:
     - name: secret-volume
       secret:
         secretName: my-cluster-cluster-ca-cert
     - name: user-secret-volume
       secret:
         secretName: my-user
    
    

