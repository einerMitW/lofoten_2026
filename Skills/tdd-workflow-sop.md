# TDD Workflow SOP

Standard Operating Procedure for Test-Driven Development (TDD) across all feature phases.

## Workflow Rules

1. **Explicit Acceptance Criteria (Akzeptanzkriterien)**:
   - Establish explicit, testable Akzeptanzkriterien (AK-1, AK-2, ...) before writing any implementation code.

2. **RED State (Write Tests First)**:
   - Write failing Unit and Integration tests (Pytest for Python backend, Vitest for Vue frontend) before creating or editing production source files.
   - Run test runner to verify test failures.

3. **GREEN State (Minimal Production Code)**:
   - Implement the minimal amount of code required to make all tests pass.
   - Re-run test runner to confirm 100% green state.

4. **REFACTOR State**:
   - Clean up and optimize code structure adhering to KISS and clean code standards without breaking existing test assertions.
