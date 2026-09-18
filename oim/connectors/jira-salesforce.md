---
layout: default
title: Jira - Salesforce Integration | OpsHub Integration Manager
description: Bidirectional integration between Jira and Salesforce. Sync cases, issues, comments, and status updates automatically. No coding required.
---

# Jira - Salesforce Integration

Connect your sales and support teams in Salesforce with your engineering team in Jira. Customer-reported issues flow automatically into development backlogs, and resolution updates flow back to the customer-facing teams in real time.

---

## The Problem This Solves

A customer reports a bug through your support team in Salesforce. Today, someone manually creates a Jira ticket, copies the details, and then checks back periodically to relay updates. The customer waits. The support agent follows up manually. The developer has no context on who reported it or how urgent it is from the customer's perspective.

OIM automates this entire loop.

---

## What Syncs

| Data Type | Sync Direction | Details |
|-----------|---------------|---------|
| Cases / Issues | Bidirectional | Salesforce Cases become Jira issues and vice versa |
| Comments | Bidirectional | Case comments and Jira comments stay aligned |
| Attachments | Bidirectional | Files, screenshots, error logs |
| Status | Bidirectional | Salesforce case status maps to Jira workflow transitions |
| Priority | Bidirectional | Configurable value mapping |
| Custom fields | Bidirectional | Any Salesforce field to any Jira field |
| Account / Contact info | Jira-bound | Customer context flows into Jira for developer visibility |

---

## Key Capabilities

- **No-code setup.** Visual field mapping between Salesforce objects and Jira issue types
- **Multi-project routing.** Different Salesforce record types route to different Jira projects
- **Conflict resolution.** Reconciliation engine handles simultaneous updates on both sides
- **External architecture.** No Salesforce packages to install. Connects via Salesforce REST API
- **Historical backfill.** Bring existing Salesforce cases into alignment with Jira issues

---

## How OIM Compares

| | OpsHub OIM | Unito | Native Salesforce-Jira | Exalate |
|--|-----------|-------|----------------------|---------|
| Sync direction | Bidirectional with reconciliation | Bidirectional (webhook) | Limited bidirectional | Bidirectional (scripted) |
| Configuration | No-code | Limited mapping | Salesforce admin | Groovy scripting |
| Custom fields | Full | Tier-locked | Limited | Script-dependent |
| On-premise | Available | No | No | No |

---

**Want to see this integration?** [Book a slot.](https://www.opshub.com/contact-us/)

---

*See also: [OIM Overview](../) | [Jira - ServiceNow Integration](jira-servicenow) | [Jira - Azure DevOps Integration](jira-azure-devops)*
