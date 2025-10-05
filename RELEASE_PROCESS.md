# Release Process

This document outlines the process for creating and publishing releases of Wrestling Simulator.

## Overview

The release process is automated using GitHub Actions and a custom release script. Releases are created by pushing git tags, which triggers the automated build and publication process.

## Prerequisites

1. **GitHub Repository Access**: You must have push access to the main repository
2. **PyPI Account**: For publishing to PyPI (optional, for public releases)
3. **Clean Working Directory**: All changes must be committed before creating a release

## Release Types

### Automated Release (Recommended)

Use the release script for automated version bumping and tagging:

```bash
# For patch releases (1.0.0 -> 1.0.1)
python scripts/release.py --patch

# For minor releases (1.0.0 -> 1.1.0)
python scripts/release.py --minor

# For major releases (1.0.0 -> 2.0.0)
python scripts/release.py --major

# For specific version
python scripts/release.py --version 1.2.3
```

### Manual Release

1. **Update Version**: Manually edit `setup.py` to update the version number
2. **Create Release Notes**: Update `RELEASE_NOTES.md` with release details
3. **Commit Changes**: 
   ```bash
   git add setup.py RELEASE_NOTES.md
   git commit -m "Bump version to X.Y.Z"
   ```
4. **Create Tag**:
   ```bash
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push origin main
   git push origin vX.Y.Z
   ```

## Release Checklist

Before creating a release, ensure:

- [ ] All tests pass (`pytest`)
- [ ] Code is formatted (`black wrestling_simulator tests`)
- [ ] Linting passes (`flake8 wrestling_simulator tests`)
- [ ] Type checking passes (`mypy wrestling_simulator`)
- [ ] Documentation is up to date
- [ ] CHANGELOG.md is updated
- [ ] RELEASE_NOTES.md is prepared
- [ ] Working directory is clean (`git status`)

## Automated Workflow

When a tag is pushed, GitHub Actions will:

1. **Checkout Code**: Get the latest code from the repository
2. **Setup Python**: Install Python 3.10
3. **Install Dependencies**: Install build tools (build, twine)
4. **Extract Version**: Get version from the git tag
5. **Update setup.py**: Ensure version matches the tag
6. **Build Package**: Create wheel and source distribution
7. **Check Package**: Validate package integrity
8. **Create GitHub Release**: Create release with assets
9. **Upload Assets**: Attach wheel and source distribution
10. **Publish to PyPI**: Upload to PyPI (for stable releases only)

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0): Incompatible API changes
- **MINOR** (X.Y.0): Backwards-compatible functionality additions
- **PATCH** (X.Y.Z): Backwards-compatible bug fixes

### Pre-release Versions

For pre-release versions, use suffixes:
- `1.0.0-alpha.1` - Alpha releases
- `1.0.0-beta.1` - Beta releases  
- `1.0.0-rc.1` - Release candidates

Pre-releases are not automatically published to PyPI.

## Release Notes

### CHANGELOG.md

Maintain a comprehensive changelog following [Keep a Changelog](https://keepachangelog.com/) format:

```markdown
## [1.0.0] - 2024-12-19

### Added
- New features

### Changed
- Changes to existing functionality

### Fixed
- Bug fixes
```

### RELEASE_NOTES.md

Create detailed release notes for each release including:
- What's new in this release
- Installation instructions
- Usage examples
- Breaking changes (if any)
- Migration guide (if needed)

## PyPI Publishing

### Setup

1. Create a PyPI account at https://pypi.org
2. Generate an API token
3. Add the token as a GitHub secret named `PYPI_API_TOKEN`

### Automatic Publishing

Stable releases (not pre-releases) are automatically published to PyPI when:
- The tag is pushed to the main branch
- The version doesn't contain alpha, beta, or rc suffixes
- The `PYPI_API_TOKEN` secret is configured

### Manual Publishing

To manually publish to PyPI:

```bash
# Build the package
python -m build

# Upload to PyPI
twine upload dist/*
```

## Rollback Process

If a release needs to be rolled back:

1. **GitHub Release**: Delete the release from GitHub (this doesn't affect the tag)
2. **PyPI**: Contact PyPI support to remove the package version
3. **Documentation**: Update documentation to reflect the rollback
4. **Communication**: Notify users of the rollback and reason

## Troubleshooting

### Common Issues

1. **Tag Already Exists**: Delete the tag locally and remotely, then recreate
2. **Build Failures**: Check GitHub Actions logs for specific errors
3. **PyPI Upload Failures**: Verify API token and package name availability
4. **Version Conflicts**: Ensure version numbers are unique and follow semver

### Getting Help

- Check GitHub Actions logs for build issues
- Review the release script output for automation issues
- Consult the [GitHub Actions documentation](https://docs.github.com/en/actions)
- Check [PyPI documentation](https://packaging.python.org/) for publishing issues

## Security Considerations

- **API Tokens**: Never commit API tokens to the repository
- **Secrets**: Use GitHub Secrets for sensitive information
- **Package Integrity**: Always verify package checksums
- **Dependencies**: Keep dependencies up to date and scan for vulnerabilities

## Best Practices

1. **Test Before Release**: Always run tests locally before creating a release
2. **Incremental Releases**: Prefer smaller, more frequent releases
3. **Clear Communication**: Write clear, detailed release notes
4. **Backward Compatibility**: Maintain backward compatibility when possible
5. **Documentation**: Keep documentation synchronized with releases
6. **Monitoring**: Monitor release success and user feedback

## Release Schedule

- **Patch Releases**: As needed for bug fixes
- **Minor Releases**: Monthly for new features
- **Major Releases**: Quarterly or when breaking changes are needed
- **Pre-releases**: As needed for testing new features

## Contact

For questions about the release process:
- Create an issue in the repository
- Contact the maintainers
- Check the documentation in the `docs/` directory
