# Short evaluation: Sandisk Corporation (SNDK) — 2026-11-18
## Bear thesis
NAND is a commodity with no pricing power: operating margin went from 12.5% (FY22) to -21.3% (FY23) to 72.7% TTM [Certain]. TTM gross margin of 80.0% and ROIC of 151.5% sit far outside anything in the 5-year record, so they look like a cyclical peak, not a new normal [Likely]. Sandisk has to fund about half of Flash Ventures' capex and fixed costs plus fixed Kioxia payments through 2029, so its costs stay fixed when prices fall [Certain]. Shares outstanding are up 7.57% YoY, which dilutes holders [Certain]. Once NAND contract prices roll over, earnings could fall faster than the price, and a P/E of 6.4x on peak earnings is not real support [Guessing].

## Bull case against the short
Most of the move has already happened. The stock fell from 2,354.39 to 797.24, is 43.2% below its 50-day average, and has an RSI of 30.9 [Certain]. Over 3 months it trails SPY by 50.2pp [Certain]. The fundamentals have not turned yet. Every trailing metric is still at its 2-year high and rising, FCF conversion is 89.4% and the company holds net cash [Certain]. At 6.5x P/FCF (a 15.31% FCF yield) the stock is cheap on cash flow, and AI datacenter demand for enterprise SSDs could stretch the cycle [Likely]. Short interest is low at 3.50% [Certain]. A rebound after the coming 8-for-1 split, or after strong results from peers, would hurt a put bought at this point [Likely].

## Decision
```json
{
  "ticker": "SNDK",
  "decision": "NO",
  "conviction": 1,
  "parts": {
    "overvaluation": 1,
    "peak_cycle": 2,
    "deterioration": 0,
    "capital_need": 1,
    "catalyst": 1,
    "momentum": -2,
    "takeover_appeal": -2,
    "crowding": 0,
    "insider_support": 0
  },
  "thesis": "Sandisk's margins are a cyclical NAND peak that will fade, but the stock has already fallen from 2,354.39 to 797.24 while the fundamentals are still rising, so a put now pays for a move that has mostly already happened.",
  "catalyst": {"text": "FQ2 FY2027 results (date not yet confirmed by stockanalysis.com)", "date": "2027-01-29"},
  "falsifiers": [
    {"text": "TTM gross margin rises above 85%: the up-cycle is still extending", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 85}},
    {"text": "TTM operating margin rises above 78%", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 78}},
    {"text": "TTM FCF margin rises above 65%", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 65}},
    {"text": "ROIC rises above 170%", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 170}}
  ],
  "bull_case": "The stock already trades at 6.5x FCF with net cash and margins that are still rising, so the cyclical fade looks priced in and the bounce risk is high."
}
```
