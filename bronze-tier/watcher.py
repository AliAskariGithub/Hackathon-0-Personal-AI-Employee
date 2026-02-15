#!/usr/bin/env python3
"""
Agent Factory Bronze Tier - File Watcher
Monitors Vault/Inbox/ for new files (.md, .txt, .docx) and processes them automatically.
"""

import os
import shutil
import time
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colorama import Fore, Back, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)


class InboxHandler(FileSystemEventHandler):
    """Handles new file events in the Inbox folder."""

    def __init__(self, inbox_path, needs_action_path, dashboard_path):
        self.inbox_path = Path(inbox_path)
        self.needs_action_path = Path(needs_action_path)
        self.dashboard_path = Path(dashboard_path)

    def on_created(self, event):
        """Called when a file is created in the watched directory."""
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        # Only process supported file types
        supported_extensions = {'.md', '.txt', '.docx'}
        if file_path.suffix.lower() not in supported_extensions:
            print(f"{Fore.YELLOW}[!] Skipped unsupported file: {file_path.name}{Style.RESET_ALL}")
            return

        # Small delay to ensure file is fully written
        time.sleep(0.1)

        try:
            self.process_file(file_path)
        except Exception as e:
            print(f"{Fore.RED}[X] Error processing {file_path.name}: {e}{Style.RESET_ALL}")

    def process_file(self, file_path):
        """Move file to Needs_Action and update Dashboard."""
        filename = file_path.name
        task_name = file_path.stem  # Filename without extension

        # Move file to Needs_Action
        destination = self.needs_action_path / filename
        shutil.move(str(file_path), str(destination))
        print(f"{Fore.GREEN}[OK] Moved: {Fore.CYAN}{filename}{Fore.GREEN} -> {Fore.MAGENTA}Needs_Action/{Style.RESET_ALL}")

        # Update Dashboard
        self.update_dashboard(task_name, filename)
        print(f"{Fore.GREEN}[OK] Updated Dashboard: {Fore.CYAN}{task_name}{Fore.GREEN} -> {Fore.YELLOW}Pending{Style.RESET_ALL}")

    def update_dashboard(self, task_name, filename):
        """Add a new row to the Dashboard task table."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Read current dashboard content
        with open(self.dashboard_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Calculate next S.NO by counting existing task rows
        import re
        existing_rows = re.findall(r'<td style="padding: 16px; text-align: center; font-weight: 700; color: #6366f1; font-size: 16px;">(\d+)</td>', content)
        next_sno = len(existing_rows) + 1

        # Determine row background (alternating)
        # Odd rows: no background, Even rows: rgba(15, 23, 42, 0.5)
        if next_sno % 2 == 0:
            row_style = 'background: rgba(15, 23, 42, 0.5); border-bottom: 1px solid rgba(99, 102, 241, 0.1);'
        else:
            row_style = 'border-bottom: 1px solid rgba(99, 102, 241, 0.1);'

        # Create new table row with Pending status (yellow/orange gradient)
        new_row = f'''    <tr style="{row_style}">
      <td style="padding: 16px; text-align: center; font-weight: 700; color: #6366f1; font-size: 16px;">{next_sno}</td>
      <td style="padding: 16px; color: #e4e6eb; font-size: 14px;">{task_name}</td>
      <td style="padding: 16px; text-align: center;">
        <span style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white; padding: 6px 16px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(245, 158, 11, 0.4);">Pending</span>
      </td>
      <td style="padding: 16px; text-align: center; color: #9ca3af; font-size: 14px;">{current_date}</td>
      <td style="padding: 16px; text-align: center; color: #9ca3af; font-size: 14px;">{current_time}</td>
      <td style="padding: 16px;"><a href="Needs_Action/{filename}" style="color: #6366f1; text-decoration: none; font-weight: 500; font-size: 14px;">📄 Needs_Action/{filename}</a></td>
    </tr>
'''

        # Insert new row before </tbody>
        content = content.replace('  </tbody>', new_row + '  </tbody>')

        # Update statistics
        content = self._update_statistics(content, total_delta=1, pending_delta=1)

        # Update last updated timestamp (if exists in footer)
        if 'Last Updated:' in content:
            content = re.sub(
                r'<p style="margin: 0; color: #[^"]+;"><strong>Last Updated:</strong> [^<]+</p>',
                f'<p style="margin: 0; color: #9ca3af;"><strong>Last Updated:</strong> {current_timestamp}</p>',
                content
            )

        # Write updated content back
        with open(self.dashboard_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def _update_statistics(self, content, total_delta=0, completed_delta=0, pending_delta=0, error_delta=0):
        """Update the statistics section in the Dashboard."""
        import re

        # Extract current statistics - updated pattern for new Dashboard format
        # Pattern: <h3 style="...font-size: 48px...">NUMBER</h3>
        total_match = re.search(
            r'<h3 style="[^"]*font-size: 48px[^"]*">(\d+)</h3>\s*<p style="[^"]*">Total Tasks</p>',
            content,
            re.DOTALL
        )
        completed_match = re.search(
            r'<h3 style="[^"]*font-size: 48px[^"]*">(\d+)</h3>\s*<p style="[^"]*">Completed</p>',
            content,
            re.DOTALL
        )
        pending_match = re.search(
            r'<h3 style="[^"]*font-size: 48px[^"]*">(\d+)</h3>\s*<p style="[^"]*">Pending</p>',
            content,
            re.DOTALL
        )
        error_match = re.search(
            r'<h3 style="[^"]*font-size: 48px[^"]*">(\d+)</h3>\s*<p style="[^"]*">Errors</p>',
            content,
            re.DOTALL
        )

        # Calculate new values
        total = int(total_match.group(1)) + total_delta if total_match else total_delta
        completed = int(completed_match.group(1)) + completed_delta if completed_match else completed_delta
        pending = int(pending_match.group(1)) + pending_delta if pending_match else pending_delta
        errors = int(error_match.group(1)) + error_delta if error_match else error_delta

        # Update statistics with new values
        # Pattern to match the number inside h3 tag before "Total Tasks"
        content = re.sub(
            r'(<h3 style="[^"]*font-size: 48px[^"]*">)\d+(</h3>\s*<p style="[^"]*">Total Tasks</p>)',
            rf'\g<1>{total}\g<2>',
            content,
            flags=re.DOTALL
        )

        # Pattern to match the number inside h3 tag before "Completed"
        content = re.sub(
            r'(<h3 style="[^"]*font-size: 48px[^"]*">)\d+(</h3>\s*<p style="[^"]*">Completed</p>)',
            rf'\g<1>{completed}\g<2>',
            content,
            flags=re.DOTALL
        )

        # Pattern to match the number inside h3 tag before "Pending"
        content = re.sub(
            r'(<h3 style="[^"]*font-size: 48px[^"]*">)\d+(</h3>\s*<p style="[^"]*">Pending</p>)',
            rf'\g<1>{pending}\g<2>',
            content,
            flags=re.DOTALL
        )

        # Pattern to match the number inside h3 tag before "Errors"
        content = re.sub(
            r'(<h3 style="[^"]*font-size: 48px[^"]*">)\d+(</h3>\s*<p style="[^"]*">Errors</p>)',
            rf'\g<1>{errors}\g<2>',
            content,
            flags=re.DOTALL
        )

        return content

    def process_existing_files(self):
        """Process files that already exist in Inbox on startup."""
        supported_extensions = {'.md', '.txt', '.docx'}
        existing_files = []

        for ext in supported_extensions:
            existing_files.extend(self.inbox_path.glob(f"*{ext}"))

        if existing_files:
            print(f"\n{Fore.CYAN}Found {len(existing_files)} existing file(s) in Inbox{Style.RESET_ALL}")
            for file_path in sorted(existing_files, key=lambda p: p.stat().st_mtime):
                try:
                    self.process_file(file_path)
                except Exception as e:
                    print(f"{Fore.RED}[X] Error processing {file_path.name}: {e}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[OK] Processed all existing files{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.CYAN}No existing files in Inbox{Style.RESET_ALL}\n")


def main():
    """Start the file watcher."""
    # Define paths
    base_path = Path(__file__).parent
    inbox_path = base_path / "Vault" / "Inbox"
    needs_action_path = base_path / "Vault" / "Needs_Action"
    dashboard_path = base_path / "Vault" / "Dashboard.md"

    # Verify paths exist
    if not inbox_path.exists():
        print(f"{Fore.RED}[X] Error: Inbox path does not exist: {inbox_path}{Style.RESET_ALL}")
        return

    if not needs_action_path.exists():
        print(f"{Fore.RED}[X] Error: Needs_Action path does not exist: {needs_action_path}{Style.RESET_ALL}")
        return

    if not dashboard_path.exists():
        print(f"{Fore.RED}[X] Error: Dashboard file does not exist: {dashboard_path}{Style.RESET_ALL}")
        return

    # Set up the observer
    event_handler = InboxHandler(inbox_path, needs_action_path, dashboard_path)
    observer = Observer()
    observer.schedule(event_handler, str(inbox_path), recursive=False)

    # Print header
    print(f"\n{Back.BLUE}{Fore.WHITE}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Back.BLUE}{Fore.WHITE}  Agent Factory Bronze Tier - File Watcher  {Style.RESET_ALL}")
    print(f"{Back.BLUE}{Fore.WHITE}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Watching: {Fore.WHITE}{inbox_path}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Supported: {Fore.WHITE}.md, .txt, .docx{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Press Ctrl+C to stop{Style.RESET_ALL}")

    # Process existing files before starting to watch
    event_handler.process_existing_files()

    # Start watching
    observer.start()
    print(f"{Fore.GREEN}Watching for new files...{Style.RESET_ALL}\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(f"\n{Fore.YELLOW}[STOP] Watcher stopped by user.{Style.RESET_ALL}")

    observer.join()


if __name__ == "__main__":
    main()
