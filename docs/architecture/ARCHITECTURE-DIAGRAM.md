```mermaid
flowchart LR
    A[Flight CSV] --> B[Ingestion]
    B --> C[Services]
    C --> D[Optimization Core]
    D --> E[Workflow]
    E --> F[MCP Publisher]
    E --> G[Audit Report]
    F --> H[AWS / OCC]
    G --> I[S3 / Storage]
