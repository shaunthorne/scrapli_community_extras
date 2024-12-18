"""scrapli_community.dlink.os.dlink_os"""
from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.dlink.os.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.dlink.os.sync_driver import default_sync_on_close, default_sync_on_open
from scrapli.channel.base_channel import ANSI_ESCAPE_PATTERN as ANS
DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^(\s{22,24})?[a-z0-9.\-_@()/:]{1,63}:(user|oper|puser|3|6)#\s*$",
            name="exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^(\s{22,24})?[a-z0-9.\-_@/:]{1,63}(:(admin|4|5))?\s*#\s*$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="",
            escalate="enable admin",
            escalate_auth=True,
            escalate_prompt=r"^[pP]ass[wW]ord:$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^(\s{22,24})?[a-z0-9.\-_@/:]{1,63}:(admin|4|5)#\s*$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Next possible completions:",
            "Available commands:",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
