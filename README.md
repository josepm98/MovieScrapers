# MovieScrapers
Web scrapers to get links for watching movies and TV series

# Software Used
* Visual Studio Community 2017 Version 15.9.7
* Microsoft SQL Server Developer Edition
* FlyWay
* Windows 10 Pro

# Frameworks and tools
* .NET Framework 4.6.1: It is the main C# framework used to develop our web api.
* EntityFramework 6.2.0: Used for accesing the database and managing transactions.
* Automapper 8.0.0: Used for mapping the data that came from entity framework models into the common model used throughout the project.

# Architecture

![Architecture Diagram](https://github.com/josepmdc/MovieScrapers/blob/master/ExamDiagram.png)

The architecture used in this project is DDD(Domain Driven Development). It consists of 4 layers that each of them has a specific functionality wich allows us to have a highly decoupled system. It could be even more decoupled by having one model for each layer instead of having one model in the common layer, but for this project we won't do it.

* **Common Logic**: It has the components and dependencies that will be used by all the other layers. For example our models or the error logging system.

* **Infrastructure**: It is in charge of connection with the database and retrieving the data.

* **Business Logic**: It is the layer that will work as a bridge between the Facade and the Infrastructure, by calling the Infrastructure and manipulating the data in order to achive the functionality we desire.

* **Business Facade**: It is an implementation of the Facade design pattern. It is where our web api resides. Its job is to call the Business Layer and return the values in JSON format through the web api.


# Design Patterns

# Good Practices and Clean Code
* SOLID: 
  * Single Responsability Principle: All the classes have one responsability.
  * Open-Closed Principle: 
* DRY(Don't Repeat Yourself): Even though I did repeat myself in some aspects, it was on different projects(or dlls) wich allows us to have a more decoupled application with less dependencies. This is good because it will be more scalable in case the application has to grow.
