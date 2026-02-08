"""Encoder/Decoder tools."""

import base64
import urllib.parse
import html
import json
import cacao as c


def render_all():
    """Render all encoder tools."""
    with c.tabs():
        with c.tab("base64", "Base64"):
            base64_tool()
        with c.tab("url", "URL"):
            url_tool()
        with c.tab("html", "HTML"):
            html_tool()
        with c.tab("jwt", "JWT"):
            jwt_tool()


def base64_tool():
    """Base64 encoder/decoder."""
    output = c.signal("", name="base64_out")
    mode = c.signal("encode", name="base64_mode")

    @c.on("base64_process")
    async def process(session, event):
        text = event.get("value", "")
        current_mode = mode.get(session)
        if not text:
            output.set(session, "")
            return
        try:
            if current_mode == "encode":
                result = base64.b64encode(text.encode()).decode()
            else:
                result = base64.b64decode(text.encode()).decode()
            output.set(session, result)
        except Exception as e:
            output.set(session, f"Error: {str(e)}")

    @c.on("base64_encode")
    async def set_encode(session, event):
        mode.set(session, "encode")

    @c.on("base64_decode")
    async def set_decode(session, event):
        mode.set(session, "decode")

    with c.card():
        c.text("Encode and decode text using Base64 encoding.", color="muted")
        c.spacer()

        # Mode toggle
        with c.row(justify="start"):
            c.button("Encode", on_click="base64_encode", variant="primary")
            c.button("Decode", on_click="base64_decode", variant="outline")

        c.spacer()

        # Side by side layout
        with c.row():
            with c.col(span=6):
                c.textarea(label="Input", placeholder="Enter text to encode/decode...", rows=6, on_change="base64_process")

            with c.col(span=6):
                c.text("Output", size="sm", color="muted")
                c.code(output)


def url_tool():
    """URL encoder/decoder."""
    output = c.signal("", name="url_out")
    mode = c.signal("encode", name="url_mode")

    @c.on("url_process")
    async def process(session, event):
        text = event.get("value", "")
        current_mode = mode.get(session)
        if not text:
            output.set(session, "")
            return
        try:
            if current_mode == "encode":
                result = urllib.parse.quote(text, safe="")
            else:
                result = urllib.parse.unquote(text)
            output.set(session, result)
        except Exception as e:
            output.set(session, f"Error: {str(e)}")

    @c.on("url_encode")
    async def set_encode(session, event):
        mode.set(session, "encode")

    @c.on("url_decode")
    async def set_decode(session, event):
        mode.set(session, "decode")

    with c.card():
        c.text("Encode and decode URLs for safe transmission.", color="muted")
        c.spacer()

        with c.row(justify="start"):
            c.button("Encode", on_click="url_encode", variant="primary")
            c.button("Decode", on_click="url_decode", variant="outline")

        c.spacer()

        with c.row():
            with c.col(span=6):
                c.textarea(label="Input", placeholder="Enter URL to encode/decode...", rows=6, on_change="url_process")

            with c.col(span=6):
                c.text("Output", size="sm", color="muted")
                c.code(output)


def html_tool():
    """HTML entity encoder/decoder."""
    output = c.signal("", name="html_out")
    mode = c.signal("encode", name="html_mode")

    @c.on("html_process")
    async def process(session, event):
        text = event.get("value", "")
        current_mode = mode.get(session)
        if not text:
            output.set(session, "")
            return
        try:
            if current_mode == "encode":
                result = html.escape(text)
            else:
                result = html.unescape(text)
            output.set(session, result)
        except Exception as e:
            output.set(session, f"Error: {str(e)}")

    @c.on("html_encode")
    async def set_encode(session, event):
        mode.set(session, "encode")

    @c.on("html_decode")
    async def set_decode(session, event):
        mode.set(session, "decode")

    with c.card():
        c.text("Encode and decode HTML entities.", color="muted")
        c.spacer()

        with c.row(justify="start"):
            c.button("Encode", on_click="html_encode", variant="primary")
            c.button("Decode", on_click="html_decode", variant="outline")

        c.spacer()

        with c.row():
            with c.col(span=6):
                c.textarea(label="Input", placeholder="Enter HTML to encode/decode...", rows=6, on_change="html_process")

            with c.col(span=6):
                c.text("Output", size="sm", color="muted")
                c.code(output)


def jwt_tool():
    """JWT decoder."""
    header_out = c.signal("{}", name="jwt_header")
    payload_out = c.signal("{}", name="jwt_payload")

    @c.on("jwt_decode")
    async def decode_jwt(session, event):
        token = event.get("value", "").strip()
        if not token:
            header_out.set(session, "{}")
            payload_out.set(session, "{}")
            return

        try:
            parts = token.split(".")
            if len(parts) != 3:
                raise ValueError("Invalid JWT format - expected 3 parts")

            # Decode header
            header_b64 = parts[0] + "=" * (-len(parts[0]) % 4)
            header = json.loads(base64.urlsafe_b64decode(header_b64))
            header_out.set(session, json.dumps(header, indent=2))

            # Decode payload
            payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
            payload = json.loads(base64.urlsafe_b64decode(payload_b64))
            payload_out.set(session, json.dumps(payload, indent=2))
        except Exception as e:
            header_out.set(session, f"Error: {str(e)}")
            payload_out.set(session, "")

    with c.card():
        c.text("Decode JWT tokens to view header and payload.", color="muted")
        c.spacer()

        c.textarea(label="JWT Token", placeholder="Paste your JWT token here...", rows=3, on_change="jwt_decode")

        c.spacer()

        with c.row():
            with c.col(span=6):
                c.text("Header", size="sm", color="muted")
                c.code(header_out, language="json")

            with c.col(span=6):
                c.text("Payload", size="sm", color="muted")
                c.code(payload_out, language="json")
