# Frequently Asked Questions

> Common questions about OpsHub integration and migration solutions

### General Questions

**What is OpsHub?**

OpsHub provides enterprise-grade integration and migration solutions for Jira and 70+ other tools. The company offers two main products: **OpsHub Integration Manager (OIM)** for ongoing bidirectional synchronization and **OpsHub Migration Manager (OMM)** for zero-downtime data migrations.

**How does OpsHub work?**

OpsHub operates as an external integration engine that connects to your tools via their APIs. It synchronizes data bidirectionally without requiring plugins inside your systems, so there is no performance impact on Jira or your connected tools.

**What tools does OpsHub support?**

OpsHub connects with 70+ tools including Azure DevOps, ServiceNow, Salesforce, GitHub, GitLab, IBM DOORS, Rally, PTC Windchill, Tricentis Tosca, and many more. See the [full list of supported systems](https://marketplace.atlassian.com/vendors/798149).

### Integration Questions

**What is the difference between OIM and OMM?**

- **OIM (Integration Manager)** keeps two or more tools synchronized on an ongoing basis. Data flows bidirectionally in real time.
- **OMM (Migration Manager)** moves data from one tool to another as a one-time migration. Teams can continue working in the source system during migration.

**Is the sync real-time?**

Yes. OIM synchronizes changes in near real-time (typically within seconds to minutes depending on configuration). You can also configure scheduled sync intervals if preferred.

**Can I sync custom fields?**

Yes. OpsHub supports mapping custom fields between systems, including complex field types, picklists, multi-select fields, and calculated fields. The AI-assisted mapper helps you set up field mappings without manual configuration.

**Does it support conditional sync?**

Yes. You can create rules that sync data only when certain conditions are met — for example, syncing only high-priority bugs, or syncing issues from specific projects.

**What happens if there is a conflict?**

OpsHub includes built-in conflict detection and resolution. You can configure conflict rules (e.g., source wins, target wins, or manual resolution) for different field types.

### Migration Questions

**Is there downtime during migration?**

No. OpsHub migrations run with zero downtime. Your teams continue working in the source system throughout the migration process.

**Can I migrate incrementally?**

Yes. OMM supports phased migration with delta syncs. You can migrate your data in stages and run incremental syncs to capture changes made after the initial migration until you are ready for the final cutover.

**What data gets preserved during migration?**

Everything — issues, comments, attachments, links, history, custom fields, workflows, and metadata. OpsHub validates data before, during, and after migration to ensure nothing is lost.

**Can I roll back a migration?**

Yes. OMM includes built-in validation and rollback capabilities so you can verify everything before making the switch permanent.

### Technical Questions

**Does OpsHub require admin access?**

OpsHub needs standard API-level access to your tools. Full admin access is not typically required — service account credentials with appropriate permissions are sufficient.

**Does it work with Jira Cloud, Data Center, and Server?**

Yes. OpsHub supports Jira Cloud, Jira Data Center, and Jira Server deployments.

**Is my data secure?**

Yes. OpsHub uses encrypted end-to-end connections, supports SSO and SAML, and complies with enterprise security requirements. Data is processed but not stored by OpsHub.

**What about rate limits?**

OpsHub handles API rate limits automatically with built-in retry logic and throttling. Your sync continues without interruption even when rate limits are encountered.

### Pricing and Licensing

**Is there a free version?**

Yes. The **[OIM Community Edition](https://marketplace.atlassian.com/apps/1215532)** is a free, no-code data integration tool for Jira that provides basic bidirectional sync capabilities.

**How is OIM priced?**

OIM pricing is based on the number of connectors and users. Visit the [Atlassian Marketplace listing](https://marketplace.atlassian.com/apps/1224525) for current pricing or [contact OpsHub sales](https://www.opshub.com/contact-us/) for enterprise quotes.

**Can I try before I buy?**

Yes. Most OpsHub products offer a free trial through the Atlassian Marketplace. Click **Try it free** on any OpsHub listing to get started.

### Learn More

- **[Getting Started Guide](getting-started.md)** — Step-by-step setup instructions
- **[Why OpsHub](why-opshub.md)** — Comparison and differentiators
- **[OpsHub Website](https://www.opshub.com)** — Full documentation and resources
- **[Atlassian Marketplace — OpsHub, Inc.](https://marketplace.atlassian.com/vendors/798149)** — All OpsHub listings
- **[Contact Sales](https://www.opshub.com/contact-us/)** — Custom requirements and enterprise pricing

*OpsHub, Inc. — Enterprise Integration and Migration for Jira*
