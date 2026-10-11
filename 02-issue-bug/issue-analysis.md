\# Issue analysis: roboflow/supervision#2578



\*\*Title:\*\* LineZone counts detections with tracker\_id = -1 as one shared track (silent count inflation with roboflow/trackers)



| Field | Value |

|---|---|

| Reporter | zachsplat (Contributor) |

| Opened | about 1 month before 11 Oct 2026 |

| Labels | bug, help wanted (added by maintainer Borda) |

| Assignee | none |

| Status | Closed as completed, about 2 weeks ago, by Borda via PR #2623 |

| Comments | 3 |

| Linked PRs | 3 (one merged: #2623) |



\## Summary of the problem

LineZone.trigger() keys its crossing state by tracker\_id. Trackers such as

roboflow/trackers return -1 for tracks they have not confirmed yet, so on a busy

frame many different unconfirmed objects share the id -1. Their independent

motion makes one phantom track cross the line again and again, and the counts

inflate silently. The reporter saw a correct \~7/9 become 97/95 on the same footage.



\## Expected behaviour

Detections with tracker\_id of -1 or None should not take part in crossing counts.



\## Fix

PR #2623 "fix(LineZone): ignore unconfirmed tracks with negative tracker\_id"

(merged). trigger() now skips detections whose tracker\_id is negative.

