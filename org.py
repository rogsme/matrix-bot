import locale
import os
from datetime import datetime

from orgparse import loads

from nextcloud import NextCloudConnection
from settings import ORG_CAPTURE_FILENAME, ORG_LINKS_FILENAME, ORG_PLAN_FILENAME

locale.setlocale(locale.LC_ALL, "es_ES.utf8")


class OrgData(NextCloudConnection):
    def _generate_today(self):
        today = datetime.today()
        today_ymd = today.strftime("%Y-%m-%d")
        today_day = today.strftime("%a").lower()
        today_hour = today.strftime("%H:%M")
        return f"{today_ymd} {today_day} {today_hour}"

    def add_new_todo(self, description: str, outcome: str, extra: str) -> None:

        self.client.download_file(ORG_CAPTURE_FILENAME, "./capture.org")

        today = self._generate_today()

        todo_template = f"""
** TODO {description} :NEW::BOT:
  Desired outcome: {outcome}
  :LOGBOOK:
  - Added: [{today}]
  :END:

  {extra}

"""

        with open("./capture.org", "a") as capture_file:
            capture_file.write(todo_template)

        self.client.upload_file("./capture.org", ORG_CAPTURE_FILENAME, overwrite=True)

        os.remove("./capture.org")

    def list_plan(self, filename: str) -> str:
        with self.client.open(ORG_PLAN_FILENAME.replace("{filename}", filename), mode="r") as agenda:
            plan = agenda.read()

        plan = loads(plan)

        return plan[-1].get_body().replace("[X]", "✅").replace("[ ]", "❌")

    def add_new_link(self, link: str) -> None:

        self.client.download_file(ORG_LINKS_FILENAME, "./links.org")

        with open("./links.org", "a") as capture_file:
            capture_file.write(link)

        self.client.upload_file("./links.org", ORG_LINKS_FILENAME, overwrite=True)

        os.remove("./links.org")
