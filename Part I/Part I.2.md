# Part I.2. (5/30 marks)

- Explain the need for messaging integration
- Why should we use message brokers in microservices architecture?
- Find AWS architecture references for the use of message broker in microservices.

## Answers

- Messaging Integration is needed for Microservices integration patterns that are based on events and asynchronous messaging to optimize scalability and resiliency. Message queuing services are used to coordinate multiple microservices at once, notify microservices of data changes, or, for example, an “Amazon firehose” event, to process IoT, social and real-time data.

- Message brokers are used in Microservices Architecture, for example, a Serverless Loan Broker with AWS Step Functions to play the executive function role and make sure a series of tasks are maintained. For example, if a task is completed out of order (asynchronously), a “Process Manager” such as “ Serverless Loan Broker with AWS Step Functions,” or “Serverless Loan Broker with GCP Workflows,” orchestrates the series of tasks and maintains state across tasks This leads to better performance.

- An example of a Message Broker in Microservices is “Amazon Simple Queue Service (SQS)” short format “Amazon SQS.” This service is used, for example, to decouple microservices and process event-driven applications separately (frontend from backend systems) in a banking application environment. It benefits bank customers by giving them an immediate response, while bill payments are processed in the background (internally by the bank).

- Message queues enable asynchronous communication, which means that the endpoints that are producing and consuming messages interact with the queue, not each other. Producers can add requests to the queue without waiting for them to be processed. Consumers process messages only when they are available. No component in the system is ever stalled waiting for another, optimizing data flow.

- Message queues provide communication and coordination for these distributed applications. Message queues can significantly simplify coding of decoupled applications, while improving performance, reliability and scalability.

## References

1. https://www.enterpriseintegrationpatterns.com
2. https://aws.amazon.com/message-queue/benefits/#:~:text=Microservices%20integration%20patterns%20that%20are,social%20and%20real%2Dtime%20data.
3. https://www.enterpriseintegrationpatterns.com/ramblings/eip1_examples_updated.html
4. https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html
5. https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html
6. https://aws.amazon.com/sqs/

end

