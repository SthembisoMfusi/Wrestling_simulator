# Release v1.0.0 - Initial Release 🎉

## 🎯 What's New

Welcome to the first official release of Wrestling Simulator! This comprehensive Python-based wrestling tournament simulation game brings the excitement of professional wrestling to your command line.

### 🥊 Core Features

#### Wrestler System
- **Customizable Stats**: Create wrestlers with unique attributes:
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

#### Tournament Management
- **Single-Elimination Tournaments**: Classic bracket-style competitions
- **Flexible Sizing**: Support for 4, 8, 16, 32+ participants
- **Random Pairings**: Fair and unpredictable matchups
- **Realistic Match Simulation**:
  - Basic attacks with damage calculation
  - Grapple attempts with success/failure mechanics
  - Pin attempts with health-based success rates
  - Stamina and health regeneration between turns

#### Roster Management
- **Save/Load System**: Persistent roster storage using pickle
- **Flexible Operations**: Add, remove, and retrieve wrestlers by name or index
- **Batch Operations**: Create multiple wrestlers efficiently

### 🚀 Getting Started

#### Installation
```bash
pip install wrestling-simulator==1.0.0
```

#### Quick Start
```bash
# Run the interactive simulator
wrestling-simulator

# Or run directly with Python
python -m wrestling_simulator.main
```

#### Programmatic Usage
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

### 🛠️ Technical Details

- **Python 3.8+** support
- **Comprehensive test suite** with pytest
- **Type hints** throughout the codebase
- **Code formatting** with Black
- **Linting** with flake8
- **CI/CD** with GitHub Actions
- **MIT License**

### 📦 Package Contents

- Core wrestling simulation engine
- CLI interface for interactive gameplay
- Programmatic API for custom implementations
- Example scripts and documentation
- Comprehensive test suite

### 🎮 Example Scripts

Check out the `examples/` directory for:
- `quick_tournament.py`: Run a quick tournament simulation
- `roster_management.py`: Advanced roster management examples

### 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=wrestling_simulator

# Run specific test file
pytest tests/test_wrestler.py -v
```

### 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### 📋 Roadmap

Future releases will include:
- Enhanced match types (ladder matches, cage matches, battle royals)
- Tag team support
- Career mode
- GUI interface
- Advanced AI
- Statistics dashboard
- Multiplayer support
- Mod support

### 🙏 Acknowledgments

- Inspired by classic wrestling video games
- Built with modern Python best practices
- Community-driven development and feedback

---

**Ready to step into the ring?** 🥊 Start your wrestling empire today!

## Installation

```bash
pip install wrestling-simulator==1.0.0
```

## Full Changelog

This is the initial release. See [CHANGELOG.md](CHANGELOG.md) for future changes.
