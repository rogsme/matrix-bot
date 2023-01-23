import locale
from datetime import datetime

from orgparse import loads

from settings import ORG_CAPTURE_FILENAME, ORG_LINKS_FILENAME, ORG_PLAN_FILENAME

locale.setlocale(locale.LC_ALL, "es_ES.utf8")


class OrgData():
    def _generate_today(self):
        today = datetime.today()
        today_ymd = today.strftime("%Y-%m-%d")
        today_day = today.strftime("%a").lower()
        today_hour = today.strftime("%H:%M")
        return f"{today_ymd} {today_day} {today_hour}"

    def add_new_todo(self, keyword: str, description: str, outcome: str, extra: str) -> None:

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
        with open(ORG_PLAN_FILENAME.replace("{filename}", filename), "r") as agenda:
            plan = agenda.read()

        plan = loads(plan)

        return plan[-1].get_body().replace("[X]", "✅").replace("[ ]", "❌")

    def add_new_link(self, link: str) -> None:

        with open(ORG_LINKS_FILENAME, "a") as capture_file:
            capture_file.write(link)
