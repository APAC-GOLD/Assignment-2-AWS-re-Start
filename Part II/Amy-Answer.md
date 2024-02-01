- [Part II. Classic AWS Architecture design (30 marks total)](#part-ii-classic-aws-architecture-design-30-marks-total)
  - [Part II.1. - Base design questions (20/30 marks)](#part-ii1---base-design-questions-2030-marks)
  - [Part II.2. - Expansive network design questions (10/30 marks)](#part-ii2---expansive-network-design-questions-1030-marks)
  - [Part II.3. - Bonus design questions (bonus 5 marks)](#part-ii3---bonus-design-questions-bonus-5-marks)
- [Part III. AWS Native Architecture design (10 marks total)](#part-iii-aws-native-architecture-design-10-marks-total)
- [Part IV. AWS Native Software Development (30 marks total)](#part-iv-aws-native-software-development-30-marks-total)
  - [Part IV.1. Setup source events (10/30 marks)](#part-iv1-setup-source-events-1030-marks)
  - [Part IV.2. Checking in (10/30 marks)](#part-iv2-checking-in-1030-marks)
  - [Part IV.3. Making a claim (10/30 marks)](#part-iv3-making-a-claim-1030-marks)
  - [Part IV.4. Bonus mark for quality (5 bonus mark)](#part-iv4-bonus-mark-for-quality-5-bonus-mark)

---

# Part II

# Classic AWS Architecture design

## (30 marks total)

# Part II.1. - Base design questions

## (20/30 marks)

---

## Objective:

R# 1. Objective
Research and improve on the base Virtual Private Cloud (VPC) example. Design a new cloud infrastructure. Produce architecture diagrams and technical specification documentation according to your new design, including security groups and route tables.

**The new design should achieve:** improved security, high availability, lower cost.

# 2. Architectural Principles

**Resilient Architecture:** This record needs to be progressively completed throughout concept and development phases. It documents the existing conditions, design considerations, parameters and details, actions, technical decisions, design verifications and safety considerations. This will also document normal design domain and any use of extended design domain and design exceptions.

The technology stack has a dependency on this work and will leverage the Amazon Web Services (AWS) capability to deliver service or secure existing services. Specifically, core AWS services in the area of compute, storage and networking, including EC2, S3, IAM, VPC, Lamda, Cloud Formation, RDS and Route 53.

Key values underpinning the design strategy are:
**- Cost-efficient**
**- Available**
**- Fault-tolerant**
**- Scalable**

## 2.1 Requirements:

Our VPC spans across 3 Availability Zones (AZ) and consists of 5 tiers:

1. **Firewall Tier:** Protects all subnets, both public and private. All traffic into or out of the VPC is inspected by the AWS Network Firewall service.
2. **Protected Tier:** Contains the Application Load Balancer (ALB), Network Address Translation Gateway (NATGW), and AWS Systems Manager.
3. **Multi-Purpose Tier:** Houses Elastic Compute Cloud (EC2) workloads and microservices, which are managed by the AutoScalingGroup and load balanced by the ALB.
4. **Management Tier:** Contains EC2 jump hosts for AWS Manager - Session Manager.
5. **Secure Tier:** Limited to database access only; no other “hops” into the Secure Tier are allowed.

## 2.2 Design Goal Opportunities/ Recommendations:

1. Plan for non-overlapping IP address spaces across Azure regions and on-premises locations in advance3.
2. Use IP addresses from the address allocation for private internet, known as RFC 1918 addresses3.
3. Don’t create large virtual networks like /16. It ensures that IP address space isn’t wasted3.
4. The smallest supported IPv4 subnet is /29, and the largest is /2 when using classless inter-domain routing (CIDR) subnet definitions3.
5. Don’t create virtual networks without planning the required address space in advance3.
6. Don’t use public IP addresses for virtual networks, especially if the public IP addresses don’t belong to your organization3.
7. Take the services you’re going to use into consideration, there are some services with reserved IPs (IP Addresses), like AKS with CNI networking3.
8. Use non-routable landing zone spoke virtual networks and Azure Private Link service to prevent IPv4 exhaustion3.
9. Use **IAM database authentication tokens** generated using AWS access keys.
10. Use **Transit Gateway** to connect VPCs to simplify network architecture.
11. Use **AWS PrivateLink** to access AWS services over private network connections instead of the public internet.
12. Use **AWS Direct Connect** to establish a dedicated network connection from on-premise to AWS.
13. Use **AWS Global Accelerator** to improve the availability and performance of applications by routing traffic over the AWS global network.
14. **Set up 3 Elastic IP address** for the NAT gateways in each AZ.
15. **Set up 3 Elastic IP address** for the ALB across each AZ
16. Network EC2 in a private subnet and public subnet with **NAT Gateway routing to private subnet**
17. Produce updated **network policy** documentation and design specification documentation regularly throughout implementation phase and after go-live.
18. ** Scaling Policy** Configure a target tracking scaling policy.
19. Use **Security Group Source** with security group ID.
20. Use **VPC Endpoint** for S3.
21. Use **Highest value for maximum connections:** i.e. “AWS RDS micro instance.”

# 3. Classless Inter-Domain Routing (CDIR) Strategy

## 3.1 Subnet Design

This table shows the CDIR Subnet Group breakdown used in the new VPC Design. From a security point of view, it's a good idea to have a 3 tiered architecture whereby there is a set of public subnets across AZ, and a set of private subnets across AZs. An example of why this is a good idea could be that public subnets (or services therein) should have no access to the database subnets directly, unless they go via the Management Tier. In this design, there will be no direct internet access to the database subnets.
Concentrating on the public security groups first; Green = most specific IP address/ route priority; Blue = private security groups; Ensuring there are enough dedicated subnet groups to scale for app/web/microservice layer resources, now and in the future.

### 3.1.2 Addressing Plan Table with Assigned CIDRs

![Alt text](<Addressing Plan Table with Assigned CIDRs.png>)
**CDIR Master:** 10.0.0.0/16 [[ℹ]](https://www.davidc.net/sites/default/subnets/subnets.html?network=192.168.0.0&mask=16&division=63.f9c4e462f4627231)

### 3.1.3 AWS Network Availability Units (NAU) Table

![Alt text](<AWS Network Address Use (NAU) Table.png>)

### 3.1.4 NAU Units Plan Calculation\*\*

15 – IPv4 subnets x15
03 – Additional Services x3
05 – Service improvements x3
18 – Application Load Balancer x3
90 – AZ 3 x 5 tier VPC X 6 per endpoint
06 – Possible Transit gateway
06 - Lambda S3
06 - NAT Gateway
06 - EFS per twin EC2 instance
03 - Network Firewall endpoint requires a dedicated subnet
**158 NAU Units Total**

## 3.2 Address Planning

1. Plan for scaling - Leverage NAU Unit Calculation for all network architecture
2. Leverage Rout Priority in assigning CDIR Blocks to instances
3. Maintain a table with the instances, subnets, instance IDs
4. Do not use reserved IP addresses when planning your subnet and instance addressing. For example, 172.17.0.0/16 CIDR range conflicts with services like AWS Cloud9 or Amazon SageMaker.
5. The AWS documentation for VPCs notes that IP addresses in each subnet CIDR block are reserved by AWS for internal use [[ℹ]]( https://repost.aws/questions/QUdGYmSmyyRQupN3_sgym8YA/how-do-i-reserve-ip-addresses-for-a-specific-purpose).
   a. `"The first IP address (x.x.x.0) is the network address and cannot be assigned to an instance."`
   b. `“The second IP address (x.x.x.1) is reserved for the VPC router."`
   c. `"The third IP address (x.x.x.2) is reserved for future use by AWS."`
   d. `"The fourth IP address (x.x.x.3) is reserved for the Domain Name System (DNS) server that Amazon VPC populates for the subnet."`
   e. `"The last IP address (x.x.x.255) is the broadcast address for the subnet and cannot be assigned."`

# 4. High Level Architecture

The following diagram provides an overview of the resources included in the VPC design. The VPC has:

- 3 Availability Zones (AZ)
- 5 Security Tiers
- 32 Subnets: 15 public, 15 private (2 remaining)

#### 4.1 Firewall Tier.

All traffic in and out of the VPC is routed through a network firewall endpoint in the same AZ.

#### 4.2 Protected Tier

The Protected Tier for each AZ, contains separate subnets for Network Address Translation (NAT) Gateway and an Application Load Balancer (ABL). This way microservices and EC2 workloads are isolated from each other on the network level for added security. It also allows applying different ingress/egress rules to each workload type independently.

#### 4.3 Multipurpose Tier

Multipurpose Tier receives traffic from clients through the ALB and the workload servers are launched and terminated using an Auto Scaling group.

#### 4.4 Secure Tier

The RDS Database (DB) and EFS Network File system have an AZ failover in AZ1 and a Read Only DB instance in AZ3. Secure Subnets can connect to Amazon S3 by using a VPC Endpoint in the Management Tier.

#### 4.5 Management Tier

Management Tier is the only route for Secure Tier Subnets to connect to the internet, which then connects to the NAT gateway in the same AZ.

### Diagram 1 - Showing Overview

![Diagram 1 - Showing Overview](<Diagram 1 - Showing Overview.png>)

# 5. Security

This section provides details about the network architecture security groups, and routing tables.

## 5.1 Best Practice

The AWS resource types which generally benefit the most from being isolated into their own dedicated subnets are [[ℹ]](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-two-zone-igw.html) [[ℹ]](https://community.aws/concepts/networking-essentials):

- **Databases and data stores**: Isolating databases like RDS improves security since they contain sensitive data and don't require direct internet access. This limits lateral movement if a subnet is compromised.

- **Application/API servers**: Placing application servers alone in subnets adheres closely to least privilege principles and avoids exposing unnecessary services or ports.

- **Load balancers**: Dedicating load balancers like ALB simplifies security configurations and prevents conflicts over static IP addresses if sharing subnets.

- **Storage resources**: File systems such as EFS and storage gateways are best isolated to restrict access and egress scope when not requiring broad access.

- **Networking resources**: Resources that route traffic between subnets like NAT Gateways, VPNs and firewalls perform optimally isolated in dedicated subnets without conflicts.

- **Management services**: Centralized access and logging services like Systems Manager are well-suited to dedicated subnets for tighter control and monitoring of network activity.

There are a few key reasons why it is considered a _best practice_ to place each AWS resource type in its own subnet, when setting up VPC architecture [[ℹ]](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-network-optimization-tips/) [[ℹ]]( https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-security)[[ℹ]](https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/centralized-inbound.html):

### 5.1.1 **Increased security.**

Isolating each resource type into its own subnet _reduces the overall attack surface area._ By segmenting resources, if one subnet or resource is compromised, it limits lateral movement and doesn't impact other subnets or resources.

### 5.1.2 **Improved manageability.**

Having one focused resource per subnet makes it _easier to administer, monitor and troubleshoot_ issues for that specific resource type. For example, all ALB-related configurations and traffic can be managed within the dedicated ALB subnet.

- Isolating the ALB in its own subnet _improves security and manageability._
- This _reduces the overall attack surface_ if the ALB subnet is compromised, limiting lateral movement
- It also makes ALB-related configurations and traffic easier to _administer separately from other resources_.

### 5.1.3 **Avoid Conflicts**

Separating resources like NAT Gateways and load balancers, which require static IP addresses, prevents conflicts that could arise if they shared the same subnet.

- Dedicated ALB subnets prevent potential conflicts that could arise if the ALB shared a subnet with other resources requiring static IP addresses.
- This enables optimal use of security controls at the subnet level through security groups and network ACLs.

### 5.1.4 **Future flexibility.**

The subnet design is not tightly coupled to specific resources. Additional subnets can be added easily for other use cases. And resources can be moved between subnets with less reconfiguration.

- Segmenting the ALB in this way also improves its availability. Critical functions like scaling or routing updates can occur independently without affecting other resources. Additional ALB subnets can also be added flexibly as needed to scale the architecture.
- _High availability is improved_ since critical updates or scaling of Systems Manager and NAT Gateway functions can occur independently without affecting other subnet resources.

### 5.1.5 **Leverage security controls**

Security groups and network ACLs applied at the subnet level allow granular control of traffic flows between subnets based on their functions.

- Placing the ALB/NAT alone in a public subnet _adheres to the principle of least privilege and minimum access._
- This _restricts_ the ALB/NAT's scope of _access and egress_ only to necessary ports and protocols, reducing vulnerabilities from any exposed services.
- Placing Systems Manager alone simplifies security group rules and network access configurations specific to its management functions.
- Changes don't impact other resources in shared subnets.

### 5.1.6 **Alternative View**

An alternative point of view is, isolating instances by subnet (1 to 1 relationship between route tables and subnets within the VPC) causes more management overhead and increases the amount of changes needed whenever there is a routing change to implement across the environment [[ℹ]]( https://medium.com/@mda590/aws-routing-101-67879d23014d).
.

### New VPC Design Combines "Ease of Use" with "Best Practice":

In the diagram below, you will see a compromise between both schools of thought. Only Public Subnet instances which are at risk of conflicts (static EIP) and would otherwise share a subnet group with the ALB and NAT Gateway, are isolated in the Protected Tier.

## Diagram 2 – Showing Route Table Logic

![Diagram 2 - Showing Route Table](<Diagram 2 - Showing Route Table.png>)
The VPC has public subnets and private subnets in three Availability Zones. The web servers run in the private subnets and receive traffic from clients through a load balancer. The security group for the web servers allows traffic from the load balancer. The database servers run in the private subnets and receive traffic from the web servers. The security group for the database servers allows traffic from the management servers. The database servers can connect to Amazon S3 by a gateway VPC endpoint.

## 6. Route Tables

This section describes the route table logic. Route tables control traffic between subnets/resources like a map, with an address book. Separating traffic flows for public internet access vs private connectivity.

### 6.1 Public Subnets

- **Diagram 2 - `Green Subnets`**
- All the subnets in the Firewall and Protected Tiers.

#### 6.1.1 Internet Gateway (IGW) Route Table

- The **Internet gateway ingress/egress route table** is configured to direct all traffic to the AWS Network Firewall endpoints in each Availability Zone (AZ).
- This ensures that traffic is symmetrically returned to the right firewall endpoint to maintain stateful traffic inspection.
- The IGW ingress/egress route table handles routing traffic both within the public subnets and between public/private subnets as it transits through the firewall endpoints and internet gateway.
- **Diagram 2 - `B`**

![Alt text](<Tables/Picture 7 - IGW Ingress Egress Local New.png>)

- The ingress routes to the firewall endpoints covers traffic entering the VPC.
- The egress route to the internet gateway allows traffic to leave after firewall inspection.
- The local route enables responses to public resources.

#### 6.1.2 Public Route Table

- Internet facing route table which connects local network `10.0.0.0/16` traffic with the internet `10.0.0.0/0`
- **Diagram 2 - `A`**

#### 6.1.3 Firewall Endpoint Route Table

- All traffic in (ingress) and out (egress) of the VPC is interrogated by the AWS Network Firewall (NWFW). However, NWFW doesn’t perform NAT; Ingress and egress to the internet depends on public EIPs associated to individual elastic network interfaces (ENIs) in the Protected Tier subnets. Firewall Route Table directs ingress traffic to an ALB or egress traffic from NAT, to the IGW.
- **Diagram 2 - `C` and ‘I`**

#### 6.1.4 NAT Route Table

- Directs traffic destined for the internet, to NWFW subnets in the corresponding AZ.
- **Diagram 2 - `H`**

#### 6.1.5 System Manager Route Table

- Public subnets with local routes to ALB, NAT gateway, and routes to direct traffic to Private subnet, VPC Endpoint.
- **Diagram 2 - `E`**

### 6.2 Public Endpoints

#### 6.2.1 EC2 Instance Connect (EIC) Route Table

- The EIC Route Table connects to Endpoints in the Management Tier, across all 3 AZ.
- Public subnets with routes to the Endpoints.

- **Diagrams 3 & 4 - `D` `K`**

![Alt text](<Tables/Picture 8 - EIC E Route Table New.png>)

- **Achieve private access to EC2 instances via the EIC endpoint** with proper route table and security group configuration to achieve private access to EC2 instances via the EIC endpoint, without exposing them publicly. This endpoint allows SSH connections directly to instance public IPs while keeping them private, improving security over bastion hosts or public IPs [[ℹ]](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-ec2-instance-connect-ssh-rdp-public-ip-address/).

### 6.3 Private Subnets

- All the subnets in the Multipurpose, Secure, and Management Tiers.

- **Diagram 2 - `Blue Subnets`**

#### 6.3.1 Multipurpose Route Table

- Private subnets with local routes, and routes to the NAT gateway.

- **Diagram 2 - `1W` `2W` `3W`**

#### 6.3.2 Secure Route Table

- Private subnets with limited local routes to the Multipurpose Subnet and from the Management Subnet.
- **Diagram 2 - `1S` `2S` `3S`**

#### 6.3.3 Protected Route Table

- Public subnets with local routes and routes to the NAT gateway.
- **Diagram 2 - `D` `E` `H`**

#### 6.3.4 Management Route Table

- Private subnets with local routes, and routes to the NAT gateway.
- **Diagram 2 - `1M` `2M` `3M`**

#### 6.3.5 Database Route Table

Private subnets with local routes, and routes to the Endpoints.

- **Diagram 2 - `1S` `2S` `3S`**

### 6.4 Private Endpoints

#### 6.4.1 **Virtual Private Cloud (VCP) Endpoints**

- Private subnets with local routes to ALB, Secure Tier Subnets, and routes to the NAT gateway.
- **Diagram 2: `1M` `2M` `3M`**

![Alt text](<Tables/Picture 11 - VPC Route Table New.png>)

A Virtual Private Cloud (VPC) in AWS is a virtual network that you define within the AWS cloud. It allows you to launch AWS resources like EC2 instances into a virtual network that you have defined.

- A VPC endpoint enables private connectivity between resources in your VPC and supported AWS services, without requiring public IP addresses or Internet Gateway.

- When you create a VPC endpoint, you specify an AWS service like S3, DynamoDB etc. that you want your VPC resources to privately access. AWS then creates an "endpoint" that serves as an entry point for traffic destined to the specified service.

- This allows resources in your VPC, like EC2 instances, to access the AWS service using a private IP address without going over the public internet. The communication happens privately within the AWS network.

- **Summary:** VPC Endpoint refers to creating a private connection/endpoint between your Virtual Private Cloud (VPC) and supported AWS services, to allow private connectivity without public IPs or internet access.

Associating an **EIP with an interface endpoint with your VPC** can provide a static, public IP address that resources in your VPC can use to access the endpoint service. This may be useful in some hybrid networking scenarios [[ℹ]](https://repost.aws/questions/QUIEQI_gnBSziGWFznpbBv0g/should-i-use-a-an-interface-vpc-endpoint-or-a-gateway-vpc-endpoint).

- Using an EIP could simplify your networking configuration if you need a static public IP for a resource to access an endpoint service, rather than dealing with private IP addressing and routing.

- **Summary** An EIP is not required for basic VPC endpoint functionality. But it could provide benefits in some hybrid or multi-VPC architectures where a static public IP is useful. an EIP incurs ongoing costs. Consider your specific use case and cost/complexity tradeoffs to determine if an EIP makes sense or if private addressing alone will suffice [[ℹ]](https://repost.aws/questions/QUf38Wtw7qTLOHeU-aiLHbfg/aws-vpc-end-point).

### 6.5 Mount Targets

#### 6.5.1 Amazon Elastic File System File System (EFS)

- The **Mount target for EFS** allows a mount target in each Availability Zone from which you want to access the file system in the secure database subnets [[ℹ]](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html).
- **Diagram 2 - `1S` `2S` `3S`**

![Alt text](<Tables/Picture 10 - Mount Targets for Amazon EFS File System New.png>)

An **EFS Mount Target** represents the endpoint within an Availability Zone that provides access to your file system. Mount targets are associated with subnets in each AZ where you want file system access.

- The Route Table controls the routing of traffic between subnets and resources within subnets. It dictates where network traffic from a subnet is directed.

- Mount targets are referenced in Route Tables using Network Access Control Lists (ACLs) to control which subnets can access the file system via the mount target endpoint.

**Mount Target IP Address:** Mount Targets provide private connectivity between your VPC and the EFS service, so public IP addresses are not strictly required. However, associating an EIP with a mount target could allow resources to access the file system using a static public IP, which may be useful for hybrid networking designs where public accessibility is needed [[ℹ]]( https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-ip-addr.html ) [[ℹ]]( https://docs.aws.amazon.com/efs/latest/ug/API_CreateMountTarget.html).

## 7. Security Groups

Security groups control network access and which resources are allowed to communicate on specific ports, at the instance-level.

- Separating access between public/private subnets and resources.
- The Endpoint Tables below display the security groups that are associated with the Virtual Private Cloud endpoint, **`vcp-id-bob`**, and allowed to access the endpoint.
- New VPC Design: _“AWS re/Start, Assignment 2 security groups_ are associated with the Network Infrastructure shown in **`Diagram 2`**

### 7.1 Public Subnet Security Groups

#### 7.1.1 **Internet Gateway (IGW)**

- The **Internet Gateway security group** allows traffic into the local network from the internet and directs traffic to the Network Firewall Endpoints.

![![Alt text](<Tables/Picture 7 - IGW New.png>)](<Tables/Picture 7 - IGW Ingress Egress Local New.png>)

#### 7.1.2 Firewall

- The **Firewall security group** allows traffic into the local network from the internet and lets traffic out of the local network to AZs or the internet.

![Alt text](<Tables/Picture 2 - Firewall New.png>)



#### 7.1.2 Load balancer

- The **Application Load Balancer** security group allows traffic from the Application Load Balancer over the listener port and protocol. It also allows health check traffic.

![Alt text](<Tables/Picture 1 - ALB New.png>)

#### 7.1.3 Protected

- The **Protected subnet security group for the web servers** allows traffic to and from the Application Load Balancer.

![Alt text](<Tables/Picture 3 - Protected New2.png>)

### 7.2 Private Subnet Security Groups

#### 7.2.1 Multipurpose

- The **Multipurpose subnet security group for the webservers** allows traffic to and from the application Load balancer, the public webservers, and the private webservers.

![Alt text](<Tables/Picture 4 - Multipurpose New2.png>)

#### 7.2.2 Secure

- The **Secure subnet security group** allows traffic from the private subnet web servers.

![Alt text](<Tables/Picture 4 - Secure New.png>)

#### 7.2.3 Management

- The **Management subnet security group** allows traffic to and from the Protected web servers.

![Alt text](<Tables/Picture 6 - Management New.png>)

### 7.4 Private Database Subnets

#### 7.4.1 Relational Database Service (RDS)

- The **RDS Database security group** rules allow the database servers to receive read and write requests from the web servers.

- The **Database servers** run in the private subnets and receive traffic from the Management web servers.

![Alt text](<Tables/Picture 5 - Database New.png>)

Amazon RDS is a managed database service provided by Amazon Web Services. It makes it easier to set up, operate, and scale a relational database in the cloud [[ℹ]](https://aws.amazon.com/blogs/database/amazon-rds-snapshot-restore-and-recovery-demystified/).

- RDS supports popular database engines like MySQL, PostgreSQL, MariaDB, Oracle, SQL Server and more. This allows you to use the same database engine you may already be familiar with.
- It offers automated provisioning, patch management, backups, and recovery capabilities. This eliminates the need to manage the underlying database software, operating system and infrastructure yourself.
- RDS databases can be scaled up or down quickly as your application needs change, avoiding over or under provisioning of resources.
- Security, networking, storage and replication features help meet the needs of mission-critical databases in production environments.
  Pricing is on a pay-as-you-go model based on the database instance's class, storage size, backup storage usage and data transfer rates.

### 7.5 Public Endpoints

#### 7.5.1 EC2 Instance Connect (EIC) Endpoint Security Group

- **EIC Endpoint Security Group** allows instances connected via the EIC endpoint to reach the database on the appropriate ports.
- **Diagrams 3 & 4 - `D` `K`**

![Alt text](<Tables/Picture 8 - EIC Endpoint Security Group New.png>)

**EIC Endpoints** for Identity and Access Management (IAM) allow you to securely access IAM resources within a VPC without an internet gateway, NAT device, VPN connection or AWS Direct Connect.

With AWS EIC, you can create a VPC endpoint that allows IAM resources like users, groups, roles, and policies to be accessed privately by applications within your VPC. This avoids exposing IAM resources to public internet access [[ℹ]]( https://aws.amazon.com/iam/identity-center/features/).
Some key benefits of AWS EIC include:

- Private access to IAM from your VPC without public IPs or internet connectivity.
- Increased security since IAM traffic stays within your AWS infrastructure.
- Potential performance improvements compared to internet-based calls to IAM APIs.
- Supports use cases that require private access for compliance or security reasons

### 7.6 Private Endpoints

#### 7.6.1 Amazon Virtual Private Cloud (VCP) Endpoints Security Group

- **VPC Endpoint Security Group** allows instances connected via the VPC endpoint to reach resources on the appropriate ports [[ℹ]]( https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/vpc-endpoints.html).
- **Diagram 2 - `1M` `2M` `3M`**

![Alt text](<Tables/Picture 12 - VPC Endpoints Security Group New.png>)

## 8. Security Policy

### 8.1 AWS Identity and Access Management (IAM)

The **IAM Policy** controls access to launch instances, modify networking configurations, manage databases, etc.

- IAM Security policy limits permissions based on ‘the principle of least privilege.’
- Least privilege means a User whom is in two or more Group with different levels of privilege attached to it, the User will automatically receive the lowest level privilege of those Groups.

## 9. Autoscaling Policy

The **Autoscaling policy** is attached to EC2 subnets in the Auto Scaling Group(s).It allows an Auto Scaling Group to dynamically scale up or down, the number of EC2 instances, based on demand. There are different policy types [[ℹ]]( https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) [[ℹ]]( https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html):

### 9.1 Target Tracking Policy

Automatically scales capacity to match a specific target value for a CloudWatch metric (e.g. CPU utilization) to keep average usage within a defined range.

### 9.2 Step Scaling Policy

Adds/removes capacity based on defined thresholds/cooldown periods for ‘CloudWatch alarms,’ for specific metrics. For example, database request counts.

End.

---

---

# Part II.2 - Expansive network design questions

## II.2.a Inconvenient/Convenient

### (5/30 marks)

To answer in file `Part II/Answer.md` and draw additional figures:

- How would you add access for the EC2 instances to S3 and DynamoDB?
  - Least convenient method explained only get 1/5 marks
  - Most convenient method explained will get 2/5 marks
  - Explain and correctly illustrate the most convenient method and all added components will get full 5/5 marks

# 2.II.2.a Answers

**Objective:** How to add access for the Amazon Elastic Compute Cloud (Amazon EC2) instances to Amazon Simple Storage Service (S3) and DynamoDB to connect to an instance within your Amazon Virtual Private Cloud (Amazon VPC) over the Internet [[ℹ]](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc-endpoints-dynamodb.html)[[ℹ]](https://repost.aws/questions/QUN54ZAARaQjSKRGgg-qPnog/can-t-connect-to-local-dynamodb-even-though-port-8000-is-reachable);
**2.II.2.a.1 Least convenient method**
**2.II.2.a.2 Most convenient method**

## 2.II.2.a.1 Least Convenient Method: Bastion Host

### 2.II.2.a.1.1. Method

To Secure Access for EC2-Instances to S3-DynamoDB-Recources, typically, you’d first have to connect to a bastion host with a public IP address that your administrator set up over an Internet Gateway (IGW) in your VPC, and then use port forwarding to reach your destination.

##### You need:

- an Internet Gateway in your VPC,
- a public IP address on your resource,
- a Bastion Host, or any agent to connect to your resources.

### 2.II.2.a.2.1. Justification

Based on the information provided, using a bastion host approach as described would generally be considered a less optimal method for allowing EC2 instances to access S3 and DynamoDB resources for a few key reasons.[[ℹ]](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc-endpoints-dynamodb.html) [[ℹ]](https://repost.aws/questions/QUN54ZAARaQjSKRGgg-qPnog/can-t-connect-to-local-dynamodb-even-though-port-8000-is-reachable):

- Bastion Host introduces additional points of failure with the bastion host itself that need to be managed and secured. If the bastion host becomes unavailable, access is disrupted.

* Bastion hosts are not AZ-failure resilient. A failure in one AZ impacts all.

- True high availability across Availability Zones cannot be achieved since the bastion host is a single point of access and management.

* Multiple bastion hosts would need to be deployed across AZs to improve resilience, increasing complexity and management overhead. A VPN connection could provide cross-AZ connectivity but adds further complexity.

- Costs are increased due to needing additional EC2 instances for the bastion hosts as well as a public IP address and Internet Gateway for external access.

#### 2.II.2.a.1.3. Options/Recommendations

A more robust and scalable approach would be to configure VPC security groups and IAM roles/policies to allow direct private access from the EC2 instances to S3 and DynamoDB without requiring public endpoints or bastion hosts.

- This simplifies configuration/management and improves availability, security and costs.
- Private VPC endpoints could also provide secure connectivity without public resources if needed.

# 2.II.2.a.2. Most Convenient Method: EC2 Instance Connect (EIC) + Identity & Access Management (IAM)

To Secure Access for EC2-Instances to S3-DynamoDB-Recources today, we can use the Command Line Interface (CLI) to launch an Amazon EC2 Instance Connect (EIC) Endpoint, a new feature (since June 2023) allows you to connect securely to your instances from the Internet.
EIC Endpoint combines identity-based and network-based access controls, providing the isolation, control, and logging needed to meet your organization’s security requirements [[ℹ]](https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/).

# 2.II.2.a.2.1. Justification

The key benefit of this approach is that it centrally manages access outside the instances, avoiding the need to hardcode or distribute credentials directly to each EC2 host. Updates are easy - just modify the role policy. This provides the most seamless integration of IAM with EC2 for S3 and DynamoDB access.

- You do not need SSH keys to use an EC2 Instance Connect Endpoint. You can control access using IAM policies and audit connection requests with CloudTrail [[ℹ]](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html).

* The AWS CLI or Console can be used to create an EIC Endpoint.

- When launching instances, place them in private subnets with no public IP access. Create an IAM role granting instances permissions to access resources and attach it to the instances.

* No internet gateway or NAT device is required since communication occurs privately in the VPC. VPC security groups allow ingress from instances to endpoints like S3 or DynamoDB on port 443.

- When an application on an instance makes a request to another service, the attached IAM role credentials are used to authenticate the request. Responses are then routed privately back to the originating instance.

* This allows access restricted to only permitted resources defined in the IAM role, without exposing instances publicly. EIC offers a simple, secure method for SSH access and identity-based access control to AWS services from EC2 instances.

### 2.II.2.a.2.2. Method

0. Check the EC2 Prerequisites before you start [[ℹ]](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-endpoint-prerequisites.html)
1. Create a VPC endpoint in your VPC. When creating the endpoint, select "EC2 Instance Connect Endpoint" as the service category.
2. Associate the endpoint with a security group. This controls access to the endpoint.
3. Select the subnet where you want the endpoint to be available.
4. Optionally add tags for identification and organization.
5. Review the settings and create the endpoint. It may take a few minutes to become available.
6. Launch EC2 instances into private subnets associated with the endpoint's subnet.
7. Create an IAM role and policy granting instances permission to use EIC; Attach the appropriate S3 and DynamoDB permissions policies (For example, the `AmazonS3FullAccess` and `AmazonDynamoDBFullAccess` policies). When you create an EC2 Instance Connect Endpoint, the service-linked role named `AWSServiceRoleForEC2InstanceConnect` and the managed policy named `EC2InstanceConnectEndpoint` are automatically created in your AWS account, and the managed policy is automatically attached to the service-linked role.
8. Attach the IAM role to your instances at launch. When launching new EC2 instances, select the IAM role from the step above in the configuration. The EC2 instances will now have access to call the S3 and DynamoDB APIs without needing to manage access keys separately. Credentials are delivered through the instance profile service at runtime.
9. Install the EC2 Instance Connect package on Linux instances to enable EIC functionality.
10. You can now use the EC2 console to connect to instances via EIC without a bastion host or public IP access.

Test: To verify, you can install and run the AWS CLI on an instance. Commands like `aws s3 ls` or `aws dynamodb list-tables` should now work without additional configuration [[ℹ]](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-instance-connect-endpoints.html)

## 2.II.2.a.2.3. Security

Use EIC Endpoints for secure access from EC2-Instances to S3-DynamoDB-Recources.

- IAM authorization is required to create the EIC Endpoint and also to make a connection. This is good because you can rely on network access controls like, security groups [[ℹ]](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-instance-connect-endpoints.html)

## 2.II.2.a.2.3.1 Route Table

- The **EIC Endpoint Route Table** with - Multi-Availability Zone capability,
- **Public-Subnet-to-Private-Subnet** routes across AZs [[ℹ]](https://docs.aws.amazon.com/managedservices/latest/appguide/about-security-groups.html) [[ℹ]](https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/) [[ℹ]](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/eice-security-groups.html).
- `Diagram 3`. Please refer to Diagram 3 in the last section of document, 2.II.2, part: a, to see an example architecture diagram.

[Almost the Most Convenient Method: Public EIC E](Answer.md) ![Public Subnet](<Tables/Picture 8 - EIC E Route Table New.png>)

## 2.II.2.a.2.3.2 Security Group

# 2.II.2.a.2.3.2.1 Public EIC Endpoints - Almost the Most Convenient Method

Table - showing EIC Endpoint Security Group
![Alt text](<Tables/Picture 8 - EIC Endpoint Security Group New.png>)

Inbound Traffic:

- An EIC endpoint allows secure remote connections to EC2 instances in **`public or private subnets`** from outside the VPC.

* It controls access at the transport layer, **`TCP ports 22 for SSH and 3389 for RDP`**.

- EIC Endpoint does not handle application layer protocols.

* The security group for an EIC endpoint only allows security group rules for inbound remote connections on ports 22 and 3389.

- All `outbound traffic` is directed by the network security group of the instance/resource the EIC Endpoint is connected to.

* Configure an EIC Endpoint Route Table to access instances/resources which already have access to thing you need (i.e. RDS Database) in your VPC.

- Configure other instances/resources to allow EIC Endpoint inbound traffic and forward outbound traffic, `TCP ports 22 for SSH and 3389 for RDP`, using Security Group settings for a public or private subnet.

Outbound Traffic:

- Port **`3306`** to allow connections from the EIC endpoint to the RDS database security group for MySQL/Aurora access.

* Port **`443`** to allow HTTPS connections in case the database supports encryption.

- Port **`22`** to allow SSH connections if managing EC2 instances in the private subnet. [[ℹ]](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/eice-security-groups.html) [[ℹ]]( https://repost.aws/questions/QUq15T_5DQTaC9mgTzWqsVxA/if-i-modify-the-port-from-22-to-2222-in-the-secure-instance-connect-feature-with-the-correct-configuration)

No additional ports need to be opened since health checking and load balancing are not applicable roles for an EIC endpoint.

# 2.II.2.a.2.3.2.2 Private EIC Endpoints - the Most Convenient Method

This allows instances connected via the EIC endpoint to reach the database on the appropriate ports [[ℹ]](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc-endpoints-dynamodb.html) [[ℹ]](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/06/12/ec2-instance-connect-endpoint.drawio-1.png).

- You don’t need a security group for the load balancer,
- a security group for the web servers,
- or a security group for the database servers [[ℹ]](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/network-isolation.html)

* For example, given EIC Endpoint was configured in the Management Tier, no other ingress rules would be needed since the management subnet should have access to the private subnet, secure resource: RDS Database
* `Diagram 4`. Please refer to Diagram 4 in the last section of document, 2.II.2, part: a, to see an example architecture diagram.

## 2.II.2.a.2.3.2.3 Destination/Target Security Group

For the security group of the private subnet with access to the database instances, add inbound rules allowing access from the security group of the EIC endpoint on ports 3306/443.

Example A:

- Source: Security group of the EIC endpoint
- Protocol: TCP
- Port Range: 3306
- Description: Allow MySQL/Aurora access from EIC endpoint

Example B:

- Source: Security group of the EIC endpoint
- Protocol: TCP
- Port Range: 443
- Description: Allow HTTPS access from EIC endpoint

# 2.II.2.a.2.4 Diagram 3 & 4 Showing - EC2 Instance Connect (EIC)

The following diagrams show how to use EIC Endpoints for secure access from EC2-Instances to S3-DynamoDB-Recources.

- Public Subnet: Diagram 3
- Private Subnet: Diagram 4

![Alt text](<Diagram 3 & 4 - Showing EIC E Public & Private Subnets New.png>)

Diagram showing - API services leverage private networking, VPC interfaces, and internal communication protocols rather than accessing each other directly from the public internet [[ℹ]]( https://blog.oyetolataiwo.com/deciding-your-software-architecture) [[ℹ]]( https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/http-api.html.).

- API services running in the "Multi-Purpose Tier"
- Private subnets communicate with each other using private IP addresses over the internal VPC network.

End.

---

---

# Part II.2 - Expansive network design questions

**(30/100 Marks)**

# Summary

##### II.2.b. showing - Intra-service communication (Green arrows)

Communication between instances in the "Multi-Purpose Tier" private subnets belonging to the same Auto Scaling Group. For example, instances from ASG 1 to ASG 1.

##### II.2.c. showing - Outbound internet access (Orange arrows)

Instances in the "Multi-Purpose Tier" private subnets reaching out to Google Maps API on the public internet, going through the ALB and NAT Gateway in the "Protected Tier" public subnets.

##### II.2.d. showing - Inbound client access (Blue arrows)

Public internet clients reaching the ALB in the "Protected Tier", which forwards requests to instances in the "Multi-Purpose Tier" private subnets.

Network Firewall inspecting traffic at the boundary of each tier, and the databases/file systems residing privately in the "Secure Tier".

End.

---

---

# II.2.b - APIs and Network Flow Diagrams

(5/30 Marks)

# II.2.b. Answers

## II.2.b.1. Intra-service communication (Green arrows)

##### 1. Intra-service communication (Green arrows)

Communication between instances in the "Multi-Purpose Tier" private subnets belonging to the same Auto Scaling Group. For example, instances from ASG 1 to ASG 1.

In the diagram below, API services leverage private networking, VPC interfaces, and internal communication protocols rather than accessing each other directly from the public internet [[ℹ]]( https://blog.oyetolataiwo.com/deciding-your-software-architecture).

### II.2.b.2. Summary

- The firewall inspection allows traffic through based on security groups and policies.
- The ALB distributes to backend targets in the protected tier.
- VPC interfaces and Route 53 (optional) facilitate private connectivity and addressability of protected resources [[ℹ]]( https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/http-api.html.).
- API services running in the "Multi-Purpose Tier" private subnets would likely communicate with each other using private IP addresses over the internal VPC network.

### II.2.b.3. Diagram - Showing Green Arrows

- `Diagram 5A` - Intra-service Communication via Private API From 1 API Service to Another (Green Arrows).
- `Diagram 5B`- Alternative View.

![Alt text](<Diagram 5A & 5B - Intra-service communication (Green arrows).png>)

#### II.2.b.3.1. Reference Items for Diagram (A-to-E)

**Firewall API** is used to configure rules allowing traffic through the firewall between the subnets, such as allowing inbound traffic from the internet to the protected tier [[ℹ]]( https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Firewall.html).
Diagram 5A: **B**

**Auto Scaling Group API** communication between Instances in the Multipurpose Tier, and instances in the Secure Tier ASG 1 to ASG 1 [[ℹ]]( https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html) [[ℹ]]( https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-auto-scaling-groups-aws-sdks.html)
Diagram 5A: **D**

**Elastic Load Balancing API** the Application Load Balancer, in the protected tier, distributes traffic to targets (EC2 instances) after being inspected by the firewall [[ℹ]]( https://docs.aws.amazon.comautoscalingec2API_AutoScalingGroup.html)
Diagram 5A: **C**

**VPC Endpoint services APIs** are used to privately connect services like S3, DynamoDB etc. to resources in the protected tier without going through the firewall [[ℹ]]( https://jayendrapatil.com/aws-application-auto-scaling/) [[ℹ]](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html?did=pg_card&trk=pg_card).
Diagram 5A: **E**

**Route 53 API** maps public DNS names to resources addressed in the protected tier, like the ALB load balancer [[ℹ]](https://docs.aws.amazon.com/architecture-diagrams/latest/multi-region-api-gateway-with-cloudfront/multi-region-api-gateway-with-cloudfront.html?did=wp_card&trk=wp_card).
Diagram 5A: **A**

#### II.2.b.3.2. Opportunities/Recommendations

##### II.2.b.3.2.1. **Autoscaling**

- A target tracking scaling policy to keep average CPU usage of an Auto Scaling group between 30-50%. This would scale the number of EC2 instances up or down as needed.

- A step scaling policy to add/remove instances at certain thresholds, like if CPU goes above 80% add 2 instances, above 90% add 3, etc.

- A scheduled action to scale an ECS service from 2 to 10 tasks every night at midnight.

- The API also lets you register and manage scalable targets, view scaling activity history, and suspend/resume automatic scaling as needed.

#### II.2.b.3.2.2. Communication

- A message broker could be used to asynchronously communicate between services via queued messages [[ℹ]]( https://medium.com/@bramkel/so-what-is-mqtt-b3982db33ca2).

- A service mesh could provide internal load balancing, discovery and traffic management between services [[ℹ]]( https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/synchronous-data-mesh-for-graphql-queries-ra.pdf?did=wp_card&trk=wp_card).

- A data access layer like Amazon DynamoDB or Amazon RDS could act as a common data store accessed by all services using a database driver/client.

- Logging/monitoring services like Amazon CloudWatch Logs could be used to share diagnostic data between services in a centralized manner [[ℹ]]( https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-multiple-stack-applications-using-aws-cdk-with-typescript.html?did=pg_card&trk=pg_card).

#### II.2.b.3.2.2.1. Methods:

- HTTP/REST APIs exposed by each service and accessed internally. This is a common way for microservices and containerized applications to communicate [[ℹ]]( https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html?did=pg_card&trk=pg_card).

- API services running in the "Multi-Purpose Tier" private subnets would likely communicate with each other using private IP addresses over the internal VPC network.
  Some possible communication methods include:

- HTTP/REST APIs exposed by each service and accessed internally. This is a common way for microservices and containerized applications to communicate [[ℹ]]( https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html?did=pg_card&trk=pg_card).

#### II.2.b.3.2.2.2. Table showing - different features of REST API and HTTP API

![Alt text](<Tables/Picture 13 - Rest APIs Etc New.png>)

End.

---

---

# Expansive network design questions

## Section II.2.c Outbound (Orange Arrows)

**(5/30 marks)**

# Answers

This image shows instances in the "Multi-Purpose Tier" private subnets reaching out to Google Maps API on the public internet, going through the ALB and NAT Gateway in the "Protected Tier" public subnets.

**"Thing"**

- Web app used by staff and employers for workforce management tasks; For example, "clock-in/clock-out" at the start and end of their shift at work.

Geofencing

- Geofencing rules set by Employers include: locations of work.
- This means staff can only "clock in" once they are within the boundaries set by their employer (geographical parameters their dedicated place of work).

API

- The API can send webhook notifications to an SNS topic when geofencing rules are met, such as checking in/out of a shift location [[ℹ]](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/services-sns.html).
- Google Maps Geocoding API can detect when a staff member is within defined boundaries, at the time of shift start/end.
- API services running in private subnets can subscribe to an SNS topic using the SNS/SQS subscriber type for the location.
- This allows the outbound API call while keeping services securely in private subnets, with traffic inspected by the network firewall.

SNS Notifications

- SNS notifications could include details like user, location, time which is published to subscribers.
- SNS Notifications to the Local Network(s) can be triggered by Google API Webhooks.
- The webhooks act as a trigger to initiate data retrieval from external APIs, with SNS helping reliably deliver notifications between geofencing, applications and services across the VPC.

SNS Topics

- SNS Topics Include "emergency alerts." i.e. someone doesn't show up for a shift, natural disasters, covid tracers et.
- Geographical data (location, time, date) in addition to qualitative HR and rostering costing data.

Data sources

- Meaningful data is assembled/organised, and combined with data sources from networked locations, on and off premise.
- scheduled/unscheduled
- on demand/periodic

### Diagram showing - outbound internet access from API services to Google Maps

![Alt text](<Diagram 6 - Outbound (Orange arrows).png>)

**API Traffic**

- Diagram 6: **1** One of the Auto Scaling groups launching API services/microservices in the "Multi-Purpose Tier" private subnets.

* Diagram 6: **2** An Application Load Balancer in the "Protected Tier" public subnets that routes traffic to the API services.

- Diagram 6: **3** A NAT Gateway in the "Protected Tier" allowing outbound internet access from the private subnets.

* Diagram 6: **4** Orange arrows showing traffic flowing from an API service instance through the ALB/NAT Gateway to the public internet.

* Diagram 6: **5** Google Maps API endpoint on the public internet where the services retrieve additional map data.

- Diagram 6: **6** The AWS Network Firewall inspecting and allowing outbound traffic at the boundary of each tier.

##### Traffic from the application to the internet (orange arrows):

1. Traffic is sent to the Gateway Load Balancer endpoint as a result of the default route configured on the application server subnet.
2. Traffic is sent to the Gateway Load Balancer, which distributes the traffic to one of the security appliances.
3. Traffic is sent back to the Gateway Load Balancer endpoint after it is inspected by the security appliance.
4. Traffic is sent to the internet gateway based on the route table configuration.
5. Traffic is routed back to the internet.

End.

---

---

# Part II.2 - Expansive network design questions

## II.2.d - Inbound Traffic (Blue arrows)
**(5/30 marks)**

# II.2.d Answers

## II.2.d.1. Inbound client access (Blue Arrows)

Public internet clients reaching the ALB in the "Protected Tier", which forwards requests to instances in the "Multi-Purpose Tier" private subnets.

- Showing how the Network Firewall inspecting traffic at the boundary of each tier, and the databases/file systems residing privately in the "Secure Tier".

##### II.2.d.2 Inbound client access (Blue arrows)
![Alt text](<Diagram 9 - Ingress Traffic (Blue Arrows).png>)

Public internet clients reaching the ALB in the "Protected Tier", which forwards requests to instances in the "Multi-Purpose Tier" private subnets.

- Network Firewall inspecting traffic at the boundary of each tier, and the databases/file systems residing privately in the "Secure Tier".

Traffic from the internet to the application (blue arrows):

1. Traffic enters the service consumer VPC through the internet gateway.
2. Traffic is sent to the Gateway Load Balancer endpoint, as a result of ingress routing.
3. Traffic is sent to the Gateway Load Balancer, which distributes the traffic to one of the security appliances.
4. Traffic is sent back to the Gateway Load Balancer endpoint after it is inspected by the security appliance.
5. Traffic is sent to the application servers (destination subnet).

This illustrates how the API services can retrieve external data despite being in private subnets, by routing through the load balancer and NAT Gateway in the public tier.

Reference/Example https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html



# Part II.3. - Bonus design questions

**(bonus 5 marks)** To answer in file Part II/Part II.1/Bonus.md and draw additional figures:
(3 marks) If you were to adopt a container orchestration engine and an associated compute engine on AWS to replace EC2 and AutoScalingGroup:

- **`a`** What would you use?
- **`b`** Why do you think you would like to work with your selected option based on your personal preference?
- **`c`** Which benefits would you gain over EC2 combined with AutoScalingGroup?
- **`d`** Can you illustrate how your new infrastructure design would look like?
  (1 mark)
- **`e`** What problem does Service Discovery solve?
- **`f`** What is the Service Discovery AWS offering for your Container Orchestration and Compute option?

# Answer

Here are my thoughts on adopting a container orchestration engine and compute engine to replace EC2/Auto Scaling in this architecture:

- **`a`**. I would use Amazon Elastic Kubernetes Service (EKS) to run Kubernetes and AWS Fargate as the serverless compute engine.

* **`b`**. I'm most familiar and comfortable with Kubernetes as the leading container orchestration tool. EKS makes it easy to set up and manage Kubernetes clusters on AWS without having to stand up the underlying infrastructure myself
  - Fargate would remove the need to provision and manage EC2 instances.
  - It allows me to focus on building and scaling containerized applications without worrying about servers.
  - This serverless model lowers operational overhead.

- **`c`**. Benefits over EC2 include:
  - Speed [[ℹ]](https://docs.aws.amazon.com/whitepapers/latest/docker-on-aws/container-benefits.html).
  - Consistency, less buggy software.
  - Density and resource efficiency due to Amazon ECS compute and container placement strategy.
  - Portability via containers, since applications would be containerized.
  - No servers to manage, not having to patch/manage EC2 instances.
  - Increased density, by running containers together on shared infrastructure.
  - Fargate further reduces costs. Specificallly, by paying only for actual container usage and the need to provision servers.

* **`d.1`**. If I were to adopt a container orchestration engine and associated compute engine on AWS to replace EC2 and AutoScalingGroup, the architecture would be similar with EKS clusters running in private subnets and Fargate tasks/pods replacing EC2 instances. References on setting this up include the AWS documentation on EKS and Fargate integration as well as blogs demonstrating sample architectures [[ℹ]]( https://docs.aws.amazon.com/whitepapers/latest/docker-on-aws/containers-orchestrations-on-aws.html)[[ℹ]]( https://aws.amazon.com/what-is/kubernetes-cluster/)[[ℹ]](https://k21academy.com/docker-kubernetes/amazon-eks-kubernetes-on-aws/).

  - I would use Kubernetes and Fargate using Amazon RDS and EKS to replace EC2/Auto Scaling in this baseline architecture:

  * Create an EKS cluster spanning the VPC subnets. Deploy Kubernetes control plane and worker nodes.

  - Store application configuration and secrets in RDS/EFS accessed via Kubernetes APIs.

  * Deploy apps to EKS Fargate pods without managing servers. Load balance via EKS ALB/NLB.

- **`d.2`** The architecture would be similar - EKS clusters in private subnets, Fargate pods replacing EC2 instances. RDS would reside in private subnets accessed securely via EKS.

* **`d.3`** _An illustrated example:_
* Public Subnets:
  - ALB/NLB
  - NAT Gateway

- Private Subnets:
  - EKS worker nodes
  - Fargate pods
  - RDS instances
  - EFS volumes

### Diagram Y showing - Kubernetes Customer VPCs "Zoom View"

![Alt text](<Kubernetes Y.png>)

### Diagram 8 showing - Kubernetes Architecture Overview

![Alt text](<Diagram 8 - Kubernetes EKS v1.png>)

### Diagram Z showing - Kubernetes Local VPC "Zoom View"

![Alt text](<Kubernetes Z.png>)


- **`e`** Service discovery solves the problem of applications and microservices needing to find each other. As services are dynamically added and removed from a distributed system, they need a way to publish their location and identify other available services.

* **`f`** For Amazon EKS and AWS Fargate, the service discovery offering is Amazon Route 53. Route 53 is a highly available and scalable cloud DNS service that is designed to give applications a reliable and cost effective way to route end users to internet applications. With Route 53, services can register themselves with a domain name to be discovered. It also supports health checking to route traffic only to healthy endpoints. This integrates nicely with the dynamic and ephemeral nature of containers on EKS and Fargate.

- In the proposed architecture replacing EC2/Auto Scaling with EKS and Fargate, Route 53 would allow containerized services and microservices to dynamically register and discover each other as tasks/pods are scheduled across subnets and availability zones. This provides the service discovery capabilities needed for inter-service communication in a containerized application deployed on AWS [[ℹ]](https://aws.amazon.com/what-is/kubernetes-cluster/) [[ℹ]](https://aws.amazon.com/blogs/machine-learning/build-flexible-and-scalable-distributed-training-architectures-using-kubeflow-on-aws-and-amazon-sagemaker/) [[ℹ]](https://aws.amazon.com/blogs/machine-learning/tag/amazon-elastic-kubernetes-service/) [[ℹ]](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service-for-kubernetes/) [[ℹ]](https://www.xenonstack.com/blog/kubernetes-architecture-components

---

# REFERENCES
## AWS Whitepapers
Building a Scalable and Secure Multi-VPC AWS Network Infrastructure

## AWS Blogs
Centralize access using VPC interface endpoints to access AWS services across multiple VPCs
Integrating AWS Transit Gateway with AWS PrivateLink and Amazon Route 53 Resolver
Simplify DNS management in a multi-account environment with Route 53 Resolver

## AWS Documentation
https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/using-nat-gateway-with-firewall.html
https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/
Configure VPC i.e. Gateway Load Balancer Endpoint (blue & yellow arrows): https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#gateway-route-tables  https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html
https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html
Amazon VPC quotas/ Limits: https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html
https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/inspection-deployment-models-with-AWS-network-firewall-ra.pdf
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-cross-zone.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html
https://aws.amazon.com/blogs/architecture/automating-multi-az-high-availability-for-weblogic-administration-server/
https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html
https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall-with-vpc-routing-enhancements/
https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ 
https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-key-considerations-and-best-practices/
https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/
Multi-AZ VPC for web and database servers: https://aws.amazon.com/rds/features/multi-az
Routing: https://medium.com/@mda590/aws-routing-101-67879d23014d
Rout Tables: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
CDIR: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html
Subnet Sizing https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html#subnet-sizing-ipv4
elastic ip webserver: https://aws.amazon.com/blogs/architecture/automating-multi-az-high-availability-for-weblogic-administration-server/
https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html
Elastic https://www.elastic.co/blog/secure-elastic-cloud-deployment-aws-privatelink-traffic-filter
Network Address Usage Calc: https://docs.aws.amazon.com/vpc/latest/userguide/network-address-usage.html
https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall-with-vpc-routing-enhancements/
An Elastic IP address: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html 
Routing AWS https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
Target Groups i.e. ALB: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-type
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html
Security Groups for ALB: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html
EC2 Jump Host: https://dev.to/aws-builders/aws-bastion-host-jump-box-5h87
EC2 Instance Connect vs. SSM Session Manager: https://carriagereturn.nl/aws/ec2/ssh/connect/ssm/2019/07/26/connect.html
Use AWS PrivateLink to set up a VPC endpoint for Session Manager: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-privatelink.html
Tunning into VPC (as opposed to Jump Host): https://carriagereturn.nl/aws/ssh/ssm/2021/01/03/tunnel-into-vpc.html
SSH connections through "Session Manager": https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html
AWS "Systems Manager" console: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
(Optional) Enable and control permissions for SSH connections through Session Manager: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html
Control session access to managed nodes: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-restrict-access.html
Use cases and best practices for AWS Systems Manager capabilities: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-best-practices.html
(Optional) Use AWS PrivateLink to set up a VPC endpoint for Session Manager: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-privatelink.html
How do I create VPC endpoints so that I can use Systems Manager to manage private EC2 instances without internet access?: https://repost.aws/knowledge-center/ec2-systems-manager-vpc-endpoints
Use AWS SSM Session Manager Over PrivateLink: https://jackiechen.blog/2019/09/12/use-aws-ssm-session-manager-over-privatelink/
SSH Logging and Session Management Using AWS SSM and VPC Endpoint: https://www.linkedin.com/pulse/ssh-logging-session-management-using-aws-ssm-vpc-endpoint-singh/?trk=public_profile_article_view

### Enpoints (gateway, VPC, interface, private, ENI, S3, DynamoDB) 
AWS services that integrate with AWS PrivateLink
Amazon VPC quotas
Quotas for your transit gateways
Amazon Route 53 Quotas
Routing to a Gateway Load Balancer endpoint: https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-internet-gateway
Access an AWS service using an interface VPC endpoint: https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html

https://osamaoracle.com/2021/08/21/vpc-endpoints-and-aws-privatelink/
Centralize access using VPC interface endpoints: https://aws.amazon.com/blogs/networking-and-content-delivery/centralize-access-using-vpc-interface-endpoints/
EFS and Mount Targets: https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html
https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access.html
https://docs.aws.amazon.com/efs/latest/ug/resource-ids.html
EC2 Instance Connect (EIC)Endpoint: https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/
Privatelink: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html
S3 Endpoints: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html 
Create privatelink Interface Endpoint: https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html 
VPC endpoint overview: https://aws.amazon.com/blogs/architecture/choosing-your-vpc-endpoint-strategy-for-amazon-s3/
Types of endpoints S3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpointshtml#types-of-vpc-endpoints-for-s3
VPC Enpoints: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html
Gateway endpoints for Dynamo DB: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html
Free Gateway endpoints: https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html 
Configure free endpoint use: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html
Enpoint CLI: https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html
Gateway Load Balancer Endpoint: https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html
Enpoint non CDIR security: https://www.elastic.co/blog/secure-elastic-cloud-deployment-aws-privatelink-traffic-filter
https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html
https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html
EFS https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html
EC2: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_createVpc_section.html
routing https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
https://docs.aws.amazon.com/vpc/latest/userguide/intra-vpc-route.html
elsatic eips: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html
Security Groups: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html
Webserver Tutorial: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html
How to integrate Duo Single Sign-On across multiple accounts with AWS Managed Microsoft AD: https://shazi.info/how-to-integrate-duo-single-sign-on-across-multiple-accounts-with-aws-managed-microsoft-ad/
https://aws.amazon.com/products/databases/learn/
https://shazi.info/aws-rds-在各-instance-type-的-max_connections-的定義/
NAT Gateway setup for private servers: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html

## AWS Open Source Projects
https://github.com/aws-samples/quickstart-aws-vpc-3tier
https://github.com/aws-samples/aws-transit-gateway-connect-sample
https://github.com/aws-samples/cloudformation-shared-vpc-model
https://github.com/aws-samples/vpc-cidr-analysis
https://github.com/aws-samples/transit-gateway-with-shared-vpc-in-single-account-solution
https://github.com/aws-ia/terraform-aws-vpc
https://github.com/aws-samples/aws-tf-kms
https://github.com/aws-ia/terraform-aws-network-hubandspoke
https://github.com/aws-samples/vpc-endpoint-sharing
https://github.com/aws-samples/hub-and-spoke-with-inspection-vpc-terraform
https://github.com/aws-samples/aws-network-hub-for-terraform

## Diagrams
VPC private & Public NAT ALB: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html
Routing https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-two-zone-igw.html
Architecture with an internet gateway and a NAT gateway - AWS Network Firewall: https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-igw-ngw.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html
https://aws.amazon.com/architecture/reference-architecture-diagrams/
https://creately.com/guides/aws-architecture-diagrams-and-use-cases/
https://www.hava.io/blog/aws-vpc-diagram-generator.
https://support.microsoft.com/en-us/office/create-aws-diagrams-in-visio-138206bf-d10f-4583-9f31-885ce706af49
https://www.lucidchart.com/blog/how-to-build-aws-architecture-diagrams
https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/transitgateway_multicast_ra.pdf?did=wp_card&trk=wp_card 
https://www.jetbrains.com/help/datagrip/creating-diagrams.html#apply-colors-to-diagram-objects
https://aws.amazon.com/solutions/guidance/building-a-containerized-and-scalable-web-application-on-aws/?did=sl_card&trk=sl_card
https://dev.to/aws-builders/aws-architecture-diagrams-guidelines-595d
https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/06/12/ec2-instance-connect-endpoint.drawio-1.png
Instance type: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-type-advice.html
Cost Managment: https://us-east-1.console.aws.amazon.com/cost-management/home?region=us-east-1#/startupError?code=_CE_Not_Ready_&title=_CE_Not_Ready_Title_ 
Secure Connectivity from Public to Private, Introducing EC2 Instance Connect Endpoint & Diagram: https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/
Create an EC2 Instance Connect Endpoint: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-instance-connect-endpoints.html
Service-linked role for EC2 Instance Connect Endpoint: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/eice-slr.html
VPC endpoints to access DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc-endpoints-dynamodb.html
DynamoDB table from Spark SQL: https://repost.aws/questions/QUcXHuBMmnRoe1vEVt5dZu0A/questions/QUcXHuBMmnRoe1vEVt5dZu0A/how-to-access-a-dynamodb-table-from-spark-sql?
VPC Overview: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/network-isolation.html
VPC Endpoints: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/vpc-endpoints-dynamodb.html
DynaboDB Tutorial: https://aws.plainenglish.io/aws-tutorials-build-a-python-crud-api-with-lambda-dynamodb-api-gateway-and-sam-874c209d8af7
Can't connect to Dynabo DB: https://repost.aws/questions/QUN54ZAARaQjSKRGgg-qPnog/can-t-connect-to-local-dynamodb-even-though-port-8000-is-reachable

#AutoScaling 
Auto Scaling group launch templates: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/client/update_auto_scaling_group.html#
Tutorial: Set up a scaled and load-balanced application: https://docs.aws.amazon.com/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html
Diagram shows overview of multi-tier architecture deployed across 3 AZ: https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html
Applicaiton API Diagram: https://jayendrapatil.com/aws-application-auto-scaling/
https://www.rackspace.com/blog/ec2-auto-scaling-lifecycle-hook-not-so-fast
AWS Auto Scaling Diagram: https://www.aws.ps/10-things-to-consider-when-building-an-auto-scaling-architicture/
RESTful API Diagram, Amazon Simple Queue Service (SQS): https://aws.amazon.com/blogs/startups/scaling-on-aws-part-4-one-million-users/
Auto Scaling groups - Amazon EC2 Auto Scaling:
docs.aws.amazon.comautoscalingec2auto-scaling-groups.html
AutoScalingGroup - Amazon EC2 Auto Scaling:
docs.aws.amazon.comautoscalingec2API_AutoScalingGroup.html
AutoScalingGroupRecommendation - AWS Compute Optimizer:
docs.aws.amazon.comcompute-optimizerlatestAPI_AutoScalingGroupRecommendation.html
EC2 Autoscaling Groups Examples for creating and managing Auto Scaling groups with the AWS SDKs: https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-auto-scaling-groups-aws-sdks.html
EC2 CreateAutoScalingGroup EC2: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html
EC2 Autoscalling groups with multiple instance types and purchase options, EC2: Setup overview: https://docs.aws.amazon.com/autoscaling/ec2/userguide/mixed-instances-groups-set-up-overview.html 
Aurora and DynamoDB Autoscaling: https://jayendrapatil.com/aws-application-auto-scaling/

# APIs
AWS API Gateway: 

Application Load Balancer is deployed in a VPC that directs web traffic to a website target group or API Gateway target group: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html?did=pg_card&trk=pg_card
HTTP API private integration Diagrams & Examples: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/http-api.html
Amazon API Gateway Private Endpoints: https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/
HTTP API & Diagrams: https://docs.aws.amazon.com/whitepapers/latest/best-practices-api-gateway-private-apis-integration/http-api.html

Test API: https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/
HTTP APIs to AWS CloudMap example: https://aws.amazon.com/blogs/compute/configuring-private-integrations-with-amazon-api-gateway-http-apis/

SYS Manager: https://jayendrapatil.com/aws-auto-scaling-elb/#google_vignette
Moving Towards A Meaningful Set Of Icons For The API Community: https://apievangelist.com/2016/01/25/moving-towards-a-meaningful-set-of-icons-for-the-api-community/
Icons To Describe Each Of Your API Resources Like AWS: https://apievangelist.com/2016/10/21/icons-to-describe-each-of-your-api-resources-like-aws/
API Explorer: https://api.thenounproject.com/explorer
Diagram Optimize Amazon S3 for High Concurrency in Distributed Workloads: https://aws.amazon.com/blogs/big-data/optimizing-amazon-s3-for-high-concurrency-in-distributed-workloads/
Tutorial: Building a serverless chat app with a WebSocket API, Lambda and DynamoDB: https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html
Deploy an Amazon API Gateway API on an internal website using private endpoints and an Application Load Balancer: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html?did=pg_card&trk=pg_card
Configuring private integrations with Amazon API Gateway HTTP APIs: https://aws.amazon.com/blogs/compute/configuring-private-integrations-with-amazon-api-gateway-http-apis/
Tutorial: Build a CRUD API with Lambda and DynamoDB: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html
Tutorial: Building an HTTP API with a private integration to an Amazon ECS service: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-private-integration.html

# Google Maps API
Catalog of Architecture Diagrams: https://developers.google.com/maps/architecture
Get DynamoDB data with API Gateway and Lambda: https://bftnagoya.hateblo.jp/entry/2021/10/27/102826
How to get the GPS coordinates, around the solution we need additional AWS Lambdas and a database like Amazon DynamoDB.: https://vunvulear.medium.com/how-to-integrate-the-google-map-support-in-amazon-lex-7752e3d2c870
Car Pooling App Lamda and Google API: https://www.electromaker.io/project/view/ini-rider-a-car-pooling-application-using-thingy-91
Google Maps Platform AWS Vue.js Introduction of image registration verification system: https://bftnagoya.hateblo.jp/entry/2022/01/20/175437
https://bftnagoya.hateblo.jp/entry/2021/10/27/102826
Researchgate: https://www.researchgate.net/publication/327644181_Use_of_Crowdsourced_Travel_Time_Data_in_Traffic_Engineering_Applications
Basic Architecture: https://devpost.com/software/courtfind

# Kubernetes
What are Kubernetes fundamentals?: https://aws.amazon.com/what-is/kubernetes-cluster/

Kubernetes Diagrams: https://k21academy.com/docker-kubernetes/amazon-eks-kubernetes-on-aws/
Build flexible and scalable distributed training architectures using Kubeflow on AWS and Amazon SageMaker: https://aws.amazon.com/blogs/machine-learning/build-flexible-and-scalable-distributed-training-architectures-using-kubeflow-on-aws-and-amazon-sagemaker/
Amazon Elastic Kubernetes Service: https://aws.amazon.com/blogs/machine-learning/tag/amazon-elastic-kubernetes-service/
Amazon Elastic Container Service for Kubernetes: https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service-for-kubernetes/
Kubernetes - A Container Orchestration Platform: https://www.xenonstack.com/blog/kubernetes-architecture-components
Running TorchServe on Amazon Elastic Kubernetes Service: https://aws.amazon.com/blogs/opensource/running-torchserve-on-amazon-elastic-kubernetes-service/
API: https://docs.aws.amazon.com/eks/latest/APIReference/API_Operations_Amazon_Elastic_Kubernetes_Service.html
RDS Data API (Data API): https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html
EKS overview: Kubernete: https://aws.amazon.com/blogs/machine-learning/optimizing-tensorflow-model-serving-with-kubernetes-and-amazon-elastic-inference/
EKS: https://repost.aws/questions/QUX84N_2iSQm2WSvppog7auQ/elastic-kubernetes-service)
EKS luster ENdpoint: https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
# Aurora 
Using RDS Data API (Aurora): https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html
Using Amazon RDS Proxy for Aurora: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html
Creating an Amazon Aurora DB cluster: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html
# How To Guides
1): https://github.com/aws-samples/quickstart-aws-vpc-3tier
2) Create Network Shared Services (NSS) VPC in the target,single AWS account: https://github.com/aws-samples/aws-tf-nw-shared-svc
3) Deployment models for AWS Network Firewall with VPC routing enhancements: https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall-with-vpc-routing-enhancements/
4): https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-inbound-inspection.html 
5): https://aws.amazon.com/builders-library/static-stability-using-availability-zones/
6): https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html
7): PDF firewall options https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/inspection-deployment-models-with-AWS-network-firewall-ra.pdf
8): https://medium.com/edureka/aws-architect-interview-questions-5bb705c6b660 
9) Routing Tables: https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#Route_Which_Associations https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/example_ec2_CreateRouteTable_section.html
https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/example_ec2_CreateRouteTable_section.html
Route Table Options: https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html
10) AWS Network Firewall instance & Route Tables:  https://docs.aws.amazon.com/network-firewall/latest/developerguide/route-tables.html
11) Best strategies for achieving high performance and high availability on Amazon RDS for MySQL with Multi-AZ DB Clusters: https://aws.amazon.com/blogs/database/best-strategies-for-achieving-high-performance-and-high-availability-on-amazon-rds-for-mysql-with-multi-az-db-clusters/
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html
12) 6 EIPs: ALB: https://repost.aws/questions/QUhGXw4ldAQlqmW5qADXz-lA/questions/QUhGXw4ldAQlqmW5qADXz-lA/can-i-associate-multiple-eips-to-single-internal-ip?
NAT: https://repost.aws/questions/QU92LTZdOSSlGfH_ugex1ZSw/i-have-a-nat-gateway-with-multiple-eips-does-aws-charge-for-the-extra-eips
13) Create a Gateway Load Balancer, register EC2 instances across Availability Zones within a VPC: https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-load-balancer.html 
14) API Everything: https://www.workfall.com/learning/blog/how-to-create-publish-and-maintain-high-scalable-apis-using-aws-api-gateway/


# Best Practice Separate Subnets for Resources: 
AWS Network Optimization Tips: https://aws.amazon.com/blogs/networking-and-content-delivery/aws-network-optimization-tips/
Centralized Inbound Traffic: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/centralized-inbound.html
https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html
https://community.aws/concepts/networking-essentials
https://repost.aws/questions/QUdGYmSmyyRQupN3_sgym8YA/how-do-i-reserve-ip-addresses-for-a-specific-purpose
#Other
Deploy multiple-stack applications using AWS CDK with TypeScript: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-multiple-stack-applications-using-aws-cdk-with-typescript.html?did=pg_card&trk=pg_card
Orchestration: https://www.datacamp.com/blog/fundamentals-of-container-orchestration-with-aws-elastic-kubernetes-service-eks
EventBridge: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/service-per-team.html
Mesh: https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/synchronous-data-mesh-for-graphql-queries-ra.pdf?did=wp_card&trk=wp_card

API: DiscoverInstances
MQTT (Message Queuing Telemetry Transport)works over TCP/IP and uses ports 1883 and 8883: https://medium.com/@bramkel/so-what-is-mqtt-b3982db33ca2
(MQ Telemetry Transport) add the MQTT integration to your Home Assistant instance: https://www.home-assistant.io/integrations/mqtt/
Amazon Q AI: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html
https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode#getting-started
https://aws.amazon.com/application-composer/
https://aws.amazon.com/codewhisperer/
https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp
Code composer: https://console.aws.amazon.com/composer/home
https://us-east-1.console.aws.amazon.com/composer/home?region=us-east-1#
_____
