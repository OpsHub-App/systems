# Jira Data Center to Jira Cloud Migration

> Migrate from Jira Data Center to Jira Cloud with zero downtime, including add-on data, using OpsHub Migration Manager.

[← Back to All Migrations](./) · [← Home](../)

---

## Overview

Moving from Jira Data Center to Jira Cloud is one of the most common — and most complex — migrations in the Atlassian ecosystem. Atlassian's own Cloud Migration Assistant handles basic data, but organizations with complex configurations, large data volumes, and critical add-on data need more control, more safety, and zero downtime.

OpsHub Migration Manager migrates your complete Jira Data Center environment to Jira Cloud — including add-on data, custom configurations, and full history — while your teams continue working without interruption.

## Why Use OpsHub Instead of Atlassian's Migration Assistant?

| Atlassian Cloud Migration Assistant | OpsHub Migration Manager |
|---|---|
| Downtime required during migration | **Zero downtime** — teams keep working throughout |
| Limited add-on data migration support | **Add-on data included** — Zephyr, Xray, Tempo, and more |
| All-or-nothing migration approach | **Selective migration** — choose projects, issue types, fields |
| No delta sync for changes during migration | **Delta sync** captures every change made during migration |
| Limited rollback options | **Reverse sync** for full rollback capability |
| Basic progress visibility | **Real-time dashboard** with detailed progress tracking |

## What Gets Migrated

**Jira Core Data:**
- All issue types (standard and custom) with full field data
- Complete revision history with original timestamps
- Comments, worklogs, and internal notes
- Attachments, inline images, and embedded files
- Custom fields with type preservation

**Project Configuration:**
- Workflows, workflow schemes, and transitions
- Screens, screen schemes, and field configurations
- Permission schemes and notification schemes
- Issue type schemes and priorities

**Add-On Data:**
- Zephyr test management data
- Xray test data
- Tempo timesheets and worklogs
- Other Marketplace add-on data (varies by add-on)

**Relationships & Structure:**
- Issue links (all link types)
- Epic-story hierarchies
- Sprint history and board configurations
- Filters and dashboards

**Users & Permissions:**
- User identity mapping (DC accounts → Atlassian accounts)
- Group memberships
- Project roles and permissions

## How It Works

### Phase 1 — Discovery
OMM scans your Data Center instance — project count, issue volume, add-on inventory, custom field complexity. Produces a detailed migration plan.

### Phase 2 — Configuration
Map configurations between DC and Cloud. Handle differences in workflow capabilities, permissions models, and add-on compatibility.

### Phase 3 — Pilot
Migrate a representative project to Cloud. Validate data accuracy, add-on data integrity, and configuration mapping.

### Phase 4 — Production
Full migration with teams still working in Data Center. Delta sync captures ongoing changes. Multiple projects migrate in parallel.

### Phase 5 — Cutover
Reconciliation report. Final delta sync. Teams switch to Cloud with complete data confidence.

---

## Get Started

| Action | Link |
|---|---|
| **Install from Atlassian Marketplace** | [OMM for Jira DC → Cloud →](https://marketplace.atlassian.com/apps/1235636/omm-for-jira-dc-to-cloud-migration-with-zero-downtime) |
| **Request a Demo** | [See DC → Cloud migration in action →](https://www.opshub.com/request-a-demo/) |
| **Free Consultation** | [Talk to a migration engineer →](https://www.opshub.com/book-a-free-migration-consultation/) |
| **Start Free Trial** | [30-day trial →](https://www.opshub.com/request-a-free-trial/) |

---

[← Back to All Migrations](./) · [← Home](../)
