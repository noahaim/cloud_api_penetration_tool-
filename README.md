Secured API in Hybrid Cloud

## Background
Recently we see many companies that are moving their data from local data centers to public-managed clouds. But with these movements, some questions raise up. Can I store my data on more than one public cloud provider? What if a company wants some of the data stored locally? How to orchestrate the data between a couple of separate clouds? A hybrid cloud can solve all of these problems. 

Hybrid cloud became the most common way where companies choose to store their data. It helps to lower costs for data that can be stored in a public data center and maintain locally only the data that should stay under private control.

When deploying/creating a hybrid cloud we need to make sure that the API not only can process data that moves between the different clouds but also protect the existing data, not letting sensitive data leak out.

The goal of this research is to study the base rules of securing a channel level API in a hybrid cloud and the importance of each and every component of the API

## Hybrid Cloud 
What is a hybrid cloud? A hybrid cloud incorporates some degree of workload portability, orchestration, and management across two or more environments; public, private, or on-premise clouds. The hybrid cloud gives companies the speed and scalability of the public cloud and the control and reliability of the private cloud. 

Orchestrating data between multiple storage services is subject to security breaches:

A security breach in the public cloud can lead to unauthorized access to the private cloud’s hardware
Vice versa, private cloud hardware which is not physically secured can lead to unauthorized access to the public cloud 
Wrong user access control management to one cloud, can cause unauthorized accesses to another one 
Wrong data organization may cause a data leak 
Data can be lost during the orchestration between the clouds 
To secure a hybrid cloud we need to understand how these clouds communicate with each other.

To process IO data, the cloud uses an API (application programming interface) – a set of definitions and protocols for building and integrating application software that lets your product or service (in this case – a cloud)  communicate with other products and services without having to know how they’re implemented. 

## Web API
Web API is an API over the web which can be accessed using the HTTPs protocol. It is a concept and not a technology. We can build Web API using different technologies to provide programmatic access to read and write data using which we can integrate different apps capabilities into our own application.

Most of the modern web APIs are built by the REST architecture – REST stands for REpresentational State Transfer. This architecture is popular due to its simplicity and the fact that it builds upon existing systems and features of the internet’s HTTP and there is no need to develop new standards or frameworks. 

The protocol used by the web APIs is SOAP (Simple Object Access Protocol). SOAP was created to provide a way to communicate between applications running on different operating systems, with different technologies and programming languages

The usage of REST architectural style and SOAP standards together creates a strongly secured web API that uses secure HTTPs queries, input validations, smart user authentication (e.g. OAuth2.0), IP address filtering, and more. It’s important to emphasise that it’s critical to use a bring-your-own-key (BYOK) approach, because data is not truly secure if an encryption key is stored with the public cloud that stores the encrypted data. 

The secured API can communicate with every web app in the cloud, add connections between the private and the public clouds, and still reduce security problems that can occur when developing an API without any base security rules or standards. 


## Secured API channel on Hybrid cloud
Migrating data between the public and private clouds in hybrid cloud is done by application programming interfaces (APIs) (or containers) that help for information transmission. 

Public Clouds, like any other web services, must have strong and secured web APIs, especially if they are part of hybrid clouds that are connected to private clouds that store much more sensitive data and are more vulnerable as they are managed by the company and not a big cloud provider. 

APIs are the most exposed parts of any system. The API is the only asset with a public IP address available outside the trusted organizational boundary. As the API discussed on this blog is used as the channel between the private and public, it is very likely to be attacked continuously. API security by design and adequate controls protecting the API channel from the attacks are required.

Looking into some of the top 10 OWASP API risks:

* Lack of Resources & Rate Limiting –  APIs do not impose any restrictions on the size or number of resources that can be requested by the client/user, which can cause not only server performance problems leading to Denial of Service (DoS), but also leaves a place to authentication flaws such as brute force.
Security Misconfiguration –  Security misconfiguration is commonly a result of unsecured default configurations, incomplete or configuration, open cloud storage like visible S3 buckets, unnecessary HTTP methods, and verbose error messages containing sensitive information.
Injection –  Injection flaws, such as SQL, NoSQL, command injection, and many more, occur when untrusted data is sent to an interpreter as part of a command or query. It causes the execution of unintended commands or accessing data without authorization.
Broken User Authentication – wrong authentication mechanisms can allow attackers to compromise authentication tokens or to exploit implementation flaws to assume other user’s identities temporarily or permanently. 
With those risks, many classic cyber attacks can be executed on hybrid clouds


* DOS\DDOS - (Distributed) Denial of service AKA (D)DOS is a type of attack, where a big amount of packets is sent to a server that can not handle this traffic and causes it to fail, or as the name states – go out of service. When looking at DDoS attacks from an API point of view, this attack can be performed with a big amount of API calls at the same time which can cause the API service to fail. If a channel API in a hybrid cloud is attacked, the whole communication between the private entity and the public entity will be disturbed and may cause – data loss, data leak, authentication problems, and more. 
 
    When performing this attack from more than one point – it becomes a distributed attack. 

    Hybrid clouds can be attacked from each one of the points with that are much more sensitive to DoS attacks – it enough that just one entry point won’t be secured and won’t have a firewall that limits the amount of traffic it can get, and the whole cloud will be out of service


* INJECTIONS - When connecting to a cloud platform using the user interface(UI) some types of data injections can be performed –

  * Cross-site scripting – a type of security vulnerability typically found in web applications. XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls 

  * SQL injection – SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application’s content or behavior.

    Those attacks are very convenient to execute duo to the fact that no SSH connection or some hacking tools are needed- when you have access to the web interface – everything is possible and we see it every day – exposed AWS S3 buckets, unsecured VMWARE labs 

* AUTHENTICATION ABUSE (brute force) – if one of the channel API’s functionalities is connecting from one cloud to another, with a gained access to one of the clouds, an attacker can gain access to the second cloud by serially guessing passwords and sending login requests to the API, this method of guessing credentials is called brute-force, the attacker won’t stop until he manages to access the cloud. Within a hybrid cloud architecture, as mentioned before, there are at least 2 access points he can try – the public entity, the public entity, and sometimes the platform. If just one of the points is vulnerable to authentication abuse – the whole cloud can be hacked. 


* WORMS -let’s assume we have a cloud application that runs on a machine, an attacker gets control over this machine and implements a malicious program – a type of a crawler that starts crawling between all the machines in this cloud and through to the second cloud. This warm can cause ransomware attack, data theft, delete data or modify it.

    When all the machines are infected there are minor chances to save them, most of the times the cloud deployment will be destroyed with all its data. 

Now It is understandable why securing hybrid cloud’s API is so important – hybrid cloud, unlike and other cloud or web application, has a lot more API outlets that can be hacked or attacked – each cloud has its user API which communicated with the users and can be a place to human mistakes (wrong access control, social engineering, open-source intelligence) And the inter-cloud APIs (channel APIs) used by the clouds themselves to communicate. 

To achieve a good level of security in those APIs we will list some of the basic security required for API:

Encrypt data in the transition between the private to the public
Use strong identity and access management capabilities
Use cryptographic protocols (SSL/TSL) for secure data transmission 
Use secured network protocols for data communication between unsecured network connections
Communicate the inherent data security risks to your customers and end-users
Prevent vulnerability exploit
Secure bot access and automated attacks
In the next steps of the research, for each of the above requirements, we will explain its importance, its security risks, and how to apply it in the APIs to achieve a secured hybrid cloud API.

# Our Goal 

The goal of this research is to study the base rules of securing a channel level API in a hybrid cloud and the importance of each and every component of the API.  By using API management tools, we can track data flow in and out of our clouds. Choosing the right rules for your hybrid cloud, based on Data sensitivity, Workloads and User access, data loss, data leak and other cyber challenges can be prevented. 

We are working on improving OpenShift’s API management tool and optimizing its security rules by creating a Rapid PT tool that the users can execute to test their API security. The tool will demonstrate several possible attacks: DoS, SQL & XSS injections, authentication abuse, and MITM. The users will get a report of the tests with tips on how to improve their API security 

