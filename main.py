# The toaster's error message, one line, to /output/entry.txt.
# Deterministic and offline: the same bytes on every run.
# Deadpan appliance voice: it is a toaster, not a woodchipper.
# The surprise is the woodchipper, not the burnt bread.
import os

ERROR = "ERROR: Bread jammed. Please stop feeding me bagels. I am a toaster, not a woodchipper."

dest = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(dest, exist_ok=True)
with open(os.path.join(dest, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ERROR)  # 86 chars, gate allows 120; lands on a single read
