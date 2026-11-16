# Evaluation: China Resources Beer (Holdings) Company Limited (HKG:0291) — 2026-11-16
## Bear case
The bottom line is shrinking while the operating line improves: net margin fell from 13.7% to 7.2% and ROE from 20.1% to 6.3% [Certain], and the cause (likely non-operating or impairment charges, possibly tied to the baijiu line) is still unidentified [Guessing]. ROIC has stepped down from 16.0% in FY2022 to 11.9% TTM, so returns on the enlarged capital base sit only just above a 10% hurdle [Certain]. Essentially all revenue is mainland China, where the price already discounts revenue shrinking 7.0% in year 1; if beer volumes really contract, premiumisation may not offset it [Likely]. The trend is weak: 11.8% below the 200-day average, the 50-day 16.9% below the 200-day, and 36.3pp behind SPY over 12 months [Certain]. Piotroski F of 5 is middling [Certain]. Country risk is unverified beyond FX: the PBoC rate and any regulation were not checked (macro overlay) [Certain].
## Bull case
The operating franchise is getting better, not worse: operating margin rose from 9.0% to 14.9% and gross margin from 39.2% to 42.3%, and on a rolling basis FCF margin is at its 2-year high of 15.3% with operating margin flat near its high [Certain]. Cash conversion is strong (FCF/net income 213.2%) and the balance sheet is net cash at -1.55x net debt/EBITDA [Certain]. Yet EV/EBITDA of 6.2x, P/FCF of 10.2x and EV/Sales of 1.3x all sit below their own 5-year minimums and below peers, with a 9.85% FCF yield [Certain]. The reverse DCF prices outright revenue decline that the rising margins do not show [Likely]. Scale and distribution in a consolidated market give a narrow moat [Likely]. The mechanical base fair value of HKD 34.11 sits well above the price, and the CNY has firmed against the dollar, a small translation tailwind (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "HKG:0291",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing is falling over 1 or 3 years. ROIC is below FY2022 (16.0% to 11.9% TTM) [RA] but has recovered from the FY2024 low of 10.3% and is flat over the last year (-0.5pp) [RA-T], while operating margin rose from 9.0% to 14.9% [IS] and FCF margin is at its 2-year high [CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Mainland China beer volumes contract and the unexplained fall in net margin and ROE proves to be recurring charges, so the operating gains do not reach shareholders.",
    "veto": null
  },
  "thesis": "A net-cash Chinese brewer with rising operating and FCF margins trades below its own 5-year minimum cash multiples, pricing shrinkage that its improving operations do not show.",
  "rationale": "Same evidence as the 2026-11-15 HOLD 4: cheap cash multiples, net cash and improving operations, against an unexplained net-income fall and a weak trend. The position is already at about its target size, so no ADD; it stays held at conviction 4.",
  "price_at_decision": 20.46,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-0291/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12.0% (14.9% now), reversing the mix and pricing gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12.0}},
    {"text": "TTM FCF margin falls below 10.0% (15.3% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "TTM ROIC falls below 10.0% (11.9% now), below the FY2025 low of 10.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10.0}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, balance sheet / ratios page) turns positive from -1.55x TTM, i.e. net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.11, "basis": "Margins hold and the market prices stable rather than shrinking revenue, reaching the mechanical blended base fair value of 34.11 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 27.98, "basis": "Operating margin stays near 14.9% [IS] and FCF near its 2-year high [CF-T], so the price moves toward the DCF base of 27.98 while EV/EBITDA stays below its 5y median [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 16.73, "basis": "China volumes contract and charges keep depressing net income (ROE 6.3% [RA]), taking the price to the mechanical bear fair value of 16.73 [IS,BS,CF,RA,ST,HI]."}
  },
  "entry_price": null,
  "entry_basis": "Held at conviction 4, so no entry price is needed; at size, an ADD is not the question.",
  "replaces": null,
  "replacement_reason": null
}
```
