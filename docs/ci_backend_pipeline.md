# CI Pipeline Backend

**Summary**: Minimalistische GitHub Actions Workflow-Konfiguration zur automatisierten Ausführung der Pytest-Testsuite.

**Sources**: [[.github/workflows/backend-ci.yml]]

**Last updated**: 2026-07-25

---

Der Workflow `ci_backend_pipeline` führt bei Pull Requests und Pushes auf den `main`-Branch sowie manuell via `workflow_dispatch` Backend-Tests in GitHub Actions aus.

## Triggers & Schritte

- **Triggers**: `push` (main), `pull_request` (main), `workflow_dispatch`.
- **Python Setup**: Verwendet `actions/setup-python@v5` mit Python 3.11.
- **Test-Ausführung**: Führt `pytest` im Arbeitsverzeichnis `backend` aus.

## Related pages
- [[test_infrastructure_backend]]
- [[backend_main]]
