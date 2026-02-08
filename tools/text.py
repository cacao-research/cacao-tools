"""Text utility tools."""

import re
import cacao as c


def render_all():
    """Render all text tools."""
    with c.tabs():
        with c.tab("stats", "Statistics"):
            stats_tool()
        with c.tab("regex", "Regex Tester"):
            regex_tool()


def stats_tool():
    """Text statistics."""
    results = c.signal("", name="stats_out")

    @c.on("analyze_text")
    async def analyze(session, event):
        text = event.get("value", "")
        if not text:
            results.set(session, "")
            return

        chars = len(text)
        chars_no_spaces = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
        words = len(text.split())
        lines = len(text.split("\n"))
        sentences = max(0, len(re.split(r"[.!?]+", text)) - 1)
        avg_word = round(chars_no_spaces / words, 2) if words > 0 else 0
        reading_time = max(1, words // 200)

        output = f"""Characters:           {chars:,}
Characters (no space): {chars_no_spaces:,}
Words:                {words:,}
Lines:                {lines:,}
Sentences:            {sentences:,}
Avg word length:      {avg_word}
Reading time:         ~{reading_time} min"""
        results.set(session, output)

    with c.card():
        c.text("Analyze text and get detailed statistics.", color="muted")
        c.spacer()

        c.textarea(label="Text", placeholder="Paste or type your text here to analyze...", rows=8, on_change="analyze_text")

        c.spacer()

        c.text("Statistics", size="sm", color="muted")
        c.code(results)


def regex_tool():
    """Regex tester."""
    pattern_sig = c.signal("", name="regex_pattern")
    text_sig = c.signal("", name="regex_text")
    results = c.signal("Enter a pattern and test text", name="regex_out")

    @c.on("set_regex_pattern")
    async def set_pattern(session, event):
        pattern_sig.set(session, event.get("value", ""))
        await test_regex(session)

    @c.on("set_regex_text")
    async def set_text(session, event):
        text_sig.set(session, event.get("value", ""))
        await test_regex(session)

    async def test_regex(session):
        pattern = pattern_sig.get(session)
        text = text_sig.get(session)

        if not pattern or not text:
            results.set(session, "Enter a pattern and test text")
            return

        try:
            regex = re.compile(pattern)
            matches = list(regex.finditer(text))
            if not matches:
                results.set(session, "No matches found")
                return

            output_lines = [f"Found {len(matches)} match(es):", ""]
            for i, m in enumerate(matches):
                output_lines.append(f"Match {i + 1}: \"{m.group()}\"")
                output_lines.append(f"  Position: {m.start()}-{m.end()}")
                if m.groups():
                    for j, g in enumerate(m.groups()):
                        output_lines.append(f"  Group {j + 1}: \"{g}\"")
                output_lines.append("")
            results.set(session, "\n".join(output_lines))
        except re.error as e:
            results.set(session, f"Invalid regex: {str(e)}")

    with c.card():
        c.text("Test regular expressions against text.", color="muted")
        c.spacer()

        with c.row():
            with c.col(span=6):
                c.input("Pattern", placeholder="Enter regex pattern (e.g., \\d+)...", on_change="set_regex_pattern")
                c.spacer()
                c.textarea(label="Test Text", placeholder="Enter text to test against...", rows=6, on_change="set_regex_text")

            with c.col(span=6):
                c.text("Results", size="sm", color="muted")
                c.code(results)
