---
published: true
---
# Tips and tricks

## Playwright in a Jupyter Notebook
When running Playwright (async, code on [playwright.dev](https://playwright.dev/python/docs/library#interactive-mode-repl)) in a Jupyter Notebook on Windows, you will receive an `NotImplementedError`.

To fix this, open the file `venv\Lib\site-packages\ipykernel\kernelapp.py` and remove the command `self._init_asyncio_patch()` (around line 702) from the function `initialize`.