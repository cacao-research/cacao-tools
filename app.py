"""
Cacao Tools - A collection of developer utilities built with Cacao.
Inspired by it-tools.tech
"""

import cacao as c

c.config(title="Cacao Tools", theme="dark")

# Import tool functions directly
from tools.encoders import base64_tool, url_tool, html_tool, jwt_tool
from tools.generators import uuid_tool, password_tool, lorem_tool
from tools.converters import json_yaml_tool, case_tool, number_base_tool
from tools.text import stats_tool, regex_tool
from tools.crypto import hash_tool, hmac_tool

# Tool definitions for the hub
TOOLS = {
    "Encoders": [
        {"key": "base64", "name": "Base64", "desc": "Encode and decode Base64 strings"},
        {"key": "url", "name": "URL Encoder", "desc": "Encode and decode URL components"},
        {"key": "html", "name": "HTML Entities", "desc": "Escape and unescape HTML entities"},
        {"key": "jwt", "name": "JWT Decoder", "desc": "Decode and inspect JWT tokens"},
    ],
    "Generators": [
        {"key": "uuid", "name": "UUID", "desc": "Generate unique identifiers"},
        {"key": "password", "name": "Password", "desc": "Create secure random passwords"},
        {"key": "lorem", "name": "Lorem Ipsum", "desc": "Generate placeholder text"},
    ],
    "Converters": [
        {"key": "json_yaml", "name": "JSON to YAML", "desc": "Convert between JSON and YAML"},
        {"key": "case", "name": "Case Converter", "desc": "Transform text case styles"},
        {"key": "number", "name": "Number Base", "desc": "Convert between number bases"},
    ],
    "Text": [
        {"key": "stats", "name": "Text Stats", "desc": "Analyze text and count words"},
        {"key": "regex", "name": "Regex Tester", "desc": "Test regular expressions"},
    ],
    "Crypto": [
        {"key": "hash", "name": "Hash Generator", "desc": "Generate MD5, SHA hashes"},
        {"key": "hmac", "name": "HMAC", "desc": "Create keyed-hash message codes"},
    ],
}

# Admin layout with sidebar navigation
with c.app_shell(brand="Cacao Tools", default="home"):
    # Navigation sidebar
    with c.nav_sidebar():
        c.nav_item("Home", key="home", icon="home")
        c.spacer(2)

        with c.nav_group("Encoders", icon="code", default_open=True):
            c.nav_item("Base64", key="base64")
            c.nav_item("URL", key="url")
            c.nav_item("HTML Entities", key="html")
            c.nav_item("JWT Decoder", key="jwt")

        with c.nav_group("Generators", icon="dice"):
            c.nav_item("UUID", key="uuid")
            c.nav_item("Password", key="password")
            c.nav_item("Lorem Ipsum", key="lorem")

        with c.nav_group("Converters", icon="shuffle"):
            c.nav_item("JSON to YAML", key="json_yaml")
            c.nav_item("Case Converter", key="case")
            c.nav_item("Number Base", key="number")

        with c.nav_group("Text", icon="text"):
            c.nav_item("Statistics", key="stats")
            c.nav_item("Regex Tester", key="regex")

        with c.nav_group("Crypto", icon="lock"):
            c.nav_item("Hash Generator", key="hash")
            c.nav_item("HMAC", key="hmac")

    # Main content area with panels for each tool
    with c.shell_content():
        # Home / Hub page
        with c.nav_panel("home"):
            c.spacer(2)

            # Hero CTA Card
            with c.card():
                with c.row(gap=4, align="center"):
                    with c.col(span=8):
                        c.title("Cacao Tools", level=1)
                        c.text("A collection of handy utilities for developers. Fast, free, and works completely offline.", size="lg")
                        c.spacer(3)
                        with c.row(gap=2):
                            c.button("Star on GitHub", on_click="link:https://github.com/cacao-research/cacao-tools", variant="primary")
                            c.button("Built with Cacao", on_click="link:https://github.com/cacao-research/Cacao", variant="outline")
                    with c.col(span=4):
                        # Stats
                        with c.row(gap=4, justify="center"):
                            c.metric("Tools", "14")
                            c.metric("Categories", "5")

            c.spacer(6)

            # Tool cards by category
            for category, tools in TOOLS.items():
                c.text(category, size="lg", color="muted")
                c.spacer(2)
                with c.row(gap=4):
                    for tool in tools:
                        with c.col(span=4):
                            with c.card():
                                c.title(tool["name"], level=4)
                                c.text(tool["desc"], size="sm", color="muted")
                                c.spacer(2)
                                c.button("Open", on_click=f"nav:{tool['key']}", variant="outline", size="sm")
                c.spacer(4)
        # Encoders
        with c.nav_panel("base64"):
            c.title("Base64 Encoder/Decoder", level=2)
            base64_tool()

        with c.nav_panel("url"):
            c.title("URL Encoder/Decoder", level=2)
            url_tool()

        with c.nav_panel("html"):
            c.title("HTML Entity Encoder/Decoder", level=2)
            html_tool()

        with c.nav_panel("jwt"):
            c.title("JWT Decoder", level=2)
            jwt_tool()

        # Generators
        with c.nav_panel("uuid"):
            c.title("UUID Generator", level=2)
            uuid_tool()

        with c.nav_panel("password"):
            c.title("Password Generator", level=2)
            password_tool()

        with c.nav_panel("lorem"):
            c.title("Lorem Ipsum Generator", level=2)
            lorem_tool()

        # Converters
        with c.nav_panel("json_yaml"):
            c.title("JSON to YAML Converter", level=2)
            json_yaml_tool()

        with c.nav_panel("case"):
            c.title("Case Converter", level=2)
            case_tool()

        with c.nav_panel("number"):
            c.title("Number Base Converter", level=2)
            number_base_tool()

        # Text
        with c.nav_panel("stats"):
            c.title("Text Statistics", level=2)
            stats_tool()

        with c.nav_panel("regex"):
            c.title("Regex Tester", level=2)
            regex_tool()

        # Crypto
        with c.nav_panel("hash"):
            c.title("Hash Generator", level=2)
            hash_tool()

        with c.nav_panel("hmac"):
            c.title("HMAC Generator", level=2)
            hmac_tool()
