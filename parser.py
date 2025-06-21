import re

def parse_snippets(text):
    entries = text.strip().split('----------------------------------------')
    result = []

    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue

        # Extract fields using more precise regular expressions
        title_match = re.search(r'^TITLE:\s*(.+)', entry, re.MULTILINE)
        source_match = re.search(r'^SOURCE:\s*(.+)', entry, re.MULTILINE)

        # Manually extract DESCRIPTION to prevent over-capture
        desc_match = re.search(r'DESCRIPTION:\s*(.+?)(?:^SOURCE:|^LANGUAGE:)', entry, re.DOTALL | re.MULTILINE)

        title = title_match.group(1).strip() if title_match else None
        description = desc_match.group(1).strip() if desc_match else None
        source = source_match.group(1).strip() if source_match else None

        # Match all LANGUAGE / CODE blocks
        code_blocks = re.findall(
            r'LANGUAGE:\s*(.+?)\nCODE:\n```(?:\w*)\n(.*?)```',
            entry,
            re.DOTALL
        )

        result.append({
            "title": title,
            "description": description,
            "source": source,
            "snippets": [
                {"language": lang.strip(), "code": code.strip()}
                for lang, code in code_blocks
            ]
        })

    return result

