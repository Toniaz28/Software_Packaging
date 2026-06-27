# 3MTT Software Packaging Project

This workspace provides a starter repository for learning and practicing software packaging concepts across three ecosystems: Node.js, Python, and Java.

## Overview

The project focuses on the DevOps packaging lifecycle:
- bundling application code and dependencies into portable artifacts
- managing versions with semantic versioning
- separating environment-specific configuration from core application code
- validating builds and security posture before deployment

## Project Goals

- Understand how packaging improves consistency across development, staging, and production.
- Practice dependency management with ecosystem-specific manifests.
- Apply semantic versioning using the MAJOR.MINOR.PATCH model.
- Explore build automation and artifact creation for Node.js, Django, and Spring Boot.
- Review dependencies for basic security hygiene.

## Suggested Learning Tasks

1. Review the dependency manifests in each ecosystem folder.
2. Install dependencies and build the artifacts locally.
3. Update the version numbers in the manifests.
4. Apply environment-specific configuration through the config examples.
5. Run the sample applications to confirm packaging basics.
6. Audit the dependency lists for outdated or vulnerable packages.

## Project Structure

- [README.md](README.md) — overview and usage guide
- [package.json](package.json) — Node packaging manifest
- [node-app/](node-app/) — simple Node.js application example
- [python-django-app/](python-django-app/) — Python packaging scaffold
- [java-springboot-app/](java-springboot-app/) — Spring Boot packaging scaffold
- [config/](config/) — environment-specific configuration samples
- [.github/workflows/ci.yml](.github/workflows/ci.yml) — basic CI pipeline example

## Quick Start

### Node.js
```bash
npm install
npm run build
npm start
```

### Python
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
pip install -r python-django-app/requirements.txt
python python-django-app/manage.py
```

### Java
```bash
mvn -f java-springboot-app/pom.xml package
java -jar java-springboot-app/target/packaging-demo-1.0.0.jar
```

## Versioning

The starter manifests use version 1.0.0 and can be updated as you practice semantic versioning.

## Security Notes

- Audit dependencies regularly.
- Prefer lockfiles and pinned versions when possible.
- Keep build and runtime images minimal and updated.
