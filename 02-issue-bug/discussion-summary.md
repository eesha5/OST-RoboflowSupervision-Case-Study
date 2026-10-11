\# Discussion and maintainer response for #2578



\## Timeline

1\. The reporter opened the issue with a minimal reproduction, expected behaviour,

&#x20;  a suggested fix and the environment (supervision 0.29.1, trackers 2.4.0,

&#x20;  numpy 2.3.5, Python 3.12). He offered to open a PR himself.

2\. Maintainer Borda added the labels bug and help wanted.

3\. zeel2104 asked: "Is it open for contribution?"

4\. srijavuppala said they would add a guard in LineZone.trigger() to skip

&#x20;  tracker\_id None or < 0, plus a regression test, and open a PR shortly.

5\. The reporter said he would watch for the PR and could add a test from his

&#x20;  RTSP pipeline.

6\. The reporter added 2 commits referencing the issue.

7\. Borda closed the issue as completed through PR #2623.



\## Observations

\- The maintainer's only visible actions were labelling and merging the final PR.

\- Three PRs were linked. Two appear to have been closed without merging and the

&#x20; one merged is #2623, so several people competed on a small fix.

\- A clear minimal reproduction made the issue easy to confirm and fix.

