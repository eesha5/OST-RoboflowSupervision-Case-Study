# Contribution Guidelines

## 1. Welcome Contributions

The Supervision project welcomes contributions that improve the library, including:

- New features that solve useful computer-vision problems.
- Documentation improvements and practical examples.
- Bug reports and issue investigations.
- Suggestions for new features.
- Improvements to test coverage.

The project's guidelines encourage contributors to discuss a proposed feature through an issue before implementing it. This helps the community assess whether the feature would benefit a broad range of projects.

**Evidence:** [Official CONTRIBUTING.md](https://github.com/roboflow/supervision/blob/develop/.github/CONTRIBUTING.md)

## 2. Code of Conduct

The repository contains a Code of Conduct that establishes expectations for respectful and constructive participation. Contributors should communicate professionally, collaborate respectfully, and help maintain an inclusive community.

**Evidence:** [CODE_OF_CONDUCT.md](https://github.com/roboflow/supervision/blob/develop/.github/CODE_OF_CONDUCT.md)

## 3. Issue Templates

The repository provides issue templates under `.github/ISSUE_TEMPLATE`. These templates help contributors structure bug reports and feature requests so maintainers can understand the problem or proposed change.

Before submitting a report, contributors should inspect the available templates and provide the information requested by the relevant template.

**Evidence:** [Issue templates](https://github.com/roboflow/supervision/tree/develop/.github/ISSUE_TEMPLATE)

## 4. API Design Principles

The contribution guidelines emphasize building generic utilities that solve common problems across computer-vision projects rather than narrowly tailored features with limited usefulness.

For example, counting objects that cross a line is a broadly useful computer-vision operation, while counting objects only when they cross at a specific percentage of an image is a much more restrictive requirement.

When proposing an API change, contributors should consult the official guidelines and consider whether the design is useful, consistent, and appropriate for the wider library.

**Evidence:** [API design and feature guidance](https://github.com/roboflow/supervision/blob/develop/.github/CONTRIBUTING.md)

## 5. Why These Guidelines Matter

Contribution guidelines help contributors understand what the project accepts, how to report problems, and how to prepare changes for review. Issue templates improve the information available to maintainers, while the Code of Conduct establishes expectations for community participation.

Together, these practices make contributions easier to evaluate and help maintain the quality and consistency of an open-source project.
