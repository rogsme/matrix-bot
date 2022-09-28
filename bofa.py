#!/usr/bin/env python3

from pyexcel_ods3 import get_data

from settings import EXPENSES_FILENAME


class BofaData():
    def get(self) -> None:
        with open(EXPENSES_FILENAME, "rb") as expenses:
            data = get_data(expenses)
            main_page = data.get("Main")

            headlines = main_page[0]
            amounts = main_page[1]

            formatted_data = {}

            for i in range(len(headlines)):
                formatted_data[headlines[i]] = amounts[i]

        return formatted_data
