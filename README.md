# CA-3: Case Study of Roboflow Supervision

Hands-on open-source case study of [Roboflow Supervision](https://github.com/roboflow/supervision): exploring the codebase, reproducing a real bug, and contributing a fix through a pull request.

## Course Details

- **Course:** Open Source Technologies (TE7756)
- **Institute:** Symbiosis Institute of Technology, Pune
- **Project studied:** [roboflow/supervision](https://github.com/roboflow/supervision), an open-source Python toolkit for computer vision
- **License:** MIT

## Group Members

| Name | Roll No. | Member | Role |
|---|---|---|---|
| **Eesha Masand** | 24070127043 | 4 | Our Contribution (Fix & Pull Request) |
| Mahek Mishra | 24070127066 | 1 | Project & Repository |
| Heer Chelwani | 24070127051 | 2 | Issue & Bug Investigation |
| Prashobh Prasad | 24070127090 | 3 | Contribution Process & PR Investigation |

## Our Upstream Contribution

**Pull request:** [roboflow/supervision #2719](https://github.com/roboflow/supervision/pull/2719): *docs: fix missing and incorrect imports in docstring examples*

- Found 4 docstring examples in Supervision that fail with `NameError` when copied
- Fixed all 4 (4 files changed, 4 insertions, 1 deletion)
- Pre-commit checks passed; full test suite: 5,393 passed, 0 failed
- **Status:** open, CLA signed, awaiting code-owner review

## Repository Contents

| Folder | Member | What's inside |
|---|---|---|
| [`01-project-repo/`](01-project-repo/) | 1 | Project identification, features, license, repository structure, code walkthrough, Git history, working demo |
| [`02-issue-bug/`](02-issue-bug/) | 2 | Issue shortlist, analysis of issue #2578, discussion summary, bug reproduction scripts and evidence |
| [`03-contribution-process/`](03-contribution-process/) | 3 | Contribution guidelines, workflow, CI and review process, analysis of a merged pull request |
| [`04-our-pull-request/`](04-our-pull-request/) | 4 | Development setup, bug discovery, the fix, testing, and our pull request #2719 |
| [`presentation/`](presentation/) | All | Presentation slides |

## Workflow

Each member works on their own branch and opens a pull request into `main`, which is reviewed by another member before merging.

## References

- Supervision repository: https://github.com/roboflow/supervision
- Supervision documentation: https://supervision.roboflow.com
- Contribution guidelines: https://github.com/roboflow/supervision/blob/develop/.github/CONTRIBUTING.md
