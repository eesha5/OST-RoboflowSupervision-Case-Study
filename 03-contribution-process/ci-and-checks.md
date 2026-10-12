# CI and Code Quality Checks

## 1. Overview

Roboflow Supervision uses automated checks to help maintain code quality, test correctness, documentation quality, and consistency across contributions.

The repository contains a pre-commit configuration and GitHub Actions workflows. These checks help contributors identify problems before their changes are merged.

## 2. Pre-commit Configuration

The configuration is available in `.pre-commit-config.yaml` in the official repository.

Source: https://github.com/roboflow/supervision/blob/develop/.pre-commit-config.yaml

The contribution guidelines mention tools such as:

- **Ruff:** checks Python code for linting issues and formatting consistency.
- **mypy:** checks Python type annotations and detects certain type-related errors.
- **codespell:** detects common spelling mistakes.
- **docformatter:** formats Python docstrings consistently.

The exact hooks and versions should be confirmed from the repository's current pre-commit configuration.

## 3. Running Checks Locally

Contributors should set up the development environment and run the project's tests before submitting changes.

```bash
uv run pytest
```

Pre-commit hooks can also be run locally when the environment has been configured:

```bash
uv run pre-commit run --all-files
```

These commands help catch test failures and code-quality issues before review. Use the repository's documented setup instructions if a command is unavailable in your environment.

## 4. GitHub Actions Workflows

The repository stores its workflow definitions in `.github/workflows/`.

Source: https://github.com/roboflow/supervision/tree/develop/.github/workflows

The visible workflow filenames include:

- `build-package.yml`
- `ci-build-docs.yml`
- `ci-check-links.yml`
- `ci-docs-stats.yml`
- `ci-github-tests.yml`
- `ci-tests.yml`
- `clear-cache.yml`
- `docs-backfill.yml`
- `pr-conflict-labeler.yml`
- `publish-docs.yml`

Workflow filenames indicate the areas automated by the repository. The exact jobs and checks performed by each workflow must be confirmed by opening its YAML file.

## 5. Pull Request Checks in Practice

The project's pull requests show the results of automated checks in the GitHub Checks tab.

For example, the group's pull request #2719 displayed successful checks for the CLA, pre-commit.ci, and Socket Security. It also displayed workflows awaiting maintainer approval and a pending code-owner review.

This demonstrates that successful individual checks do not necessarily mean a pull request is ready to merge. Required reviews and other pending checks must also be resolved.

Evidence: https://github.com/roboflow/supervision/pull/2719

## 6. Why These Checks Matter

Automated testing helps detect regressions. Linting and formatting tools encourage consistent code. Type checking catches certain mistakes before runtime, while documentation and link checks help keep project resources usable.

Together, local checks, continuous integration, and human review provide multiple layers of quality control before a contribution is merged.
