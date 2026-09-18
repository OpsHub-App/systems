---
layout: default
title: Migrate Jira Data Center to Jira Cloud | OpsHub Migration Manager
description: Zero-disruption migration from Jira Data Center to Jira Cloud. Preserve full history, relationships, and custom fields. No downtime required.
---

# Migrate to Jira Cloud from Jira Data Center

With Jira Data Center approaching end-of-life (March 2029), teams are moving to Jira Cloud. OpsHub Migration Manager handles the migration without downtime and without losing data.

---

## Why This Migration Matters

Atlassian has announced end-of-support for Jira Data Center. Teams that rely on Data Center need a migration path to Jira Cloud that does not require a system freeze, does not lose historical data, and does not break the relationships between issues that teams depend on for traceability.

---

## What Migrates

| Data Type | Preserved |
|-----------|-----------|
| Issues (all types) | Yes, including custom issue types |
| Comments | Yes, with original author and timestamp |
| Attachments | Yes, all files |
| Custom fields | Yes, with value mapping for custom field types |
| Workflows and statuses | Yes, mapped to Cloud workflow equivalents |
| Links and relationships | Yes, parent-child, epic links, issue links |
| Sprint history | Yes |
| Labels and components | Yes |
| Watchers and voters | Yes |

---

## How It Works

1. **Assess.** OpsHub analyzes your Data Center instance: project count, issue volume, custom fields, add-ons, and workflow configurations
2. **Map.** Configure field mappings, value mappings, and workflow transitions between DC and Cloud schemas
3. **Pilot.** Run a test migration on one project to validate completeness
4. **Migrate.** Full migration runs while teams continue working. No freeze window
5. **Reconcile.** Any records created or modified during migration are captured and synced
6. **Validate.** Post-migration reports confirm record counts, field completeness, and relationship integrity

---

**Planning your DC-to-Cloud move?** [Book a slot.](https://www.opshub.com/contact-us/)

---

*Back to [OMM Overview](../)*
