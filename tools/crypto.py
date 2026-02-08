"""Cryptography and hashing tools."""

import hashlib
import hmac as hmac_lib
import cacao as c


def render_all():
    """Render all crypto tools."""
    with c.tabs():
        with c.tab("hash", "Hash Generator"):
            hash_tool()
        with c.tab("hmac", "HMAC"):
            hmac_tool()


def hash_tool():
    """Hash generator."""
    results = c.signal("", name="hash_out")

    @c.on("compute_hash")
    async def compute(session, event):
        text = event.get("value", "")
        if not text:
            results.set(session, "")
            return

        data = text.encode("utf-8")
        output_lines = [
            f"MD5:     {hashlib.md5(data).hexdigest()}",
            f"SHA-1:   {hashlib.sha1(data).hexdigest()}",
            f"SHA-256: {hashlib.sha256(data).hexdigest()}",
            f"SHA-512: {hashlib.sha512(data).hexdigest()}",
        ]
        results.set(session, "\n".join(output_lines))

    with c.card():
        c.text("Generate cryptographic hashes from text.", color="muted")
        c.spacer()

        c.textarea(label="Text", placeholder="Enter text to hash...", rows=4, on_change="compute_hash")

        c.spacer()

        c.text("Hash Results", size="sm", color="muted")
        c.code(results)


def hmac_tool():
    """HMAC generator."""
    message_sig = c.signal("", name="hmac_msg")
    key_sig = c.signal("", name="hmac_key")
    result = c.signal("Enter message and key", name="hmac_out")

    @c.on("set_hmac_msg")
    async def set_msg(session, event):
        message_sig.set(session, event.get("value", ""))
        await compute_hmac(session)

    @c.on("set_hmac_key")
    async def set_key(session, event):
        key_sig.set(session, event.get("value", ""))
        await compute_hmac(session)

    async def compute_hmac(session):
        msg = message_sig.get(session)
        key = key_sig.get(session)

        if not msg or not key:
            result.set(session, "Enter message and key")
            return

        h = hmac_lib.new(key.encode(), msg.encode(), hashlib.sha256)
        result.set(session, f"HMAC-SHA256:\n{h.hexdigest()}")

    with c.card():
        c.text("Generate HMAC (Hash-based Message Authentication Code).", color="muted")
        c.spacer()

        with c.row():
            with c.col(span=6):
                c.textarea(label="Message", placeholder="Enter message...", rows=4, on_change="set_hmac_msg")
                c.spacer()
                c.input("Secret Key", placeholder="Enter secret key...", on_change="set_hmac_key")

            with c.col(span=6):
                c.text("HMAC Result", size="sm", color="muted")
                c.code(result)
