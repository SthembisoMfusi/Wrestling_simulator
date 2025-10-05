#!/usr/bin/env python3
"""
Release automation script for Wrestling Simulator.

This script automates the process of creating releases by:
1. Bumping version numbers
2. Creating git tags
3. Generating release notes
4. Pushing changes to GitHub

Usage:
    python scripts/release.py --version 1.0.0
    python scripts/release.py --patch
    python scripts/release.py --minor
    python scripts/release.py --major
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


class ReleaseManager:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.setup_py = self.project_root / "setup.py"
        self.changelog = self.project_root / "CHANGELOG.md"
        self.release_notes = self.project_root / "RELEASE_NOTES.md"
        
    def get_current_version(self) -> str:
        """Extract current version from setup.py"""
        with open(self.setup_py, 'r') as f:
            content = f.read()
        match = re.search(r'version="([^"]+)"', content)
        if not match:
            raise ValueError("Could not find version in setup.py")
        return match.group(1)
    
    def bump_version(self, current_version: str, bump_type: str) -> str:
        """Bump version based on type (major, minor, patch)"""
        parts = current_version.split('.')
        if len(parts) != 3:
            raise ValueError(f"Invalid version format: {current_version}")
        
        major, minor, patch = map(int, parts)
        
        if bump_type == 'major':
            major += 1
            minor = 0
            patch = 0
        elif bump_type == 'minor':
            minor += 1
            patch = 0
        elif bump_type == 'patch':
            patch += 1
        else:
            raise ValueError(f"Invalid bump type: {bump_type}")
        
        return f"{major}.{minor}.{patch}"
    
    def update_setup_py(self, new_version: str) -> None:
        """Update version in setup.py"""
        with open(self.setup_py, 'r') as f:
            content = f.read()
        
        content = re.sub(
            r'version="[^"]+"',
            f'version="{new_version}"',
            content
        )
        
        with open(self.setup_py, 'w') as f:
            f.write(content)
        
        print(f"Updated setup.py version to {new_version}")
    
    def run_command(self, command: str, check: bool = True) -> subprocess.CompletedProcess:
        """Run a shell command"""
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if check and result.returncode != 0:
            print(f"Command failed: {command}")
            print(f"Error: {result.stderr}")
            sys.exit(1)
        return result
    
    def check_git_status(self) -> None:
        """Check if git working directory is clean"""
        result = self.run_command("git status --porcelain")
        if result.stdout.strip():
            print("Error: Working directory is not clean. Please commit or stash changes.")
            sys.exit(1)
    
    def create_git_tag(self, version: str) -> None:
        """Create and push git tag"""
        tag_name = f"v{version}"
        
        # Check if tag already exists
        result = self.run_command(f"git tag -l {tag_name}", check=False)
        if tag_name in result.stdout:
            print(f"Error: Tag {tag_name} already exists")
            sys.exit(1)
        
        # Create tag
        self.run_command(f"git tag -a {tag_name} -m 'Release {tag_name}'")
        print(f"Created tag: {tag_name}")
    
    def push_changes(self, version: str) -> None:
        """Push changes and tags to remote"""
        tag_name = f"v{version}"
        
        # Push commits
        self.run_command("git push origin main")
        
        # Push tag
        self.run_command(f"git push origin {tag_name}")
        
        print(f"Pushed changes and tag {tag_name} to remote")
    
    def generate_release_notes(self, version: str) -> str:
        """Generate release notes for the given version"""
        if version == "1.0.0":
            return self.generate_initial_release_notes()
        
        # For future releases, we would parse CHANGELOG.md
        # For now, return a basic template
        return f"""# Release {version}

## What's New
- Bug fixes and improvements
- See CHANGELOG.md for detailed changes

## Installation
```bash
pip install wrestling-simulator=={version}
```

## Full Changelog
See [CHANGELOG.md](CHANGELOG.md) for the complete list of changes.
"""
    
    def generate_initial_release_notes(self) -> str:
        """Generate release notes for the initial v1.0.0 release"""
        return """# Release v1.0.0 - Initial Release 🎉

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
"""
    
    def create_release_notes_file(self, version: str) -> None:
        """Create RELEASE_NOTES.md file"""
        notes = self.generate_release_notes(version)
        with open(self.release_notes, 'w') as f:
            f.write(notes)
        print(f"Created release notes: {self.release_notes}")
    
    def release(self, version: Optional[str] = None, bump_type: Optional[str] = None) -> None:
        """Main release process"""
        current_version = self.get_current_version()
        print(f"Current version: {current_version}")
        
        if version:
            new_version = version
        elif bump_type:
            new_version = self.bump_version(current_version, bump_type)
        else:
            print("Error: Must specify either --version or a bump type (--major, --minor, --patch)")
            sys.exit(1)
        
        print(f"New version: {new_version}")
        
        # Confirm release
        response = input(f"Create release {new_version}? (y/N): ")
        if response.lower() != 'y':
            print("Release cancelled")
            sys.exit(0)
        
        # Check git status
        self.check_git_status()
        
        # Update version in setup.py
        self.update_setup_py(new_version)
        
        # Create release notes
        self.create_release_notes_file(new_version)
        
        # Commit changes
        self.run_command("git add setup.py RELEASE_NOTES.md")
        self.run_command(f"git commit -m 'Bump version to {new_version}'")
        
        # Create and push tag
        self.create_git_tag(new_version)
        self.push_changes(new_version)
        
        print(f"\n🎉 Release {new_version} created successfully!")
        print(f"GitHub Actions will now build and publish the release.")
        print(f"Check: https://github.com/SthembisoMfusi/Wrestling_simulator/actions")


def main():
    parser = argparse.ArgumentParser(description="Release automation for Wrestling Simulator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--version", help="Specific version to release (e.g., 1.0.0)")
    group.add_argument("--major", action="store_true", help="Bump major version")
    group.add_argument("--minor", action="store_true", help="Bump minor version")
    group.add_argument("--patch", action="store_true", help="Bump patch version")
    
    args = parser.parse_args()
    
    # Determine bump type
    bump_type = None
    if args.major:
        bump_type = "major"
    elif args.minor:
        bump_type = "minor"
    elif args.patch:
        bump_type = "patch"
    
    manager = ReleaseManager()
    manager.release(version=args.version, bump_type=bump_type)


if __name__ == "__main__":
    main()
