# Part I.1. (5/30 marks)

- Explain eventual and strong consistency
- Which AWS persistent services/feature should you expect eventual consistency?
- Which AWS persistent services/feature should you expect strong consistency?
- Name some (2-3) usecases where eventually consistent persistences are acceptable

## Answers

### Strong Consistency :

- After a “write operation”, “read operation” will see it.
- Data is replicated synchronously (events occurring at the same time).
- All partitioned data accessed by each read operation is consistent. i.e. each read operation returns a result that reflects write operations which have been executed successfully prior to the read.
- Examples:
  - Amazon S3
  - Amazon Elastic Block Store, EBS-specialized data store, “Physalia”

### Eventual Consistency :

- After a “write operation,” delay, “read operation.”
- Data is replicated asynchronously (two or more events not happening at the same time).
- If a company needs “eventual consistency” they may have a system which depends on a high tolerance for errors to work. Examples are: DNS, VoIP, video chat and, email (high availability systems).
- Examples:
  - Amazon DynamoDB
  - AWS KMS API

“Eventual consistency” and “strong consistency,” are “CAP Theorem” expressions.

### CAP Theorem

CAP Theorem is based on three properties:

1. consistency (C) equivalent to having a single up-to-date copy of the data; Every read request receives the most recent write or an error when consistency can’t be guaranteed.
2. high availability (A) of that data (for updates); Every request receives a non-error response, even when nodes are down or unavailable.
3. tolerance to network partitions (P). The system continues to operate despite the loss of an arbitrary number of messages between nodes.

CAP Theorem is based on the assumption there is a “Trade-off” in distributed system design: a maximum of two CAP properties are achievable at any given time, for any networked shared-data system.

## References

References

1. https://serverlessland.com/event-driven-architecture/visuals
2. https://www.amazon.science/blog/amazon-ebs-addresses-the-challenge-of-the-cap-theorem-at-scale
3. Hagit Attiya, Amotz Bar-Noy, Danny Dolev, Daphne Koller, David Peleg, and Rüdiger Reischuk. Achievable cases in an asynchronous environment. In 28th Annual Symposium on Foundations of Computer Science, pages 337-346, Los Angeles, California, October 1987.
4. https://aws.plainenglish.io/distributed-system-cap-theorem-3ca7d933f5e7
5. https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/
6. https://www.linkedin.com/pulse/cap-theorem-revisited-ripan-sarkar/
7. https://techbeats.blog/cap-theorem-availability-vs-consistency
8. https://aws.amazon.com/s3/consistency/
9. https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html
10. https://docs.aws.amazon.com/whitepapers/latest/comparing-dynamodb-and-hbase-for-nosql/consistency-model.html
11. https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/cap-theorem.html

### CAP Theorem

![CAP Theorem](<../A2_Notes/Screenshot 2023-12-18 at 11.50.10 AM.png>)

### Cost of Consistency, AWS Reading & Writing

![Cost of Consistency, AWS Reading & Writing](<../A2_Notes/Screenshot 2024-01-01 at 3.12.03 PM.png>)

### CAP Strong, eventual consistency

![CAP Strong, eventual consistency](<../A2_Notes/Screenshot 2023-12-18 at 6.43.46 AM.png>)


end