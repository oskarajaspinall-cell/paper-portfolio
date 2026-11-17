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


def test_short_mandate_for_the_overview_links_to_the_process(cfg):
    html = mandate_html(cfg, short=True)
    assert "Objective: beat the S&amp;P 500" in html and "Screen → Research" in html and "#process" in html and "<ol" not in html
