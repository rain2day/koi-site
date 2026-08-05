"""Static site generator for the KOI Keyboard public website.

Content lives as structured data in ``content_zh`` and ``content_en``. The two
modules expose the same page keys and section shapes, so a section that exists
in one language and not the other fails at render time instead of reaching
production. ``components`` turns section data into HTML; ``layout`` wraps it in
the document shell.

The package depends only on the Python standard library so that the GitHub
Pages workflow can run it with a bare ``python3``.
"""
