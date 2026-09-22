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
        "desc": "OpsHub delivers dependable two-way synchronization between Jira and ServiceNow, covering tables, tasks, tests, steps, comments, attachments, links, and more.",
        "syncs": "Tables, tasks, incidents, problems, change records, requests, tests, steps, sprints, assignment groups, comments, attachments, links, mentions, rich text (HTML/Wiki), and history",
        "syncs_paragraph": "Every record syncs in both directions. OIM handles field-level conflicts automatically, retries any failed updates, and logs errors so data stays consistent across both platforms.",
        "highlights": [
            ["Bidirectional ServiceNow and Jira sync", "Tables, tests, sprints, and add-on data stay in sync across both tools. HTML/Wiki formatting is preserved, ServiceNow Assignment Groups map to Jira Projects, and comments, attachments, links, mentions, rich text, and history all travel with every record."],
            ["Configure your Jira ServiceNow integration easily", "Skip custom code and complex webhook setups. OIM connects through native APIs with a no-code configuration interface, letting you integrate 10 or 1,000+ projects without degrading performance on either platform."],
            ["Reliable Jira and ServiceNow sync", "Field-level conflicts are detected and resolved automatically, failed updates are retried, and all errors are logged for full visibility. An eventual consistency model guarantees every entity and update reaches the target system as intended."],
        ],
        "how_it_works": "OpsHub Integration Manager (OIM) connects ServiceNow and Jira through native APIs — no custom code, no performance overhead on either platform.\n\nWhen support teams log incidents or problems in ServiceNow, OpsHub automatically creates matching Jira issues in the right format — bugs, tasks, or stories. Developers continue working in Jira, and every update flows back to ServiceNow in near real time. Comments, attachments, and links remain aligned across both tools, so every team member sees the latest context in whichever system they use.",
        "use_cases": [
            "Faster incident resolution — ServiceNow incidents and requests automatically appear in Jira as bugs or tasks, letting engineering act without delay",
            "Delivery ownership clarity — ServiceNow change records stay linked to Jira tasks, keeping approvals and development work in their respective systems",
            "End-to-end defect visibility — Jira defects tied to customer impact link back to ServiceNow records so support teams can track resolution",
            "Portfolio-level transparency — high-level Jira epics or initiatives sync with ServiceNow records for consolidated reporting and oversight",
        ],
        "deploy_text": "OpsHub connects through native APIs with a no-code setup, introducing zero performance overhead on either tool.",
        "faqs": [
            {
                "q": "Why do teams integrate ServiceNow with Jira?",
                "a": "Many organizations rely on ServiceNow for IT operations and Jira for development, but without a connection between them, teams spend time on manual updates and work from outdated data. OpsHub keeps both systems in sync automatically, so each team stays in their preferred tool while sharing priorities and progress in real time.",
            },
            {
                "q": "What happens if a sync fails?",
                "a": "OpsHub automatically retries any failed update and logs the error for review. The platform uses an eventual consistency model, meaning every change is guaranteed to reach the target system even if a temporary issue causes a delay.",
            },
            {
                "q": "Is technical coding required to set up the integration?",
                "a": "No. The entire integration is configured through a no-code interface that connects via native APIs. There is no need for custom scripts, middleware, or ongoing webhook maintenance.",
            },
        ],
    },
    {
        "slug": "zendesk-jira",
        "name": "Zendesk Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1234611",
        "tool": "Zendesk",
        "subtitle": "Seamlessly connect Zendesk and Jira with near real-time, bidirectional sync.",
        "desc": "A data-rich, two-way integration that turns Zendesk tickets into fully contextualized Jira issues — complete with ownership, priority, and a clear path for engineering escalation.",
        "syncs": "Tickets, issues, comments, attachments, links, priorities, statuses, custom fields, users, and related entities",
        "syncs_paragraph": "OpsHub keeps Zendesk and Jira in continuous two-way sync. Automatic failure retry and reconciliation work behind the scenes to ensure data consistency across both platforms.",
        "highlights": [
            ["High data fidelity integration", "Every Zendesk ticket converts to a Jira issue through controlled mapping rules that carry over all synced fields, comments, attachments, and links — giving engineering teams full context, clear ownership, and a predictable escalation path."],
            ["Centralized integration logic, zero tool impact", "All synchronization logic runs inside OpsHub, so neither Zendesk nor Jira is modified in any way. There is no risk of users accidentally breaking the integration by editing fields, workflows, or records in either tool."],
            ["Low-maintenance integration built to scale", "A no-code UI lets teams manage the Zendesk–Jira integration with reusable field mappings, automatic failure retry, and built-in reconciliation — keeping maintenance low even as project count and data volume grow."],
        ],
        "how_it_works": "All synchronization logic runs inside OpsHub, leaving both Zendesk and Jira completely unmodified. Because the integration layer is separate, there is no risk of users accidentally disrupting it by changing fields, workflows, or records.\n\nTo get started, connect your Zendesk and Jira instances, pick the projects and entities you want to integrate, set the sync direction and any filters, and map the required fields. From there, OpsHub handles every update automatically.",
        "use_cases": [
            "Centralizing support and engineering workflows across Zendesk and Jira",
            "Syncing Zendesk tickets to Jira issues with complete context and ownership",
            "Maintaining consistent priorities and statuses across both platforms",
        ],
        "deploy_text": "All synchronization logic runs inside OpsHub, so neither Zendesk nor Jira is modified or impacted.",
        "faqs": [
            {
                "q": "Can Zendesk and Jira be integrated seamlessly?",
                "a": "Yes. OpsHub provides a continuous two-way sync covering tickets, issues, comments, attachments, priorities, statuses, and more. The result is less manual data entry, better cross-team visibility, and full traceability between support and engineering.",
            },
            {
                "q": "How do I set up Zendesk and Jira integration with OpsHub?",
                "a": "Connect your Zendesk and Jira instances, select the projects and entities to integrate, define the sync direction and any filters, and map your fields. OpsHub takes over from there and keeps everything in sync automatically.",
            },
            {
                "q": "What data can be synchronized between Zendesk and Jira?",
                "a": "The integration covers tickets, issues, comments, attachments, priorities, statuses, users, custom fields, and related entities. You can tailor the data flow to match your team’s collaboration needs and remove the need for manual updates.",
            },
        ],
    },
    {
        "slug": "github-jira",
        "name": "GitHub Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1234617",
        "tool": "GitHub",
        "subtitle": "Seamlessly connect GitHub and Jira with near real-time, bidirectional sync.",
        "desc": "An enterprise-grade integration that keeps GitHub and Jira in continuous two-way sync — covering epics, issues, pull requests, and commits while bridging GitHub markdown and Jira wiki markup automatically.",
        "syncs": "Epics, issues, pull requests, commits, branches, comments, attachments, links, mentions, status updates, and development activity",
        "syncs_paragraph": "Every record syncs in both directions in near real time. OIM detects field-level conflicts, retries any failed updates, and logs all sync activity to prevent data drift.",
        "highlights": [
            ["GitHub Jira rich data sync for dev teams", "Epics and issues stay synchronized across GitHub and Jira in near real time. Comments, attachments, links, and mentions travel with every record, and OIM automatically converts between GitHub markdown and Jira wiki markup so formatting is never lost."],
            ["Configure your Integration with no code", "There are no scripts to write and no webhooks to maintain. OIM connects through native APIs and provides a no-code configuration interface, keeping performance unaffected on both GitHub and Jira."],
            ["Reliable GitHub and Jira synchronization", "Field-level conflicts are detected and resolved, failed updates are retried automatically, and every sync event is logged to prevent data drift. An eventual consistency model ensures development activity and project tracking stay aligned at all times."],
        ],
        "how_it_works": "OpsHub Integration Manager (OIM) connects GitHub and Jira through native APIs — no custom scripts, no performance overhead on either platform.\n\nProduct teams create epics, stories, or issues in Jira, and OpsHub automatically links them to the corresponding GitHub branches and pull requests. As developers commit code and open PRs, those updates flow back to Jira in near real time. Comments, status changes, and development activity remain aligned across both systems, giving every team member up-to-date visibility in whichever tool they prefer.",
        "use_cases": [
            "Controlled change traceability linking commits to Jira issues",
            "Accurate release alignment through branch and PR updates in Jira",
            "Program visibility consolidating GitHub activity into Jira",
            "Enterprise-grade synchronization without complex scripting",
        ],
        "deploy_text": "OpsHub connects through native APIs, introducing zero performance overhead on either tool.",
        "faqs": [
            {
                "q": "Why do teams integrate GitHub with Jira?",
                "a": "Development and project management often live in separate tools. Without a live connection, teams resort to manual copy-paste, work from stale data, and lose sight of what's happening across workflows. OpsHub bridges that gap by keeping both systems in sync automatically — each team stays in their preferred tool while sharing priorities and progress in real time.",
            },
            {
                "q": "What happens if a sync fails?",
                "a": "Any update that doesn't go through on the first attempt is automatically retried, and the event is logged for review. Because OpsHub uses an eventual consistency model, every change is guaranteed to reach the target system even after a temporary disruption.",
            },
            {
                "q": "Is technical coding required to set up the integration?",
                "a": "No. The entire setup is handled through a no-code interface that connects via native APIs. You don't need to write scripts or manage webhooks.",
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

    # Build highlights table rows from per-product data
    highlights_rows = ""
    for label, detail in product["highlights"]:
        highlights_rows += f"| **{label}** | {detail} |\n"

    # Build FAQ section from per-product data
    faq_text = ""
    for faq in product["faqs"]:
        faq_text += f"**{faq['q']}**\n\n{faq['a']}\n\n"

    content = f"""# {product['name']}

**{product['subtitle']}**

[![View listing](https://img.shields.io/badge/View_listing-0052CC?style=flat&logo=atlassian&logoColor=white)]({product['url']})

{product['desc']}

## Key Highlights

| Highlight | Details |
|-----------|---------|
{highlights_rows}
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
