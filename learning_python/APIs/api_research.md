# API Research

## What are APIs? 
* API: `Application Programming Interfaces`.
* A` set of rules and protocols` that allow different software applications to communicate with each other. 
* They enable developers to access certain functionalities or data of another application, service, or platform without needing to understand its internal workings. 

## How are they used and why are they so popular?
* `Integration`: APIs allow different systems to work together, enabling integration between various software applications.
* `Efficiency`: they save time and effort by providing pre-built functions and operations. 
* `Scalability`: create scalable solutions by allowing developers to build on top of existing services.
* `Innovation`: by allowing developers to create new applications that leverage existing services and data.

## Create a diagram to showcase the data transfer process in API communication.
1. `Client`: Sends a request to the server.
2. `Server`: Processes the request.
3. `Server`: Sends a response back to the client.

![what_is_an_api](../../images/img_4.png)

## What is a REST API? 
REST API: Representational State Transfer API.
* It's a type of API that adheres to the principles of REST, an architectural style for designing networked applications.

## What makes an API RESTful? What are the REST guidelines?
RESTful Characteristics:
* `Stateless`: each request from a client to server must contain all the information needed to understand and process the request.
* `Client-Server Architecture`: separation from client and server concerns. 
* `Cacheable`: responses must define themselves as cacheable or not to prevent clients from reusing stale data.
* `Uniform Interface`: Simplifies and decouples the architecture, which enables each part to evolve independently.
* `Layered System`: The client cannot ordinarily tell whether it is connected directly to the end server or to an intermediary along the way.

## What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)
`HTTP`: HyperText Transfer Protocol.
* is the foundation of data communication on the web. 
* It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.
`HTTPS`: HyperText Transfer Protocol Secure.
* is the secure version of HTTP. 
* It uses encryption (via SSL/TLS) to secure data transfer between the client and server, ensuring data integrity and privacy.

## Explain HTTP request structure using the diagrams provided, or your own.
A HTTP request typically consists of three main parts: the `request line`, `headers`, and `message body`:
* `Request Line`: Contains the HTTP method (e.g., GET, POST), the URL, and the HTTP version. 
  * The HTTP method specifies the action to be taken on the resource.
* `Headers`: Provide additional information about the request (e.g., content type, user agent).  
  * Headers are case-sensitive and are followed by a colon (':') and a value.
* `Message Body`: Contains the data to be sent to the server (used in POST, PUT, PATCH requests). 
  * The message body is often used when creating or updating a resource on the server. 

![http_request_structure](../../images/img.png) 

#### Additional things about HTTP requests:
A HTTP request typically consists of:
* A `blank line` separates the header meta-information from the rest of the request. 
* The request ends with a bank line, which is an extra `<CR><LF>` or `\r\n`. 
* The `order` in which header fields with different field names are received is not significant. 
* The standard doesn't limit the size of each header field name or value, or the number of fields. However, most servers, clients, and proxy software do impose some limits. 
* To `make a line a comment` in an HTTP request, start the line with `//` or `#`. 

## Explain HTTP response structure using the diagram provided, or your own.
An HTTP response typically consists of:
* `Status Line`: Contains the HTTP version, status code (e.g., 200 OK), and status message. 
* `Headers`: Provide additional information about the response (e.g., content type, content length). 
* `Body`: Contains the data returned by the server.

![http_response_structure](../../images/img_1.png)


## What are the 5 HTTP verbs and what do they do?
* `GET` → Retrieves data from the server.
* `POST` → Sends data to the server to create a new resource.
* `PUT` → Updates an existing resource with new data.
* `PATCH` → Partially updates an existing recourse.
* `DELETE` → Deletes an existing resource.

## What is statelessness? Show examples of “stateless” and stateful http requests.
`Statelessness`: each request from a client to server must contain all the information needed to understand and process the request. The server does not store any state about the client session.
* It means that each request from a client to a server is independent. 
* The server does not remember anything about the client between requests. 
* Each request is self-contained.
* Each request must contain all the information needed for the server to understand and process it.

### For example
1. The client sends a GET request to retrieve a list of tasks.
2. The request includes an authorization token to verify the client's identity.
3. The server processes the request and responds with the list of tasks.
4. The server does not remember the client or the request after responding.

## What is stateful?
`Stateful`:
* The server remembers the client between requests, often using sessions.

### For example
1. The client sends a POST request to log in, providing a username and password.
2. The server responds with a session ID stored in a cookie.
3. The client includes this session ID in subsequent requests.
4. The server uses the session ID to remember the client's state and provide the appropriate response.


![img_3.png](../../images/img_3.png)
![img_2.png](../../images/img_2.png)

## What is caching?
`Caching` is the process of `storing copies of files or data in a cache`, or temporary storage location, 
so that they can be `accessed more quickly`. 
* In the context of web APIs, caching can `reduce the load on the server` and `decrease the time it takes to retrieve data`.

> Around close of COB, post a link in the main chat to the specific section of your repo where this tasks is.


