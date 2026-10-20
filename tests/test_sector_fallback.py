import fetch_data as F


def page(industry, sector=None):
    rows = [{"t": "Industry", "v": industry}] + ([{"t": "Sector", "v": sector}] if sector else [])
    return [{"infoTable": rows}]


def test_site_sector_is_used_when_present(monkeypatch):
    monkeypatch.setattr(F, "parse_info", lambda nodes, url: {"type": "stock"})
    out = F.parse_overview(page("Consumer Electronics", "Technology"), "u")
    assert (out["sector"], out["sector_source"]) == ("Technology", "OV")


def test_missing_sector_is_mapped_from_the_industry_or_unknown(monkeypatch):
    monkeypatch.setattr(F, "parse_info", lambda nodes, url: {"type": "stock"})
    out = F.parse_overview(page("Deep Sea Foreign Transportation of Freight"), "u")
    assert out["sector"] == "Industrials" and "mapped from the industry" in out["sector_source"]
    out = F.parse_overview(page("Land Subdividers and Developers, Except Cemeteries"), "u")
    assert out["sector"] == "Real Estate"
    out = F.parse_overview(page("Something Unmapped"), "u")
    assert (out["sector"], out["sector_source"]) == ("Unknown", "[data unavailable]")
