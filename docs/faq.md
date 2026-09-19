# Frequently Asked Questions

> Common questions about OpsHub Integration Manager (OIM) and OpsHub Migration Manager (OMM).

[← Back to Docs](./) · [← Home](../)

---

## General

**What is OpsHub?**
OpsHub provides enterprise integration and migration solutions for ALM, DevOps, ITSM, and PLM systems. Two core products: OpsHub Integration Manager (OIM) for real-time bi-directional synchronization, and OpsHub Migration Manager (OMM) for zero-downtime data migrations.

**How many tools does OpsHub support?**
OpsHub supports 60+ enterprise tools, including Jira, Azure DevOps, ServiceNow, IBM DOORS, Salesforce, Rally, BMC Remedy, HubSpot, OpenText ALM, Tricentis Tosca, and many more.

**Is OpsHub available on Atlassian Marketplace?**
Yes. OpsHub has 20+ apps on the [Atlassian Marketplace](https://marketplace.atlassian.com/vendors/798149/opshub-inc) covering integrations and migrations.

---

## Integration (OIM)

**Is the sync bi-directional?**
Yes. OIM syncs data in both directions in real time. Changes in either system reflect in the other automatically.

**What data gets synced?**
Core entities (issues, bugs, incidents, requirements), comments with author attribution, attachments, custom fields, statuses, workflows, and relationships. The exact data depends on the specific integration.

**Does it require coding?**
No. OIM uses a no-code, drag-and-drop interface with AI-assisted configuration. No scripts, plugins, or middleware required.

**Will it slow down my Jira instance?**
No. OIM is designed for zero performance impact on connected systems.

**Can I choose which projects and fields to sync?**
Yes. Selective sync lets you choose exactly which projects, issue types, fields, and direction to synchronize.

**Is there a free version?**
Yes. The [OIM Community Edition](https://marketplace.atlassian.com/apps/1215532/opshub-integration-manager-oim-community-edition) is available for free on Atlassian Marketplace.

---

## Migration (OMM)

**Do teams have to stop working during migration?**
No. OMM's Live++ technology keeps both source and target systems running in parallel. Teams continue working in the source system throughout the migration.

**What happens to changes made during the migration?**
OMM's delta sync captures all changes made in the source system during migration. A final delta sync before cutover ensures nothing is missed.

**Can I roll back if something goes wrong?**
Yes. Reverse sync can transfer data back to the source system if needed for compliance or rollback.

**What if the migration fails partway through?**
OMM's failure recovery allows restarting from any failure point without starting over from scratch.

**How long does a migration take?**
It depends on data volume and complexity. OMM's Data Discovery Utility estimates timelines upfront. Multiple projects can migrate in parallel to reduce total time.

**Does OMM migrate test data?**
Yes. Test Plans, Test Suites, Test Cases with steps, Test Results, and Test Runs all migrate — including Zephyr and Xray data.

---

## Security & Deployment

**Where does my data go?**
Your data stays under your control. OpsHub supports on-premise, cloud, and hybrid deployment models.

**Is OpsHub SOC 2 compliant?**
Contact [OpsHub](https://www.opshub.com/contact-us/) for details on security certifications and compliance.

**Who uses OpsHub?**
Enterprise organizations including ABB, Airbus, AMD, American Express, Bosch, Deloitte, Lockheed Martin, Panasonic Avionics, and Roche.

---

## Get More Answers

| Resource | Link |
|---|---|
| **Request a Demo** | [opshub.com/request-a-demo](https://www.opshub.com/request-a-demo/) |
| **Talk to an Expert** | [opshub.com/contact-us](https://www.opshub.com/contact-us/) |
| **Technical Documentation** | [docs.opshub.com](https://docs.opshub.com) |
| **Atlassian Marketplace** | [All OpsHub Apps](https://marketplace.atlassian.com/vendors/798149/opshub-inc) |

---

[← Back to Docs](./) · [← Home](../)
