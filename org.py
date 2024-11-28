"""Org module."""

import locale
from datetime import datetime

from orgparse import loads

from settings import ORG_CAPTURE_FILENAME, ORG_LINKS_FILENAME, ORG_PLAN_FILENAME

locale.setlocale(locale.LC_ALL, "es_ES.utf8")


class OrgData:
    """Manage org-mode files for TODO items, plans, and links.

    Provides functionality to read and write org-mode formatted data, including
    TODOs, daily plans, and links. Handles file operations and data formatting.
    """

    def _generate_today(self):
        """Generate a formatted timestamp for today's date.

        Returns:
            str: Formatted string with date, day, and time (YYYY-MM-DD day HH:MM)
        """
        today = datetime.today()
        today_ymd = today.strftime("%Y-%m-%d")
        today_day = today.strftime("%a").lower()
        today_hour = today.strftime("%H:%M")
        return f"{today_ymd} {today_day} {today_hour}"

    def add_new_todo(self, keyword: str, description: str, outcome: str, extra: str) -> None:
        """Add a new TODO item to the capture file.

        Args:
            keyword: Category of TODO (e.g., 'TODO', 'REPEAT', 'NEXT')
            description: Title/description of the task
            outcome: Desired outcome or objective
            extra: Additional notes or context
        """
        today = self._generate_today()

        todo_template = f"""
** {keyword.upper()} {description} :NEW::BOT:
  Desired outcome: {outcome}
  :LOGBOOK:
  - Added: [{today}]
  :END:

  {extra}
"""

        with open(ORG_CAPTURE_FILENAME, "a") as capture_file:
            capture_file.write(todo_template)

    def list_plan(self, filename: str) -> str:
        """Get and format the daily plan from an org file.

        Args:
            filename: Type of plan to retrieve ('free' or 'work')

        Returns:
            str: Formatted plan with checkboxes converted to emoji markers
        """
        try:
            with open(ORG_PLAN_FILENAME.replace("{filename}", filename), "r") as agenda:
                plan = agenda.read()

            plan = loads(plan)

            return plan[-1].get_body().replace("[X]", "✅").replace("[ ]", "❌")
        except FileNotFoundError:
            return f"No plan found for {filename}."

    def add_new_link(self, link: str) -> None:
        """Add a new link to the links file.

        Args:
            link: URL to be saved
        """
        with open(ORG_LINKS_FILENAME, "a") as capture_file:
            capture_file.write(link)
