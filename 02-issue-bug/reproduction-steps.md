\# Reproduction steps for issue #2578



Issue: LineZone counts detections with tracker\_id = -1 as one shared track.



\## Setup

1\. python -m venv .venv and activate it

2\. pip install supervision==0.29.1 numpy==2.3.5

3\. Save repro\_2578.py (from the issue's minimal example) and run it



\## Expected

Unconfirmed detections (tracker\_id -1) should not take part in crossing counts.

Both lines should print 0 0.



\## Actual (supervision 0.29.1, numpy 2.3.5)

2 3

0 0

Two different objects with id -1 are merged into one track, giving 5 phantom crossings.



\## After the fix (develop, 0.31.0.dev0)

0 0

0 0



\## Extra finding

supervision 0.29.1 with numpy 2.5.4 crashes in LineZone.trigger with

"ValueError: Both input arrays must be 3-dimensional vectors" (np.cross on 2-D

vectors). Related to the NumPy 2.0 deprecation reported in issue #2384.



Screenshots: see the screenshots/ folder.

