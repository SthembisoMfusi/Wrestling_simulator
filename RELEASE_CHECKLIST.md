# Release Checklist

Use this checklist before creating any release to ensure quality and completeness.

## Pre-Release Checklist

### Code Quality
- [ ] All tests pass (`pytest`)
- [ ] Code coverage meets requirements (`pytest --cov=wrestling_simulator`)
- [ ] Code is formatted with Black (`black wrestling_simulator tests`)
- [ ] Linting passes (`flake8 wrestling_simulator tests`)
- [ ] Type checking passes (`mypy wrestling_simulator`)
- [ ] No security vulnerabilities detected

### Documentation
- [ ] README.md is up to date
- [ ] CHANGELOG.md is updated with new changes
- [ ] RELEASE_NOTES.md is prepared for this release
- [ ] API documentation is current (if applicable)
- [ ] Example scripts work correctly

### Version Management
- [ ] Version number follows semantic versioning
- [ ] setup.py version matches intended release version
- [ ] All version references are consistent

### Git Status
- [ ] Working directory is clean (`git status`)
- [ ] All changes are committed
- [ ] Branch is up to date with main
- [ ] No uncommitted changes

### Testing
- [ ] Manual testing of key features completed
- [ ] Example scripts tested
- [ ] CLI interface tested
- [ ] Cross-platform compatibility verified (if applicable)

## Release Process

### Automated Release (Recommended)
- [ ] Run release script: `python scripts/release.py --[patch|minor|major]`
- [ ] Confirm version bump is correct
- [ ] Verify release notes are generated
- [ ] Check that tag is created and pushed

### Manual Release
- [ ] Update version in setup.py
- [ ] Update RELEASE_NOTES.md
- [ ] Commit changes with appropriate message
- [ ] Create and push git tag
- [ ] Push changes to main branch

## Post-Release Checklist

### Verification
- [ ] GitHub release is created successfully
- [ ] Release assets are uploaded correctly
- [ ] PyPI package is published (for stable releases)
- [ ] Installation works: `pip install wrestling-simulator==X.Y.Z`

### Communication
- [ ] Release notes are clear and comprehensive
- [ ] Breaking changes are documented (if any)
- [ ] Migration guide provided (if needed)
- [ ] Community is notified (if applicable)

### Monitoring
- [ ] Monitor GitHub Actions for any failures
- [ ] Check PyPI for successful upload
- [ ] Monitor for user feedback and issues
- [ ] Verify download statistics

## Emergency Procedures

### If Release Fails
- [ ] Check GitHub Actions logs
- [ ] Verify git tag was created correctly
- [ ] Check for any missing dependencies
- [ ] Contact maintainers if needed

### If Rollback is Needed
- [ ] Document reason for rollback
- [ ] Delete GitHub release (if created)
- [ ] Contact PyPI support to remove package
- [ ] Update documentation
- [ ] Notify users of rollback

## Release Types

### Patch Release (X.Y.Z -> X.Y.Z+1)
- [ ] Bug fixes only
- [ ] No new features
- [ ] Backward compatible
- [ ] Quick testing cycle

### Minor Release (X.Y.Z -> X.Y+1.0)
- [ ] New features added
- [ ] Backward compatible
- [ ] Full testing cycle
- [ ] Documentation updated

### Major Release (X.Y.Z -> X+1.0.0)
- [ ] Breaking changes
- [ ] Migration guide provided
- [ ] Extensive testing
- [ ] Community notification
- [ ] Deprecation warnings (if applicable)

## Quality Gates

### Must Pass
- All tests pass
- Code formatting is correct
- Linting passes
- Type checking passes
- Documentation is current

### Should Pass
- Code coverage > 80%
- No security vulnerabilities
- Performance benchmarks met
- Cross-platform compatibility

### Nice to Have
- Performance improvements
- New features
- Enhanced documentation
- Additional test coverage

## Notes

- Always test the release process in a development environment first
- Keep release notes user-friendly and informative
- Consider the impact on existing users
- Plan releases during low-activity periods when possible
- Have a rollback plan ready

---

**Remember**: Quality over speed. It's better to delay a release than to ship broken code.
