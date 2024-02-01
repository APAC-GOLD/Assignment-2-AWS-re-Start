# Part I.6. (5/30 marks)

- Given a simple AWS EC2 in a Auto Scaling Group architecture with ALB and a dedicated DB instance, name 5 system design components/techniques that can help you scale your system to meet more end-customers demand. Hinted layers:
  - Static content cache
  - Dynamic content cache
  - Compute distribution
  - Persistency
  - Decoupling methods
- For each component, explain in few words (other than adding complexity), what are the trade offs of introducing these components if they weren't added before

## Answers
Registering your Auto Scaling group with an Elastic Load Balancing load balancer helps you set up a load-balanced application. Elastic Load Balancing works with Amazon EC2 Auto Scaling to distribute incoming traffic across your healthy Amazon EC2 instances. This increases the scalability and availability of your application. You can enable Elastic Load Balancing within multiple Availability Zones to increase the fault tolerance of your applications. 

To scale an AWS EC2 in an Auto Scaling Group architecture with ALB and a dedicated DB instance, these five system design options should be considered: 
### 1.	Static content cache:
- Caching static content such as images, videos, and HTML pages can help reduce the load on the web server and improve the response time for the end-users. 
- This can lead to a better user experience and increased customer satisfaction.

### 2.	Dynamic content cache:
- Caching dynamic content such as database queries and API responses can help reduce the load on the database and improve the response time for the end-users.
- This can lead to a better user experience and increased customer satisfaction.

### 3.	Compute distribution:
- Distributing the compute load across multiple servers can help improve the performance and scalability of the system. 
- This can lead to faster response times and increased customer satisfaction.

### 4.	Persistency: 
- Using a persistent storage solution such as Amazon Elastic Block Store (EBS) or Amazon Elastic File System (EFS) can help ensure data durability and availability. 
- This can lead to increased reliability and customer trust.

### 5.	Decoupling methods: 
- Decoupling the different components of the system can help improve the scalability and maintainability of the system. For example, using message queues to decouple the web server from the database can help reduce the load on the database and improve the response time for the end-users.
- This can lead to a better user experience and increased customer satisfaction

### The trade-offs of introducing these components if they weren't added before are:

1.	Static content cache: a static content cache may require additional resources to maintain the cache.

2.	Dynamic content cache:  a dynamic content cache may require additional resources to maintain the cache.

3.	Compute distribution: may require additional resources to manage the distributed compute.

4.	Persistency:  may increase the cost of the system and require additional resources to manage the storage.

5.	Decoupling methods: may require additional resources to manage the decoupled components.

## References:
1.	Nick Do https://miro.com/app/board/uXjVNVsQIDE=/
2.	https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html 
3.	https://www.reddit.com/r/aws/comments/yjg5ag/my_first_aws_architecture_need_feedbacksuggestions/?rdt=59543
4.	https://math.mit.edu/~lguth/Math118/DecLect1.pdf
5.	https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
6.	https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/example-templates-autoscaling.html
7.	https://www.linkedin.com/pulse/mastering-art-decoupling-application-architecture-aws-amit-meena/
8.	https://aws.amazon.com/blogs/compute/decoupling-larger-applications-with-amazon-eventbridge/ 
9.	https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html
10.	https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html.
11.	https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/.
12.	https://aws.amazon.com/caching/cdn/
13.	https://aws.amazon.com/blogs/networking-and-content-delivery/deliver-your-apps-dynamic-content-using-amazon-cloudfront-getting-started-template/


### EC2 Auto Scaling Load Balancer Tutorial Image

![EC2 Auto Scaling Load Balancer Tutorial Image](../A2_Notes/ec2-auto-scaling-load-balancer-elb-tutorial-architecture-diagram.png)


### Decoupling larger applications with Amazon EventBridge – Original

![Decoupling larger applications with Amazon EventBridge – Original ](<../A2_Notes/Decoupling larger applications with Amazon EventBridge - v1 Original.png>)
The original version of this application uses Amazon S3 event notifications to invoke AWS Lambda functions to index content in the Amazon Elasticsearch Service


### Decoupling larger applications with Amazon EventBridge - v2 New

![Decoupling larger applications with Amazon EventBridge - v2 New](<../A2_Notes/Decoupling larger applications with Amazon EventBridge - v2 New.png>)
The new design uses events to decouple each service used to process incoming S3 objects. It can also use one or more buckets as event sources, which you can change dynamically as needed. Most importantly, it can be easier to introduce changes and new functionality, since the application is no longer deployed as a mono-repo. The new architecture uses this design.


end