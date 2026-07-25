# CI Pipeline Frontend

**Summary**: Minimalistische GitHub Actions Workflow-Konfiguration zur automatisierten Ausführung der Vitest-Testsuite.

**Sources**: [[.github/workflows/frontend-ci.yml]]

**Last updated**: 2026-07-25

---

Der Workflow `ci_frontend_pipeline` führt bei Pull Requests und Pushes auf den `main`-Branch sowie manuell via `workflow_dispatch` Frontend-Tests in GitHub Actions aus.

## Triggers & Schritte

- **Triggers**: `push` (main), `pull_request` (main), `workflow_dispatch`.
- **Node Setup**: Verwendet `actions/setup-node@v4` mit Node.js 20.
- **Test-Ausführung**: Führt `npm test` (`vitest run`) im Arbeitsverzeichnis `frontend` aus.

## Related pages
- [[test_infrastructure_frontend]]
- [[frontend_main]]
