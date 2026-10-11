\# Issue shortlist



Repository: roboflow/supervision. Date of search: 11 Oct 2026.



\## How the candidates were chosen

\- All open issues labelled `bug` already have a linked pull request (a search for

&#x20; open bugs without a linked PR returned zero results), so no unfixed open bug was

&#x20; available to investigate.

\- Open issues labelled `question` that looked like bugs (#1838, #1728) turned out

&#x20; to be usage or configuration problems, not library bugs.

\- We therefore chose recently closed bugs that have a short, runnable example,

&#x20; so the problem can be reproduced on an older version and checked against the fix.



\## Candidate 1 (selected): #2578

LineZone counts detections with tracker\_id = -1 as one shared track.

\- Reporter: zachsplat. Labels: bug, help wanted. Closed by PR #2623.

\- Why: 3 comments and 3 linked PRs, pure NumPy example with no video or model,

&#x20; exact environment given. Reproduced: yes (supervision 0.29.1 + numpy 2.3.5 gives

&#x20; "2 3"; develop gives "0 0").



\## Candidate 2 (backup): #2658

LineZoneAnnotator(text\_orient\_to\_line=True) raises TypeError for flipCode

without OpenCV.

\- Reporter: kari-pikkarainen. Label: bug. Closed by PR #2659 two days after opening.

\- Why: short example, ties to the no-OpenCV fallback. Reproduction script written

&#x20; (repro\_2658.py), fixed behaviour confirmed on develop. No discussion on the issue.



\## Candidate 3 (backup): #2598

LineZone: sub-threshold flicker produces a spurious crossing in the opposite direction.

\- Reporter: jharie. Label: bug. Closed about 3 weeks before 11 Oct 2026, 1 PR, 3 comments.

\- Why: pure LineZone logic with a discussion. Not yet reviewed in detail.



\## Candidates rejected

\- #1838, #1728: question-labelled, user configuration problems.

\- #2674: no longer reproduces on develop and its reporter already has a fix.

\- #2594: needs a model and image slicing to reproduce.

\- #2384, #2434: too trivial or with too little discussion.



\## Agreement with Member 4

Selected issue: #2578 (to be confirmed with Member 4).

Member 4's own pull request should target a different, still-open issue.

