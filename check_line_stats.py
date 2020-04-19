#!/usr/bin/env python3
"""
Pull line stats from VDSL modem
"""

from netmiko import ConnectHandler
from ttp import ttp
from modem import modem


def main() -> None:
    """
    Execution starts here
    """

    net_connect = ConnectHandler(
        device_type="generic_termserver",
        host=modem["host"],
        username=modem["username"],
        password=modem["password"],
    )

    xdslctl_info_output = net_connect.send_command("xdslctl info")

    net_connect.disconnect()

    parser = ttp(
        data=xdslctl_info_output, template="templates/xdslctl_info.txt"
    )
    parser.parse()
    print(parser.result(format="json")[0])


if __name__ == "__main__":
    main()
