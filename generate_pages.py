#!/usr/bin/env python3
"""Generate all OpsHub Marketplace GitHub pages."""

import os

# =============================================================================
# MASTER PRODUCT LIST
# =============================================================================

INTEGRATIONS = [
    {
        "slug": "servicenow-jira",
        "name": "ServiceNow Integration for Jira",
        "url": "https://marketplace.atlassian.com/apps/1236368",
        "tool": "ServiceNow",
        "desc": "Rich and reliable bidirectional data sync between Jira and ServiceNow for tables, tasks, tests, steps, comments, attachments, links, and more.",
        "syncs": "Tables, tasks, tests, steps, comments, attachments, links, mentions, rich text, and history",
        "use_cases": ["IT teams managing incidents in ServiceNow while developers track work in Jira", "Syncing change requests between ITSM and development workflows", "Keeping service desk tickets and engineering issues connected end-to-end"],
    },
    {
        "slug": "azure-devops-jira",
        "name": "Azure DevOps Integration for Jira",
        "tool": "Azure DevOps",
        "url": "https://marketplace.atlassian.com/apps/1234612",
        "desc": "Bridge Jira and Azure DevOps with two-way synchronization of work items, custom fields, comments, attachments, links, and mentions. Keep both platforms current without manual effort.",
        "syncs": "Work items, bugs, tasks, epics, user stories, custom fields, comments, attachments, inline images, and links",
        "use_cases": ["Organizations using Jira for project management and Azure DevOps for development", "Cross-team collaboration where some teams prefer Azure DevOps and others Jira", "Consolidating reporting across both platforms without duplicate data entry"],
    },
    {
        "slug": "azure-devops-jsm",
        "name": "Azure DevOps Integration for Jira Service Management",
        "tool": "Azure DevOps",
        "url": "https://marketplace.atlassian.com/apps/3318012835",
        "desc": "Integrate Azure DevOps with Jira Service Management to synchronize service requests, incidents, and work items bidirectionally. Enable seamless collaboration between IT service teams and developers.",
        "syncs": "Service requests, incidents, work items, comments, attachments, and custom fields",
        "use_cases": ["IT service desks using JSM while engineering teams work in Azure DevOps", "Automated escalation of service tickets to development work items", "Unified incident tracking across service management and development"],
    },
    {
        "slug": "jsm-jira",
        "name": "OIM for Bidirectional JSM and Jira Integration",
        "tool": "Jira Service Management",
        "url": "https://marketplace.atlassian.com/apps/1624606962",
        "desc": "Synchronize incidents, problems, issues, and more between Jira Service Management and Jira bidirectionally. AI-assisted, no-code setup preserves rich data across both platforms.",
        "syncs": "Incidents, problems, service requests, changes, comments, attachments, SLA data, and custom fields",
        "use_cases": ["Service teams using JSM while product teams use Jira Software", "Syncing customer-reported issues to development backlogs automatically", "Maintaining full visibility across service and development workflows"],
    },
    {
        "slug": "ibm-doors-jira",
        "name": "IBM DOORS and Jira Integration",
        "tool": "IBM Rational DOORS",
        "url": "https://marketplace.atlassian.com/apps/1234709",
        "desc": "Enable two-way synchronization between IBM Rational DOORS and Jira with rich data support including work items, tests, OLE objects, hierarchies, and full traceability at enterprise scale.",
        "syncs": "Requirements, work items, test cases, OLE objects, module hierarchies, links, comments, and attachments",
        "use_cases": ["Defense and aerospace teams managing requirements in DOORS while tracking development in Jira", "Maintaining traceability between requirements and development artifacts", "Regulated industries needing audit-ready requirement-to-delivery linkage"],
    },
    {
        "slug": "ibm-doors-ng-jira",
        "name": "IBM DOORS Next Generation Integration for Jira",
        "tool": "IBM DOORS NG",
        "url": "https://marketplace.atlassian.com/apps/1237857",
        "desc": "Connect IBM DOORS Next Generation with Jira for bidirectional synchronization of requirements, artifacts, and traceability links. Keep engineering and development workflows aligned.",
        "syncs": "Requirements, artifacts, modules, traceability links, comments, attachments, and custom attributes",
        "use_cases": ["Systems engineering teams using DOORS NG for requirements and Jira for execution", "Establishing end-to-end traceability from requirements to delivery", "Regulated industries needing synchronized requirement management"],
    },
    {
        "slug": "ibm-ewm-jira",
        "name": "IBM EWM (Formerly IBM RTC) Integration for Jira",
        "tool": "IBM Engineering Workflow Management",
        "url": "https://marketplace.atlassian.com/apps/1237867",
        "desc": "Integrate IBM Engineering Workflow Management (formerly Rational Team Concert) with Jira. Bidirectionally sync work items, plans, and development artifacts across both platforms.",
        "syncs": "Work items, defects, tasks, plans, comments, attachments, links, and custom attributes",
        "use_cases": ["Teams transitioning from IBM RTC to Jira while maintaining connectivity", "Cross-platform collaboration between IBM EWM and Jira teams", "Keeping legacy IBM toolchain data synchronized with Jira projects"],
    },
    {
        "slug": "ibm-etm-jira",
        "name": "IBM Engineering Test Management (ETM) Integration for Jira",
        "tool": "IBM ETM",
        "url": "https://marketplace.atlassian.com/apps/1237868",
        "desc": "Connect IBM Engineering Test Management with Jira for two-way synchronization of test cases, execution records, and defects. Maintain complete test-to-development traceability.",
        "syncs": "Test cases, test plans, execution records, defects, results, comments, and attachments",
        "use_cases": ["QA teams using IBM ETM while developers work in Jira", "Linking test results to Jira issues for complete quality visibility", "Regulated environments needing connected test and development records"],
    },
    {
        "slug": "opentext-alm-jira",
        "name": "OpenText ALM (HP ALM) and Jira Integration",
        "tool": "OpenText ALM / HP ALM / Micro Focus ALM",
        "url": "https://marketplace.atlassian.com/apps/1236342",
        "desc": "Synchronize issues and tests between OpenText ALM (formerly HP ALM / Micro Focus ALM) and Jira with two-way, rich data sync. Connect quality management with agile development.",
        "syncs": "Defects, requirements, tests, test sets, test runs, comments, attachments, and custom fields",
        "use_cases": ["QA teams on ALM working alongside development teams on Jira", "Migrating workflows from HP ALM to Jira while keeping both systems active", "Enterprise testing teams needing visibility across ALM and Jira"],
    },
    {
        "slug": "salesforce-jira",
        "name": "Salesforce Integration for Jira",
        "tool": "Salesforce",
        "url": "https://marketplace.atlassian.com/apps/1237866",
        "desc": "No-code, bidirectional, data-rich sync between Salesforce and Jira for Cases, Opportunities, Feeds, Accounts, and Custom Objects. Bridge the gap between sales and engineering teams.",
        "syncs": "Cases, opportunities, accounts, contacts, leads, feeds, custom objects, comments, attachments, @mentions, and relationships",
        "use_cases": ["Sales teams reporting customer issues in Salesforce while engineering fixes them in Jira", "Syncing product feedback from CRM to development backlogs", "Keeping customer-facing teams informed about bug fix progress"],
    },
    {
        "slug": "hubspot-jira",
        "name": "HubSpot Integration for Jira",
        "tool": "HubSpot",
        "url": "https://marketplace.atlassian.com/apps/1238418",
        "desc": "Real-time, two-way sync between HubSpot and Jira so go-to-market and engineering teams stay aligned, reduce handoff gaps, and resolve issues faster.",
        "syncs": "Deals, tickets, contacts, notes, tasks, comments, ownership changes, stages, attachments, and status updates",
        "use_cases": ["Marketing and sales teams on HubSpot while product teams use Jira", "Automatically creating Jira issues from HubSpot support tickets", "Tracking customer requests from CRM through to development completion"],
    },
    {
        "slug": "zendesk-jira",
        "name": "Zendesk Integration for Jira",
        "tool": "Zendesk",
        "url": "https://marketplace.atlassian.com/apps/1234611",
        "desc": "Enterprise-grade, two-way sync between Zendesk and Jira. Keep support tickets and development issues connected with rich data synchronization and automated workflows.",
        "syncs": "Tickets, comments, attachments, custom fields, tags, organizations, and users",
        "use_cases": ["Support teams on Zendesk while engineering resolves issues in Jira", "Automatically escalating critical Zendesk tickets to Jira development sprints", "Providing support agents real-time visibility into engineering fix status"],
    },
    {
        "slug": "rally-jira",
        "name": "Rally Integration for Jira",
        "tool": "Rally (Broadcom)",
        "url": "https://marketplace.atlassian.com/apps/1234735",
        "desc": "Bidirectional, real-time sync between Rally and Jira. Synchronize user stories, defects, tasks, and test cases across both agile management platforms without manual duplication.",
        "syncs": "Portfolio items, user stories, defects, tasks, test cases, change sets, risks, comments, attachments, links, and inline images",
        "use_cases": ["Organizations with teams split between Rally and Jira for agile planning", "Consolidating portfolio-level visibility across both platforms", "Transitioning from Rally to Jira while keeping both systems functional"],
    },
    {
        "slug": "enterprise-architect-jira",
        "name": "Sparx Enterprise Architect and Jira Integration",
        "tool": "Sparx Enterprise Architect",
        "url": "https://marketplace.atlassian.com/apps/1234974",
        "desc": "Bidirectionally integrate Sparx EA elements, diagrams, and packages with Jira issues using a simple drag-and-drop interface. Bridge model-based systems engineering with agile development.",
        "syncs": "EA elements, diagrams, packages, operations, attributes, Jira issues, sub-tasks, versions, worklogs, attachments, history, and relationships",
        "use_cases": ["Systems engineers modeling in EA while developers track work in Jira", "Linking architecture models to development tasks for traceability", "MBSE teams needing visibility between design models and Jira backlogs"],
    },
    {
        "slug": "aras-jira",
        "name": "Aras Innovator and Jira Integration",
        "tool": "Aras Innovator",
        "url": "https://marketplace.atlassian.com/apps/1235048",
        "desc": "Enable a Digital Thread with two-way rich data sync between Aras Innovator and Jira for all system and custom entities. Connect PLM workflows with agile development processes.",
        "syncs": "System entities, custom entities, parts, BOMs, documents, ECOs, Jira issues, and comments",
        "use_cases": ["Engineering teams managing product data in Aras while development teams use Jira", "Creating a connected digital thread from product design to software delivery", "PLM-to-Jira traceability for regulated manufacturing environments"],
    },
    {
        "slug": "pagerduty-jira",
        "name": "PagerDuty and Jira Integration",
        "tool": "PagerDuty",
        "url": "https://marketplace.atlassian.com/apps/1237335",
        "desc": "Bidirectional, real-time sync between PagerDuty and Jira. Automatically create and update Jira issues from PagerDuty incidents and keep incident response teams connected with development.",
        "syncs": "Incidents, issues, comments, attachments, links, mentions, rich text, status transitions, and history",
        "use_cases": ["DevOps teams using PagerDuty for on-call while tracking fixes in Jira", "Automatic Jira issue creation from PagerDuty alerts", "Post-incident workflows that link PagerDuty incidents to Jira follow-up tasks"],
    },
    {
        "slug": "tricentis-tosca-jira",
        "name": "Tricentis Tosca Integration for Jira",
        "tool": "Tricentis Tosca",
        "url": "https://marketplace.atlassian.com/apps/1237180",
        "desc": "Rich data sync between Tricentis Tosca and Jira for TestCases, ExecutionLogs, TCFolders, Requirements, Issues, and Modules. Enable test automation at scale with a no-code setup.",
        "syncs": "Test cases, execution logs, test case folders, requirements, issues, modules, and results",
        "use_cases": ["QA automation teams on Tosca while developers and PMs use Jira", "Linking automated test results back to Jira user stories and defects", "Enterprise test management with centralized visibility in Jira"],
    },
    {
        "slug": "tricentis-qtest-jira",
        "name": "Tricentis qTest and Jira Integration",
        "tool": "Tricentis qTest",
        "url": "https://marketplace.atlassian.com/apps/1237064",
        "desc": "Two-way, no-code sync between Tricentis qTest and Jira. Synchronize test cases, defects, requirements, and execution results to keep QA and development fully aligned.",
        "syncs": "Test cases, test runs, defects, requirements, releases, cycles, comments, and attachments",
        "use_cases": ["Test management teams on qTest collaborating with developers on Jira", "Automatic defect creation in Jira from failed qTest test runs", "Unified test and development reporting across qTest and Jira"],
    },
    {
        "slug": "jama-jira",
        "name": "Jama Connect Integration for Jira",
        "tool": "Jama Connect",
        "url": "https://marketplace.atlassian.com/apps/1234765",
        "desc": "Bidirectional sync between Jama Connect and Jira. Synchronize requirements, test cases, and defects to maintain traceability from requirements through to delivery.",
        "syncs": "Requirements, test cases, defects, relationships, comments, attachments, and custom fields",
        "use_cases": ["Product teams defining requirements in Jama while developers work in Jira", "Maintaining requirements-to-code traceability in regulated industries", "Cross-platform collaboration between systems engineering and software teams"],
    },
    {
        "slug": "codebeamer-jira",
        "name": "PTC Codebeamer ALM and Jira Integration",
        "tool": "PTC Codebeamer",
        "url": "https://marketplace.atlassian.com/apps/1234937",
        "desc": "Bidirectional integration between PTC Codebeamer ALM and Jira. Enterprise-grade sync for requirements, test cases, defects, and more across both ALM platforms.",
        "syncs": "Requirements, work items, test cases, defects, risks, traceability links, comments, and attachments",
        "use_cases": ["Automotive and medical device teams on Codebeamer collaborating with Jira teams", "Maintaining ALM traceability across regulated development environments", "Connecting safety-critical requirements in Codebeamer to Jira development tasks"],
    },
    {
        "slug": "windchill-jira",
        "name": "Bidirectional PTC Windchill RV&S Integration for Jira",
        "tool": "PTC Windchill RV&S",
        "url": "https://marketplace.atlassian.com/apps/1236668",
        "desc": "Easy-to-setup, data-rich, two-way sync for requirements, change requests, work items, documents, and custom entities between PTC Windchill RV&S (formerly Windchill ALM / MKS) and Jira.",
        "syncs": "Change Orders, Change Requests, Defects, Documents, Requirements, Tests, MKS Solutions, Model Element Specifications, custom entities, comments, attachments, and links",
        "use_cases": ["Requirements teams managing work in Windchill RV&S while developers track delivery in Jira", "Syncing change orders and defects between Windchill ALM and Jira for end-to-end traceability", "Preserving hierarchies and linked records across PTC Windchill RV&S and Jira projects"],
    },
    {
        "slug": "windchill-plm-jira",
        "name": "PTC Windchill PLM/PDM Integration for Jira",
        "tool": "PTC Windchill PLM/PDM",
        "url": "https://marketplace.atlassian.com/apps/1572722965",
        "desc": "Bidirectional sync between PTC Windchill PLM/PDM and Jira. Keep product data management and software development connected with real-time data exchange.",
        "syncs": "Parts, CAD documents, change requests, change notices, product structures, Jira issues, and comments",
        "use_cases": ["Product engineering teams on Windchill PDM coordinating with Jira software teams", "Linking hardware design changes to software development tasks", "Unified change management across mechanical and software engineering"],
    },
    {
        "slug": "polarion-jira",
        "name": "Siemens Polarion ALM Integration for Jira",
        "tool": "Siemens Polarion ALM",
        "url": "https://marketplace.atlassian.com/apps/2439406316",
        "desc": "Bidirectional sync between Siemens Polarion ALM and Jira. Connect requirements, work items, and test cases across both platforms for complete lifecycle traceability.",
        "syncs": "Work items, requirements, test cases, documents, traceability links, comments, and attachments",
        "use_cases": ["Automotive and aerospace teams using Polarion for ALM alongside Jira", "Maintaining safety and compliance traceability across Polarion and Jira", "Cross-team collaboration between Polarion requirements engineers and Jira developers"],
    },
    {
        "slug": "vmanager-jira",
        "name": "vManager (Verisium Manager) Integration for Jira",
        "tool": "Cadence vManager / Verisium Manager",
        "url": "https://marketplace.atlassian.com/apps/1237997",
        "desc": "Bi-directional integration between vManager (now Verisium Manager) and Jira. Sync verification data, defects, and requirements with full lifecycle traceability for semiconductor design teams.",
        "syncs": "Verification sessions, regression runs, defects, requirements, coverage data, comments, and custom fields",
        "use_cases": ["Semiconductor verification teams on vManager collaborating with Jira project teams", "Linking chip verification results to development tracking in Jira", "Full lifecycle traceability from design verification to issue resolution"],
    },
    {
        "slug": "github-saas-jira",
        "name": "GitHub (SaaS) and Jira Integration",
        "tool": "GitHub (Cloud)",
        "url": "https://marketplace.atlassian.com/apps/1237063",
        "desc": "Bidirectional sync between GitHub (SaaS) and Jira. Connect issues, pull requests, and repositories with Jira projects for seamless developer-to-project-manager collaboration.",
        "syncs": "Issues, pull requests, commits, epics, comments, labels, attachments, and mentions",
        "use_cases": ["Development teams on GitHub while project managers track progress in Jira", "Automatic Jira issue updates when GitHub PRs are merged", "Linking code changes in GitHub to Jira user stories and epics"],
    },
    {
        "slug": "github-jira",
        "name": "GitHub Integration for Jira",
        "tool": "GitHub (Enterprise/On-Prem)",
        "url": "https://marketplace.atlassian.com/apps/1234617",
        "desc": "Enterprise-grade, bidirectional sync between GitHub and Jira. Keep code repositories and project management aligned with rich data synchronization across both platforms.",
        "syncs": "Issues, pull requests, commits, code reviews, comments, labels, and milestones",
        "use_cases": ["Enterprise teams on GitHub Enterprise Server working with Jira projects", "Bridging GitHub-based open source development workflows with Jira tracking", "Unified visibility across code management and project management"],
    },
    {
        "slug": "gitlab-jira",
        "name": "GitLab and Jira Integration",
        "tool": "GitLab",
        "url": "https://marketplace.atlassian.com/apps/1236602",
        "desc": "Bidirectional integration between GitLab and Jira. Sync issues, merge requests, and pipelines with Jira projects for connected DevOps and project management workflows.",
        "syncs": "Commits, epics, issues, comments, attachments, links, and mentions",
        "use_cases": ["DevOps teams on GitLab while project managers use Jira for planning", "Linking GitLab CI/CD pipeline results to Jira development tasks", "Cross-platform visibility for organizations using both GitLab and Jira"],
    },
    {
        "slug": "digital-ai-jira",
        "name": "Digital.ai Agility (VersionOne) and Jira Integration",
        "tool": "Digital.ai Agility / VersionOne",
        "url": "https://marketplace.atlassian.com/apps/1237865",
        "desc": "Bidirectional sync between Digital.ai Agility (formerly VersionOne) and Jira. Keep portfolio-level planning aligned with team-level execution across both agile platforms.",
        "syncs": "Epics, stories, defects, tasks, iterations, sprints, comments, and attachments",
        "use_cases": ["Portfolio planning in Digital.ai Agility with team execution in Jira", "Transitioning from VersionOne to Jira while maintaining bidirectional sync", "Multi-level agile planning across enterprise and team tools"],
    },
    {
        "slug": "bugzilla-jira",
        "name": "Bugzilla and Jira Integration",
        "tool": "Bugzilla",
        "url": "https://marketplace.atlassian.com/apps/4186937217",
        "desc": "Bidirectional sync between Bugzilla and Jira. Connect legacy bug tracking workflows with modern agile development to keep both systems current without manual updates.",
        "syncs": "Bugs, enhancements, tasks, comments, attachments, custom fields, and status changes",
        "use_cases": ["Teams transitioning from Bugzilla to Jira while keeping both systems active", "Open source projects on Bugzilla collaborating with enterprise Jira teams", "Maintaining legacy Bugzilla records while doing active development in Jira"],
    },
    {
        "slug": "helix-alm-jira",
        "name": "Perforce Helix ALM Integration for Jira",
        "tool": "Perforce Helix ALM",
        "url": "https://marketplace.atlassian.com/apps/1238235",
        "desc": "Bidirectional sync between Perforce Helix ALM and Jira. Connect requirements, test cases, and issues across both platforms for comprehensive application lifecycle traceability.",
        "syncs": "Requirements, test cases, test runs, issues, documents, traceability links, comments, and attachments",
        "use_cases": ["QA and requirements teams on Helix ALM while developers work in Jira", "Maintaining test-to-requirement traceability across Helix ALM and Jira", "Regulated environments needing connected ALM records with Jira development data"],
    },
    {
        "slug": "clearquest-jira",
        "name": "IBM ClearQuest Integration for Jira",
        "tool": "IBM ClearQuest",
        "url": "https://marketplace.atlassian.com/apps/2378820378",
        "desc": "Bidirectional integration between IBM ClearQuest and Jira. Synchronize defect tracking and change management records across both platforms to bridge legacy and modern workflows.",
        "syncs": "Defects, change requests, records, comments, attachments, history, and custom fields",
        "use_cases": ["Organizations migrating from ClearQuest to Jira while keeping historical data connected", "Teams on ClearQuest collaborating with Jira-based development groups", "Legacy defect tracking systems that need real-time connection to Jira"],
    },
    {
        "slug": "blueprint-jira",
        "name": "Blueprint Integration for Jira",
        "tool": "Blueprint Requirements Center",
        "url": "https://marketplace.atlassian.com/apps/1589521068",
        "desc": "Bidirectional sync between Blueprint Requirements Center and Jira. Connect requirements definition with agile delivery for complete traceability from concept to code.",
        "syncs": "Requirements, artifacts, use cases, business rules, comments, attachments, and traceability links",
        "use_cases": ["Business analysts defining requirements in Blueprint while developers use Jira", "Maintaining requirements traceability in FDA-regulated environments", "Connecting business requirements to Jira stories and tasks automatically"],
    },
    {
        "slug": "aha-jira",
        "name": "Aha! Integration for Jira",
        "tool": "Aha! Roadmaps",
        "url": "https://marketplace.atlassian.com/apps/1237084",
        "desc": "Bidirectional sync between Aha! Roadmaps and Jira. Connect product strategy and roadmap planning with development execution to keep PMs and engineers aligned.",
        "syncs": "Features, requirements, initiatives, releases, epics, stories, comments, and custom fields",
        "use_cases": ["Product managers planning in Aha! while engineering delivers in Jira", "Syncing roadmap priorities with sprint backlogs automatically", "Unified product and engineering visibility across Aha! and Jira"],
    },
    {
        "slug": "dynamics-365-jira",
        "name": "Microsoft Dynamics 365 Integration for Jira",
        "tool": "Microsoft Dynamics 365",
        "url": "https://marketplace.atlassian.com/apps/1237998",
        "desc": "No-code, two-way sync between Microsoft Dynamics 365 CRM and Jira. Connect customer relationship data with development workflows to close the loop between sales and engineering.",
        "syncs": "Cases, accounts, contacts, opportunities, tasks, notes, and custom entities",
        "use_cases": ["Sales teams on Dynamics 365 while product teams track work in Jira", "Escalating CRM cases to Jira engineering issues automatically", "Unified view of customer issues across CRM and development platforms"],
    },
    {
        "slug": "monday-jira",
        "name": "Monday.com Integration for Jira",
        "tool": "Monday.com",
        "url": "https://marketplace.atlassian.com/apps/336223777",
        "desc": "Bidirectional integration between Monday.com and Jira. Synchronize items, tasks, and updates across both work management platforms for cross-team collaboration.",
        "syncs": "Items, subitems, tickets, contacts, deals, leads, workspaces, boards, groups, sprints, comments, attachments, mentions, and dependencies",
        "use_cases": ["Non-technical teams on Monday.com collaborating with Jira development teams", "Syncing project timelines and tasks across Monday.com and Jira", "Organizations using both platforms for different departments"],
    },
    {
        "slug": "servicenow-jsm",
        "name": "ServiceNow and Jira Service Management Integration",
        "tool": "ServiceNow",
        "url": "https://marketplace.atlassian.com/apps/249435302",
        "desc": "Integrate ServiceNow with Jira Service Management for bidirectional sync of incidents, requests, and changes. Unify IT service management across both ITSM platforms.",
        "syncs": "Incidents, requests, changes, problems, tasks, comments, attachments, and configuration items",
        "use_cases": ["Organizations running both ServiceNow and JSM across departments", "Merging IT service desks after acquisitions", "Unified incident management across multiple ITSM platforms"],
    },
    {
        "slug": "mbse-jira",
        "name": "MBSE Integration for Jira",
        "tool": "MBSE Tools (Cameo, MagicDraw)",
        "url": "https://marketplace.atlassian.com/apps/3248021866",
        "desc": "Bidirectional integration connecting Model-Based Systems Engineering tools with Jira. Synchronize SysML models, requirements, and design elements with Jira development workflows.",
        "syncs": "SysML elements, blocks, requirements, parametric models, activities, Jira issues, and traceability links",
        "use_cases": ["Systems engineers modeling in Cameo/MagicDraw while developers track in Jira", "Linking system architecture models to software implementation tasks", "Defense and aerospace programs needing MBSE-to-Jira traceability"],
    },
    {
        "slug": "bmc-helix-jira",
        "name": "BMC Helix ITSM Integration for Jira",
        "tool": "BMC Helix ITSM / BMC Remedy",
        "url": "https://marketplace.atlassian.com/apps/2812486966",
        "desc": "Connect BMC Helix ITSM (formerly BMC Remedy) with Jira for bidirectional sync of incidents, changes, and problems. Bridge IT service management with development workflows.",
        "syncs": "Incidents, change requests, problems, tasks, work orders, comments, attachments, and custom fields",
        "use_cases": ["IT operations on BMC Helix while developers resolve issues in Jira", "Automating incident-to-engineering-task escalation", "Unified ITSM and development tracking across BMC Helix and Jira"],
    },
    {
        "slug": "teamforge-jira",
        "name": "Digital.ai TeamForge Integration for Jira",
        "tool": "Digital.ai TeamForge",
        "url": "https://marketplace.atlassian.com/apps/1336073391",
        "desc": "Bidirectional integration between Digital.ai TeamForge and Jira. Synchronize trackers, artifacts, and tasks across both ALM platforms for cross-team collaboration.",
        "syncs": "Trackers, artifacts, tasks, planning folders, documents, comments, and attachments",
        "use_cases": ["Organizations transitioning from TeamForge to Jira", "Cross-team collaboration between TeamForge and Jira groups", "Maintaining legacy TeamForge data while active development moves to Jira"],
    },
    {
        "slug": "caliber-jira",
        "name": "OpenText PPM (Caliber RM) Integration for Jira",
        "tool": "OpenText PPM / Caliber RM",
        "url": "https://marketplace.atlassian.com/apps/3804751386",
        "desc": "Two-way sync between OpenText PPM (formerly Caliber RM) and Jira. Connect requirements management with agile development for complete traceability.",
        "syncs": "Requirements, baselines, traceability links, discussions, Jira issues, comments, and custom fields",
        "use_cases": ["Requirements teams using Caliber while development teams use Jira", "Maintaining requirements-to-development traceability", "Legacy Caliber environments needing connection to modern Jira workflows"],
    },
    {
        "slug": "snowflake-jira",
        "name": "Snowflake and Jira Integration",
        "tool": "Snowflake",
        "url": "https://marketplace.atlassian.com/apps/1238393",
        "desc": "Create a Jira-to-Snowflake data lake with full history and normalized data, AI-ready for copilots, analytics, and engineering insights. One-way incremental sync keeps your Snowflake warehouse current.",
        "syncs": "Issues, issue links, full history, sprint transitions, status transitions, comments, custom fields, workflows, and plugin data (Zephyr, Xray, R4J, and more)",
        "use_cases": ["Building an AI-ready engineering data lake from Jira data in Snowflake", "Powering copilots and analytics dashboards with rich, normalized Jira history", "Measuring cycle time, identifying bottlenecks, and supporting root-cause analysis with Jira data in Snowflake"],
        "one_way": True,
    },
    {
        "slug": "subversion-jira",
        "name": "Subversion (SVN) Integration for Jira",
        "tool": "Apache Subversion",
        "url": "https://marketplace.atlassian.com/apps/1556228798",
        "desc": "Real-time integration between Subversion and Jira. Connect SVN commits, branches, and tags with Jira issues for development traceability without switching to Git.",
        "syncs": "Commits, branches, tags, changesets, file changes, and Jira issue links",
        "use_cases": ["Teams using SVN for version control while managing projects in Jira", "Linking code commits in Subversion to Jira issues automatically", "Organizations maintaining SVN repositories that need Jira integration"],
    },
    {
        "slug": "jenkins-jira",
        "name": "Jenkins and Jira Integration",
        "tool": "Jenkins",
        "url": "https://marketplace.atlassian.com/apps/1327211723",
        "desc": "Bidirectional integration between Jenkins CI/CD and Jira. Connect build and deployment pipelines with project tracking for complete DevOps visibility.",
        "syncs": "Build results, pipeline stages, deployment status, test results, and Jira issue updates",
        "use_cases": ["DevOps teams linking Jenkins build results to Jira issues", "Automatic Jira updates when Jenkins deployments succeed or fail", "End-to-end CI/CD visibility from Jira story to production deployment"],
    },
    {
        "slug": "zephyr-enterprise-testRail",
        "name": "Zephyr Enterprise for Jira and TestRail Integration",
        "tool": "Zephyr Enterprise / TestRail",
        "url": "https://marketplace.atlassian.com/apps/1100050933",
        "desc": "Bidirectionally sync steps, cycles, folders, and test cases between Zephyr Enterprise and TestRail. AI-assisted, no-code setup preserves rich test data across both platforms.",
        "syncs": "Test cases, test steps, test cycles, test plans, folders, execution results, and attachments",
        "use_cases": ["Enterprise QA teams bridging Zephyr Enterprise with TestRail", "Centralized test reporting across multiple test management tools", "Organizations standardizing on one test tool while maintaining connectivity to the other"],
    },
    {
        "slug": "xray-testRail",
        "name": "Xray for Jira and TestRail Integration",
        "tool": "Xray / TestRail",
        "url": "https://marketplace.atlassian.com/apps/1238271",
        "desc": "Bidirectional sync between Xray for Jira and TestRail. Keep test cases, plans, and execution results aligned across both test management platforms.",
        "syncs": "Test cases, test plans, test executions, test sets, preconditions, results, and attachments",
        "use_cases": ["Teams using Xray in Jira while other teams use TestRail", "Consolidating test management data across Xray and TestRail", "Migration scenarios where both test management tools are active"],
    },
    {
        "slug": "zephyr-jama",
        "name": "Zephyr for Jira and Jama Integration",
        "tool": "Zephyr for Jira / Jama Connect",
        "url": "https://marketplace.atlassian.com/apps/1238264",
        "desc": "Connect Zephyr for Jira test management with Jama Connect requirements management. Bidirectional sync keeps tests and requirements linked for full V-model traceability.",
        "syncs": "Test cases, requirements, traceability links, execution results, comments, and attachments",
        "use_cases": ["QA teams on Zephyr for Jira needing traceability to Jama requirements", "V-model development with requirements in Jama and tests in Zephyr", "Regulated industries needing connected requirements-to-test evidence"],
    },
    {
        "slug": "two-way-sync-jira",
        "name": "Two-Way Internal and External Sync for Jira",
        "tool": "Jira (Multi-Instance)",
        "url": "https://marketplace.atlassian.com/apps/2019250150",
        "desc": "Bidirectional sync between multiple Jira instances, both internal and external. Keep projects, issues, and workflows aligned across separate Jira deployments without manual duplication.",
        "syncs": "Issues, projects, workflows, comments, attachments, custom fields, sprints, and boards",
        "use_cases": ["Organizations with multiple Jira instances that need cross-instance visibility", "Vendor-client Jira synchronization without sharing full access", "Post-acquisition Jira consolidation with real-time sync during transition"],
    },
    {
        "slug": "smart-data-lake-jira",
        "name": "OpsHub Smart Data Lake for Jira",
        "tool": "Data Analytics",
        "url": "https://marketplace.atlassian.com/apps/1238384",
        "desc": "Make Jira data AI-ready with a unified, context-rich data lake and real-time integration across DevOps, test, and requirements tools. Power copilots, analytics, and engineering insights.",
        "syncs": "Issues, workflows, updates, test cases, requirements, incidents, custom fields, status transitions, and plugin data across connected tools",
        "use_cases": ["Building an AI-ready data lake by connecting Jira with Azure DevOps, ServiceNow, and 70+ tools", "Powering copilots and AI systems with context-aware, linked data from requirements to incidents", "Engineering analytics across the full DevOps lifecycle with unified Jira data"],
    },
    {
        "slug": "redmine-jira",
        "name": "Redmine Integration for Jira",
        "tool": "Redmine",
        "url": "https://marketplace.atlassian.com/apps/1238263",
        "desc": "Bidirectional, no-code sync between Redmine and Jira. Keep issues, comments, attachments, and status changes synchronized across both platforms in real time.",
        "syncs": "Issues, custom issue types, comments, attachments, relationships, inline formatting, custom fields, and history",
        "use_cases": ["Teams running Redmine alongside Jira without duplicating data entry", "Gradual transition from Redmine to Jira while keeping both systems active", "Cross-team collaboration between Redmine and Jira projects"],
    },
    {
        "slug": "xray-jama",
        "name": "Xray for Jira Integration for Jama",
        "tool": "Xray for Jira / Jama Connect",
        "url": "https://marketplace.atlassian.com/apps/1238223",
        "desc": "Bidirectional sync between Xray for Jira and Jama Connect. Synchronize test entities, requirements, and attachments to maintain complete test-to-requirement traceability.",
        "syncs": "Test cases, test plans, test executions, requirements, attachments, comments, and traceability relationships",
        "use_cases": ["QA teams using Xray for test management while requirements live in Jama", "Maintaining bidirectional traceability between Jama requirements and Xray tests", "Regulated industries needing connected test evidence and requirements"],
    },
    {
        "slug": "ca-sdm-jira",
        "name": "CA Service Desk Manager (SDM) Integration for Jira",
        "tool": "CA Service Desk Manager",
        "url": "https://marketplace.atlassian.com/apps/1059270378",
        "desc": "Bidirectional integration between Broadcom CA Service Desk Manager and Jira. Synchronize incidents, requests, and change orders across both ITSM platforms.",
        "syncs": "Incidents, requests, change orders, problems, tasks, comments, attachments, and custom fields",
        "use_cases": ["IT teams using CA SDM for service management while development uses Jira", "Automated escalation from CA SDM tickets to Jira engineering tasks", "Unified ITSM reporting across CA SDM and Jira"],
    },
    {
        "slug": "jira-align-jira",
        "name": "Jira Align Integration for Jira",
        "tool": "Jira Align",
        "url": "https://marketplace.atlassian.com/apps/1237429",
        "desc": "Connect Jira Align portfolio management with Jira execution through OpsHub Integration Manager. Synchronize epics, features, and strategic themes across both platforms.",
        "syncs": "Epics, features, capabilities, strategic themes, programs, iterations, and custom fields",
        "use_cases": ["Portfolio teams in Jira Align aligning with delivery teams in Jira", "Synchronizing SAFe artifacts between Jira Align and Jira", "Enterprise agile planning with connected portfolio and team-level data"],
    },
    {
        "slug": "modern-requirements-jira",
        "name": "Modern Requirements Integration for Jira",
        "tool": "Modern Requirements4DevOps",
        "url": "https://marketplace.atlassian.com/apps/2428745038",
        "desc": "Bidirectional sync between Modern Requirements4DevOps and Jira. Connect requirements authored in Azure DevOps with Jira development workflows.",
        "syncs": "Requirements, use cases, user stories, traceability matrices, comments, and attachments",
        "use_cases": ["Requirements teams on Modern Requirements while developers use Jira", "Cross-platform requirements traceability between Azure DevOps and Jira", "Regulated environments needing connected requirement and development records"],
    },
    {
        "slug": "solarwinds-jira",
        "name": "SolarWinds Service Desk Integration for Jira",
        "tool": "SolarWinds Service Desk",
        "url": "https://marketplace.atlassian.com/apps/1591510710",
        "desc": "Bidirectional sync between SolarWinds Service Desk and Jira. Connect IT service management with development workflows to keep service and engineering teams aligned.",
        "syncs": "Incidents, requests, problems, changes, tasks, comments, attachments, and custom fields",
        "use_cases": ["IT service desk teams on SolarWinds while engineering uses Jira", "Automatic escalation from SolarWinds tickets to Jira development tasks", "Unified service and development visibility across SolarWinds and Jira"],
    },
    {
        "slug": "testRail-jira",
        "name": "TestRail Integration for Jira",
        "tool": "TestRail",
        "url": "https://marketplace.atlassian.com/apps/1237332",
        "desc": "Bidirectional sync between TestRail and Jira through OpsHub Integration Manager. Connect test management with development tracking for complete quality visibility.",
        "syncs": "Test cases, test runs, test plans, milestones, results, defects, comments, and attachments",
        "use_cases": ["QA teams managing tests in TestRail while developers track work in Jira", "Automatic Jira defect creation from failed TestRail test runs", "Unified test and development reporting across TestRail and Jira"],
    },
    {
        "slug": "cadence-midas-jira",
        "name": "Bidirectional Cadence Midas and Jira Integration",
        "tool": "Cadence Midas",
        "url": "https://marketplace.atlassian.com/apps/107948785",
        "desc": "Connect functional safety analysis with engineering execution for end-to-end traceability and compliance. Two-way sync of safety mechanisms, test results, issues, and requirements between Cadence Midas and Jira.",
        "syncs": "Safety mechanisms, test results, issues, requirements, safety requirements, verification records, comments, attachments, and custom fields",
        "use_cases": ["Functional safety teams using Cadence Midas while engineering tracks work in Jira", "Maintaining traceability and visibility into data flow to support ISO 26262 compliance", "Syncing safety requirements and verification records between Cadence Midas and Jira at scale"],
    },
    {
        "slug": "selenium-jira",
        "name": "Selenium and Jira Bidirectional Integration",
        "tool": "Selenium",
        "url": "https://marketplace.atlassian.com/apps/954531136",
        "desc": "Bidirectional integration between Selenium test automation and Jira. Synchronize test scripts with Jira issues using AI-assisted, no-code entity mapping while preserving rich data.",
        "syncs": "Test scripts, Jira issues, comments, attachments, images, @mentions, relationships, history, and custom fields",
        "use_cases": ["QA automation teams syncing Selenium test scripts with Jira issues for traceability", "Keeping test automation artifacts connected with Jira development workflows", "End-to-end visibility from Selenium test scripts to Jira development tasks"],
    },
    {
        "slug": "bmc-helix-jsm",
        "name": "BMC Helix ITSM Connector for Jira Service Management",
        "tool": "BMC Helix ITSM",
        "url": "https://marketplace.atlassian.com/apps/1812291670",
        "desc": "Connect BMC Helix ITSM with Jira Service Management for bidirectional sync of incidents, changes, and service requests. Unify IT service operations across both ITSM platforms.",
        "syncs": "Incidents, change requests, service requests, problems, tasks, comments, attachments, and custom fields",
        "use_cases": ["IT operations on BMC Helix ITSM while service teams use JSM", "Unified incident management across BMC Helix and Jira Service Management", "Cross-platform ITSM workflows bridging BMC Helix and JSM"],
    },
    {
        "slug": "zendesk-jsm",
        "name": "Zendesk and Jira Service Management Integration",
        "tool": "Zendesk",
        "url": "https://marketplace.atlassian.com/apps/3226008278",
        "desc": "Bidirectional sync between Zendesk and Jira Service Management. Connect customer support workflows with IT service management to keep both platforms aligned in real time.",
        "syncs": "Tickets, service requests, comments, attachments, custom fields, tags, and SLA data",
        "use_cases": ["Support teams on Zendesk while IT teams manage services in JSM", "Escalating Zendesk customer tickets to JSM service requests automatically", "Unified support and ITSM visibility across Zendesk and JSM"],
    },
    {
        "slug": "enterprise-architect-jsm",
        "name": "Enterprise Architect and Jira Service Management Integration",
        "tool": "Sparx Enterprise Architect",
        "url": "https://marketplace.atlassian.com/apps/2860047764",
        "desc": "Bidirectional integration between Sparx Enterprise Architect and Jira Service Management. Connect system architecture models with IT service management workflows.",
        "syncs": "EA elements, packages, diagrams, requirements, JSM service requests, comments, and custom properties",
        "use_cases": ["Systems architects modeling in EA while IT teams track services in JSM", "Linking architecture decisions to service management workflows", "MBSE teams needing visibility between design models and JSM service requests"],
    },
    {
        "slug": "salesforce-jsm",
        "name": "OpsHub Connector for Salesforce and JSM",
        "tool": "Salesforce",
        "url": "https://marketplace.atlassian.com/apps/3993596569",
        "desc": "No-code, bidirectional sync between Salesforce and Jira Service Management. Connect CRM data with IT service management to bridge customer-facing and service operations teams.",
        "syncs": "Cases, accounts, contacts, service requests, incidents, comments, attachments, and custom objects",
        "use_cases": ["Sales teams on Salesforce while IT service teams work in JSM", "Escalating Salesforce cases to JSM service requests automatically", "Unified CRM and ITSM visibility across Salesforce and JSM"],
    },
    {
        "slug": "trac-jira",
        "name": "Trac Bidirectional Integration for Jira",
        "tool": "Trac",
        "url": "https://marketplace.atlassian.com/apps/1949729264",
        "desc": "Bidirectional sync between Trac and Jira. Keep tickets, milestones, and wiki content synchronized across both project management platforms without manual duplication.",
        "syncs": "Trac tickets, Jira issues, sub-tasks, versions, work logs, comments, attachments, and history",
        "use_cases": ["Teams running Trac alongside Jira without duplicating data entry", "Gradual transition from Trac to Jira while keeping both systems active", "Open source projects on Trac collaborating with enterprise Jira teams"],
    },
    {
        "slug": "multi-instance-jira",
        "name": "Multi-Instance Sync for Jira",
        "tool": "Jira (Multi-Instance)",
        "url": "https://marketplace.atlassian.com/apps/2588044797",
        "desc": "Keep multiple Jira instances in sync with full context, reliable updates, and no scripts, eliminating manual work across teams.",
        "syncs": "Issues, comments, attachments, relationships, custom fields, work logs, and hierarchy across Jira instances",
        "use_cases": ["Enterprises with multiple Jira instances needing cross-instance visibility", "Post-acquisition Jira synchronization during consolidation", "Vendor-client Jira collaboration without sharing full instance access"],
    },
    {
        "slug": "secure-archiving-jira",
        "name": "Secure Archiving of Jira Data for Compliance and Scalability",
        "tool": "Data Archiving",
        "url": "https://marketplace.atlassian.com/apps/650669298",
        "desc": "Archive Jira data securely for compliance, scalability, and performance optimization. Preserve complete project history while keeping your active Jira instance lean and fast.",
        "syncs": "Issues, projects, comments, attachments, custom fields, changelogs, workflows, and full audit history",
        "use_cases": ["Organizations needing compliant long-term archival of Jira project data", "Improving Jira performance by archiving completed projects", "Regulated industries requiring audit-ready historical records from Jira"],
    },
]

MIGRATIONS = [
    {
        "slug": "any-tool-to-jira",
        "name": "OpsHub Migration Manager (OMM) for Jira",
        "url": "https://marketplace.atlassian.com/apps/1224539",
        "tool": "Any Tool",
        "desc": "Migrate issues, comments, attachments, links, history, and more from Azure DevOps, Rally, HP ALM, Helix, IBM DOORS, and 70+ other tools to Jira with zero downtime.",
        "syncs": "Issues, work items, test cases, requirements, comments, attachments, links, history, and custom fields from 70+ source platforms",
        "use_cases": ["Consolidating multiple legacy tools onto Jira", "Enterprise-wide migration to Jira from any ALM, DevOps, or ITSM tool", "Preserving complete project history during tool transitions"],
    },
    {
        "slug": "jira-dc-to-cloud",
        "name": "OMM for Jira DC to Cloud Migration",
        "url": "https://marketplace.atlassian.com/apps/1235636",
        "tool": "Jira Data Center",
        "desc": "Migrate Jira Data Center to Jira Cloud (including add-ons) from one or multiple instances with zero downtime and zero disruption to your teams.",
        "syncs": "Projects, issues, workflows, custom fields, users, comments, attachments, links, labels, versions, sprint data, history, and add-on data (Xray, Zephyr, JSM)",
        "use_cases": ["Organizations moving from Jira Data Center to Jira Cloud", "Consolidating multiple Jira DC instances into a single Cloud instance", "Phased migration with zero downtime and full data integrity"],
    },
    {
        "slug": "cloud-to-cloud-jira",
        "name": "Cloud to Cloud Migration for Jira",
        "url": "https://marketplace.atlassian.com/apps/2961517783",
        "tool": "Jira Cloud",
        "desc": "Migrate or consolidate Jira Cloud instances with zero downtime. Preserve comments, attachments, history, and more during Cloud-to-Cloud transitions.",
        "syncs": "Projects, issues, workflows, comments, attachments, history, custom fields, boards, and sprints",
        "use_cases": ["Consolidating multiple Jira Cloud instances after acquisitions", "Moving projects between Jira Cloud organizations", "Re-organizing Jira Cloud instances for better governance"],
    },
    {
        "slug": "bmc-remedy-to-jira",
        "name": "BMC Remedy ITSM to Jira Migration",
        "url": "https://marketplace.atlassian.com/apps/1350560408",
        "tool": "BMC Remedy ITSM",
        "desc": "Migrate BMC Remedy ITSM requests to Jira without downtime. Preserve comments, attachments, request history, and custom fields throughout the transition.",
        "syncs": "Incidents, change requests, problems, tasks, comments, attachments, work logs, and request history",
        "use_cases": ["Organizations replacing BMC Remedy with Jira Service Management", "IT departments modernizing their ITSM platform", "Preserving years of ITSM history while moving to Jira"],
    },
    {
        "slug": "redmine-to-jira",
        "name": "Redmine to Jira Migration",
        "url": "https://marketplace.atlassian.com/apps/537531440",
        "tool": "Redmine",
        "desc": "Migrate from Redmine to Jira without disruption. Preserve comments, attachments, inline images, wiki content, and complete project history during the transition.",
        "syncs": "Issues, trackers, comments, attachments, inline images, wiki pages, custom fields, and history",
        "use_cases": ["Open source teams moving from Redmine to Jira", "Organizations outgrowing Redmine and standardizing on Jira", "Preserving complete Redmine project history in Jira"],
    },
    {
        "slug": "zephyr-to-xray",
        "name": "Zephyr to Xray Migration",
        "url": "https://marketplace.atlassian.com/apps/396795523",
        "tool": "Zephyr",
        "desc": "Migrate from Zephyr to Xray without downtime. Preserve test steps, comments, attachments, relationships, test executions, and all test data during the migration.",
        "syncs": "Test cases, test steps, test cycles, test executions, comments, attachments, relationships, and folders",
        "use_cases": ["Organizations switching test management from Zephyr to Xray", "Consolidating test management on a single Jira-native platform", "Preserving complete test history when changing test tools"],
    },
    {
        "slug": "xray-dc-to-cloud",
        "name": "Xray on Jira DC to Xray on Cloud Migration",
        "url": "https://marketplace.atlassian.com/apps/1535785919",
        "tool": "Xray (Data Center)",
        "desc": "Migrate Xray test management data from Jira Data Center to Jira Cloud with zero downtime. Preserve all test cases, executions, and traceability during the transition.",
        "syncs": "Test cases, test plans, test executions, test sets, preconditions, test runs, and traceability links",
        "use_cases": ["Moving Xray test data as part of a Jira DC to Cloud migration", "Preserving test management history during cloud transitions", "Zero-downtime migration of test management infrastructure"],
    },
    {
        "slug": "zephyr-squad-dc-to-cloud",
        "name": "Zephyr Squad DC to Cloud Migration",
        "url": "https://marketplace.atlassian.com/apps/2540227454",
        "tool": "Zephyr Squad (Data Center)",
        "desc": "Migrate Zephyr Squad (now Zephyr Essential) test data from Jira Data Center to Jira Cloud with zero downtime. Preserve test cases, executions, folders, and full test history.",
        "syncs": "Test cases, test executions, test plans, folders, attachments, comments, relationships, and historical records",
        "use_cases": ["Moving Zephyr Squad test data as part of a Jira DC to Cloud migration", "Preserving complete test management history during cloud transitions", "Zero-downtime migration of Zephyr Squad test infrastructure"],
    },
    {
        "slug": "jsm-migration",
        "name": "Migration for Jira Service Management (JSM)",
        "url": "https://marketplace.atlassian.com/apps/3179316431",
        "tool": "Any ITSM Tool",
        "desc": "Zero-downtime migration to Jira Service Management from any ITSM platform. Preserve service requests, incidents, knowledge base articles, and complete service history.",
        "syncs": "Service requests, incidents, changes, problems, knowledge articles, SLAs, comments, and attachments",
        "use_cases": ["Migrating from any ITSM tool to Jira Service Management", "IT departments consolidating service desks onto JSM", "Preserving complete ITSM history during platform transitions"],
    },
    {
        "slug": "azure-devops-to-jira",
        "name": "Azure DevOps (TFS or VSTS) to Jira Migration",
        "url": "https://marketplace.atlassian.com/apps/1464584616",
        "tool": "Azure DevOps / TFS / VSTS",
        "desc": "Migrate from Azure DevOps, TFS, or VSTS to Jira with zero downtime. Preserve work items, test cases, builds, comments, attachments, and complete project history.",
        "syncs": "Work items, bugs, tasks, test cases, test plans, builds, comments, attachments, links, and history",
        "use_cases": ["Organizations moving from Azure DevOps to Jira for project management", "Consolidating TFS or VSTS data into Jira", "Preserving complete Azure DevOps project history during migration to Jira"],
    },
    {
        "slug": "fogbugz-to-jira",
        "name": "Zero Downtime FogBugz to Jira Migration",
        "url": "https://marketplace.atlassian.com/apps/257470442",
        "tool": "FogBugz",
        "desc": "Migrate from FogBugz to Jira without downtime. Preserve cases, discussions, attachments, and complete project history throughout the transition.",
        "syncs": "Cases, comments, attachments, relationships, and history",
        "use_cases": ["Teams moving from FogBugz to Jira for modern project management", "Preserving complete FogBugz case history in Jira", "Zero-disruption migration from FogBugz with incremental sync support"],
    },
    {
        "slug": "selective-migration-jira",
        "name": "Selective Migration for Jira Without Full Instance Move",
        "url": "https://marketplace.atlassian.com/apps/2936265464",
        "tool": "Jira",
        "desc": "Selectively migrate specific projects, issues, or data subsets between Jira instances without a full instance migration. Move exactly what you need with zero downtime.",
        "syncs": "Selected projects, issues, workflows, comments, attachments, custom fields, and history",
        "use_cases": ["Moving specific projects between Jira instances without full migration", "Cherry-picking data subsets for targeted Jira consolidation", "Reorganizing Jira instances by selectively migrating projects"],
    },
]

PLATFORM = [
    {
        "slug": "oim-enterprise",
        "name": "OpsHub Integration Manager (OIM) for Jira",
        "url": "https://marketplace.atlassian.com/apps/1224525",
        "tool": "70+ Systems",
        "desc": "Enterprise integration platform connecting Jira with 70+ ALM, DevOps, ITSM, and CRM tools. Bidirectional, real-time sync with no-code configuration and AI-assisted setup.",
        "syncs": "Work items, issues, requirements, test cases, defects, comments, attachments, custom fields, and relationships across 70+ tools",
        "use_cases": ["Organizations needing Jira integration with any enterprise tool", "Multi-tool environments requiring centralized data synchronization", "Enterprise-wide integration strategy with a single platform"],
    },
    {
        "slug": "oim-community",
        "name": "OpsHub Integration Manager (OIM) Community Edition",
        "url": "https://marketplace.atlassian.com/apps/1215532",
        "tool": "Multiple Systems",
        "desc": "Enterprise-grade integration for Jira with leading ALM tools at no cost. Connect Jira with ServiceNow, Azure DevOps, OpenText ALM, Digital.ai Agility, Jira Align, Rally, and Salesforce using a no-code interface.",
        "syncs": "Projects, entities, comments, attachments, inline content, and traceability data across supported tools",
        "use_cases": ["Teams wanting enterprise-grade Jira integration at no cost", "Connecting Jira with ServiceNow, Azure DevOps, Rally, Salesforce, and other supported tools", "Evaluation and proof-of-concept for enterprise integration projects"],
    },
]


def generate_integration_page(product):
    """Generate a markdown page for an integration product."""
    benefits = [
        ("Eliminate Manual Work", "Stop copying data between systems. Changes sync automatically in both directions, freeing your team to focus on what matters."),
        ("Always Accurate", f"Real-time synchronization ensures {product['tool']} and Jira always show the same information. No stale data, no conflicts."),
        ("No-Code Setup", "Configure your integration visually with an AI-assisted, drag-and-drop interface. No scripting or API knowledge needed."),
        ("Enterprise Ready", "Built for scale with support for complex field mappings, custom workflows, conditional sync rules, and full audit logging."),
    ]

    uc_text = "\n".join([f"- {uc}" for uc in product["use_cases"]])

    content = f"""# {product['name']}

**Seamlessly connect {product['tool']} and Jira with real-time, bidirectional sync.**

[![Get It Now](https://img.shields.io/badge/Get_It_Now-0052CC?style=for-the-badge&logo=atlassian&logoColor=white)]({product['url']})

{product['desc']}

## Why Integrate {product['tool']} with Jira?

| Benefit | Details |
|---------|---------|
| **{benefits[0][0]}** | {benefits[0][1]} |
| **{benefits[1][0]}** | {benefits[1][1]} |
| **{benefits[2][0]}** | {benefits[2][1]} |
| **{benefits[3][0]}** | {benefits[3][1]} |

## What Gets Synced

{product['syncs']}

{"Data flows from Jira to " + product["tool"] + " with incremental sync." if product.get("one_way") else "All data flows bidirectionally in real time."} Custom field mappings, conditional rules, and conflict resolution ensure your data stays consistent across both platforms.

## Common Use Cases

{uc_text}

## Get Started

[![See All Connectors](https://img.shields.io/badge/See_All_Connectors-2684FF?style=for-the-badge)](https://marketplace.atlassian.com/vendors/798149) &nbsp; [![Learn More](https://img.shields.io/badge/Learn_More-172B4D?style=for-the-badge)](https://www.opshub.com)

[![Built on OIM](https://img.shields.io/badge/Built_on-OpsHub_Integration_Manager-00A36C?style=flat-square)](https://www.opshub.com/products/opshub-integration-manager/) &nbsp; Trusted by leading enterprises
"""
    return content


def generate_migration_page(product):
    """Generate a markdown page for a migration product."""
    uc_text = "\n".join([f"- {uc}" for uc in product["use_cases"]])

    content = f"""# {product['name']}

**Migrate to Jira from {product['tool']} with zero downtime and complete data fidelity.**

[![Start Now](https://img.shields.io/badge/Start_Now-0052CC?style=for-the-badge&logo=atlassian&logoColor=white)]({product['url']})

{product['desc']}

## Why Choose OpsHub for This Migration?

| Benefit | Details |
|---------|---------|
| **Zero Downtime** | Your teams keep working in the source system throughout the migration. No freeze windows, no lost productivity. |
| **Complete Data Fidelity** | Every comment, attachment, link, and custom field is preserved exactly as-is. Nothing gets lost or reformatted. |
| **Incremental Sync** | Migrate in phases. Run delta syncs to capture changes made after the initial migration until you are ready to cut over. |
| **Rollback Ready** | Built-in validation and rollback capabilities ensure you can verify everything before making the switch permanent. |

## What Gets Migrated

{product['syncs']}

All data is validated before, during, and after migration to ensure complete accuracy.

## Common Use Cases

{uc_text}

## Get Started

[![See All Migrations](https://img.shields.io/badge/See_All_Migrations-2684FF?style=for-the-badge)](https://marketplace.atlassian.com/vendors/798149) &nbsp; [![Learn More](https://img.shields.io/badge/Learn_More-172B4D?style=for-the-badge)](https://www.opshub.com)

[![Built on OMM](https://img.shields.io/badge/Built_on-OpsHub_Migration_Manager-00A36C?style=flat-square)](https://www.opshub.com/products/opshub-migration-manager/) &nbsp; Trusted by leading enterprises
"""
    return content


def generate_platform_page(product):
    """Generate a markdown page for a platform product."""
    uc_text = "\n".join([f"- {uc}" for uc in product["use_cases"]])

    content = f"""# {product['name']}

**Enterprise-grade integration and migration for Jira — connect 70+ tools with no-code setup.**

[![Get It Now](https://img.shields.io/badge/Get_It_Now-0052CC?style=for-the-badge&logo=atlassian&logoColor=white)]({product['url']})

{product['desc']}

## Why OpsHub?

| Benefit | Details |
|---------|---------|
| **Broadest Connectivity** | Connects with 70+ ALM, DevOps, ITSM, CRM, and PLM tools out of the box. |
| **No-Code Configuration** | Visual, AI-assisted setup means anyone can configure integrations without writing code. |
| **Enterprise Scale** | Handles millions of records, complex field mappings, and conditional sync rules with built-in conflict resolution. |
| **Proven Reliability** | Trusted by leading enterprises for mission-critical integration and migration workloads. |

## What Gets Synced

{product['syncs']}

## Common Use Cases

{uc_text}

## Get Started

[![See All Solutions](https://img.shields.io/badge/See_All_Solutions-2684FF?style=for-the-badge)](https://marketplace.atlassian.com/vendors/798149) &nbsp; [![Learn More](https://img.shields.io/badge/Learn_More-172B4D?style=for-the-badge)](https://www.opshub.com)

[![OpsHub Inc](https://img.shields.io/badge/OpsHub,_Inc.-Enterprise_Integration_&_Migration-00A36C?style=flat-square)](https://www.opshub.com)
"""
    return content


def generate_readme(integrations, migrations, platform):
    """Generate the main README.md landing page."""
    # Build integration table rows
    int_rows = ""
    for p in sorted(integrations, key=lambda x: x["tool"]):
        int_rows += f"| [{p['tool']}](integrations/{p['slug']}.md) | {p['name']} | [Marketplace]({p['url']}) |\n"

    # Build migration table rows
    mig_rows = ""
    for p in migrations:
        mig_rows += f"| [{p['tool']}](migrations/{p['slug']}.md) | {p['name']} | [Marketplace]({p['url']}) |\n"

    # Build platform table rows
    plat_rows = ""
    for p in platform:
        plat_rows += f"| [{p['tool']}](migrations/{p['slug']}.md) | {p['name']} | [Marketplace]({p['url']}) |\n"

    content = f"""# OpsHub on Atlassian Marketplace

**Enterprise Integration and Migration Solutions for Jira**

OpsHub connects Jira with 70+ ALM, DevOps, ITSM, CRM, and PLM tools through bidirectional, real-time synchronization. Whether you need to integrate your existing tools with Jira or migrate to Jira from legacy platforms, OpsHub makes it simple with no-code configuration and zero-downtime execution.

---

## Integration Solutions

Connect Jira with any of these tools for real-time, bidirectional sync:

| Tool | Integration | Link |
|------|-------------|------|
{int_rows}
---

## Migration Solutions

Move to Jira from any platform with zero downtime:

| Source | Migration | Link |
|--------|-----------|------|
{mig_rows}
---

## Platform Products

| Product | Description | Link |
|---------|-------------|------|
{plat_rows}
---

## Why OpsHub?

- **70+ Connectors** — The broadest range of enterprise tool integrations on the market
- **Zero Downtime** — Migrations and integrations that never interrupt your teams
- **No-Code Setup** — AI-assisted configuration with drag-and-drop simplicity
- **Enterprise Scale** — Trusted by Fortune 500 companies for mission-critical workloads
- **Complete Data Fidelity** — Every comment, attachment, and custom field preserved

---

## Learn More

- **[OpsHub Website](https://www.opshub.com)** — Product details, documentation, and resources
- **[Atlassian Marketplace — OpsHub, Inc.](https://marketplace.atlassian.com/vendors/798149)** — All OpsHub listings
- **[Contact Sales](https://www.opshub.com/contact/)** — Custom requirements and enterprise pricing

---

*OpsHub, Inc. — Enterprise Integration and Migration for Jira*
"""
    return content


def main():
    base_dir = "/home/claude/opshub-marketplace"

    # Write integration pages
    for product in INTEGRATIONS:
        filepath = os.path.join(base_dir, "integrations", f"{product['slug']}.md")
        content = generate_integration_page(product)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  Created: integrations/{product['slug']}.md")

    # Write migration pages
    for product in MIGRATIONS:
        filepath = os.path.join(base_dir, "migrations", f"{product['slug']}.md")
        content = generate_migration_page(product)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  Created: migrations/{product['slug']}.md")

    # Write platform pages (in integrations folder as they're core products)
    for product in PLATFORM:
        filepath = os.path.join(base_dir, "integrations", f"{product['slug']}.md")
        content = generate_platform_page(product)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  Created: integrations/{product['slug']}.md")

    # Write README
    readme = generate_readme(INTEGRATIONS + PLATFORM, MIGRATIONS, PLATFORM)
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(readme)
    print(f"  Created: README.md")

    # Count
    total = len(INTEGRATIONS) + len(MIGRATIONS) + len(PLATFORM)
    print(f"\nTotal product pages: {total}")
    print(f"  Integrations: {len(INTEGRATIONS)}")
    print(f"  Migrations: {len(MIGRATIONS)}")
    print(f"  Platform: {len(PLATFORM)}")


if __name__ == "__main__":
    main()
