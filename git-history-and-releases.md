# Git History and Releases Investigation

**Investigated by:** Mahek Mishra — Member 1  
**Investigation date:** 11 October 2026  
**Official repository:** https://github.com/roboflow/supervision  
**Source branch inspected:** develop

## 1. Investigation Method

I cloned the official Supervision repository and inspected its Git
history, author commit counts, version tags, and GitHub release notes.

Commands used:

```bash
git remote -v
git rev-parse HEAD
git --no-pager log -10 --oneline
git shortlog -sn HEAD
git tag --sort=-version:refname
```

## 2. Source Revision

The inspected develop branch pointed to this commit:
714ad2378aa4b20b7cc41170b564a7214669a0aa
Recording the commit identifies the source revision used for this
investigation, even if the branch changes later.
The local demonstration used the installed Supervision package
version 0.30.9. The inspected develop branch and the installed release
are separate versions of the project.

## 3. Recent Commit Observations

The ten recent commits inspected included:
- A fix to limit MeanAverageRecall detections per image and class.
- A fix for conversion of NumPy-backed Ultralytics results.
- New depth-map loading and distance-measurement features.
- New COCO keypoint evaluation support.
- Documentation and development-tool updates.
This sample shows several kinds of maintenance: bug fixes, new
features, documentation, and tooling. Ten commits alone do not
establish the project's long-term commit frequency.

## 4. Author Commit Counts

The command git shortlog -sn HEAD grouped commits by author identity
in the history reachable from the inspected revision.
Examples from the output:
Author identity	Commit count
SkalskiP	855
Onuralp SEZER	847
pre-commit-ci[bot]	585
Piotr Skalski	494
LinasKo	379
dependabot[bot]	378

The output includes human author identities and automated bots.
Different names may belong to the same person, so these rows should
not be treated as a count of unique people.
Commit counts also do not measure contribution quality or include
every activity, such as reviews, discussions, and issue reporting.

## 5. Version Tags and Releases

The version-sorted tag list began with:
- 0.30.9
- 0.30.8
- 0.30.7
- 0.30.6
- 0.30.5
The GitHub releases page marked supervision-0.30.9 as Latest at the
time of inspection.
Its release notes described changes including:
- More consistent BoxAnnotator borders with and without OpenCV.
- Video-reading fixes for certain WebM and MKV files.
- Validation fixes for invalid bounding-box coordinates.
- Rejection of negative values of k in get_top_k.
- Cleanup of expired tracks in DetectionsSmoother.
These are observations from the published release notes. My local
demo tested annotation and confidence filtering, rather than all
the changes listed in this release.

## 6. Evidence

- S16-upstream-git-history.png
- S17-contributor-commit-counts.png
- S18-version-tags.png
- S19-release-notes.png

## 7. References
- Official repository: https://github.com/roboflow/supervision
- Releases: https://github.com/roboflow/supervision/releases
