# Member 2: Issue and Bug Investigation

Name: Heer Chelwani

Selected project: Roboflow Supervision

Official repository: https://github.com/roboflow/supervision

Issue investigated: https://github.com/roboflow/supervision/issues/2578

Fixing pull request: https://github.com/roboflow/supervision/pull/2623

## My Responsibilities

- Search Supervision's issue tracker and shortlist candidate issues with reasons for each.
- Select one issue that can be reproduced on a laptop without a trained model or video.
- Analyse the selected issue: reporter, labels, status, linked pull requests and timeline.
- Summarise the discussion and the maintainer's response.
- Record the exact environment: operating system, Python, Supervision and NumPy versions.
- Write a reproduction script based on the issue's minimal example.
- Reproduce the bug on the affected release and record expected versus actual results.
- Confirm the fix on the develop branch.
- Document extra findings, such as the NumPy 2.5.4 crash on the old release.
- Capture screenshots as evidence for each stage.
- Prepare my report sections (Issue Investigation, Bug Investigation) and presentation slides.

## Summary

| Item | Result |
|---|---|
| Issue | #2578: LineZone counts detections with tracker_id = -1 as one shared track |
| Buggy version | supervision 0.29.1, NumPy 2.3.5: prints `2 3` (5 phantom crossings) |
| Fixed version | develop (0.31.0.dev0): prints `0 0` (correct) |
| Fixed by | PR #2623, merged by maintainer Borda |
| Extra finding | 0.29.1 with NumPy 2.5.4 crashes with a ValueError from np.cross |

## Contents

- [Issue shortlist](issue-shortlist.md)
- [Issue analysis](issue-analysis.md)
- [Discussion summary](discussion-summary.md)
- [Environment](environment.md)
- [Reproduction steps](reproduction-steps.md)
- [Reproduction script
