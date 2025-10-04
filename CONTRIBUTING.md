# Contributing to Wrestling Simulator

Thank you for your interest in contributing to the Wrestling Simulator! This document provides guidelines and information for contributors.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include screenshots and animated GIFs if possible

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Describe the current behavior and explain which behavior you expected to see instead
- Explain why this enhancement would be useful

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SthembisoMfusi/Wrestling_simulator.git
   cd Wrestling_simulator
   ```

2. Install the package in development mode:
   ```bash
   pip install -e .[dev]
   ```

### Running Tests

```bash
pytest tests/ -v
```

### Code Style

This project uses several tools to maintain code quality:

- **Black** for code formatting
- **flake8** for linting
- **mypy** for type checking

Run these tools before submitting a pull request:

```bash
black wrestling_simulator tests
flake8 wrestling_simulator tests
mypy wrestling_simulator
```

### Pre-commit Hooks

You can set up pre-commit hooks to automatically run these tools:

```bash
pip install pre-commit
pre-commit install
```

## Project Structure

```
wrestling_simulator/
├── wrestling_simulator/          # Main package
│   ├── core/                     # Core functionality
│   │   ├── wrestler.py          # Wrestler class
│   │   ├── roster.py            # Roster management
│   │   └── tournament.py        # Tournament logic
│   ├── data/                    # Data files
│   │   └── wrestler_names/      # Name lists
│   ├── main.py                  # CLI entry point
│   └── __init__.py
├── tests/                       # Test files
├── docs/                        # Documentation
├── examples/                    # Example scripts
└── setup.py                     # Package setup
```

## Testing Guidelines

- Write tests for new functionality
- Ensure all tests pass before submitting
- Aim for good test coverage
- Use descriptive test names
- Follow the existing test patterns

## Documentation

- Update documentation for any new features
- Use clear and concise language
- Include examples where helpful
- Follow the existing documentation style

## Release Process

Releases are managed through GitHub tags. When a new version is ready:

1. Update the version in `setup.py`
2. Update the changelog
3. Create a new tag
4. The CI/CD pipeline will automatically build and publish to PyPI

## Questions?

If you have any questions about contributing, please open an issue or contact the maintainers.
