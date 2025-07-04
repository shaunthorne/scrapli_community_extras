"""scrapli_community.orion.nos.sync_driver"""
from scrapli.driver import NetworkDriver


def default_sync_on_open(conn: NetworkDriver) -> None:
    """
    orion_esr on_open callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="terminal page-break disable")


def default_sync_on_close(conn: NetworkDriver) -> None:
    """
    orion_esr default on_close callable

    Args:
        conn: NetworkDriver object

    Returns:
        N/A

    Raises:
        N/A

    """
    # write exit directly to the transport as channel would fail to find the prompt after sending
    # the exit command!
    conn.acquire_priv(desired_priv=conn.default_desired_privilege_level)
    conn.send_command(command="terminal page-break disable")
    conn.channel.write(channel_input="exit")
    conn.channel.send_return()
