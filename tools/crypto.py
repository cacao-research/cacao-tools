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
    c.text("Generate cryptographic hashes from text.", color="muted")
    c.spacer("sm")

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

    c.input("Text", placeholder="Enter text to hash...", on_change="compute_hash")
    c.spacer("sm")
    c.code(results)


def hmac_tool():
    """HMAC generator."""
    c.text("Generate HMAC (Hash-based Message Authentication Code).", color="muted")
    c.spacer("sm")

    message_sig = c.signal("", name="hmac_msg")
    key_sig = c.signal("", name="hmac_key")
    result = c.signal("", name="hmac_out")

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
        result.set(session, f"HMAC-SHA256: {h.hexdigest()}")

    c.input("Message", placeholder="Enter message...", on_change="set_hmac_msg")
    c.input("Secret Key", placeholder="Enter secret key...", on_change="set_hmac_key")
    c.spacer("sm")
    c.code(result)
