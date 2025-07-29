# Git Branching Strategy: Feature → Dev → Main

This document outlines the branching strategy for the PharmaSage project, implementing a three-tier workflow for safe and controlled code deployment.

## Branch Structure

### 1. **Main Branch** (`main`)
- **Purpose**: Production-ready code
- **Protection**: Highly protected, only accepts merges from `dev`
- **Deployment**: Automatically deployed to production
- **Rules**: 
  - No direct commits allowed
  - Only merge from `dev` after thorough testing
  - All merges require pull request review

### 2. **Development Branch** (`dev`)
- **Purpose**: Integration and staging environment
- **Protection**: Moderately protected, accepts merges from feature branches
- **Testing**: All features are integrated and tested here
- **Rules**:
  - No direct commits for features
  - Only merge from feature branches via pull requests
  - Must pass all CI/CD tests before merging to `main`

### 3. **Feature Branches** (`features/*`)
- **Purpose**: Individual feature development
- **Naming Convention**: `features/feature-name` or `features/issue-number-description`
- **Lifecycle**: Created from `dev`, merged back to `dev`
- **Rules**:
  - Always branch from latest `dev`
  - Regular commits during development
  - Merge to `dev` via pull request

## Workflow Process

### Step 1: Feature Development
```bash
# Start from dev branch
git checkout dev
git pull origin dev

# Create feature branch
git checkout -b features/your-feature-name

# Develop your feature
# ... make changes, commits ...

# Push feature branch
git push -u origin features/your-feature-name
```

### Step 2: Feature to Dev
```bash
# Create pull request: features/your-feature-name → dev
# After review and approval, merge to dev
git checkout dev
git pull origin dev

# Feature branch can be deleted after merge
git branch -d features/your-feature-name
git push origin --delete features/your-feature-name
```

### Step 3: Dev to Main (Release)
```bash
# After thorough testing in dev environment
# Create pull request: dev → main
# After review and approval, merge to main
git checkout main
git pull origin main

# Tag the release (optional but recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Branch Protection Rules

### Main Branch Protection
- Require pull request reviews before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Restrict pushes that create files larger than 100MB
- Do not allow force pushes
- Do not allow deletions

### Dev Branch Protection
- Require pull request reviews before merging
- Require status checks to pass before merging
- Allow force pushes (for emergency fixes)

## Best Practices

### 1. **Feature Branch Naming**
- Use descriptive names: `features/user-authentication`
- Include issue numbers: `features/123-fix-login-bug`
- Use kebab-case: `features/api-integration-improvements`

### 2. **Commit Messages**
- Use conventional commits format
- Examples:
  - `feat: add user authentication system`
  - `fix: resolve login redirect issue`
  - `docs: update API documentation`
  - `test: add unit tests for user service`

### 3. **Pull Request Guidelines**
- Provide clear description of changes
- Include screenshots for UI changes
- Reference related issues
- Ensure all tests pass
- Request appropriate reviewers

### 4. **Testing Strategy**
- **Feature Branch**: Unit tests and local testing
- **Dev Branch**: Integration tests, staging environment testing
- **Main Branch**: Production deployment with monitoring

## Emergency Hotfixes

For critical production issues:

```bash
# Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-bug-fix

# Make the fix
# ... implement fix ...

# Push and create PR to main
git push -u origin hotfix/critical-bug-fix
# Create PR: hotfix/critical-bug-fix → main

# After merging to main, also merge to dev
git checkout dev
git merge main
git push origin dev
```

## Current Branch Status

- ✅ **main**: Production branch (current: `5a5a1ac`)
- ✅ **dev**: Development branch (created and synced)
- 🔄 **features/**: Existing feature branches available for cleanup/migration

## Migration of Existing Feature Branches

Existing feature branches should be evaluated:
- `features/api_payload_validation` - Can be rebased onto dev if needed
- `features/backend_setup` - Review and potentially merge or close
- `features/buyer_discovery_frontend_changes` - Review and potentially merge or close
- `features/perplexity_api_integration` - Review and potentially merge or close

## Tools and Automation

Consider implementing:
- **GitHub Actions** for CI/CD pipeline
- **Branch protection rules** in GitHub
- **Automated testing** on pull requests
- **Code quality checks** (linting, security scans)
- **Deployment automation** from main branch

## Getting Started

1. **For new features**: Always start from `dev` branch
2. **For bug fixes**: Create feature branch from `dev`
3. **For releases**: Merge `dev` to `main` after thorough testing
4. **For hotfixes**: Branch from `main`, fix, merge to both `main` and `dev`

This strategy ensures code quality, reduces production bugs, and provides a clear path for feature development and deployment.
