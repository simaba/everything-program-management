from pathlib import Path


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples" / "data"
PROHIBITED_MARKERS = (
    "Sima Bagheri",
    "Supplier API",
    "Product Steering",
)


def test_public_examples_are_explicitly_fictional_and_sanitized() -> None:
    """Keep bundled examples clearly separate from real personal or work artifacts."""
    files = sorted(EXAMPLES_DIR.glob("*"))
    assert files, "expected bundled example artifacts"

    for path in files:
        text = path.read_text(encoding="utf-8")
        assert "fictional" in text.lower(), f"{path.name} must identify itself as fictional"
        for marker in PROHIBITED_MARKERS:
            assert marker.lower() not in text.lower(), (
                f"{path.name} contains a prohibited public-example marker: {marker}"
            )
