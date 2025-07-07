# What

## Open-Closed Principle (OCP):
Focuses on behavioral extension. It dictates that existing code should not be modified when new functionality is added. Instead, you should extend its behavior, typically by creating new classes that implement an interface or extend an abstract class, or by using composition. The emphasis is on adding features by adding new code, not by changing old code.

## Dependency Inversion Principle (DIP):
Focuses on dependency direction and abstraction. It states that high-level modules (which contain important business logic) should not depend on low-level modules (which handle details like database interaction or file I/O). Instead, both should depend on abstractions (interfaces or abstract classes). This “inverts” the typical top-down dependency flow, promoting a system where concrete details depend on abstract contracts.
