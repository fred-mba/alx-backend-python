### Unittests and Integration Tests

### Learning Objectives
1. The difference between unit and integration tests.
2. Common testing patterns such as mocking, parametrizations and fixtures
- **Mocking**
- A mock is an object that simulates the behavior of real objects in controlled ways. They are primarily used in unit testing to isolate the code being tested and ensures it behaves as expected without relying on external systems.

Why Use Mocks?
- _Isolation_: Ensure tests are not dependent on external systems like databases, APIs, or file systems.
- _Control_: Simulate specific scenarios, such as error conditions, that might be hard to reproduce with real objects.
- _Speed_: Tests run faster since they don't perform actual I/O operations or complex computations.
- _Verification_: Verify interactions with other components (e.g., ensuring a method was called with specific arguments)
