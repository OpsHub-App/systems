# Getting Started with OpsHub

> Your step-by-step guide to integrating with OpsHub on the Atlassian Marketplace

## Available Integrations

OpsHub provides integration and migration solutions for Jira. OpsHub Integration Manager (OIM) provides bidirectional, real-time synchronization, and OpsHub Migration Manager (OMM) handles one-time data migrations. The following integration connectors are available on the Atlassian Marketplace:

- **[ServiceNow Integration for Jira](../integrations/servicenow-jira.md)** — [View on Marketplace](https://marketplace.atlassian.com/apps/1236368)
- **[Zendesk Integration for Jira](../integrations/zendesk-jira.md)** — [View on Marketplace](https://marketplace.atlassian.com/apps/1234611)
- **[GitHub Integration for Jira](../integrations/github-jira.md)** — [View on Marketplace](https://marketplace.atlassian.com/apps/1234617)

## Quick Setup Guide

**Step 1: Install from the Marketplace**

1. Go to the [OpsHub vendor page on Atlassian Marketplace](https://marketplace.atlassian.com/vendors/798149)
2. Find the connector for your specific tools (e.g., ServiceNow + Jira, Zendesk + Jira, GitHub + Jira)
3. Click **Try it free** or **Buy now**
4. Follow the Atlassian installation prompts

**Step 2: Configure your connection**

1. Provide API credentials for both systems. Standard service account permissions are sufficient.
2. Use the no-code interface to map fields, workflows, and entities between systems.
3. Reusable field mappings make configuration fast.

**Step 3: Start syncing**

1. Enable real-time bidirectional synchronization
2. OpsHub handles field-level conflict management, automatic retry on failures, and sync activity logging
3. Monitor sync status from the OpsHub dashboard

## How It Works

OpsHub operates as an external integration engine — it connects to your tools through their native APIs and synchronizes data without requiring plugins installed inside either system. This means:

- **Zero performance impact** on Jira or your connected tool
- **No admin access required** — standard API credentials are sufficient
- **Field-level conflict management** handles data conflicts automatically
- **Automatic retry** on transient failures like API rate limits or connectivity drops

## Need Help?

- **[OpsHub Website](https://www.opshub.com)** — Product details and resources
- **[Contact Sales](https://www.opshub.com/contact-us/)** — Custom requirements and enterprise pricing
- **[Atlassian Marketplace — OpsHub, Inc.](https://marketplace.atlassian.com/vendors/798149)** — Browse all OpsHub listings

*OpsHub, Inc. — Enterprise Integration and Migration for Jira*
