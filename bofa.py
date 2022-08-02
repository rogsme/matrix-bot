#!/usr/bin/env python3

from pyexcel_ods3 import get_data

from nextcloud import NextCloudConnection
from settings import EXPENSES_FILENAME


class BofaData(NextCloudConnection):
    def get(self) -> None:
        with self.client.open(EXPENSES_FILENAME, mode="rb") as expenses:
            data = get_data(expenses)
            main_page = data.get("Main")

            headlines = main_page[0]
            amounts = main_page[1]

            formatted_data = {}

            for i in range(len(headlines)):
                formatted_data[headlines[i]] = amounts[i]

        return formatted_data
