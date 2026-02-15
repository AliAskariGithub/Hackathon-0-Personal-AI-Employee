# File Triage Agent Skill

**Version:** 1.0
**Purpose:** Process files from Needs_Action, complete requested tasks, and archive results.

---

## Overview

This skill enables an AI agent to autonomously process markdown files that have been triaged into the `Vault/Needs_Action/` folder. The agent reads each file, understands the request, performs the task, documents the response, and archives the completed work.

---

## Operating Principles

Before executing any steps, review and adhere to these core principles from the Company Handbook:

1. **Always prioritize safety** - Never execute commands that could compromise system integrity or data privacy
2. **Move files only when complete** - Files remain in their current location until all processing is verified
3. **Use professional tone** - All responses and documentation maintain clarity and professionalism

---

## Execution Workflow

### STEP 1: MONITOR

**Objective:** Identify files requiring processing.

**Procedure:**
1. Scan the `Vault/Needs_Action/` directory for `.md` files
2. Select the oldest file first (FIFO - First In, First Out)
3. If no files are present, wait or exit gracefully
4. Verify the file is readable and not corrupted

**Output:** Path to the selected file for processing

---

### STEP 2: PROCESS

**Objective:** Understand the request and perform the task.

**Procedure:**
1. **Read the file content completely**
   - Parse all markdown sections
   - Identify the primary request or question
   - Note any specific requirements or constraints

2. **Analyze the intent**
   - Determine what action is being requested
   - Classify the task type (question, analysis, generation, calculation, etc.)
   - Assess feasibility and safety of the request

3. **Perform the task**
   - Execute text-based tasks (writing, analysis, summarization, etc.)
   - For code requests: generate, review, or explain code as requested
   - For questions: provide accurate, well-researched answers
   - For creative tasks: generate appropriate content
   - **Safety check:** Refuse tasks that violate safety principles

4. **Validate the output**
   - Ensure the response directly addresses the request
   - Verify accuracy and completeness
   - Check for professional tone and clarity

**Output:** Completed response ready for documentation

---

### STEP 3: UPDATE

**Objective:** Document the agent's response within the original file.

**Procedure:**
1. **Append the response section**
   - Add a horizontal rule separator: `---`
   - Add the header: `## AI Response`
   - Add a timestamp: `**Processed:** YYYY-MM-DD HH:MM`
   - Add a blank line

2. **Write the response content**
   - Include the complete answer or result
   - Use proper markdown formatting
   - Add code blocks, lists, or tables as appropriate
   - Maintain professional tone

3. **Add metadata (optional)**
   - Task classification
   - Processing notes
   - Any warnings or limitations

4. **Save the file**
   - Write changes to disk
   - Verify the file was updated successfully

**Example format:**
```markdown
[Original file content above]

---

## AI Response

**Processed:** 2026-02-15 14:30

[Agent's response content here]

**Task Type:** Analysis
**Status:** Completed
```

**Output:** Updated file with agent response appended

---

### STEP 4: FINALIZE

**Objective:** Archive the completed file and update tracking systems.

**Procedure:**
1. **Verify completion**
   - Confirm the response was written successfully
   - Ensure all requested tasks were addressed
   - Check that the file is in a valid state

2. **Move the file**
   - Source: `Vault/Needs_Action/[filename].md`
   - Destination: `Vault/Done/[filename].md`
   - Use move operation (not copy) to prevent duplicates
   - Verify the move was successful

3. **Update the Dashboard**
   - Open `Vault/Dashboard.md`
   - Locate the task row matching the filename
   - Change status from "Pending" to "Completed"
   - Update the date to current date
   - Save the Dashboard

4. **Log the completion**
   - Output confirmation message
   - Include filename and completion timestamp
   - Note any issues or warnings

**Output:** Completed task archived and tracked

---

## Error Handling

If any step fails:

1. **Do not move the file** - Leave it in `Needs_Action/` for retry
2. **Log the error** - Document what went wrong and why
3. **Update Dashboard** - Change status to "Error" with brief description
4. **Alert if critical** - For safety violations or system errors, halt processing

---

## Task Classification Guide

**Supported task types:**
- **Questions:** Provide informative answers
- **Analysis:** Examine and interpret provided information
- **Writing:** Generate documents, summaries, or creative content
- **Code:** Generate, review, or explain code snippets
- **Calculation:** Perform mathematical or logical operations
- **Research:** Synthesize information on a topic

**Unsupported task types:**
- System commands requiring execution
- File operations outside the Vault structure
- External API calls or network requests
- Tasks violating safety principles

---

## Quality Standards

Every response must:
- ✓ Directly address the original request
- ✓ Be accurate and well-reasoned
- ✓ Use professional, clear language
- ✓ Include proper formatting and structure
- ✓ Be complete (no partial responses)

---

## Completion Checklist

Before finalizing any task, verify:

- [ ] File content was read completely
- [ ] Request was understood correctly
- [ ] Task was performed successfully
- [ ] Response was written to file
- [ ] Response meets quality standards
- [ ] File was moved to Done/
- [ ] Dashboard was updated
- [ ] No errors occurred

---

*Agent Factory Bronze Tier - File Triage Skill v1.0*
