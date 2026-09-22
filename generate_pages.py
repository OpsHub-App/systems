#!/usr/bin/env python3
"""Generate OpsHub Marketplace GitHub pages — 3 integration listings.

Every piece of content is per-product and strictly derived from the
actual Atlassian Marketplace listing for that integration. Nothing is
shared-template guesswork.
"""

import os

# =============================================================================
# PRODUCT DATA — per-product, strictly from each Atlassian listing
# =============================================================================

INTEGRATIONS = [
    {
        "slug": "servicenow-jira",
        "name": "ServiceNow Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1236368",
        "tool": "ServiceNow",
        "subtitle": "Seamlessly connect ServiceNow and Jira with rich, bidirectional data sync.",
        "desc": "Rich and reliable bidirectional data sync between Jira and ServiceNow for tables, tasks, tests, steps, comments, attachments, links, and more.",
        "syncs": "Tables, tasks, incidents, problems, change records, requests, tests, steps, sprints, assignment groups, comments, attachments, links, mentions, rich text (HTML/Wiki), and history",
        "syncs_paragraph": "All data flows bidirectionally. Field-level conflict management, automatic retry, and error logging ensure your data stays consistent across both platforms.",
        "benefits": [
            ["Eliminate Manual Work", "Stop copying data between systems. Changes sync automatically in both directions, freeing your team to focus on what matters."],
            ["Always Accurate", "OIM manages field-level conflicts, retries failed updates, and logs errors to keep data consistent. Built on an eventual consistency model, every update reaches the target as intended."],
            ["No-Code Setup", "Avoid custom code or webhook-heavy setups. Using native APIs and no-code configuration, OIM integrates across projects without slowing end-systems."],
            ["Enterprise Ready", "Built for scale with field-level conflict management, automatic retry on failures, and error logging."],
        ],
        "how_it_works": "OpsHub Integration Manager (OIM) uses native APIs to connect ServiceNow and Jira with no-code configuration and no impact on performance on either tool.\n\nSupport teams log incidents or problems in ServiceNow. OpsHub syncs them to Jira as appropriate issue types — bugs, tasks, or stories. Developers work in Jira, with updates syncing back automatically. Comments, attachments, links, and more stay aligned across tools. Everyone sees the latest context without switching tools.",
        "use_cases": [
            "Faster resolution syncing ServiceNow incidents and requests to Jira as bugs or tasks",
            "Clear delivery ownership linking ServiceNow change records to Jira tasks",
            "Improved defect visibility connecting Jira defects to ServiceNow customer impact records",
            "Portfolio-level transparency syncing high-level Jira epics with ServiceNow records",
        ],
        "deploy_text": "OpsHub connects using native APIs and no-code setup without slowing end-systems.",
        "faqs": [
            {
                "q": "Why do teams integrate ServiceNow with Jira?",
                "a": "ServiceNow and Jira are often used by different teams within the same organization. Without integration, teams waste time on manual updates, work with outdated information, and lose visibility across workflows. OpsHub keeps both systems synchronized automatically, so each team continues working in their preferred tool while staying aligned on priorities and progress.",
            },
            {
                "q": "What happens if a sync fails?",
                "a": "OpsHub manages field-level conflicts, retries failed updates, and logs errors to keep data consistent. Built on an eventual consistency model, every update reaches the target as intended.",
            },
            {
                "q": "Is technical coding required to set up the integration?",
                "a": "No. OpsHub provides no-code configuration using native APIs. Teams can set up and manage integrations without custom code or webhook-heavy setups.",
            },
        ],
    },
    {
        "slug": "zendesk-jira",
        "name": "Zendesk Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1234611",
        "tool": "Zendesk",
        "subtitle": "Seamlessly connect Zendesk and Jira with near real-time, bidirectional sync.",
        "desc": "Intelligent, data-rich two-way sync between Zendesk and Jira for any issue type. Zendesk tickets transform into Jira issues with complete context, clear ownership, and predictable engineering escalation.",
        "syncs": "Tickets, issues, comments, attachments, links, priorities, statuses, custom fields, users, and related entities",
        "syncs_paragraph": "OpsHub bidirectionally integrates Zendesk and Jira in near real time. Auto failure retry and reconciliation ensure your data stays consistent across both platforms.",
        "benefits": [
            ["Eliminate Manual Work", "Reduces manual work, improves visibility, and maintains traceability across support and engineering teams."],
            ["Always Accurate", "Zendesk tickets are reliably transformed into Jira issues using controlled rules, preserving full context through synced fields, comments, attachments, and links."],
            ["No-Code Setup", "Manage integration through a no-code UI that scales across teams and projects, using reusable mappings to minimize maintenance."],
            ["Enterprise Ready", "Synchronization runs centrally in OpsHub with zero tool impact. Auto failure retry and reconciliation keep data consistent as volume grows."],
        ],
        "how_it_works": "Synchronization runs centrally in OpsHub, keeping Zendesk and Jira clean and untouched. Users cannot accidentally break integrations by editing fields, workflows, or records.\n\nConfigure Zendesk and Jira, select the projects and entities to integrate, choose the sync direction and filters, then map the required fields. OpsHub handles the synchronization automatically.",
        "use_cases": [
            "Centralizing support and engineering workflows across Zendesk and Jira",
            "Syncing Zendesk tickets to Jira issues with complete context and ownership",
            "Maintaining consistent priorities and statuses across both platforms",
        ],
        "deploy_text": "Synchronization runs centrally in OpsHub, keeping Zendesk and Jira clean and untouched.",
        "faqs": [
            {
                "q": "Can Zendesk and Jira be integrated seamlessly?",
                "a": "Yes. OpsHub bidirectionally integrates Zendesk and Jira, syncing tickets, issues, comments, attachments, priorities, statuses, and other fields in near real time. This reduces manual work, improves visibility, and maintains traceability across support and engineering teams.",
            },
            {
                "q": "How do I set up Zendesk and Jira integration with OpsHub?",
                "a": "Configure Zendesk and Jira, select the projects and entities to integrate, choose the sync direction and filters, then map the required fields. OpsHub handles the synchronization automatically.",
            },
            {
                "q": "What data can be synchronized between Zendesk and Jira?",
                "a": "OpsHub syncs tickets, issues, comments, attachments, priorities, statuses, users, custom fields, and related entities. Teams can customize data flow to improve collaboration and eliminate manual updates.",
            },
        ],
    },
    {
        "slug": "github-jira",
        "name": "GitHub Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1234617",
        "tool": "GitHub",
        "subtitle": "Seamlessly connect GitHub and Jira with near real-time, bidirectional sync.",
        "desc": "Enterprise-grade, bidirectional sync between GitHub and Jira. Sync epics, issues, pull requests, and commits in near real-time. Bridges GitHub markdown and Jira wiki markup for seamless data flow.",
        "syncs": "Epics, issues, pull requests, commits, branches, comments, attachments, links, mentions, status updates, and development activity",
        "syncs_paragraph": "All data flows bidirectionally in near real-time. Field-level conflict management and automatic retry ensure your data stays consistent across both platforms.",
        "benefits": [
            ["Eliminate Manual Work", "Stop copying data between systems. Changes sync automatically in both directions, freeing your team to focus on what matters."],
            ["Always Accurate", "Near real-time synchronization keeps GitHub and Jira aligned. OIM manages field-level conflicts and retries failed updates to prevent data drift."],
            ["No-Code Setup", "Configure your integration with no-code setup using native APIs. No scripting or webhook maintenance needed."],
            ["Enterprise Ready", "Built for scale with field-level conflict management, automatic retry on failures, and sync activity logging."],
        ],
        "how_it_works": "OpsHub Integration Manager (OIM) uses native APIs to connect GitHub and Jira with no-code configuration and no impact on performance on either tool.\n\nProduct teams create epics, stories, or issues in Jira. OpsHub links these with related GitHub branches and pull requests. Developers create commits and pull requests tied to Jira issues. Comments, status updates, and development activity stay aligned across both systems, giving teams near real-time visibility without switching tools.",
        "use_cases": [
            "Controlled change traceability linking commits to Jira issues",
            "Release alignment through branch and PR updates in Jira",
            "Program visibility consolidating GitHub activity into Jira",
            "Enterprise synchronization without complex scripting",
        ],
        "deploy_text": "OpsHub connects through native APIs with no impact on performance on either tool.",
        "faqs": [
            {
                "q": "Why do teams integrate GitHub with Jira?",
                "a": "GitHub and Jira are often used by different teams within the same organization. Without integration, teams waste time on manual updates, work with outdated information, and lose visibility across workflows. OpsHub keeps both systems synchronized automatically, so each team continues working in their preferred tool while staying aligned on priorities and progress.",
            },
            {
                "q": "What happens if a sync fails?",
                "a": "OpsHub retries failed updates and logs sync activity to prevent data drift. Built on an eventual consistency model, it keeps your data aligned across both platforms.",
            },
            {
                "q": "Is technical coding required to set up the integration?",
                "a": "No. OpsHub provides no-code configuration using native APIs. Teams can set up and manage integrations without scripting or webhook maintenance.",
            },
        ],
    },
]

# Slugs of the 3 listings — used for Related Connectors cross-linking
ACTIVE_SLUGS = [p["slug"] for p in INTEGRATIONS]


# =============================================================================
# PAGE GENERATOR — all content comes from per-product data, no shared template
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

    # Build benefits table rows from per-product data
    benefits_rows = ""
    for label, detail in product["benefits"]:
        benefits_rows += f"| **{label}** | {detail} |\n"

    # Build FAQ section from per-product data
    faq_text = ""
    for faq in product["faqs"]:
        faq_text += f"**{faq['q']}**\n\n{faq['a']}\n\n"

    content = f"""# {product['name']}

**{product['subtitle']}**

[![View listing](https://img.shields.io/badge/View_listing-0052CC?style=flat&logo=atlassian&logoColor=white)]({product['url']})

{product['desc']}

## Why Integrate {tool} with Jira?

| Benefit | Details |
|---------|---------|
{benefits_rows}
## What Gets Synced

{product['syncs']}

{product['syncs_paragraph']}

## How It Works

{product['how_it_works']}

## Common Use Cases

{uc_text}

## Supported Deployment

| Deployment | Supported |
|------------|-----------|
| Jira Cloud | ✓ |

{product['deploy_text']}

## Frequently Asked Questions

{faq_text}## Related Connectors

If you use {tool} with Jira, you may also need:

{related_lines}

## Get Started

[![Open listings](https://img.shields.io/badge/Open_listings-0052CC?style=flat&logo=atlassian&logoColor=white)](https://marketplace.atlassian.com/vendors/798149) &nbsp; [![Learn more](https://img.shields.io/badge/Learn_more-172B4D?style=flat)](https://www.opshub.com)
"""
    return content


def generate_readme(integrations):
    """Generate the main README.md landing page."""
    int_rows = ""
    for p in sorted(integrations, key=lambda x: x["tool"]):
        int_rows += f"| [{p['tool']}](integrations/{p['slug']}.md) | {p['name']} | [Marketplace]({p['url']}) |\n"

    content = f"""# OpsHub on Atlassian Marketplace

**Enterprise Integration Solutions for Jira**

OpsHub connects Jira with enterprise tools through bidirectional, near real-time synchronization. No-code configuration, no performance impact, and complete data fidelity.

## Integration Solutions

Connect Jira with any of these tools for near real-time, bidirectional sync:

| Tool | Integration | Link |
|------|-------------|------|
{int_rows}
## Why OpsHub?

- **No-Code Setup** — No-code configuration using native APIs
- **Bidirectional Sync** — Near real-time, two-way data flow with field-level conflict management
- **Enterprise Scale** — Built for large-scale enterprise projects
- **Complete Data Fidelity** — Comments, attachments, links, and mentions stay aligned
- **No Performance Impact** — Connects through native APIs with no impact on your tools

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
