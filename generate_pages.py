#!/usr/bin/env python3
"""Generate OpsHub Marketplace GitHub pages — 3 integration listings."""

import os

# =============================================================================
# PRODUCT DATA — Only the 3 public listings
# =============================================================================

INTEGRATIONS = [
    {
        "slug": "servicenow-jira",
        "name": "ServiceNow Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1236368",
        "tool": "ServiceNow",
        "desc": "Rich and reliable bidirectional data sync between Jira and ServiceNow for tables, tasks, tests, steps, comments, attachments, links, and more.",
        "syncs": "Tables, tasks, incidents, problems, change records, requests, tests, steps, sprints, assignment groups, comments, attachments, links, mentions, rich text (HTML/Wiki), and history",
        "use_cases": [
            "Converting ServiceNow incidents and requests to Jira bugs, tasks, or stories",
            "Linking ServiceNow change records to Jira tasks",
            "Connecting Jira defects to ServiceNow customer impact records",
            "Syncing high-level Jira epics with ServiceNow records for portfolio visibility",
        ],
    },
    {
        "slug": "zendesk-jira",
        "name": "Zendesk Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1234611",
        "tool": "Zendesk",
        "desc": "Intelligent, data-rich two-way sync between Zendesk and Jira for any issue type. Zendesk tickets transform into Jira issues with complete context, clear ownership, and predictable engineering escalation.",
        "syncs": "Tickets, issues, comments, attachments, priorities, statuses, custom fields, user info, related entities, entity mentions, user mentions, and issue and project movements",
        "use_cases": [
            "Centralizing support and engineering workflows across Zendesk and Jira",
            "Syncing Zendesk tickets to Jira issues with complete context and ownership",
            "Maintaining consistent priorities and statuses across both platforms",
        ],
    },
    {
        "slug": "github-jira",
        "name": "GitHub Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1234617",
        "tool": "GitHub",
        "desc": "Enterprise-grade, bidirectional sync between GitHub and Jira. Sync epics, issues, pull requests, and commits in near real-time. Bridges GitHub markdown and Jira wiki markup for seamless data flow.",
        "syncs": "Epics, issues, pull requests, commits, branches, comments, status updates, and development activity",
        "use_cases": [
            "Controlled change traceability linking commits to Jira issues",
            "Release alignment through branch and PR updates in Jira",
            "Program visibility consolidating GitHub activity into Jira",
            "Enterprise synchronization without complex scripting",
        ],
    },
]

# Slugs of the 3 listings — used for Related Connectors cross-linking
ACTIVE_SLUGS = [p["slug"] for p in INTEGRATIONS]


# =============================================================================
# PAGE GENERATOR
# =============================================================================

def get_related_connectors(current_slug):
    """Return the other 2 integrations for internal linking."""
    related = []
    for p in INTEGRATIONS:
        if p["slug"] != current_slug:
            related.append({"name": p["name"], "path": f"{p['slug']}.md"})
    return related


def generate_integration_page(product):
    """Generate a markdown page for an integration product."""
    tool = product["tool"]
    uc_text = "\n".join([f"- {uc}" for uc in product["use_cases"]])
    related = get_related_connectors(product["slug"])
    related_lines = "\n".join([f"- [{r['name']}]({r['path']})" for r in related])

    content = f"""# {product['name']}

**Seamlessly connect {tool} and Jira with real-time, bidirectional sync.**

[![View Listing](https://img.shields.io/badge/View_Listing-0052CC?style=for-the-badge&logo=atlassian&logoColor=white)]({product['url']})

{product['desc']}

## Why Integrate {tool} with Jira?

| Benefit | Details |
|---------|---------|
| **Eliminate Manual Work** | Stop copying data between systems. Changes sync automatically in both directions, freeing your team to focus on what matters. |
| **Always Accurate** | Real-time synchronization ensures {tool} and Jira always show the same information. No stale data, no conflicts. |
| **No-Code Setup** | Configure your integration visually with a no-code interface using native APIs. No scripting or API knowledge needed. |
| **Enterprise Ready** | Built for scale with support for complex field mappings, custom workflows, field-level conflict management, and full audit logging. |

## What Gets Synced

{product['syncs']}

All data flows bidirectionally in real time. Custom field mappings, field-level conflict management, and automatic retry ensure your data stays consistent across both platforms.

## How It Works

OpsHub Integration Manager connects {tool} and Jira through their native APIs, operating as an external engine between both platforms. No plugins are installed inside your systems, so there is zero performance impact on either tool.

The integration process follows three steps:

1. **Connect** — Provide API credentials for {tool} and Jira. Standard service account permissions are sufficient.
2. **Map** — Use the no-code interface to map fields, workflows, and entities between systems. Reusable field mappings make configuration fast.
3. **Sync** — Enable real-time bidirectional synchronization. OpsHub handles field-level conflict management, automatic retry on failures, and sync activity logging.

## Common Use Cases

{uc_text}

## Supported Deployment

| Deployment | Supported |
|------------|-----------|
| Jira Cloud | ✓ |

OpsHub connects through external APIs and operates as an external engine between both platforms, with zero performance impact on either tool.

## Frequently Asked Questions

**Why do teams integrate {tool} with Jira?**

{tool} and Jira are often used by different teams within the same organization. Without integration, teams waste time on manual data entry, work with outdated information, and lose visibility across workflows. OpsHub keeps both systems synchronized automatically, so each team continues working in their preferred tool while staying aligned on priorities and progress.

**What happens if a sync fails due to an API or connectivity issue?**

OpsHub has built-in retry logic and error-handling mechanisms. Syncs automatically retry on transient failures such as API rate limits or connectivity drops. If issues persist, alerts are triggered and detailed logs are available for troubleshooting. Your data remains consistent throughout.

**Is technical coding required to set up the integration?**

No. OpsHub provides a no-code configuration interface using native APIs. Teams can set up and manage integrations without custom scripting, middleware, or API development work.

## Related Connectors

If you use {tool} with Jira, you may also need:

{related_lines}

## Get Started

[![View all listings](https://img.shields.io/badge/View_all_listings-2684FF?style=for-the-badge&logo=atlassian&logoColor=white)](https://marketplace.atlassian.com/vendors/798149) &nbsp; [![Learn More](https://img.shields.io/badge/Learn_More-172B4D?style=for-the-badge)](https://www.opshub.com)
"""
    return content


def generate_readme(integrations):
    """Generate the main README.md landing page."""
    int_rows = ""
    for p in sorted(integrations, key=lambda x: x["tool"]):
        int_rows += f"| [{p['tool']}](integrations/{p['slug']}.md) | {p['name']} | [Marketplace]({p['url']}) |\n"

    content = f"""# OpsHub on Atlassian Marketplace

**Enterprise Integration Solutions for Jira**

OpsHub connects Jira with enterprise tools through bidirectional, real-time synchronization. No-code configuration, zero performance impact, and complete data fidelity.

## Integration Solutions

Connect Jira with any of these tools for real-time, bidirectional sync:

| Tool | Integration | Link |
|------|-------------|------|
{int_rows}
## Why OpsHub?

- **No-Code Setup** — No-code configuration using native APIs
- **Bidirectional Sync** — Real-time, two-way data flow with conflict detection and resolution
- **Enterprise Scale** — Trusted by leading enterprises for mission-critical workloads
- **Complete Data Fidelity** — Every comment, attachment, and custom field preserved
- **External Architecture** — Runs outside your tools with zero performance impact

## Learn More

- **[OpsHub Website](https://www.opshub.com)** — Product details, documentation, and resources
- **[Atlassian Marketplace — OpsHub, Inc.](https://marketplace.atlassian.com/vendors/798149)** — All OpsHub listings
- **[Contact Sales](https://www.opshub.com/contact-us/)** — Custom requirements and enterprise pricing

*OpsHub, Inc. — Enterprise Integration for Jira*
"""
    return content


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ensure integrations directory exists
    os.makedirs(os.path.join(base_dir, "integrations"), exist_ok=True)

    # Write integration pages
    for product in INTEGRATIONS:
        filepath = os.path.join(base_dir, "integrations", f"{product['slug']}.md")
        content = generate_integration_page(product)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  Created: integrations/{product['slug']}.md")

    # Write README
    readme = generate_readme(INTEGRATIONS)
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(readme)
    print(f"  Created: README.md")

    print(f"\nTotal pages: {len(INTEGRATIONS)} integrations + README")


if __name__ == "__main__":
    main()
