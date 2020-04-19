#!/usr/bin/env python3
"""
Pull line stats from VDSL modem
"""

from modem_info import modem_info
from modem import Modem
import json


def main() -> None:
    """
    Execution starts here
    """

    vdsl_modem = Modem(
        host=modem_info["host"],
        username=modem_info["username"],
        password=modem_info["password"],
    )
    line_stats = vdsl_modem.get_line_stats()
    print(json.dumps(line_stats, indent=2))


if __name__ == "__main__":
    main()
