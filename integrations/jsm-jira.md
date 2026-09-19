# Jira Service Management (JSM) ↔ Jira Software Integration

> Bi-directional, real-time synchronization between Jira Service Management and Jira Software using OpsHub Integration Manager (OIM).

[← Back to All Integrations](./) · [← Home](../)

---

## Overview

When service teams work in Jira Service Management (JSM) and development teams work in Jira Software, keeping both sides in sync is critical. Escalated incidents need to reach developers fast. Bug fixes need to flow back to service agents. Without integration, teams waste time on manual updates, duplicate entries, and stale information.

OpsHub Integration Manager bridges JSM and Jira Software with **real-time, bi-directional synchronization** — so every escalation, status change, comment, and resolution flows automatically between service and development teams.

## Why Integrate JSM with Jira Software?

| Challenge Without Integration | With OpsHub Integration |
|---|---|
| Service agents manually copy incidents to dev backlog | Incidents auto-sync to Jira Software as issues |
| Developers don't see customer impact or SLA urgency | Full context — priority, SLA, customer details — syncs with every issue |
| Status updates require switching between tools | Status changes flow bi-directionally in real time |
| Duplicate data entry across systems | Single source of truth, data entered once |
| Resolution updates delayed to service desk | Bug fixes and releases reflect instantly in JSM |

## What Gets Synced

**Core Entities:**
- Incidents, service requests, and change requests (JSM) ↔ Issues, bugs, stories, tasks (Jira Software)
- Priorities, statuses, and workflow transitions
- Assignees and reporter details

**Rich Data:**
- Comments and internal notes (with original author and timestamps)
- Attachments and inline images
- Custom fields and field mappings
- Labels and components

**Relationships:**
- Parent/child links
- Related issue references
- Cross-project dependencies

## How It Works

### 1. Connect
Pre-built connectors link JSM and Jira Software instances. No global admin access required. Supports cloud, Data Center, and hybrid environments.

### 2. Configure
Map fields, statuses, and workflows between the two systems using OIM's no-code interface. Define sync rules — what gets synced, in which direction, and under what conditions.

### 3. Sync
Once activated, OIM synchronizes data bi-directionally in real time. Changes in either system reflect in the other automatically. Historical data can also be synced for a complete baseline.

### 4. Monitor
Built-in dashboards show sync status, throughput, and any errors. Teams have full visibility into data flow without checking logs manually.

## Use Cases

**Incident Escalation**
A service agent in JSM receives a critical incident. It auto-syncs to the development team's Jira Software backlog as a high-priority bug. Developers fix it, update the status, and the resolution flows back to JSM — the agent sees it without switching tools.

**Change Management**
Change requests created in JSM sync to Jira Software as tasks for the engineering team. Approval workflows, implementation status, and completion updates flow back to JSM for full audit trail.

**Cross-Team Visibility**
Product managers see both service trends (from JSM) and development progress (from Jira Software) in a unified view, enabling data-driven prioritization.

---

## Get Started

| Action | Link |
|---|---|
| **Install from Atlassian Marketplace** | [JSM ↔ Jira Integration →](https://marketplace.atlassian.com/apps/1624606962/oim-for-bidirectional-jsm-and-jira-integration) |
| **Try Free** | [OIM Community Edition →](https://marketplace.atlassian.com/apps/1215532/opshub-integration-manager-oim-community-edition) |
| **Request a Demo** | [See it in action with your data →](https://www.opshub.com/request-a-demo/) |
| **Documentation** | [docs.opshub.com](https://docs.opshub.com) |

---

[← Back to All Integrations](./) · [← Home](../)
