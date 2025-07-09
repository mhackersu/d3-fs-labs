# Design Notebook

## Languages
- Python

Why Python?
Python handles the kinds of problems that the C# and Java world has been working on for years. Startups become real businesses; web apps and scripted automations are becoming (whisper it) enterprise software.

In the Python world, we often quote the Zen of Python: "There should be one—​and preferably only one—​obvious way to do it."[1] Unfortunately, as project size grows, the most obvious way of doing things isn’t always the way that helps you manage complexity and evolving requirements.

Observing the classics in the field such as [Eric Evans’s Domain-Driven Design](../design/methods/d3/reference/domain-driven-design.pdf) or Martin Fowler’s Patterns of Enterprise Application Architecture (both published by Addison-Wesley Professional).

But all the classic code examples in the literature do tend to be written in Java or C++/#, and if you’re a Python person and haven’t used either of those languages in a long time (or indeed ever), those code listings can be quite…​trying. There’s a reason the latest edition of that other classic text, Fowler’s Refactoring (Addison-Wesley Professional), is in JavaScript.

## ADRs
- Structural, MVC, API

## Patterns
- [D3|Solid Aggregates](./methods/d3/aggregates.json)

### OOP

- S
- L
- I
- D

### D3

- Behavioral
    - Chain of Responsibility
- Creational
    - Builder
    - Factory
- Structural
    - Adapter
    - Decorator
    - Facade