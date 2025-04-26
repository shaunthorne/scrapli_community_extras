"""scrapli_community.dell.enterprisesonic.sonic"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.dell.enterprisesonic.async_driver import (
    default_async_on_close,
    default_async_on_open,
)
from scrapli_community.dell.enterprisesonic.sync_driver import (
    default_sync_on_close,
    default_sync_on_open,
)

DEFAULT_PRIVILEGE_LEVELS = {
    "linux": (
        PrivilegeLevel(
            pattern=r"^[\w.-]+@[\w.-]+:[\w\/~]+[#$]\s*$",
            name="linux",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\w.-]+#\s*$",
            name="exec",
            previous_priv="linux",
            deescalate="exit",
            escalate="sonic-cli",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[\w.-]+\(config(\S*)?\)#\s*$",
            name="configuration",
            previous_priv="exec",
            deescalate="exit",
            escalate="configure terminal",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}


SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "command not found",
            "Permission denied",
            "% Error:",
            "Warning: Idle timeout",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
    "variants": {},
}
