# MBSE Tools ↔ Jira Integration

> Bi-directional synchronization between Model-Based Systems Engineering (MBSE) tools and Jira using OpsHub Integration Manager (OIM).

[← Back to All Integrations](./) · [← Home](../)

---

## Overview

Model-Based Systems Engineering (MBSE) tools like IBM Rhapsody, Capella, and Cameo Systems Modeler are used to design complex systems in aerospace, defense, automotive, and industrial sectors. When systems engineers model in MBSE tools and software teams build in Jira, connecting model elements to development work items is essential for traceability.

OpsHub Integration Manager connects MBSE tools and Jira using a **custom-developed connector** — syncing model elements, blocks, and relationships to Jira automatically without plugins or manual intervention.

## Why Integrate MBSE Tools with Jira?

| Challenge Without Integration | With OpsHub Integration |
|---|---|
| Model elements are manually transcribed to Jira tickets | Model elements auto-sync as Jira work items |
| Engineering context is lost in the handoff | Full model context and relationships preserved |
| Traceability from model to code is manual | End-to-end traceability maintained automatically |
| Changes in the model require manual Jira updates | Changes batch-sync in real time |
| Version history is fragmented across tools | Clean, audit-ready model history |

## What Gets Synced

**Core Entities:**
- MBSE model elements and blocks ↔ Jira issues, stories, tasks
- Structural connections and dependencies between model components
- Project information and issue data

**Rich Data:**
- Attachments and link relationships
- Complete model context and relationships
- Custom fields and field mappings

**Relationships:**
- Model element dependencies
- Cross-system traceability links
- Structural relationships between components

## Supported MBSE Tools

| Tool | Description |
|---|---|
| **IBM Rhapsody** | UML/SysML modeling for systems and software |
| **Capella** | Open-source MBSE tool for system architecture |
| **Cameo Systems Modeler** | SysML-based modeling for complex systems |

## Use Cases

**Digital Thread for Defense**
A defense contractor uses Cameo for system modeling. Model elements sync to Jira where software teams implement them. The complete chain — from model to code to test — is traceable for program audits.

**Automotive Systems Development**
An automotive OEM designs systems architecture in Capella. Architectural elements auto-sync to Jira for Agile development teams, maintaining the connection between system design and software implementation.

**Aerospace Traceability**
Systems engineers define architecture in IBM Rhapsody. OpsHub syncs model elements to Jira, preserving dependencies and relationships so that changes in either system stay aligned.

---

## Get Started

| Action | Link |
|---|---|
| **Install from Atlassian Marketplace** | [MBSE ↔ Jira Integration →](https://marketplace.atlassian.com/apps/3248021866/bidirectional-mbse-integration-for-jira) |
| **Try Free** | [OIM Community Edition →](https://marketplace.atlassian.com/apps/1215532/opshub-integration-manager-oim-community-edition) |
| **Request a Demo** | [See it in action with your data →](https://www.opshub.com/request-a-demo/) |
| **Documentation** | [docs.opshub.com](https://docs.opshub.com) |

---

[← Back to All Integrations](./) · [← Home](../)
