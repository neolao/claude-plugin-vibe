import html


def render_report(report, fmt="plain"):
    lines = [f"{item['label']}: {item['value']}" for item in report["items"]]
    if fmt == "html":
        rows = "".join(f"<li>{html.escape(line)}</li>" for line in lines)
        return f"<h1>{html.escape(report['title'])}</h1><ul>{rows}</ul>"
    return "\n".join([report["title"], *lines])
