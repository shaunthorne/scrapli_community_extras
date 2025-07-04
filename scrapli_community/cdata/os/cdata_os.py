"""scrapli_community.cdata.os.cdata_os"""
from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.cdata.os.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.cdata.os.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[a-zA-Z0-9.\-_@/:]{1,63}>\s?$",
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
            pattern=r"^[a-zA-Z0-9.\-_@/:]{1,63}#\s?$",
            name="privilege_exec",
            previous_priv="exec",
            deescalate="",
            escalate="enable",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[a-zA-Z0-9.\-_@/:]{1,63}\(config[a-z0-9.\-@/:\+]{0,32}\)#\s?$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="end",
            escalate="config",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",  # generic|network
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "configuration",
        "sync_on_open": default_sync_on_open,
        "auth_telnet_login_pattern": ">>User name:",
        "auth_password_pattern": ".+pass.+:",
        "comms_return_char": '\r\n',        
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": ["Unknown command: (vtysh)", "Command incomplete."],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
