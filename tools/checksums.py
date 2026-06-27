#!/usr/bin/env python3
import hashlib
import glob
import os
import sys

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def find_artifacts():
    patterns = [
        '*.tgz',
        'java-springboot-app/target/*.jar',
        'python-django-app/dist/*',
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    return sorted(files)

def write_checksums(files, out_path='artifacts/checksums.sha256'):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as out:
        for f in files:
            h = sha256_file(f)
            out.write(f"{h}  {f}\n")
    print('Wrote', out_path)

def verify_checksums(path='artifacts/checksums.sha256'):
    if not os.path.exists(path):
        print('Checksum file not found:', path)
        return 2
    ok = True
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            expected, fname = line.split(None, 1)
            fname = fname.strip()
            if not os.path.exists(fname):
                print('Missing artifact:', fname)
                ok = False
                continue
            actual = sha256_file(fname)
            if actual != expected:
                print('Mismatch:', fname)
                ok = False
    return 0 if ok else 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--verify':
        sys.exit(verify_checksums())
    files = find_artifacts()
    if not files:
        print('No build artifacts found to checksum; run builds first.')
        sys.exit(1)
    write_checksums(files)
