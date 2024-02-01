# Part I.4. (5/30 marks)

- Explain idempotency in the context of transactional processing
- What does it mean to have an idempotent consumer?
- Given SQS as the message broker, and Lambda function as the message consumer
  - How would you implement Lambda as an idempotent consumer?
  - Which component would become the bottleneck when you implement idempotent consumers?

## Answers

- The “idempotency property” of a system ensures an operation can be executed more than once, with consistent results. In the context of transactional processing, idempotency ensures that the same transaction is not processed twice, which can lead to inconsistencies in a system. The concept of idempotence is used in mathematics, computer science, abstract algebra, and functional programming.

- Example: Your bank card is swiped to make a payment for your new vehicle tires, and the eftpos machine says the transaction failed or the system was down, however, you and the supplier are unaware that your account was successfully debited. In this example, you would not want to be able to make multiple payments/withdrawals for the same transaction from your account.

- The payment request for payment of your tires had a unique “request id,” and the server was configured not to serve the same request id, twice. In theory, when the supplier gives you the eftpos machine again to put through the payment, your account will not be debited multiple times because idempotency message protocol works by utilising unique client/server identifiers (request id) for each individual interaction with the server.

- An “idempotent consumer” is a message consumer that can process the same message multiple times without causing any side effects beyond the first processing. In other words, the consumer can handle duplicate messages without causing any harm to the system.

- To implement Lambda as an idempotent consumer with Amazon SQS as the message broker, you can use the following steps:

1. Configure the SQS queue to use “content-based deduplication”. This feature ensures that duplicate messages are not delivered to the consumer.

2. Implement the Lambda function to be “idempotent. “This means that the function should be able to handle the same message multiple times without causing any side effects beyond the first processing.

3. Use the “message deduplication ID” provided by SQS to ensure that the same message is not processed twice by the Lambda function.

- When implementing idempotent consumers, the “message broker” can become the bottleneck. This is because the broker needs to ensure that duplicate messages are not delivered to the consumer, which can cause delays in message delivery.

# References

1. https://medium.com/@ohm.patel1997/designing-payment-system-using-idempotent-apis-45526d080dc2
2. https://en.wikipedia.org/wiki/Idempotence
3. https://serverlessland.com/search?search=idempotent
4. https://serverlessland.com/patterns/eventbridge-api-destinations-idempotency-cdk?ref=search
5. https://blogs.sap.com/2023/10/03/sap-cloud-integration-idempotent-process-call/
6. https://help.sap.com/docs/cloud-integration/sap-cloud-integration/idempotent-process-call-handles-duplicates
7. https://help.sap.com/docs/cloud-integration/sap-cloud-integration/idempotent-process-call-handles-duplicates-with-alternative-response
8. https://api.sap.com/api/MessageProcessingLogs/resource/Idempotent_Repository
9. https://medium.com/@ohm.patel1997/designing-payment-system-using-idempotent-apis-45526d080dc2
10. https://www.moderntreasury.com/journal/why-idempotency-matters-in-payments
11. https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation
12. https://docs.python.org/2/library/stdtypes.html#set

### Amazon SQS

![Amazon SQS](<../A2_Notes/idempotent API operation.png>)

### Idempotent-process same message with same order num on subsequent order request will not process

![idempotent-process same message with same order num on subsequent order request will not process](<../A2_Notes/idempotent-process same message with same order num.PNG>)

### Idempotent-process-call-handles-duplicates with alternative response to sender

![idempotent-process-call-handles-duplicates with alternative response to sender](<../A2_Notes/idempotent-process-call-handles-duplicates with alternative response.PNG>)

end
