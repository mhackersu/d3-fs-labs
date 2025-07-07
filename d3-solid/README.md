# SOLID D3 Aggregates Map

# References
- [faif/python-patterns](https://github.com/faif/python-patterns)
- [foster-academy/py101](https://github.com/foster-academy/py101)

# S
## Single-responsibility Principle (SRP):
A class should have one and only one reason to change, meaning that a class should have only one job.

- Behavioral
  - [Chain of Responsibility](./d3-solid/behavioral/chain_of_responsibility.py)
- Creational
  - [Factory](./d3-solid/creational/factory.py)
  - [Builder](./d3-solid/creational/factory.py)
- Structural
  - [Decorator](./d3-solid/structural/decorator.py)
  - [Adapter](./d3-solid/structural/adapter.py)

# O
## Open-closed Principle (OCP):
Objects or entities should be open for extension but closed for modification.

- Behavioral
  - [Chain of Responsibility](./d3-solid/behavioral/chain_of_responsibility.py)
- Structural
  - [Decorator](./d3-solid/structural/decorator.py)
- Creational
  - [Factory](./d3-solid/creational/factory.py)

## **L**
### Liskov Substitution Principle (LSP):
Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.

- Behavioral
  - [Chain of Responsibility](./d3-solid/behavioral/chain_of_responsibility.py)
- Structural
  - [Decorator](./d3-solid/structural/decorator.py)

## **I**
### Interface Segregation Principle (ISP):
Clients should not be forced to depend on interfaces they do not use.

- Structural
  - [Facade](./d3-solid/structural/facade.py)
- Behavioral
  - [Chain of Responsibility](./d3-solid/behavioral/chain_of_responsibility.py)
- Structural
  - [Decorator](./d3-solid/structural/decorator.py)
- Creational
  - [Factory](./d3-solid/creational/factory.py)
  - [Builder](./d3-solid/creational/factory.py)
- Structural
  - [Adapter](./d3-solid/structural/adapter.py)

# D
## Dependency Inversion Principle (DIP):
High-level modules should not depend on low-level modules; both should depend on abstractions. Also, abstractions should not depend on details; details should depend on abstractions.

- Structural
  - [Facade](./d3-solid/structural/facade.py)
- Behavioral
  - [Chain of Responsibility](./d3-solid/behavioral/chain_of_responsibility.py)
- Structural
  - [Decorator](./d3-solid/structural/decorator.py)
- Creational
  - [Factory](./d3-solid/creational/factory.py)
  - [Builder](./d3-solid/creational/factory.py)
- Structural
  - [Adapter](./d3-solid/structural/adapter.py)

# Domain Driven Design

```
{
  "D3": {
    "What": [
      "OCP",
      "DIP"
    ],
    "Why": [
      "Maintainabe",
      "Flexible",
      "Extensible",
      "Tested",
      "Clean"
    ],
    "How": [
      "Identify",
      "Extract",
      "SRP"
    ]
  }
}
```
