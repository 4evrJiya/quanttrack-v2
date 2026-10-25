# QuantTrack UI redesign — first pass

## What changed
- Introduced a shared dark navy / teal design system in `ui_helpers.py`.
- Updated the global Streamlit theme in `.streamlit/config.toml`.
- Rebuilt the home page around a clearer product introduction and three workflow cards.
- Removed emoji-based page filenames so navigation labels are clean and consistent.
- Updated page titles, descriptions, primary action labels, and several status messages across Backtest, Portfolio, Forecast, Account, and Learn.
- Escaped the signed-in username before rendering it in the sidebar's HTML.

## What did not change
- Strategy formulas, backtest calculations, forecast calculations, portfolio calculations, and database logic were intentionally left unchanged.
- This is a visual/product pass, not a quant-correctness or security release.

## Validation
- All app Python files passed Python compilation and AST parsing.
- Streamlit is not installed in the analysis environment, so the app could not be launched for browser-based visual verification here. Please run it locally and inspect every page before merging.

## Run locally
```bash
streamlit run Home.py
```
