"""Converter tools."""

import json
import cacao as c


def render_all():
    """Render all converter tools."""
    with c.tabs():
        with c.tab("json_yaml", "JSON to YAML"):
            json_yaml_tool()
        with c.tab("case", "Case Converter"):
            case_tool()
        with c.tab("number", "Number Base"):
            number_base_tool()


def _to_yaml(data, indent=0):
    """Convert data to YAML format."""
    lines = []
    prefix = "  " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{prefix}{key}:")
                lines.append(_to_yaml(value, indent + 1))
            else:
                lines.append(f"{prefix}{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                lines.append(f"{prefix}-")
                lines.append(_to_yaml(item, indent + 1))
            else:
                lines.append(f"{prefix}- {item}")
    return "\n".join(lines)


def json_yaml_tool():
    """JSON to YAML converter."""
    output = c.signal("", name="yaml_out")

    @c.on("convert_yaml")
    async def convert(session, event):
        text = event.get("value", "").strip()
        if not text:
            output.set(session, "")
            return
        try:
            data = json.loads(text)
            result = _to_yaml(data)
            output.set(session, result)
        except Exception as e:
            output.set(session, f"Error: {str(e)}")

    with c.card():
        c.text("Convert JSON to YAML format.", color="muted")
        c.spacer()

        with c.row():
            with c.col(span=6):
                c.textarea(label="JSON Input", placeholder='{"key": "value", "array": [1, 2, 3]}', rows=10, on_change="convert_yaml")

            with c.col(span=6):
                c.text("YAML Output", size="sm", color="muted")
                c.code(output, language="yaml")


def case_tool():
    """Case converter."""
    results = c.signal("", name="case_out")

    @c.on("convert_case")
    async def convert(session, event):
        text = event.get("value", "")
        if not text:
            results.set(session, "")
            return

        words = text.replace("-", " ").replace("_", " ").split()
        output_lines = [
            f"lowercase:     {text.lower()}",
            f"UPPERCASE:     {text.upper()}",
            f"Title Case:    {text.title()}",
            f"camelCase:     {words[0].lower() + ''.join(w.capitalize() for w in words[1:]) if words else ''}",
            f"PascalCase:    {''.join(w.capitalize() for w in words)}",
            f"snake_case:    {'_'.join(w.lower() for w in words)}",
            f"kebab-case:    {'-'.join(w.lower() for w in words)}",
            f"CONSTANT_CASE: {'_'.join(w.upper() for w in words)}",
        ]
        results.set(session, "\n".join(output_lines))

    with c.card():
        c.text("Convert text between different case formats.", color="muted")
        c.spacer()

        c.input("Text Input", placeholder="Enter text to convert...", on_change="convert_case")

        c.spacer()

        c.text("Results", size="sm", color="muted")
        c.code(results)


def number_base_tool():
    """Number base converter."""
    results = c.signal("", name="base_out")

    @c.on("convert_base")
    async def convert(session, event):
        value = event.get("value", "").strip()
        if not value:
            results.set(session, "")
            return
        try:
            num = int(value, 10)
            output_lines = [
                f"Binary:      {bin(num)[2:]}",
                f"Octal:       {oct(num)[2:]}",
                f"Decimal:     {num}",
                f"Hexadecimal: {hex(num)[2:].upper()}",
            ]
            results.set(session, "\n".join(output_lines))
        except ValueError:
            results.set(session, "Error: Invalid decimal number")

    with c.card():
        c.text("Convert numbers between binary, octal, decimal, and hexadecimal.", color="muted")
        c.spacer()

        c.input("Decimal Number", placeholder="Enter a decimal number (e.g., 255)...", on_change="convert_base")

        c.spacer()

        c.text("Conversions", size="sm", color="muted")
        c.code(results)
