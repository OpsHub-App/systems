# Frequently Asked Questions

> Common questions about OpsHub integration solutions for Jira

## General Questions

**What is OpsHub?**

OpsHub provides enterprise-grade integration solutions for Jira. OpsHub Integration Manager (OIM) enables ongoing bidirectional synchronization between Jira and tools like ServiceNow, Zendesk, and GitHub.

**How does OpsHub work?**

OpsHub operates as an external integration engine that connects to your tools via their native APIs. It synchronizes data bidirectionally without requiring plugins inside your systems, so there is no performance impact on Jira or your connected tools.

## Integration Questions

**Is the sync real-time?**

Yes. OpsHub synchronizes changes in near real-time. You can also configure scheduled sync intervals if preferred.

**Can I sync custom fields?**

Yes. OpsHub supports mapping custom fields between systems, including complex field types, picklists, multi-select fields, and calculated fields. The no-code interface helps you set up field mappings without manual configuration.

**What happens if there is a conflict?**

OpsHub includes field-level conflict management. You can configure conflict rules for different field types. Built-in automatic retry handles transient failures like API rate limits or connectivity drops.

**What data gets synced?**

OpsHub syncs a wide range of data depending on the connector:

- **ServiceNow + Jira** - Tables, tasks, incidents, problems, change records, requests, tests, steps, sprints, assignment groups, comments, attachments, links, mentions, rich text, and history
- **Zendesk + Jira** - Tickets, issues, comments, attachments, priorities, statuses, custom fields, user info, related entities, entity mentions, user mentions, and issue and project movements
- **GitHub + Jira** - Epics, issues, pull requests, commits, branches, comments, status updates, and development activity

## Technical Questions

**Does OpsHub require admin access?**

OpsHub needs standard API-level access to your tools. Full admin access is not typically required - service account credentials with appropriate permissions are sufficient.

**What Jira deployment does it support?**

The ServiceNow, Zendesk, and GitHub integrations for Jira are available on Jira Cloud.

**Is my data secure?**

Yes. OpsHub uses encrypted connections and complies with enterprise security requirements. Data is processed but not stored by OpsHub.

**What about rate limits?**

OpsHub handles API rate limits automatically with built-in retry logic. Your sync continues without interruption even when rate limits are encountered.

**Is technical coding required to set up the integration?**

No. OpsHub provides a no-code configuration interface using native APIs. Teams can set up and manage integrations without custom scripting, middleware, or API development work.

## Pricing

**How is OIM priced?**

OIM pricing is based on the number of connectors and users. Visit the [Atlassian Marketplace listing](https://marketplace.atlassian.com/vendors/798149) for current pricing or [contact OpsHub sales](https://www.opshub.com/contact-us/) for enterprise quotes.

**Can I try before I buy?**

Yes. OpsHub products offer a free trial through the Atlassian Marketplace. Click **Try it free** on any OpsHub listing to get started.

## Learn More

- **[Getting Started Guide](getting-started.md)** - Step-by-step setup instructions
- **[Why OpsHub](why-opshub.md)** - Differentiators
- **[OpsHub Website](https://www.opshub.com)** - Full documentation and resources
- **[Atlassian Marketplace - OpsHub, Inc.](https://marketplace.atlassian.com/vendors/798149)** - All OpsHub listings
- **[Contact Sales](https://www.opshub.com/contact-us/)** - Custom requirements and enterprise pricing

*OpsHub, Inc. - Enterprise Integration and Migration for Jira*
