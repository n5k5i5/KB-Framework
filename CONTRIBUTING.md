# CONTRIBUTING

Thank you for considering contributing to KB-OSINT. This project aims to be secure, extensible, and community-friendly.

## Ground Rules
- Follow security-first principles
- Keep modules minimal and well-documented
- Write tests when adding functionality (future phases)
- Use semantic versioning

## Code Standards
- Consistent naming (Turkish UI, English code identifiers acceptable)
- Clear manifest metadata for modules
- Avoid hardcoding secrets; use environment variables

## Testing Requirements
- Unit tests and smoke tests for new modules (templates will be provided)
- Dependency and CVE scanning for third-party packages

## Documentation
- Update relevant docs in `docs/` folders
- Provide usage examples and permission requirements for modules

## Security Review
- Module signature verification (planned)
- Developer whitelist for community modules (planned)
- Runtime sandbox policies (planned)

## Pull Request Process
1. Fork and create a feature/fix branch
2. Make changes and update docs
3. Ensure basic checks pass
4. Submit a PR with a clear description and checklist