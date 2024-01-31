## Part II.3
![Alt text](image.png)

- I would adopt a container orchestration model to and associated compute to replace EC2 Autoscaling because,
- in my example, the client is the resource consumer, and may have high demand for compute power at “end of month” when running payroll and other business applications. 
- By using container orchestration, for example **Kubernetes (EKS)**, only the resources that were being used would be chargeable. 
- This means that the number of “Pods” required for services to run at maximum efficiency would reap the reward of **$$$** reduced costs in the form of overhead for my company, and happy customers, whom can easily run resource intensive reporting applications. 
- **Service Discovery** helps by providing a database of available service instances so that services can be discovered, registered, and de-registered.  
- An AWS Elastic Load Balancer (ELB) and Application Load Balancer (ALB), is an example of server-side discovery. A client makes HTTP(s) requests (or opens TCP connections) to the ELB, which load balances the traffic amongst a set of EC2 instances.

#### Diagram 10 - Showing AutoScaling Compute and DataBases ![Diagram 10 - Showing AutoScaling Compute and DataBases](<Diagram 10 - Showing Autoscaling Compute for DB.png>)

VPC - Basic architecture without pods 

