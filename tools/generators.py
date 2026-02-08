"""Generator tools."""

import uuid as uuid_lib
import secrets
import string
import random
import cacao as c


def render_all():
    """Render all generator tools."""
    with c.tabs():
        with c.tab("uuid", "UUID"):
            uuid_tool()
        with c.tab("password", "Password"):
            password_tool()
        with c.tab("lorem", "Lorem Ipsum"):
            lorem_tool()


def uuid_tool():
    """UUID generator."""
    c.text("Generate UUIDs (Universally Unique Identifiers).", color="muted")
    c.spacer("sm")

    result = c.signal(str(uuid_lib.uuid4()), name="uuid_result")

    @c.on("gen_uuid")
    async def generate(session, event):
        result.set(session, str(uuid_lib.uuid4()))

    c.button("Generate UUID", on_click="gen_uuid", variant="primary")
    c.spacer("sm")

    with c.card():
        c.code(result)


def password_tool():
    """Password generator."""
    c.text("Generate secure random passwords.", color="muted")
    c.spacer("sm")

    # Generate initial password
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    initial_pwd = "".join(secrets.choice(chars) for _ in range(16))

    password = c.signal(initial_pwd, name="password")
    length = c.signal(16, name="pwd_length")

    @c.on("gen_password")
    async def generate(session, event):
        pwd_len = length.get(session)
        pwd = "".join(secrets.choice(chars) for _ in range(pwd_len))
        password.set(session, pwd)

    @c.on("set_pwd_length")
    async def set_length(session, event):
        length.set(session, event.get("value", 16))

    c.slider("Length", min=8, max=64, value=16, on_change="set_pwd_length")
    c.spacer("sm")
    c.button("Generate Password", on_click="gen_password", variant="primary")
    c.spacer("sm")

    with c.card():
        c.code(password)


def lorem_tool():
    """Lorem Ipsum generator."""
    c.text("Generate placeholder text.", color="muted")
    c.spacer("sm")

    LOREM_WORDS = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing",
        "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore",
        "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam",
    ]

    def gen_paragraph():
        def gen_sentence():
            length = random.randint(8, 16)
            words = [random.choice(LOREM_WORDS) for _ in range(length)]
            words[0] = words[0].capitalize()
            return " ".join(words) + "."
        sentences = [gen_sentence() for _ in range(random.randint(4, 8))]
        return " ".join(sentences)

    initial_text = "\n\n".join(gen_paragraph() for _ in range(3))
    output = c.signal(initial_text, name="lorem_out")
    para_count = c.signal(3, name="lorem_para")

    @c.on("gen_lorem")
    async def generate(session, event):
        count = para_count.get(session)
        result = "\n\n".join(gen_paragraph() for _ in range(count))
        output.set(session, result)

    @c.on("set_lorem_para")
    async def set_para(session, event):
        para_count.set(session, int(event.get("value", 3)))

    with c.row():
        c.select("Paragraphs", ["1", "2", "3", "4", "5"], on_change="set_lorem_para")
        c.button("Generate", on_click="gen_lorem", variant="primary")

    c.spacer("sm")
    c.text(output)
