# Justification for My Design Choice.

#### Assignment Question Part II.2

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 7.35.10 PM.png>)

I choose EIC Endpoint because it is the best option. My own research and analysis of the pros and cons for various methods to deploy a minimal viable product, is why I went a different direction to the rest of the class. Furthermore, what makes a method "convenient" (or not), seems to depend on your roles and responsibilities.

**Most Convenient Method**
(1) I leaned business owners and management do not see staff accessing Private Subnets directly, as convenient. It makes them nervous. For example, a System Admin may see the "correct answer", for most convenient method, as the safest method EIC+Public Subnet (so produced Diagram 3).

(2) Developers on the other hand, would see the most convenient method as the most direct, with the least amount of effort to get access to the instance which they need, EIC+ Private Subnet (so produced Diagram 4).

Both options are _convenient_ for different reasons, here are some more:

(a) EIC Endpoints don’t require your VPC to have direct Internet connectivity

(b) No need to create/manage extra instances

(c) No SSH security keys to configure.

(d) The EIC design is Multi-AZ Compatible, via 3 VPC in the Management Tier, which incorporates the design features from earlier instructions, Part II.1.

(e) Security groups and

(f) Route tables give just the right amount of access to reach resources, on each AZ , or to access an S3 with DynamoDB.

#### Part II.2 Marks

(Q1) _How would you add access for EC2 and S3?"_ I answered this question in the top most section of the file document named,'Part II.2.

(Bullet points 1 & 2) I provided a case with justification for least/most convenient methods.

(Bullet point 3) I produced a big new illustration with all the added components for the design: (i) new EIC Security Group, (ii) EIC Endpoint (iii) Route table (iv) EIC2 Instance Connect Endpoint Service, (v) New Policy with access to EIC, S3 and Dynamo DB, (vi) New IAM role for access to EIC, EC2 & S3 read/write capability....

In summary, my design meets the specification in Assignment 2 Part II.2 and incorporates/ meets security requirements of Part II.1, introduced by the AWS re/Start Course Instructor. Specifically, the rules for access to the DataBase (ONLY via public subnet NWFW --> to protected subnet --> to management subnet --> to secure subnet --> to DB). I stand by my research. Kindly, please review my marks.

**Attachments**
(diagram 3) screenshots

- **Public Subnet** Access option, _"Almost The Most Convenient Method."_

(diagram 4) screenshots

- **Private Subnet** Access Option, _"Most Convenient Method"_

With either option, Egress data flows through the subnets according to the route tables and security groups, in keeping with the natural rules of the VPC.

Amy Newkirk
1 February 2024

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 8.44.59 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 8.43.04 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 8.43.18 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 8.43.33 PM.png>)

Reference: 
EIC Endpoints - Why?: https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/
Secure Ingress/ Egress w/ DynamoDB/S3 via Endpoints in Diagram 3 & 4: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc-endpoints-dynamodb.html

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 9.26.46 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 9.28.14 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 9.33.56 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 9.36.17 PM.png>)

![Alt text](<Assignment 2 Part II.2 Design Justification x2/Screenshot 2024-02-01 at 9.37.15 PM.png>)
