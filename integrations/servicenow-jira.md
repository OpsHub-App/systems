# ServiceNow ↔ Jira Integration

> Bi-directional, real-time synchronization between ServiceNow and Jira using OpsHub Integration Manager (OIM).

[← Back to All Integrations](./) · [← Home](../)

---

## Overview

IT service teams work in ServiceNow. Development teams work in Jira. When an incident requires a code fix or a feature request comes through the service desk, the handoff between these two systems is where things break down — manual ticket creation, lost context, delayed updates.

OpsHub Integration Manager eliminates this gap with **real-time, bi-directional synchronization** between ServiceNow and Jira. Incidents become bugs. Change requests become tasks. Status updates flow back. Automatically.

## Why Integrate ServiceNow with Jira?

| Challenge Without Integration | With OpsHub Integration |
|---|---|
| Service agents manually create Jira tickets for dev teams | Incidents auto-sync to Jira as bugs or tasks |
| Developers don't see SLA timelines or customer impact | Full context — priority, SLA, affected CIs — syncs with every issue |
| Resolution updates delayed back to service desk | Bug fixes reflect instantly in ServiceNow |
| Duplicate data entry across both systems | Data entered once, synced everywhere |
| No audit trail across systems | Complete sync history for compliance |

## What Gets Synced

**Core Entities:**
- Incidents, problems, change requests (ServiceNow) ↔ Issues, bugs, stories, tasks (Jira)
- Priorities, statuses, and workflow transitions
- Assignment groups and individual assignees

**Rich Data:**
- Comments and work notes (with original author and timestamps)
- Attachments and inline images
- Custom fields and field mappings
- SLA data and priority classifications
- Configuration item references

**Relationships:**
- Parent/child task links
- Related incident references
- Change-to-incident associations

## How It Works

### 1. Connect
Pre-built connectors link ServiceNow and Jira instances. No global admin access required. Supports ServiceNow (all versions), Jira Cloud, and Jira Data Center.

### 2. Configure
Map fields, statuses, and workflows using OIM's no-code interface. Define sync rules — what gets synced, in which direction, and under what conditions.

### 3. Sync
Once activated, OIM synchronizes data bi-directionally in real time. Changes in either system reflect in the other automatically.

### 4. Monitor
Built-in dashboards show sync status, throughput, and any errors.

## Use Cases

**Incident-to-Bug Escalation**
A P1 incident in ServiceNow automatically creates a high-priority bug in Jira. The dev team fixes it, updates the status, and the resolution flows back to ServiceNow — the service agent sees it without switching tools.

**Change Management**
Change requests in ServiceNow sync to Jira for implementation tracking. Approval workflows, implementation status, and completion updates flow back for a full audit trail.

**Cross-Team Reporting**
Management sees both service trends (from ServiceNow) and development progress (from Jira) without manual data consolidation.

---

## Get Started

| Action | Link |
|---|---|
| **Install from Atlassian Marketplace** | [ServiceNow ↔ Jira Integration →](https://marketplace.atlassian.com/apps/1236368/servicenow-integration-for-jira-bidirectional-sync) |
| **Try Free** | [OIM Community Edition →](https://marketplace.atlassian.com/apps/1215532/opshub-integration-manager-oim-community-edition) |
| **Request a Demo** | [See it in action with your data →](https://www.opshub.com/request-a-demo/) |
| **Documentation** | [docs.opshub.com](https://docs.opshub.com) |

---

[← Back to All Integrations](./) · [← Home](../)
