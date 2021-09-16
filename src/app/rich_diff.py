import difflib

from rich.markdown import Markdown
from textual.app import App
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import ScrollView


class RichDiff(App):
    async def on_load(self, event):
        await self.bind("q", "quit", description="Close")

    async def on_mount(self) -> None:
        file1 = str(self.runtime_config.file1)
        file2 = str(self.runtime_config.file2)
        diff_type = self.runtime_config.diff_type
        lines = self.runtime_config.lines
        with open(file1) as f1:
            f1_content = f1.readlines()
        with open(self.runtime_config.file2) as f2:
            f2_content = f2.readlines()

        diff = ""
        if diff_type == "unified_diff":
            diff = difflib.unified_diff(
                f1_content,
                f2_content,
                file1,
                file2,
                n=lines,
            )
        elif diff_type == "context_diff":
            diff = difflib.context_diff(
                f1_content,
                f2_content,
                file1,
                file2,
                n=lines,
            )
        elif diff_type == "ndiff":
            diff = difflib.ndiff(f1_content, f2_content)

        diffy = "\n".join(list(diff))
        body = ScrollView(
            Markdown(
                f"""
```diff
{diffy}
```
""",
                code_theme="vim",
            ),
        )
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(body)
