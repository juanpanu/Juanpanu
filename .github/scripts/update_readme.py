import yaml
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
now = yaml.safe_load((ROOT / "now.yml").read_text(encoding="utf-8"))
readme = (ROOT / "README.md").read_text(encoding="utf-8")

updated = datetime.now(timezone.utc).strftime("%B %Y")
block = f"""<!-- currently:start -->
<h3>📍 Currently</h3>

| | |
|---|---|
| **Focus** | {now['focus']} |
| **Learning** | {now['learning']} |
| **Exploring** | {now['exploring']} |

<sub>Last updated: {updated}</sub>
<!-- currently:end -->"""

if "<!-- currently:start -->" in readme:
    import re
    readme = re.sub(
        r"<!-- currently:start -->.*?<!-- currently:end -->",
        block,
        readme,
        flags=re.DOTALL,
    )
else:
    readme = readme.rstrip() + "\n\n" + block + "\n"

(ROOT / "README.md").write_text(readme, encoding="utf-8")
print(f"README updated ({updated})")
