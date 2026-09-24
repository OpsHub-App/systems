#!/usr/bin/env python3
"""Generate OpsHub Marketplace GitHub pages - 3 integration listings.

Every piece of content is per-product and strictly derived from the
actual Atlassian Marketplace listing for that integration. Nothing is
shared-template guesswork.
"""

import os

# =============================================================================
# PRODUCT DATA - per-product, strictly from each Atlassian listing
# =============================================================================

INTEGRATIONS = [
    {
        "slug": "servicenow-jira",
        "name": "ServiceNow Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1236368/servicenow-integration-for-jira-bidirectional-sync?utm_source=SNOW+and+jira+Atlassian+listing+on+github+shadow+marketplace&utm_medium=referral&utm_campaign=SNOW+and+jira+Atlassian+listing+on+github+shadow+marketplace",
        "tool": "ServiceNow",
        "subtitle": "Connect ServiceNow and Jira with rich, bidirectional data sync.",
        "desc": "Achieve reliable two-way synchronization between Jira and ServiceNow, for tables, tasks, tests, steps, comments, attachments, links, and more.",
        "highlights": [
            ["Bidirectional ServiceNow and Jira sync", "Tables, tests, sprints, and add-on data stay in sync across both tools. HTML/Wiki formatting is preserved, ServiceNow Assignment Groups map to Jira Projects, and comments, attachments, links, mentions, rich text, and history all travel with every record."],
            ["Configure your Jira ServiceNow integration easily", "Skip custom code and complex webhook setups. OIM connects through native APIs with a no-code configuration interface, letting you integrate 10 or 1,000+ projects without degrading performance on either platform."],
            ["Reliable Jira and ServiceNow sync", "Field-level conflicts are detected and resolved automatically, failed updates are retried, and all errors are logged for full visibility. An eventual consistency model guarantees every entity and update reaches the target system as intended."],
        ],
        "how_it_works": "OpsHub Integration Manager (OIM) connects ServiceNow and Jira through native APIs.\n\nWhen support teams log incidents or problems in ServiceNow, OpsHub automatically syncs them to Jira as bugs, tasks, or stories. Developers continue working in Jira, and every update flows back to ServiceNow in near real time.",
        "use_cases": [
            "ServiceNow incidents and requests automatically appear in Jira as bugs or tasks, letting engineering act without delay",
            "ServiceNow change records stay linked to Jira tasks, keeping approvals and development work in their respective systems",
            "Jira defects tied to customer impact link back to ServiceNow records so support teams can track resolution",
            "High-level Jira epics or initiatives sync with ServiceNow records for consolidated reporting and oversight",
        ],
        "deploy_text": "",
        "faqs": [
            {
                "q": "What should organizations evaluate before selecting a ServiceNow-Jira integration solution?",
                "a": "Evaluate bidirectional synchronization, content transformation, custom field support, monitoring, auditability, security, scalability, conflict resolution, and ease of maintenance. These factors typically have a greater impact on long-term success than connectivity alone.",
            },
            {
                "q": "What is the best ServiceNow-Jira integration tool?",
                "a": "The best ServiceNow-Jira integration tool depends on your workflows, scale, and governance requirements. OIM provides these capabilities through a configurable integration layer that scales with your organization.",
            },
            {
                "q": "How can I set up a seamless integration between ServiceNow and Jira?",
                "a": "With OpsHub Integration Manager (OIM), you configure your ServiceNow-Jira integration entirely through a GUI. Set your field mappings, sync rules, and data flow direction, and OIM keeps both systems aligned from the first sync.",
            },
        ],
    },
]

# Slugs of the listings
ACTIVE_SLUGS = [p["slug"] for p in INTEGRATIONS]


# =============================================================================
# PAGE GENERATOR - all content comes from per-product data, no shared template
# =============================================================================


def generate_integration_page(product):
    """Generate a markdown page for an integration product."""
    tool = product["tool"]
    uc_text = "\n".join([f"- {uc}" for uc in product["use_cases"]])

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

[![View listing](https://img.shields.io/badge/View_listing-0052CC?style=flat&logo=atlassian&logoColor=white)]({product['url']}) &nbsp; [![Learn more](https://img.shields.io/badge/Learn_more-172B4D?style=flat)](https://www.opshub.com/products/opshub-integration-manager/?utm_source=oim+product+page+on+github+shadow+marketplace&utm_medium=referral&utm_campaign=oim+product+page+on+github+shadow+marketplace)

{product['desc']}

## Key Highlights

| Highlight | Details |
|-----------|---------|
{highlights_rows}
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

{faq_text}## Get Started

[![Open listings](https://img.shields.io/badge/Open_listings-0052CC?style=flat&logo=atlassian&logoColor=white)](https://marketplace.atlassian.com/vendors/798149/?utm_source=OpsHub+Vendor+page+%28Atlassian%29+on+Github+shadow+marketplace&utm_medium=referral&utm_campaign=OpsHub+Vendor+page+%28Atlassian%29+on+Github+shadow+marketplace)
"""
    return content


def generate_readme(integrations):
    """Generate the main README.md landing page."""
    int_list = ""
    for p in sorted(integrations, key=lambda x: x["tool"]):
        int_list += f"- [{p['name']}](integrations/{p['slug']}.md)\n"

    content = f"""# OpsHub on Atlassian Marketplace

**Enterprise Integration Solutions for Jira**

OpsHub connects Jira with 70+ ALM, DevOps, ITSM systems through no-code, easy GUI configurations. Sync live data two-way, complete with mentions, comments, attachments, inline files, data movements, and entity deletions.

## Why OpsHub?

- **Zero user overhead** - No plugins are installed in any tool. OpsHub syncs data automatically through each tool's API
- **Bidirectional Sync** - Near real-time, two-way data flow with field-level conflict management
- **Enterprise scale, reliable and fault tolerant** - Sync high volumes of tickets across cross-functional teams without performance impact. Detects and resolves conflicts automatically with built-in retry, recovery, and detailed logging for full visibility

## Integration Solutions

{int_list}
## Learn More

- **[OpsHub Website](https://www.opshub.com/?utm_source=OpsHub+homepage+on+github+shadow+marketplace&utm_medium=referral&utm_campaign=OpsHub+homepage+on+github+shadow+marketplace)** - Product details, documentation, and resources
- **[Atlassian Marketplace - OpsHub, Inc.](https://marketplace.atlassian.com/vendors/798149/?utm_source=OpsHub+Vendor+page+%28Atlassian%29+on+Github+shadow+marketplace&utm_medium=referral&utm_campaign=OpsHub+Vendor+page+%28Atlassian%29+on+Github+shadow+marketplace)** - All OpsHub listings
- **[Contact Sales](https://www.opshub.com/contact-us/?utm_source=contact+us+page+on+github+shadow+marketplace&utm_medium=referral&utm_campaign=contact+us+page+on+github+shadow+marketplace)** - Custom requirements and enterprise pricing

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
