"""FastMCP application instance — single shared `mcp` object.

Tools live in :mod:`moai_imweb.tools.*` and register themselves on this instance
via ``@mcp.tool()``. :mod:`moai_imweb.server` imports the tools package to trigger
registration, then runs the server.

Keeping the instance in its own module avoids a circular import between
``server`` (runs the server) and ``tools.*`` (register tools).
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp: FastMCP = FastMCP("moai-imweb")
