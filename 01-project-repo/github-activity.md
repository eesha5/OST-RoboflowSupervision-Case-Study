# GitHub Activity Investigation

**Investigated by:** Mahek Mishra — Member 1
**Observation date:** 11 October 2026

## Contributor Activity

I inspected the official Supervision repository's GitHub
Contributors page.

The captured contributor cards showed:

| Account | Displayed commits |
|---|---:|
| Borda | 189 |
| codex | 87 |
| claude[bot] | 66 |
| claude | 58 |
| pre-commit-ci[bot] | 48 |
| kevin9327 | 35 |

These values describe the selected view when the screenshot
was captured. They are not necessarily lifetime commit totals.

Accounts explicitly marked [bot] represent automated accounts.
Account names alone do not establish the identity of a human author.

## Commit Frequency Observations

The contributor graphs show activity across the displayed
August–October 2026 period.

Several accounts have contributions in multiple time intervals.
The bars vary in height, showing that activity was uneven
throughout the displayed period.

These individual graphs support an observation of recurring
contributions. They do not establish an exact repository-wide
daily or weekly commit rate.

## Difference from Local Git Counts

The local command git shortlog -sn HEAD groups commits by author
identity in the history reachable from the inspected revision.

GitHub's contributor view uses its own account attribution and
selected view. Its displayed counts can therefore differ from
the local Git output.

Neither commit counts nor lines changed directly measure
contribution quality.

## Evidence

See evidence/S20-github-activity.png.

## Reference

https://github.com/roboflow/supervision/graphs/contributors
