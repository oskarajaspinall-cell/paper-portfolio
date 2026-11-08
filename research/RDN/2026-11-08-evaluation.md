# Evaluation: Radian Group Inc. (RDN) — 2026-11-08
## Bear case
The cheapness is mostly an illusion of the mechanical model. On earnings RDN is expensive against itself: P/E of 8.8x sits above its 5y maximum of 8.4x and in line with peers [Certain]. P/B of 1.0x is at the top of its 0.8x–1.0x range [Certain], while ROE has slid from 18.2% (FY2022) to 12.4% TTM [Certain]. The P/B + ROE fair value assumes that ROE holds, which the trend does not support [Likely]. The P/E method's base of 29.47 is below the price [Certain]. The Inigo deal adds an unseasoned Lloyd's book, and Q3 was flattered by benign catastrophe losses [Likely]. It was part-funded by a $600M [company-reported] loan that thins the PMIERs cushion, which could slow buybacks [Guessing]. A new CEO, GSE/FHFA policy risk and short interest up 63.7% on the month add uncertainty [Certain]. The P/FCF of 3.2x is unreliable because insurer FCF conversion swings from -110.0% to 252.8% [Certain].

## Bull case
Mortgage insurance is a capital-regulated oligopoly with high barriers to entry [Likely]. RDN earns ROIC of 11.3%, up 1.5pp over the last twelve months (rising, not falling) [Certain]. It trades at book value, 11% below the peer P/B median of 1.1x, with a 4.92% fall in the share count [Certain]. Q3 adjusted EPS beat [Likely], and the stock has not re-rated: there was no earnings-type reaction [Certain]. Leverage is modest at 1.32x net debt/EBITDA [Certain]. If Specialty proves a durable second earnings stream, book value compounds at a low-teens ROE and the market may pay a peer-like multiple [Guessing]. The mechanical fair-value range (bear 45.52, base 55.49, bull 62.33) sits wholly above the 35.97 close [Certain]. Beta of 0.66 makes it a diversifying financial [Certain].

## Decision
```json
{
  "ticker": "RDN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A capital-regulated US mortgage insurer at book value with a new, unseasoned Lloyd's specialty arm earns a declining low-teens ROE, so the stock is fairly priced on earnings and only looks cheap through a P/B model that assumes ROE holds.",
  "rationale": "Mechanical upside relies on the P/B + ROE method while ROE trends down, P/E is above its 5y high and the P/E method sits below the price. Specialty earnings are untested after benign catastrophe losses, leadership is new and the PMIERs cushion is thinner. Good, not compelling: conviction 3, so AVOID.",
  "price_at_decision": 35.97,
  "price_date": "2026-11-06",
  "research_note": "research/RDN/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9% (11.3% now), showing Specialty or mortgage credit is eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM ROE falls below 10% (12.4% now), extending the downtrend from 18.2% in FY2022 and breaking the P/B-at-book case.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.32x now), showing the Inigo funding is straining the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "Specialty combined ratio in the quarterly release on radian.com exceeds 100% for two consecutive quarters, or, positively, stays below it through a normal catastrophe year while ROE turns up."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 46.0, "basis": "Specialty holds up through a normal catastrophe year and P/B re-rates to the 1.1x peer median [RA, P:MTG/ESNT/NMIH/ACT] on book compounding at a low-teens ROE [RA], reaching about the mechanical bear fair value of 45.52; below the base 55.49 because that assumes today's ROE is sustainable despite its slide from 18.2% [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 38.0, "basis": "P/B stays near 1.0x, the top of its 5y range [RA], while book grows at the 12.4% TTM ROE [RA] less buyback and Specialty capital needs (note section 5); well below the P/B + ROE base of 68.51 because the P/E method (base 29.47) shows earnings do not support that value."},
    "bear": {"probability": 0.25, "target_price_12m": 29.0, "basis": "A normal or heavy catastrophe year hits Specialty (Q3 transcript, benign losses) and ROE keeps falling, so P/B returns to its 5y low of 0.8x [RA] and price falls to around the P/E-method base of 29.47 [fact sheet Fair value]."}
  },
  "entry_price": 28.78,
  "entry_basis": "P/B back at its 5y low of 0.8x [RA] (1.0x at the 35.97 close), near the P/E-method base of 29.47; the default base 55.49 x 0.8 is above the price, so it cannot anchor the entry. At that level a low-teens ROE book would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```
