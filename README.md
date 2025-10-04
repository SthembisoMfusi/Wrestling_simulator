# Wrestling Simulator

[![CI](https://github.com/SthembisoMfusi/Wrestling_simulator/workflows/CI/badge.svg)](https://github.com/SthembisoMfusi/Wrestling_simulator/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A comprehensive Python-based wrestling tournament simulation game that allows you to create custom wrestlers, manage rosters, and run exciting tournaments with realistic match mechanics.

## 🎯 Features

### 🥊 Wrestler System
- **Customizable Stats**: Create wrestlers with unique attributes including:
  - **Strength**: Damage resistance and grappling power
  - **Speed**: Attack and reaction speed
  - **Agility**: Escape ability from grapples and pins
  - **Health**: Total damage capacity
  - **Power**: Attack damage output
  - **Grapple**: Grappling success rate
  - **Stamina**: Special move frequency
- **Multiple Creation Methods**: Manual input or auto-generation with random stats
- **Gender Diversity**: Support for male, female, and other gender identities
- **Training System**: Improve wrestler stats over time

### 🏆 Tournament Management
- **Single-Elimination Tournaments**: Classic bracket-style competitions
- **Flexible Sizing**: Support for 4, 8, 16, 32+ participants
- **Random Pairings**: Fair and unpredictable matchups
- **Realistic Match Simulation**: 
  - Basic attacks with damage calculation
  - Grapple attempts with success/failure mechanics
  - Pin attempts with health-based success rates
  - Stamina and health regeneration between turns

### 💾 Roster Management
- **Save/Load System**: Persistent roster storage using pickle
- **Flexible Operations**: Add, remove, and retrieve wrestlers by name or index
- **Batch Operations**: Create multiple wrestlers efficiently

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/SthembisoMfusi/Wrestling_simulator.git
cd Wrestling_simulator

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e .[dev]
```

### Basic Usage

```bash
# Run the interactive simulator
wrestling-simulator

# Or run directly with Python
python -m wrestling_simulator.main
```

### Programmatic Usage

```python
from wrestling_simulator import Wrestler, Roster, Tournament

# Create a wrestler
wrestler = Wrestler("The Rock", "male", 90, 80, 70, 160, 95, 15, 85)

# Create a roster
roster = Roster(8)
# ... fill roster with wrestlers

# Run a tournament
tournament = Tournament(roster, 8)
tournament.tournamentPlay()
```

## 📁 Project Structure

```
wrestling_simulator/
├── wrestling_simulator/          # Main package
│   ├── core/                     # Core functionality
│   │   ├── wrestler.py          # Wrestler class and mechanics
│   │   ├── roster.py            # Roster management
│   │   └── tournament.py        # Tournament logic
│   ├── data/                    # Data files
│   │   └── wrestler_names/      # Name lists for auto-creation
│   ├── main.py                  # CLI entry point
│   └── __init__.py
├── tests/                       # Test suite
├── docs/                        # Documentation
├── examples/                    # Example scripts
├── .github/workflows/           # CI/CD configuration
└── setup.py                     # Package setup
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=wrestling_simulator

# Run specific test file
pytest tests/test_wrestler.py -v
```

## 🛠️ Development

### Code Quality Tools

```bash
# Format code
black wrestling_simulator tests

# Lint code
flake8 wrestling_simulator tests

# Type checking
mypy wrestling_simulator
```

### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
```

## 📖 Documentation

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [API Documentation](docs/api.md) (coming soon)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to:

- Report bugs
- Suggest features
- Submit pull requests
- Set up the development environment

## 📋 Roadmap

- [ ] **Enhanced Match Types**: Ladder matches, cage matches, battle royals
- [ ] **Tag Team Support**: Multi-wrestler matches and team management
- [ ] **Career Mode**: Long-term wrestler development and storylines
- [ ] **GUI Interface**: Modern graphical user interface
- [ ] **Advanced AI**: Strategic decision-making algorithms
- [ ] **Statistics Dashboard**: Detailed analytics and reporting
- [ ] **Multiplayer Support**: Online tournaments and competitions
- [ ] **Mod Support**: Custom moves, arenas, and game modes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic wrestling video games
- Built with modern Python best practices
- Community-driven development and feedback

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/SthembisoMfusi/Wrestling_simulator/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/SthembisoMfusi/Wrestling_simulator/discussions)
- 📧 **Contact**: [thanduxolomfusi@gmail.com](mailto:thanduxolomfusi@gmail.com)

---

**Ready to step into the ring?** 🥊 Start your wrestling empire today!

