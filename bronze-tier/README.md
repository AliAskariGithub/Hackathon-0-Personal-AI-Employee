# Agent Factory - Bronze Tier

An AI-powered agent system for automated file triage and task management with enhanced visual tracking.

## Project Overview

The Agent Factory Bronze Tier is a foundational implementation of an autonomous agent system designed to process, categorize, and manage files and tasks through a structured workflow. It features real-time AI processing via Groq API, multi-format file support, and a rich HTML/CSS Dashboard for comprehensive task tracking.

## Folder Structure

```
bronze-tier/
├── DOCS/                   # Comprehensive documentation
│   ├── README.md          # Documentation index
│   ├── ABOUT.md           # Complete system overview
│   ├── GROQ_INTEGRATION.md # AI integration guide
│   ├── QUICK_REFERENCE.md  # Quick start guide
│   ├── CHANGELOG.md        # Version history
│   ├── INTEGRATION_SUMMARY.md # Technical details
│   └── PROJECT_STATUS.md   # Current state
├── History/                # Development history
│   └── PHR_Session_2026-02-15.md # Prompt history record
├── Vault/
│   ├── Inbox/          # New items awaiting triage
│   ├── Needs_Action/   # Items requiring processing
│   ├── Done/           # Completed items
│   ├── Dashboard.md    # Task tracking and status overview
│   └── Company_Handbook.md  # Operating rules and guidelines
├── skills/
│   └── file-triage/
│       └── SKILL.md    # Agent instruction manual
├── Test_Scripts/       # Testing and validation scripts
│   └── test_workflow.py
├── .venv/              # UV virtual environment (auto-generated)
├── watcher.py          # Automated file monitoring script
├── agent.py            # File triage agent (processes tasks)
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Dependency lock file
├── .python-version     # Python version specification (3.13.2)
├── .env.example        # Environment configuration template
├── .env                # Your API keys (create from .env.example)
└── README.md           # This file
```

## Setup Instructions

### Prerequisites

This project uses [UV](https://docs.astral.sh/uv/) for Python package and environment management.

1. **Install UV** (if not already installed):
   ```bash
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### Project Setup

1. **Initialize the project**: All directories are pre-created and ready to use.

2. **Install dependencies**: UV will automatically use Python 3.13.2 and install required packages.
   ```bash
   uv sync
   ```

   This will:
   - Install Python 3.13.2 (if not already available)
   - Create a virtual environment in `.venv/`
   - Install all dependencies (watchdog, groq, python-docx, python-dotenv)

3. **Configure Groq API** (for real AI responses):
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env and add your Groq API key
   # Get a free API key at: https://console.groq.com/
   ```

   Edit `.env` file:
   ```bash
   GROQ_API_KEY=your_actual_groq_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   MAX_TOKENS=2048
   TEMPERATURE=0.7
   ```

   **Note**: Without a Groq API key, the agent will run in simulation mode with placeholder responses.

4. **Review the Company Handbook**: Familiarize yourself with the core operating rules in `Vault/Company_Handbook.md`.

4. **Monitor the Dashboard**: Track task progress using `Vault/Dashboard.md`.

## Usage

### Running the File Watcher

Start the automated file monitoring system:

```bash
uv run python watcher.py
```

The watcher will:
- Monitor `Vault/Inbox/` for new files (`.md`, `.txt`, `.docx`)
- Process existing files on startup (not just new ones)
- Automatically move them to `Vault/Needs_Action/`
- Update `Vault/Dashboard.md` with task entries (S.NO, Pending status, timestamp, link)
- Update Dashboard statistics (increment Total Tasks and Pending)
- Display colorful real-time processing notifications

Press `Ctrl+C` to stop the watcher.

### Running the File Triage Agent

Start the agent to process files in `Needs_Action/`:

```bash
# Continuous mode (checks every 5 seconds)
uv run python agent.py

# Process one file and exit
uv run python agent.py --once

# Custom check interval (e.g., every 10 seconds)
uv run python agent.py --interval 10
```

The agent will:
- Monitor `Vault/Needs_Action/` for files to process (`.md`, `.txt`, `.docx`)
- Read and analyze each file's content
- Classify task type (Question, Analysis, Writing, Code, Calculation, General)
- Generate AI responses using Groq API (or simulation mode)
- Append responses to the original files with timestamps
- Move completed files to `Vault/Done/`
- Update Dashboard status to "Completed" with completion time and Done/ link
- Update Dashboard statistics (decrement Pending, increment Completed)

Press `Ctrl+C` to stop the agent.

### Complete Automated Workflow

Run both systems together for full automation:

**Terminal 1 - File Watcher:**
```bash
uv run python watcher.py
```

**Terminal 2 - Processing Agent:**
```bash
uv run python agent.py
```

Now the system will:
1. Watch for new files (`.md`, `.txt`, `.docx`) in `Inbox/`
2. Move them to `Needs_Action/` and log to Dashboard with Pending status
3. Add task entry with S.NO, timestamp, and Needs_Action/ link
4. Process each file and generate AI responses via Groq API
5. Append AI responses to original files with timestamps
6. Archive completed files to `Done/`
7. Update Dashboard with Completed status, completion time, and Done/ link
8. Update statistics (Total Tasks, Completed, Pending counts)

### Viewing the Enhanced Dashboard

The Dashboard provides a comprehensive visual overview of all tasks:

```bash
# View in terminal (basic)
cat Vault/Dashboard.md

# View in browser (recommended for full styling)
# Open Vault/Dashboard.md in any web browser to see:
# - Gradient backgrounds and modern dark theme
# - Color-coded status badges with shadows
# - Clickable file links
# - Real-time statistics with gradient cards
# - Professional table layout with alternating rows
```

**Dashboard Features:**
- Serial numbers for easy task reference
- Precise timestamps (date and time separately)
- Direct links to files in Needs_Action/ or Done/
- Statistics cards showing Total, Completed, Pending, Errors
- Status legend with color-coded badges
- Last updated timestamp in footer
- System operational status indicator

### Manual Workflow

1. Place new files (`.md`, `.txt`, `.docx`) in `Vault/Inbox/`
2. The watcher detects and moves items to `Vault/Needs_Action/`
3. Dashboard updated with Pending status, S.NO, timestamp, and link
4. The agent processes files and generates AI responses
5. Responses appended to original files with timestamps
6. Completed items are archived in `Vault/Done/`
7. Dashboard updated with Completed status, completion time, and Done/ link
8. Track all activity via the enhanced Dashboard with real-time statistics

## Core Principles

- **Safety First**: All operations prioritize security and data integrity
- **Structured Workflow**: Clear progression from Inbox → Needs_Action → Done
- **Professional Standards**: Maintain quality and clarity in all operations

---

*Agent Factory Bronze Tier - Version 3.0 - Enhanced Dashboard Edition*
*Initialized: 2026-02-15 | Last Updated: 2026-02-15*

## Project Statistics

- **Version**: 3.0.0 (Enhanced Dashboard)
- **Total Tasks Processed**: 11 (as of 2026-02-15)
- **Success Rate**: 100%
- **Supported File Formats**: 3 (.md, .txt, .docx)
- **Total Lines of Code**: ~737 lines
  - agent.py: 514 lines
  - watcher.py: 223 lines
- **Dependencies**: 5 packages (watchdog, groq, python-docx, python-dotenv, colorama)
- **Python Version**: 3.13.2 (managed by UV)
- **Documentation Files**: 5 comprehensive guides in DOCS/

## Features

### Enhanced Dashboard (v3.0)
- **Modern Dark Theme**: Professional dark UI with gradient backgrounds and enhanced visual hierarchy
- **Serial Numbers (S.NO)**: Automatic sequential numbering for all tasks (1, 2, 3...)
- **Precise Timestamps**: Separate Date and Time columns for detailed tracking (YYYY-MM-DD HH:MM:SS)
- **Clickable File Links**: Direct links to file locations in Needs_Action/ or Done/ folders
- **Real-Time Statistics**: Dynamic counters with gradient cards showing:
  - Total Tasks (all-time count)
  - Completed (successfully processed)
  - Pending (awaiting processing)
  - Errors (failed tasks)
- **Status Badges**: Color-coded pills with gradients and shadows
  - Green gradient: Completed
  - Yellow gradient: Pending
  - Red gradient: Error
  - Blue gradient: Processing
- **Status Legend**: Visual guide for all task statuses
- **Auto-Updates**: Dashboard automatically updates as tasks move through the workflow
- **Alternating Row Colors**: Enhanced readability with alternating background colors
- **Last Updated Timestamp**: Footer shows when Dashboard was last modified
- **System Status Indicator**: Shows operational status in footer

### AI-Powered Processing
- **Groq API Integration**: Real AI responses using Llama 3.3 70B model
- **Intelligent Task Classification**: Automatically categorizes requests (Question, Analysis, Writing, Code, Calculation, General)
- **Fallback Mode**: Runs in simulation mode if API key is not configured
- **Customizable Parameters**: Adjust model, temperature, and max tokens via .env

### Multi-Format Support
- **Markdown (.md)**: Full support with preserved formatting
- **Plain Text (.txt)**: Simple text file processing
- **Word Documents (.docx)**: Read and write Microsoft Word files with paragraph-based processing
- **Extensible**: Easy to add support for more formats (PDF, CSV, etc.)

### Automated Workflow
- **File Watching**: Real-time monitoring of Inbox folder with existing file detection on startup
- **FIFO Processing**: First-in, first-out task queue
- **Enhanced Status Tracking**: Dashboard updates with detailed task progress, timestamps, and file links
- **Error Handling**: Graceful fallback and error reporting with status tracking
- **Colorful CLI Output**: Color-coded terminal messages for better visibility
  - Green: Success operations
  - Yellow: Warnings and pending states
  - Red: Errors and failures
  - Blue: Information and headers
  - Cyan: File names and paths
  - Magenta: Folder names

### Developer-Friendly
- **UV Package Manager**: Fast, modern Python dependency management
- **Python 3.13.2**: Latest Python features and performance
- **Environment Variables**: Secure API key management via .env files
- **Modular Design**: Easy to extend and customize
- **Comprehensive Documentation**: 5 documentation files in DOCS/ folder
- **Test Scripts**: Validation scripts in Test_Scripts/ folder
- **Code Metrics**: ~737 lines of Python code (agent.py: 514 lines, watcher.py: 223 lines)


## Documentation

Comprehensive documentation is available in the `DOCS/` folder:

- **[DOCS/README.md](DOCS/README.md)** - Documentation index and navigation
- **[DOCS/ABOUT.md](DOCS/ABOUT.md)** - Complete system overview and architecture (14KB)
- **[DOCS/QUICK_REFERENCE.md](DOCS/QUICK_REFERENCE.md)** - Quick start guide and command reference
- **[DOCS/PROJECT_STATUS.md](DOCS/PROJECT_STATUS.md)** - Current system state and capabilities
- **[DOCS/CHANGELOG.md](DOCS/CHANGELOG.md)** - Version history and changes

## Development History

Complete development history is available in the `History/` folder:

- **[History/PHR_Session_2026-02-15.md](History/PHR_Session_2026-02-15.md)** - Prompt History Record of entire development session

## Version History

### v3.0.0 (2026-02-15) - Enhanced Dashboard Edition
- **Added**: Modern dark theme Dashboard with HTML/CSS styling
- **Added**: Serial numbers (S.NO) for all tasks
- **Added**: Separate Date and Time columns for precise tracking
- **Added**: Clickable file links to Needs_Action/ and Done/ folders
- **Added**: Real-time statistics with gradient cards (Total, Completed, Pending, Errors)
- **Added**: Color-coded status badges with gradients and shadows
- **Added**: Status legend and system status indicator
- **Added**: Alternating row colors for better readability
- **Added**: Last updated timestamp in footer
- **Changed**: Updated watcher.py to maintain enhanced Dashboard format (223 lines)
- **Changed**: Updated agent.py to maintain enhanced Dashboard format (514 lines)
- **Changed**: Dashboard now updates dynamically with statistics

### v2.0.0 (2026-02-15) - Groq API Integration & Multi-Format Support
- **Added**: Groq API integration with Llama 3.3 70B model
- **Added**: Multi-format support (.md, .txt, .docx)
- **Added**: Colorful CLI output with colorama
- **Added**: Existing file detection on watcher startup
- **Added**: Comprehensive documentation in DOCS/ folder
- **Changed**: Enhanced agent.py with AI processing (430 lines → 514 lines)
- **Changed**: Enhanced watcher.py with multi-format support

### v1.0.0 (2026-02-15) - UV Migration
- **Added**: UV package manager integration
- **Added**: Python 3.13.2 version lock
- **Added**: pyproject.toml and uv.lock
- **Fixed**: Unicode encoding issues

### v0.1.0 (2026-02-15) - Initial Release
- **Added**: File watcher and processing agent
- **Added**: Vault folder structure
- **Added**: Dashboard and Company Handbook
- **Added**: SKILL.md agent instruction manual

## Contributing

To extend the Bronze Tier system:

1. **Add New File Formats**: Extend `read_file_content()` and `_update_*()` methods in agent.py
2. **Add New Skills**: Create new skill folders in `skills/` with SKILL.md instructions
3. **Enhance Dashboard**: Modify Dashboard update methods in watcher.py and agent.py
4. **Add New AI Models**: Update .env with different Groq models
5. **Improve Error Handling**: Enhance error tracking in Dashboard statistics

## Support & Resources

- **Groq Console**: https://console.groq.com/ (Get API keys)
- **Groq Documentation**: https://console.groq.com/docs (API reference)
- **UV Documentation**: https://docs.astral.sh/uv/ (Package manager)
- **Python-docx**: https://python-docx.readthedocs.io/ (Word document library)
- **Watchdog**: https://python-watchdog.readthedocs.io/ (File system monitoring)

## License

This project is part of the Agent Factory initiative.

---

**Agent Factory Bronze Tier v3.0.0**
*Enhanced Dashboard Edition - Production Ready*
*Last Updated: 2026-02-15*