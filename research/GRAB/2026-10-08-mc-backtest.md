## Monte Carlo calibration backtest — GRAB (2026-10-08)
flat base case (no historical research): idiosyncratic and factor expected moves 0, no jumps; factor regression and vol from data available at each date.

| Horizon | Inside P5-P95 (target ~90%) | Inside P25-P75 (target ~50%) |
|---|---|---|
| 3m | 7/8 (88%) | 4/8 (50%) |
| 6m | 7/8 (88%) | 4/8 (50%) |

| As of | 3m realised | 3m P5 / P95 | 6m realised | 6m P5 / P95 |
|---|---|---|---|---|
| 2024-06-30 | +2.8% | -38.7% / +50.0% | +38.4% | -51.1% / +72.5% |
| 2024-09-30 | +24.9% | -36.8% / +46.8% | +18.7% | -48.7% / +67.8% |
| 2024-12-31 | -5.0% | -35.4% / +45.0% | +2.3% | -47.5% / +65.2% |
| 2025-03-31 | +7.7% | -29.3% / +35.4% | +33.7% | -39.8% / +51.0% |
| 2025-06-30 | +24.2% | -30.2% / +37.0% | +4.7% | -40.9% / +53.1% |
| 2025-09-30 | -15.7% | -29.7% / +36.4% | -41.6% | -40.3% / +51.8% |
| 2025-12-31 | -30.7% | -28.8% / +34.9% | -31.1% | -39.1% / +50.5% |
| 2026-03-31 | -0.6% | -28.9% / +35.1% | -12.3% | -39.2% / +50.2% |

Eight dates is a small sample: treat coverage as a rough calibration check, not a test of skill.
