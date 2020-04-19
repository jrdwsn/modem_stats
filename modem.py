from netmiko import ConnectHandler
from ttp import ttp
from typing import Dict


class Modem:

    line_stats_cmd = "xdslctl info"
    line_stats_template = "templates/xdslctl_info.txt"

    def __init__(self, host: str, username: str, password: str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self._netmiko_device = None
        self._output = None  # for debugging

    @property
    def _netmiko_info(self) -> Dict:
        netmiko_info = {
            "device_type": "generic_termserver",
            "host": self.host,
            "username": self.username,
            "password": self.password,
        }
        return netmiko_info

    def _connect(self) -> None:
        self._netmiko_device = ConnectHandler(**self._netmiko_info)

    def _disconnect(self) -> None:
        self._netmiko_device.disconnect()
        self._netmiko_device = None

    def _send_command(self, cmd: str) -> str:
        output = self._netmiko_device.send_command(cmd)
        self._output = output  # for debugging
        return output

    @staticmethod
    def _parse_line_stats(output: str, template: str) -> Dict:
        parser = ttp(data=output, template=template)
        parser.parse()
        return parser.result(format="raw")[0]

    def get_line_stats(self) -> Dict:
        self._connect()
        output = self._send_command(self.line_stats_cmd)
        parsed = self._parse_line_stats(output, self.line_stats_template)
        self._disconnect()
        return parsed
