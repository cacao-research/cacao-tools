# Cacao Tools

A collection of developer utilities built with the Cacao framework. Inspired by [it-tools.tech](https://it-tools.tech/).

## Features

### Encoders / Decoders
- **Base64** - Encode and decode Base64 text
- **URL Encode/Decode** - URL encoding and decoding
- **HTML Entities** - Encode and decode HTML entities
- **JWT Decoder** - Decode JWT tokens to view header and payload

### Generators
- **UUID Generator** - Generate UUID v1 and v4
- **Password Generator** - Generate secure random passwords
- **Lorem Ipsum** - Generate placeholder text
- **QR Code** - Generate QR codes (requires `qrcode` package)

### Converters
- **JSON to YAML** - Convert between JSON and YAML formats
- **JSON to CSV** - Convert between JSON arrays and CSV
- **Case Converter** - Convert text between camelCase, snake_case, etc.
- **Number Base** - Convert numbers between binary, octal, decimal, hex

### Text Utilities
- **Text Diff** - Compare two texts and see differences
- **Text Statistics** - Analyze text (word count, reading time, etc.)
- **Regex Tester** - Test regular expressions against text
- **Markdown Preview** - Live markdown preview

### Crypto / Hash
- **Hash Generator** - Generate MD5, SHA-1, SHA-256, SHA-384, SHA-512 hashes
- **Bcrypt** - Hash and verify passwords using bcrypt
- **HMAC Generator** - Generate HMAC signatures

## Running

```bash
cd cacao-tools
cacao run app.py
```

Or specify a port:

```bash
cacao run app.py --port 8080
```

## Optional Dependencies

Some tools work better with additional packages:

```bash
pip install pyyaml    # For YAML conversion
pip install bcrypt    # For bcrypt hashing
pip install qrcode    # For QR code generation
pip install pillow    # For QR code image support
```

## Adding New Tools

1. Create a new function in the appropriate category file (e.g., `tools/encoders.py`)
2. The function should return a Cacao UI component
3. Register the tool in `app.py` under the appropriate category in `TOOLS`

Example:

```python
# In tools/encoders.py
def my_new_tool():
    input_text = Signal("")

    return ui.col(
        ui.text("My new tool description", color="secondary"),
        ui.textarea(
            placeholder="Enter text...",
            value=input_text,
            on_change=lambda v: input_text.set(v),
        ),
        # ... rest of your UI
    )

# In app.py, add to TOOLS:
"my_tool": {"name": "My Tool", "component": encoders.my_new_tool},
```
