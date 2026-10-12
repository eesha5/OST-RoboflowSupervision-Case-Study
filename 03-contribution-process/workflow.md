# Contribution Workflow

This document describes the contribution process followed by the Roboflow Supervision open-source project, from preparing a development environment to reviewing and merging a pull request.

## Step 1: Fork the Repository

Create a fork of the official repository under your GitHub account. A fork provides a personal copy where changes can be developed without directly modifying the original project.

Official repository: https://github.com/roboflow/supervision

## Step 2: Clone and Configure Upstream

Clone your fork and configure the official repository as the upstream remote.

```bash
git clone https://github.com/YOUR_USERNAME/supervision.git
cd supervision
git remote add -t develop upstream https://github.com/roboflow/supervision.git
git fetch upstream
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 3: Create a Branch

Create a working branch from the official project's development branch. The contribution guidelines use prefixes to communicate the type of change.

```bash
git checkout -b docs/my-documentation-change upstream/develop
```

Common branch prefixes include:

- `feat/` — new features
- `fix/` — bug fixes
- `docs/` — documentation changes
- `chore/` — maintenance tasks
- `test/` — testing changes
- `refactor/` — code restructuring

## Step 4: Set Up the Development Environment and Run Checks

Follow the repository's documented environment setup instructions. The contribution instructions specify using a virtual environment and `uv`.

The documented dependency installation command is:

```bash
uv pip install -r pyproject.toml --group dev --group docs --extra metrics
```

Run the test suite using:

```bash
uv run pytest
```

Also run the required formatting, linting, and other checks described in the project's contribution guidelines.

## Step 5: Commit Changes

Use conventional commit messages that explain the type of change.

Examples:

```text
feat: add a useful computer vision feature
fix: correct line zone tracking behavior
docs: improve API usage examples
test: add regression tests
```

The general format is `<type>[optional scope]: <description>`.

## Step 6: Open a Pull Request

Push the branch to your fork and open a pull request against the official repository's `develop` branch.

```bash
git push -u origin docs/my-documentation-change
```

Follow the repository's pull request template. Explain the motivation, describe the changes, and provide the required testing and documentation information.

## Step 7: Complete CLA and CI Requirements

Complete the Contributor License Agreement (CLA) process when prompted by the CLA Assistant.

Wait for the required automated checks to run. Resolve any failing tests, linting problems, or other reported issues before requesting the changes be merged.

For first-time contributors, some GitHub Actions workflows may require a maintainer's approval before execution.

## Step 8: Code Review and Merge

The pull request is reviewed by maintainers and, where configured, code owners. Reviewers assess correctness, tests, documentation, completeness, and risk.

Address requested changes and update the pull request when necessary. The project can merge the contribution after its required review and repository checks are satisfied.

## Evidence and Source

These steps summarize the intended workflow. Individual pull requests may take different amounts of time or require additional revisions.

Official contribution instructions: https://github.com/roboflow/supervision/blob/develop/.github/CONTRIBUTING.md

Pull request template: https://github.com/roboflow/supervision/blob/develop/.github/PULL_REQUEST_TEMPLATE.md
