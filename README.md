# Developer Environment Setup

## Overview

This project documents the setup of a developer environment using Cursor IDE with AI coding extensions, completed as part of a technical interview assessment.

---

## Tools Installed

### 1. Git
Version control system required for local Claude Code sessions and repository management.

### 2. Claude Code (Anthropic)
- **Extension ID:** `anthropic.claude-code`
- **Version:** 2.1.181
- AI coding agent by Anthropic, integrated directly into Cursor IDE.
- Runs on Claude Sonnet 4.6 via a Claude Pro account.

### 3. Codex (OpenAI)
- **Extension ID:** `openai.chatgpt`
- **Version:** 26.609.30741
- OpenAI's coding agent for writing, reviewing, and shipping code from within the IDE.

---

## Steps Completed

1. **Installed Git** for local version control and Claude Code session support.
2. **Opened the repository in Cursor IDE.**
3. **Installed the Claude Code extension** via the Cursor Extensions panel (`Ctrl+Shift+X`), searching for `anthropic.claude-code`.
4. **Fixed PowerShell execution policy** to allow npm scripts to run (see Issues section).
5. **Launched Claude Code** successfully via the terminal using the `claude` command.
6. **Authenticated with Anthropic** — logged in with a Claude Pro account (Sonnet 4.6).
7. **Installed the Codex extension** by OpenAI via the Extensions panel.

---

## Issues Encountered & Solutions

### Issue 1: Wrong application open
**Problem:** Attempted to open the Extensions panel from the Claude desktop app instead of Cursor IDE.  
**Solution:** Closed the Claude app and opened Cursor as a separate application, then used `Ctrl+Shift+X` to access extensions.

### Issue 2: Claude Code sidebar warning
**Problem:** After installing Claude Code, a warning appeared:
```
View container 'claude-sidebar-secondary' does not exist and all registered to it will be added to 'Explorer'.
```
**Solution:** This is a known Cursor compatibility issue. The Claude Code panel is automatically moved to the Explorer section of the sidebar. No action required — the extension still functions normally.

### Issue 3: PowerShell execution policy blocking `claude` command
**Problem:** Running `claude` in the terminal returned:
```
claude : No se puede cargar el archivo ... claude.ps1 porque la ejecución de scripts está deshabilitada en este sistema.
```
This is a Windows security policy that blocks npm scripts from running in PowerShell.  
**Solution:** Ran the following command in the terminal to allow scripts for the current user:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
After this, the `claude` command launched successfully.

### Issue 4: `codex` terminal command not found
**Problem:** Running `codex` in the terminal returned a `CommandNotFoundException` error.  
**Solution:** Codex is a UI-based extension, not a CLI tool. It is accessed through the Cursor sidebar, not the terminal.

---

## Result

Both Claude Code and Codex are successfully installed and running in Cursor IDE. Claude Code is authenticated and active on Claude Pro (Sonnet 4.6).

---

# Step 2 — Research Project: LinkedIn Organic Content Strategy for B2B SaaS

## Topic

**LinkedIn Organic Content Strategy for B2B SaaS**

Chosen because LinkedIn is the highest-ROI organic channel for B2B SaaS companies, and organic content is increasingly replacing ads as the primary pipeline driver. 

## What This Research Covers

A curated collection of content from 10 practitioners who actively build and teach LinkedIn organic strategy for B2B SaaS. The goal is to extract repeatable frameworks, content formats, and distribution tactics that can be synthesized into a real playbook.

## Expert Selection Criteria

- **Practitioners first:** Every expert on this list actively runs LinkedIn content, not just writes about it
- **B2B SaaS focus:** Their work is specifically applicable to SaaS companies, not generic marketing
- **Diverse angles:** The list covers content strategy, positioning, demand gen, audience research, and growth — giving a full-stack view of what makes LinkedIn organic work

## The 10 Experts

| # | Name | Focus Area | LinkedIn |
|---|---|---|---|
| 1 | Lara Acosta | LinkedIn content creation, story-driven growth | [Profile](https://www.linkedin.com/in/laraacosta/) |
| 2 | Justin Welsh | Solopreneur systems, LinkedIn organic monetization | [Profile](https://www.linkedin.com/in/justinwelsh/) |
| 3 | Dave Gerhardt | B2B brand, demand gen, founder-led content | [Profile](https://www.linkedin.com/in/davegerhardt/) |
| 4 | Amanda Natividad | Zero-click content, B2B audience research | [Profile](https://www.linkedin.com/in/amandanat/) |
| 5 | Ross Simmonds | B2B content distribution, "create once distribute forever" | [Profile](https://www.linkedin.com/in/rosssimmonds/) |
| 6 | Megan Bowen | SaaS demand gen, dark social, pipeline from content | [Profile](https://www.linkedin.com/in/megansbowen/) |
| 7 | Anthony Pierri | SaaS positioning, LinkedIn messaging strategy | [Profile](https://www.linkedin.com/in/anthonypierri/) |
| 8 | Kyle Poyar | PLG, SaaS growth content, pricing strategy | [Profile](https://www.linkedin.com/in/kylepoyar/) |
| 9 | Diandra Escobar | Content flywheels, personal brand for SaaS leaders | [Profile](https://www.linkedin.com/in/diandraescobar/) |
| 10 | Peep Laja | B2B brand, positioning, content-led authority | [Profile](https://www.linkedin.com/in/peeplaja/) |

## Repository Structure

```
/research/
  sources.md                    # Full expert list with annotations
  /linkedin-posts/              # Recent posts organized by author
  /youtube-transcripts/         # Video transcripts organized by creator
  /other/                       # Podcast excerpts, newsletters, additional materials
```

## Status

- [x] Expert selection complete
- [ ] LinkedIn posts collected
- [ ] YouTube transcripts collected
- [ ] Additional materials gathered
