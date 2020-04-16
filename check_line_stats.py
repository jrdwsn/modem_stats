#!/usr/bin/env python3
"""
Pull line stats from VDSL modem
"""

from netmiko import ConnectHandler
from modem import modem


def main() -> None:
    """
    Execution starts here
    """

    net_connect = ConnectHandler(
        device_type="generic_termserver",
        host=modem["host"],
        username=modem["username"],
        password=modem["password"]
    )

    output = net_connect.send_command("xdslctl info")

    print(output)

    net_connect.disconnect()


if __name__ == "__main__":
    main()
