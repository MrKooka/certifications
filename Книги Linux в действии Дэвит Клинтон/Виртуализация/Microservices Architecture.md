# Microservices Architecture

## What is Microservices Architecture?
Microservices architecture is a design pattern for structuring applications as a collection of loosely (loosely) coupled (в паре), independently deployable services. Each **microservice** focuses on a specific business capability, communicates with other services through lightweight protocols (typically HTTP/REST or messaging), and can be developed, deployed, and scaled independently.

## Key Characteristics:
- **Independent Deployment:** Each microservice can be deployed and updated independently, without affecting the entire system.
- **Decentralized Data Management:** Each microservice can manage its own database or data store, leading to polyglot persistence (приводящее к полиглотической настойчивости) (use of different data storage technologies).
- **Modularity:** Microservices divide large systems into smaller, more manageable pieces, making it easier to develop, test, and maintain them.
- **Fault Isolation:** If a microservice fails, it typically doesn’t bring down the entire system. This enhances the overall resilience of the application.

## Benefits of Microservices:
- **Scalability:** Services can be scaled individually, allowing for more efficient use of resources. For example, a high-demand service can be scaled up without scaling the entire system.
- **Faster Development Cycles:** Teams can work on different services simultaneously, speeding up the overall development process.
- **Technology Agnostic:** Microservices can be built using different programming languages or technologies, as long as they adhere to the defined communication protocols (like HTTP or gRPC).
- **Easier Maintenance:** With smaller, focused services, it’s easier to identify, isolate, and fix bugs.

## Challenges of Microservices:
- **Complexity:** Managing multiple microservices requires a robust orchestration platform like Kubernetes, as well as service discovery, load balancing, and monitoring tools.
- **Data Consistency:** Since each service can have its own database, maintaining consistency across services can be challenging.
- **Inter-Service Communication:** Services must be able to communicate efficiently, often requiring tools like message brokers (e.g., RabbitMQ, Kafka) to handle asynchronous communication and events.
- **Latency:** Because microservices often communicate over a network, there's a risk of increased latency compared to monolithic architectures.

## Common Use Cases:
- **Highly Scalable Applications:** Microservices are ideal for applications that need to scale different parts independently, such as e-commerce platforms, where inventory, payment processing, and customer services can scale separately.
- **Continuous Deployment Pipelines:** Microservices enable faster, more frequent deployments as small, independent services can be updated without affecting the entire system.
- **Complex Systems with Varying Resource Requirements:** Applications where different components have vastly different resource needs (e.g., CPU, memory, storage) benefit from the fine-grained resource management provided by microservices.

## Communication Patterns:
- **REST (Representational State Transfer):** A widely used synchronous communication method for inter-service communication using HTTP.
- **gRPC:** A high-performance, language-agnostic RPC framework developed by Google for more efficient communication.
- **Message Brokers (Asynchronous):** Tools like Apache Kafka, RabbitMQ, or AWS SQS facilitate event-driven communication and asynchronous message passing between microservices.

## Tools and Platforms:
- **Docker:** Often used to package and run microservices in isolated containers, ensuring consistency across different environments.
- **Kubernetes:** A container orchestration platform that helps manage the deployment, scaling, and operation of microservices in containers.
- **API Gateway:** A management tool that handles all API calls, routing requests to the appropriate microservices, managing authentication, rate limiting, and load balancing.

## Microservices vs Monolithic Architecture:
- **Monolithic Architecture:** In a monolith, the entire application is built as a single, interconnected unit. All components are tightly coupled, which can make it difficult to scale, maintain, or update parts of the system independently.
- **Microservices Architecture:** In contrast, microservices break down the application into small, independent services that can evolve separately, making the system more modular, scalable, and resilient.

| **Monolithic**               | **Microservices**           |
|------------------------------|-----------------------------|
| Tightly coupled components    | Loosely coupled services    |
| Single codebase               | Multiple codebases          |
| Scaling is harder             | Scaling is easier, per service |
| Single point of failure       | Fault isolation             |

## Examples of Companies Using Microservices:
- **Netflix:** Known for pioneering the microservices architecture to handle massive scaling and service availability for its streaming platform.
- **Amazon:** Uses microservices to manage different parts of its large-scale e-commerce platform, allowing each part to scale independently.
- **Uber:** Employs microservices to manage the complex system of driver, rider, and location data with high scalability and fault tolerance.

## Related Notes:
- [[Kubernetes Overview]]
- [[Docker Basics]]
- [[Monolithic Architecture]]
- [[Service Discovery in Microservices]]
- [[API Gateway]]
