# etlcli
*A notebook-native ETL runner with strict parameter control and Papermill-powered reproducibility.*

---

## Overview

`etlcli` is a configuration-driven ETL orchestrator that treats notebooks as first-class execution units.  
Pipelines are authored and parameterized in notebooks, while execution happens via a safe CLI interface.  
The executor cannot alter runtime parameters — ensuring reproducibility, traceability, and author control.

This project is designed with a hybrid purpose:  
it is currently portfolio-oriented, but structured to evolve into a full open-source ETL framework (V2).

---

## Key Design Principles

| Principle | Description |
|----------|-------------|
| **Notebooks-first** | Pipelines are authored as `.ipynb` files — ideal for experimentation and auditability. |
| **Config-driven** | Bundles and pipelines are defined in `config.json`, not in code. |
| **Strict parameter control** | Authors control parameters from inside notebooks, not from CLI. |
| **Reproducible runs** | Every execution creates a log notebook via Papermill. |
| **Future extensibility** | V2 introduces a GUI Workbench + metadata DB for observability. |

---

## Architecture (Mermaid)

```mermaid
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
    DASH[Terminal / Workbench (planned)]
    README_DOCS[docs/ examples]
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