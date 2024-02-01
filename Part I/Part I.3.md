# Part I.3. (5/30 marks)

- Explain the differences between point-to-point messaging pattern (Queue) and publish/subscribe pattern (Pub/Sub)
- When would you use point-to-point messaging over the other?
- When would you use publish/subscribe over the other?
- Find AWS architecture references for point-to-point messaging
- Find AWS architecture references for publish/subscribe

## Answer

- Point to Point (Queue) and Pub/Sub are two types of messaging models that support asynchronous messaging between various digital systems and platforms. Both models allow exchange of messages.

- Point-to-point messaging is useful when there is a need for a one-to-one relationship between the sender and the receiver.

- Publish/subscribe pattern is useful when there is a need for a one-to-many relationship between the sender and the receiver.

- Amazon SQS and Amazon SNS are serverless, fully managed message queue service APIs. You can use Amazon SQS and Amazon SNS to decouple and scale microservices, distribute systems and serverless applications. If companies are migrating to the cloud, they can use Amazon MQ message broker service. It supports industry-standard APIs and protocols such as JMS, AMQP, and MQTT (so that they don’t have to re-code existing architecture).

- AWS Copilot uses pub/sub architecture. The AWS Copilot CLI is a tool that developers use to build, manage, and operate Linux and Windows containers on Amazon Elastic Container Service (Amazon ECS), AWS Fargate, and AWS App Runner.

## References

1. https://aws.amazon.com/blogs/compute/implementing-enterprise-integration-patterns-with-aws-messaging-services-point-to-point-channels/.
2. https://serverlessland.com/event-driven-architecture/point-to-point-messaging
3. https://www.ibm.com/docs/en/ibm-mq/7.5?topic=architecture-point-point-messaging
4. https://aws.amazon.com/architecture/
5. https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/pub-sub.html
6. https://www.geeksforgeeks.org/differences-between-pointtopoint-and-publish-subscribe-model-in-jms/
7. https://aws.amazon.com/blogs/containers/implementing-a-pub-sub-architecture-with-aws-copilot/
8. https://aws.amazon.com/messaging/
9. https://aws.amazon.com/blogs/compute/implementing-enterprise-integration-patterns-with-aws-messaging-services-point-to-point-channels/


end
