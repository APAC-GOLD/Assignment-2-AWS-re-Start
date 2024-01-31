---

>

## REFERENCES
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

End. 
_____