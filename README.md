# Calculator Project

A simple calculator project demonstrating unit and integration testing with GitHub Actions.

## Project Structure

- `src/calculator.py`: Contains the Calculator class implementation
- `tests/test_calculator.py`: Unit tests
- `tests/test_calculator_integration.py`: Integration tests

## Testing

The project uses pytest for testing. Two types of tests are implemented:

1. Unit Tests: Testing individual calculator operations
2. Integration Tests: Testing complex calculations and operation chains

## GitHub Actions

- Pull Requests: Runs unit tests only
- Main Branch: Runs both unit and integration tests

## Setup

```bash
pip install -r requirements.txt
```

## Running Tests Locally

```bash
# Run all tests
pytest tests/ -v

# Run unit tests only
pytest tests/test_calculator.py -v

# Run integration tests only
pytest tests/test_calculator_integration.py -v
```