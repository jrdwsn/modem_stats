from netmiko import ConnectHandler
from ttp import ttp


class Modem:

    line_stats_cmd = "xdslctl info"
    line_stats_template = "templates/xdslctl_info.txt"

    def __init__(self, host: str, username: str, password: str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self._netmiko_device = None

    def _connect(self) -> None:
        self._netmiko_device = ConnectHandler(
            device_type="generic_termserver",
            host=self.host,
            username=self.username,
            password=self.password,
        )

    def _disconnect(self) -> None:
        self._netmiko_device.disconnect()

    def _send_command(self, cmd: str) -> str:
        output = self._netmiko_device.send_command(cmd)
        return output

    @staticmethod
    def _parse_line_stats(output: str, template: str) -> str:
        parser = ttp(data=output, template=template)
        parser.parse()
        return parser.result(format="json")[0]

    def get_line_stats(self) -> str:
        self._connect()
        output = self._send_command(self.line_stats_cmd)
        parsed_output = self._parse_line_stats(
            output, self.line_stats_template
        )
        self._disconnect()
        return parsed_output
