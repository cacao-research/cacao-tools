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

# Admin layout with sidebar navigation
with c.app_shell(brand="Cacao Tools", default="base64"):
    # Navigation sidebar
    with c.nav_sidebar():
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
