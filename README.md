# Developer Environment Setup

## Overview

This project documents the setup of a developer environment using Cursor IDE with AI coding extensions, completed as part of a portfolio project.

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

### Issue 1: Claude Code sidebar warning
**Problem:** After installing Claude Code, a warning appeared:
```
View container 'claude-sidebar-secondary' does not exist and all registered to it will be added to 'Explorer'.
```
**Solution:** This is a known Cursor compatibility issue. The Claude Code panel is automatically moved to the Explorer section of the sidebar. No action required — the extension still functions normally.

### Issue 2: PowerShell execution policy blocking `claude` command
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

### Issue 3: `codex` terminal command not found
**Problem:** Running `codex` in the terminal returned a `CommandNotFoundException` error.  
**Solution:** Codex is a UI-based extension, not a CLI tool. It is accessed through the Cursor sidebar, not the terminal.

---

## Result

Both Claude Code and Codex are successfully installed and running in Cursor IDE. Claude Code is authenticated and active on Claude Pro (Sonnet 4.6).
