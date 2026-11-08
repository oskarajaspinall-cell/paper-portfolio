# Evaluation: Gaming and Leisure Properties (GLPI) — 2026-11-08
## Bear case
The discount is about Bally's, not mispricing. Bally's supplies 19.4% of cash income [company-reported] and disclosed substantial going-concern doubt in August 2026 [Certain]. GLPI has funded $640.7 million of up to $940.0 million for Bally's Chicago, whose rent is deferred until completion [company-reported], so more money is going to a stressed tenant [Certain]. A restructuring could reset rent, and a licensed casino is hard to re-tenant [Likely]. The Q3 10-Q took a large credit-loss provision [Certain]. Leverage is already 5.09x net debt/EBITDA (site definition) and shares grew 2.88% YoY, so growth is partly dilutive [Certain]. ROIC was flat over the last year, at 9.7% against a 10.0% 2-year high: no improvement is under way [Certain]. The macro overlay tilts small toward bear: HY spreads widened and VIX rose, both raising Bally's funding risk [Likely]. The mechanical fair value uses multiples from before this tenant risk existed [Likely].
## Bull case
Every multiple is below its 5y minimum: P/E 11.9x against 15.3x–22.4x, and EV/EBITDA 12.3x against a 5y minimum of 13.3x and a peer median of 14.9x [Certain]. Even the mechanical bear fair value of 48.64 is above the 38.89 close [Certain]. Q3 was a record for revenue, AFFO and adjusted EBITDA. FY guidance was held and the AFFO beat consensus [Likely]. Master leases cross-bind the tenant's properties and gaming licences make the assets essential to any operator, so in a Bally's restructuring the leases would probably be assumed rather than rejected [Likely]. Deal flow continues, with the Prologis Joliet JV and Bally's Lincoln [Certain]. The 10y yield of 4.84% is priced in, and lower real yields would re-rate the stock [Guessing]. Net debt/EBITDA has fallen over five years [Certain].
## Decision
```json
{
  "ticker": "GLPI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A licence-protected casino landlord with contractual rent trades below every 5-year multiple minimum, but the discount reflects an unresolved going-concern risk at its largest stressed tenant (Bally's) rather than mispricing.",
  "rationale": "The stock is cheap on its own history and peers, but the expected value sits only modestly above the price because a Bally's restructuring is a live binary risk, while GLPI keeps funding Chicago and leverage is elevated. Good but not compelling: conviction 3, so no position until Bally's credit risk resolves.",
  "price_at_decision": 38.89,
  "price_date": "2026-11-06",
  "research_note": "research/GLPI/2026-11-08.md",
  "triggers": [
    {"text": "Bally's going-concern doubt is removed in its filings, or Bally's completes a refinancing that covers its maturities, as disclosed in a GLPI or Bally's release/10-Q (would lift conviction)."},
    {"text": "Bally's Chicago opens in the first half of 2027 as guided on the Q3 call and rent recognition begins, with no further credit-loss provisions on the Bally's-related investments in the 10-Q."},
    {"text": "Net debt/EBITDA rises above 6.0x (5.09x now), showing growth is being funded by leverage.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.0}},
    {"text": "TTM ROIC falls below 8.5% (9.7% now), showing rent losses or impairments are eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 50.0, "basis": "Bally's refinances and Chicago opens on schedule (Q3 call, fact sheet news), so P/E re-rates to its 5y minimum of 15.3x [RA]. This is below the mechanical bull of 60.85 because tenant concentration caps a return to the 18.0x median."},
    "base": {"probability": 0.4, "target_price_12m": 43.0, "basis": "Bally's stays stressed but pays, FY AFFO guidance holds, and EV/EBITDA recovers partly toward its 5y minimum of 13.3x [RA]. This is below the mechanical base of 55.54 because that historic P/FFO ignores the going-concern risk (note, 10-Q); the probability is trimmed for the macro overlay's small toward-bear tilt (research/GLPI/2026-11-08-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 30.0, "basis": "Bally's restructures (19.4% of cash income [company-reported], 10-Q), rent is reset and the Chicago funding is provisioned, compressing the multiple further below its 5y minimum [RA]. This is below the mechanical bear of 48.64, which does not model a tenant default; the probability is raised for the overlay's widening HY spreads (research/GLPI/2026-11-08-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default entry (base 55.54 x 0.8) is already above the price. The blocker is the unresolved Bally's going-concern risk, so a lower price alone would not lift conviction to 4. Resolution of that risk (the first trigger) would.",
  "replaces": null,
  "replacement_reason": null
}
```
