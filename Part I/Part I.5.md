# Part I.5. (5/30 marks)

- What is Change Data Capture (CDC)? 
- What is CDC useful for? 
- Which additional architecture patterns can CDC enable?
- Find AWS architecture references for the use of CDC
  - Transactional Processing
  - Analytics Processing

## Answers
- Change Data Capture (CDC) identifies and captures changes made to data in a database and then delivers the changes in real-time to “downstream system” which is dependant on that data to deliver a service. 


- CDC is useful for enabling real-time analytics use cases and zero-downtime database migrations. 

- CDC can enable additional architecture patterns such as “event-driven architecture,” “microservices,” and “serverless computing.”

## Examples: 
### Transactional Processing: 
- Amazon MSK Connect and AWS Glue Schema Registry can be used to build an end-to-end CDC solution for transactional processing
- The solution uses a MySQL-compatible Amazon Aurora database as the data source, and a Debezium MySQL connector to perform CDC. 
- The Debezium connector continuously monitors the databases and pushes row-level changes to an Apache Kafka Topic.
- Kafka Topic allows users to store and organize data according to different categories and use cases (a topic is a category of messages that can have multiple consumers and producers).
- The connector fetches the schema from the database to serialize the records into a binary form. 
- If the schema doesn’t already exist in the registry, the schema will be registered.

### Analytics Processing: 
- Amazon Kinesis Data Streams and AWS Lambda can be used to build a real-time analytics solution using CDC. The solution uses a DynamoDB table as the data source, and a Lambda function to process the data. 
- The Lambda function is triggered by a “Kinesis Data Streams” stream, which is populated by a “DynamoDB Stream.”
- The DynamoDB stream captures changes to items in a DynamoDB table, and optionally, to the attribute values of those items.
- The Kinesis Data Streams break up data into shards (used to define the capacity you provision your stream of data to your clients). Kinesis stream can flex shard capacity ‘on demand,’ and uses a partition key to distribute data across shards. 
- The Lambda function processes the data and writes the results to an Amazon S3 bucket.


## References
1.	https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.CDC.html
2.	https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html
3.	https://insnerds.com/upstream-vs-downstream-systems-challenges-and-mind-sets-in-system-modernization/
4.	https://softwareengineering.stackexchange.com/questions/312401/which-way-are-downstream-and-upstream-services
5.	https://dattell.com/data-architecture-blog/what-is-a-kafka-topic/
6.	https://developer.confluent.io/learn/apache-kafka-on-the-go/topics/
7.	https://docs.aws.amazon.com/streams/latest/dev/introduction.html
8.	https://aws.amazon.com/blogs/aws/amazon-kinesis-data-streams-on-demand-stream-data-at-scale-without-managing-capacity/
9.	https://aws.amazon.com/kinesis/
10.	https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB_Streams.html


end
