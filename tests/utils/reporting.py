import functools


def add_custom_report(item, custom_html):
    if not hasattr(item, "custom_html"):
        item.custom_html = ""
    item.custom_html += custom_html

