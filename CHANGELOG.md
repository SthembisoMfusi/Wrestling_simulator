# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [1.0.1] - 2024-12-19

### Fixed
- Fixed GitHub Actions release workflow permissions
- Updated release workflow to use modern GitHub CLI instead of deprecated actions
- Improved release automation and error handling

### Changed
- Updated release process documentation
- Enhanced release checklist and quality gates

## [1.0.0] - 2024-12-19

### Added
- **Initial Release** 🎉
- **Wrestler System**:
  - Customizable wrestler stats (Strength, Speed, Agility, Health, Power, Grapple, Stamina)
  - Multiple creation methods (manual input or auto-generation)
  - Gender diversity support (male, female, other)
  - Training system for stat improvement
  - Wrestler name generation from data files

- **Tournament Management**:
  - Single-elimination tournament system
  - Flexible tournament sizing (4, 8, 16, 32+ participants)
  - Random pairing system for fair matchups
  - Realistic match simulation with:
    - Basic attacks with damage calculation
    - Grapple attempts with success/failure mechanics
    - Pin attempts with health-based success rates
    - Stamina and health regeneration between turns

- **Roster Management**:
  - Save/load system using pickle for persistent storage
  - Flexible operations (add, remove, retrieve wrestlers by name or index)
  - Batch operations for efficient wrestler creation
  - Roster size validation and management

- **CLI Interface**:
  - Interactive command-line interface
  - Menu-driven navigation
  - User-friendly prompts and error handling
  - Console script entry point (`wrestling-simulator`)

- **Programmatic API**:
  - Clean, well-documented Python API
  - Type hints throughout the codebase
  - Modular design for easy extension
  - Example scripts and usage patterns

- **Development Tools**:
  - Comprehensive test suite with pytest
  - Code formatting with Black
  - Linting with flake8
  - Type checking with mypy
  - CI/CD pipeline with GitHub Actions
  - Coverage reporting

- **Documentation**:
  - Comprehensive README with usage examples
  - Contributing guidelines
  - Code of conduct
  - API documentation structure
  - Example scripts and tutorials

- **Package Management**:
  - PyPI-ready package configuration
  - Proper dependency management
  - Development dependencies separation
  - Entry points for CLI access

### Technical Details
- **Python 3.8+** compatibility
- **MIT License** for open source distribution
- **Semantic versioning** for release management
- **GitHub Actions** for automated testing and building
- **Modern Python practices** with type hints and proper packaging

### Files Added
- Core wrestling simulation engine (`wrestling_simulator/core/`)
- CLI interface (`wrestling_simulator/cli/`)
- Utility functions (`wrestling_simulator/utils/`)
- Wrestler name data files (`wrestling_simulator/data/`)
- Comprehensive test suite (`tests/`)
- Example scripts (`examples/`)
- Documentation files (README, CONTRIBUTING, etc.)
- CI/CD configuration (`.github/workflows/`)
- Package configuration (`setup.py`, `pyproject.toml`)

---

## Release Notes Format

Each release entry follows this structure:

### Added
- New features and functionality

### Changed
- Changes to existing functionality

### Deprecated
- Features that will be removed in future versions

### Removed
- Features that were removed in this version

### Fixed
- Bug fixes

### Security
- Security-related changes

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

## Links

- [Unreleased]: https://github.com/SthembisoMfusi/Wrestling_simulator/compare/v1.0.0...HEAD
- [1.0.0]: https://github.com/SthembisoMfusi/Wrestling_simulator/releases/tag/v1.0.0
