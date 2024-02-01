Part III looks like the photos in S3
gives list of all the elements
put all the elements in draw io 
create connections with arrows
don't need everything

# Part III. AWS Native Architecture design (10 marks total)

Research, design, draw figures. 

Design exercise requirements:
- The client wishes to build a news aggregator web app to earn money with Google Ads
  - The backend constantly look for latest news from many different news websites. Some sites require refreshing data every 10 seconds, some sites less frequently
  - Save the aggregated news headline and links into a no management database with infinite scale
  - The backend should use a no management APIGW to allow for the static website to make API calls to
- The website should be ideally 
  - Very cheap to host, and 
  - Deployed to a globally available CDN 
  - Completely billed by on-demand pricing models
  - Has no management effort required, except for incident resolution
- Both the APIGW and the static website have domain name
  - Static website has CNAME `www.` points to `bestnewsaggregator.com`
  - APIGW has domain record `api.`
  - The APIGW should be protected against Layer 7 attacks such as SQL injection, or DDOS protection
  - Both needs to be secured by SSL certificate from a publically trusted CA
- The backend should be consisted of:
  - `GET /news API` to get the latest news from the static website. It may look at geolocation, device, and browser information to customize the news resource
  - `GET /news API` response should also be cached to save infrastructure cost
  - Only the Origin `www.` should be able to make request to `api.` (CORS)
  - A scheduler component that trigger scalable backend job to fetch for lastest news articles
  - Fetched links need to be checked if they are actually new according to the internal database with infinite scale mentioned earlier
  - The combination infrastructure of scheduling + fan-out scheduling event to the list of new source + get news executor should be fast, management free, and scalable
  - Some news sources are only updated once daily while others are known to have new articles to be released at any given moment. Thus, the design should be able to trigger news source aggregators tailored for individual websites at a different rate, depending on the frequency settings of each of the crawled websites. Note that there are thousands of websites thus the chosen scheduling setup should be scalable to reduce overheads on the engineers to add more sources.

As the lead engineer, you are tasked with designing this architecture to fulfill all of the customer requirements using AWS Cloud.

Expected submission formats are:
- Produce your architecture design into graphics files `.drawio` or exported `.png` in high resolution
- Make short notes on the AWS Components on how some of the requirements are fulfilled
- It is encourged to reference to `.png` images inside file `Part III/Answer.md`

You should be able to design the architecture with only AWS services (don't have to use all of these) such as:
- EventBridge scheduler
- SNS
- SQS
- S3
- CloudFront
- APIGW
- WAF
- Route53
- ACM
- DynamoDB
- Lambda
- StepFunction
- EventBridge

# Answer

Here is one way you could design the architecture to meet the client's requirements using AWS services:

* *Use Amazon EventBridge to schedule events to trigger fetching of latest news from different sources at varying frequencies (e.g. every 10 seconds for some sources, daily for others).

- Have an EventBridge rule target an SNS topic when an event is scheduled.

* Configure SNS to fan-out the message to multiple SQS queues, with each queue corresponding to a different news source.

- Have AWS Lambda functions subscribed to the SQS queues. The Lambda functions would fetch the latest news from each source when a message is received.

* Store the aggregated news articles in Amazon DynamoDB. Configure DynamoDB auto scaling to handle infinite scale of data.

- Build a static website hosted on S3 and distributed globally using CloudFront. Configure the S3 bucket and CloudFront distribution for SSL using ACM.
Protect the API Gateway endpoint using WAF to guard against attacks.

* Configure API Gateway and Lambda to implement the GET /news API. Cache responses in API Gateway.

- Use Route53 for DNS, configuring a CNAME for the static website and record set for the API domain.