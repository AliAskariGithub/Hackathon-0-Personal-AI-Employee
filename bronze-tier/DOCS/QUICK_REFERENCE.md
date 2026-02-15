# Quick Reference Guide

## Bronze Tier Agent Factory v3.0.0

### System Overview
AI-powered file triage system with Groq API integration, multi-format support, and enhanced HTML/CSS Dashboard with real-time statistics.

---

## Getting Started

### 1. Setup (One-time)
```bash
# Install dependencies
uv sync

# Configure Groq API
cp .env.example .env
# Edit .env: GROQ_API_KEY=your_key_here
```

### 2. Run the System
```bash
# Terminal 1: File Watcher
uv run python watcher.py

# Terminal 2: Processing Agent
uv run python agent.py
```

### 3. View Enhanced Dashboard
```bash
# View in terminal (basic)
cat Vault/Dashboard.md

# View in browser (recommended for full styling)
# Open Vault/Dashboard.md in any web browser to see:
# - Modern dark theme with gradients
# - Color-coded status badges
# - Real-time statistics cards
# - Clickable file links
# - Serial numbers and timestamps
```

### 4. Create Tasks
```bash
# Markdown file
echo "# Task\n\nPlease analyze..." > Vault/Inbox/task.md

# Text file
echo "What is Python?" > Vault/Inbox/question.txt

# Word document (via Python)
uv run python -c "from docx import Document; doc = Document(); doc.add_paragraph('Request here'); doc.save('Vault/Inbox/task.docx')"
```

---

## Enhanced Dashboard Features (v3.0)

### Visual Features
- **Modern Dark Theme**: Professional UI with gradient backgrounds
- **Serial Numbers**: Automatic S.NO for all tasks (1, 2, 3...)
- **Precise Timestamps**: Separate Date (YYYY-MM-DD) and Time (HH:MM:SS) columns
- **Clickable Links**: Direct links to files in Needs_Action/ or Done/
- **Status Badges**: Color-coded pills with gradients
  - Green: Completed
  - Yellow: Pending
  - Red: Error
  - Blue: Processing

### Statistics Cards
- **Total Tasks**: All-time task count (purple gradient)
- **Completed**: Successfully processed tasks (green gradient)
- **Pending**: Tasks awaiting processing (yellow gradient)
- **Errors**: Failed tasks (red gradient)

### Additional Features
- Status legend with all badge types
- Last updated timestamp in footer
- System operational status indicator
- Alternating row colors for readability

---

## Supported File Formats

| Format | Extension | Use Case | Processing |
|--------|-----------|----------|------------|
| Markdown | .md | Documentation, formatted requests | Preserves formatting |
| Plain Text | .txt | Simple questions, notes | Basic text processing |
| Word Doc | .docx | Formal documents, reports | Paragraph-based |

---

## Configuration Options

### .env File
```bash
# Required
GROQ_API_KEY=your_api_key_here

# Optional (with defaults)
GROQ_MODEL=llama-3.3-70b-versatile
MAX_TOKENS=2048
TEMPERATURE=0.7
```

### Available Models
- `llama-3.3-70b-versatile` - Best balance (default)
- `llama-3.1-70b-versatile` - Alternative
- `mixtral-8x7b-32768` - Longer context
- `gemma2-9b-it` - Faster, smaller

### Parameter Tuning
- **MAX_TOKENS**: 512-8192 (response length)
- **TEMPERATURE**: 0.0-1.0 (creativity)
  - 0.0 = Focused, deterministic
  - 0.7 = Balanced (default)
  - 1.0 = Creative, varied

---

## Common Commands

### Check Status
```bash
# View enhanced Dashboard (terminal)
cat Vault/Dashboard.md

# View Dashboard in browser (recommended)
# Open Vault/Dashboard.md in Chrome/Firefox/Edge

# List completed tasks
ls -la Vault/Done/

# View a completed task
cat Vault/Done/task-name.md

# Check statistics
grep -A 2 "font-size: 36px" Vault/Dashboard.md
```

### Process Single File
```bash
# Process one file and exit
uv run python agent.py --once
```

### Custom Check Interval
```bash
# Check every 10 seconds instead of 5
uv run python agent.py --interval 10
```

---

## Workflow

1. **Create** → Place file in `Vault/Inbox/`
2. **Watch** → Watcher detects and moves to `Vault/Needs_Action/`
3. **Track** → Dashboard updated with Pending status, S.NO, timestamp, link
4. **Statistics** → Total Tasks and Pending counters increment
5. **Process** → Agent reads file and calls Groq API
6. **Classify** → Task type identified (Question, Analysis, Writing, Code, Calculation, General)
7. **Respond** → AI response appended to file with timestamp
8. **Archive** → File moved to `Vault/Done/`
9. **Complete** → Dashboard updated to Completed with completion time and Done/ link
10. **Statistics** → Pending decrements, Completed increments

---

## Troubleshooting

### "GROQ_API_KEY not found"
**Fix:** Create `.env` file from `.env.example` and add your API key

### "API call failed"
**Fix:** Check API key, internet connection, or Groq API status
**Note:** Agent will fallback to simulation mode

### File not processing
**Fix:**
- Verify file extension (.md, .txt, or .docx)
- Check file is in correct folder
- Ensure agent is running
- Check terminal for errors

### Dashboard not showing colors
**Fix:** Open Dashboard.md in a web browser (Chrome, Firefox, Edge) instead of text editor

### Response too short/long
**Fix:** Adjust `MAX_TOKENS` in `.env`

### Response too creative/boring
**Fix:** Adjust `TEMPERATURE` in `.env`

### Statistics not updating
**Fix:** Check that both watcher.py and agent.py are using the latest version (v3.0)

---

## File Locations

```
Vault/
├── Inbox/          # Place new tasks here
├── Needs_Action/   # Files being processed
├── Done/           # Completed tasks
└── Dashboard.md    # Enhanced tracking (view in browser)
```

---

## Documentation

- **README.md** - Main documentation (comprehensively updated)
- **DOCS/ABOUT.md** - Complete system overview (14KB)
- **DOCS/QUICK_REFERENCE.md** - This file
- **DOCS/PROJECT_STATUS.md** - Current system state
- **DOCS/CHANGELOG.md** - Version history
- **History/PHR_Session_2026-02-15.md** - Complete development history

---

## Get Help

- Groq Console: https://console.groq.com/
- Groq Docs: https://console.groq.com/docs
- UV Docs: https://docs.astral.sh/uv/
- Python-docx: https://python-docx.readthedocs.io/
- Watchdog: https://python-watchdog.readthedocs.io/

---

## Tips

1. **View Dashboard in Browser**: For full visual experience with gradients and colors
2. **Batch Processing**: Drop multiple files in Inbox for sequential processing
3. **Model Selection**: Use smaller models for faster responses
4. **Token Limits**: Reduce MAX_TOKENS for quicker processing
5. **File Size**: Keep requests concise for better AI responses
6. **Testing**: Use simulation mode (no API key) for testing workflow
7. **Statistics**: Check Dashboard statistics to monitor system performance
8. **File Links**: Click links in Dashboard (browser view) to quickly access files

---

## Version Information

**Version:** 3.0.0 (Enhanced Dashboard Edition)
**Status:** Production Ready
**Last Updated:** 2026-02-15
**Key Features:** Modern dark theme, S.NO, timestamps, file links, real-time statistics
