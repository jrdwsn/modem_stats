#!/usr/bin/env python3
"""
Pull line stats from VDSL modem
"""

from modem_info import modem_info
from modem import Modem


def main() -> None:
    """
    Execution starts here
    """

    vdsl_modem = Modem(
        modem_info["host"], modem_info["username"], modem_info["password"]
    )
    line_stats = vdsl_modem.get_line_stats()
    print(line_stats)


if __name__ == "__main__":
    main()
