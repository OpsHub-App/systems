# Jira ↔ Jira Two-Way Sync (Internal & External)

> Bi-directional synchronization between multiple Jira instances — internal or external — using OpsHub Integration Manager (OIM).

[← Back to All Integrations](./) · [← Home](../)

---

## Overview

Large enterprises often run multiple Jira instances — separate instances for different business units, partner organizations, or internal vs. external teams. Keeping issues, comments, and attachments in sync across Jira instances without granting direct access is a common challenge.

OpsHub Integration Manager provides **plugin-free, bi-directional Jira-to-Jira synchronization** — connecting internal and external Jira instances through a centralized layer that operates outside both systems using secure APIs.

## Why Sync Jira to Jira?

| Challenge Without Sync | With OpsHub Sync |
|---|---|
| External partners can't access your internal Jira | Selective sync shares only what you choose |
| Internal teams manually copy issues between instances | Issues auto-sync with full context |
| Sensitive data may leak when sharing Jira access | Field-level control with encryption in transit and at rest |
| No unified view across multiple Jira instances | Bi-directional sync creates a connected view |
| Firewall rules complicate cross-instance access | No firewall access required — works via secure APIs |

## What Gets Synced

**Core Entities:**
- Issues, bugs, stories, tasks, and epics across Jira instances
- Comments with original author and timestamps
- Attachments, links, and inline content
- Test data and custom issue types

**Rich Data:**
- All standard and custom fields
- Workflow transitions and statuses
- User mentions and embedded images
- Custom fields and field mappings

**Security Features:**
- Field-level control over what gets shared
- Sensitive data protection with encryption
- No direct system access required
- Role-based access controls

## Use Cases

**Vendor Collaboration**
An enterprise works with an external vendor on a software project. Both sides use Jira. OpsHub syncs relevant issues between the two instances — each team sees only what they need, without granting direct access to the other's Jira.

**Business Unit Consolidation**
A company has separate Jira instances for different divisions. OpsHub syncs shared projects across instances so cross-divisional work stays aligned without merging instances.

**Regulated Data Sharing**
A defense contractor needs to share project data with a government agency's Jira. OpsHub's field-level controls ensure only approved data syncs — with encryption and audit logging for compliance.

---

## Deployment Options

| Option | Description |
|---|---|
| **On-Premises** | Run OpsHub within your own infrastructure |
| **Customer Cloud** | Deploy in your own cloud environment |
| **OpsHub Secure Cloud** | Hosted by OpsHub with enterprise security |

---

## Get Started

| Action | Link |
|---|---|
| **Install from Atlassian Marketplace** | [Jira ↔ Jira Sync →](https://marketplace.atlassian.com/apps/2019250150/two-way-internal-and-external-sync-for-jira) |
| **Try Free** | [OIM Community Edition →](https://marketplace.atlassian.com/apps/1215532/opshub-integration-manager-oim-community-edition) |
| **Request a Demo** | [See it in action with your data →](https://www.opshub.com/request-a-demo/) |
| **Documentation** | [docs.opshub.com](https://docs.opshub.com) |

---

[← Back to All Integrations](./) · [← Home](../)
