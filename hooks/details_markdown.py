"""Make markdown inside <details> blocks render (the MCQ answers use them)."""
import re


def on_page_markdown(markdown, **kwargs):
    return re.sub(r"<details(?![^>]*markdown)", '<details markdown="1"', markdown)
