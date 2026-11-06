import copy

from common import load_config
from dashboard import mandate_html


def test_mandate_follows_the_config():
    cfg = load_config()
    html = mandate_html(cfg)
    sz = cfg["core"]["conviction_size_pct"]
    assert f"{sz['4']:g}% (conviction 4)" in html and f"{sz['5']:g}% (5)" in html
    assert f"{cfg['portfolio']['max_sector_pct']:g}% per sector" in html and "China/HK 25%" in html
    c2 = copy.deepcopy(cfg)
    c2["portfolio"]["max_sector_pct"] = 27
    assert "27% per sector" in mandate_html(c2)
    assert "<script" not in html  # text is escaped
