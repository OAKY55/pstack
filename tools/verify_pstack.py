#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "PSTACK_MANIFEST.json").read_text(encoding="utf-8"))
canonical = ROOT / manifest["canonical_file"]
data = canonical.read_bytes()

header = f"blob {len(data)}\0".encode("utf-8")
git_blob_sha1 = hashlib.sha1(header + data).hexdigest()
expected = manifest["canonical_git_blob_sha1"]

print(f"PSTACK_VERSION={manifest['version']}")
print(f"CANONICAL_FILE={manifest['canonical_file']}")
print(f"EXPECTED_GIT_BLOB_SHA1={expected}")
print(f"ACTUAL_GIT_BLOB_SHA1={git_blob_sha1}")

if git_blob_sha1 == expected:
    print("PSTACK_CHECKSUM_STATUS=PASS")
    raise SystemExit(0)

print("PSTACK_CHECKSUM_STATUS=FAIL")
raise SystemExit(1)
