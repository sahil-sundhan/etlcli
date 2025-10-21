# etlcli

flowchart TD
  subgraph Author
    A[Pipeline Author]
    CFG[config.json]
    NB[Notebooks (pipelines)]
  end

  subgraph Executor
    CLI[etlcli.py / __main__.py]
  end

  subgraph Runtime
    PM[Papermill Executor]
    LOG_NB[Run Output Notebooks (per-run)]
    DB_META[(Logging DB - metadata)]
  end

  subgraph Observability
    DASH[Terminal / GUI (planned)]
    README_DOCS[docs/ README / screenshots]
  end

  A --> NB
  A --> CFG
  CLI --> CFG
  CLI --> PM
  PM --> LOG_NB
  PM --> DB_META
  LOG_NB --> README_DOCS
  DB_META --> DASH
  CLI --> DASH


# ETLCLI — Config-driven Notebook ETL Orchestrator

**Tagline:** Notebooks as first-class ETL artifacts. Config-driven execution. Safe, reproducible runs.

## Summary
ETLCLI allows pipeline authors to define bundles and pipelines in `config.json`. Executors trigger runs via CLI; notebooks contain parameters and produce run-output notebooks (logs) captured via Papermill.

## Quickstart

```bash
# Run a pipeline (executor)
python -b <bundle_name> -n <pipeline_name>

# Module entry (alternative)
python -m etlcli -b <bundle_name> -n <pipeline_name>

