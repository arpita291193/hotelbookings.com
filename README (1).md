# Hotel Bookings Intelligence Dashboard

An interactive Streamlit dashboard for the hotel bookings dataset (119k+ reservations)
with KPI cards, demographics, geography bubble charts, 3D exploratory visuals,
cancellation risk analysis, a searchable/sortable listings table, and auto-generated
business insights & recommendations.

## Setup

1. Make sure `hotel_bookings_data.csv` is in the same folder as `app.py`
   (already included here).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. It will open automatically at `http://localhost:8501`.

## What's inside

- **Sidebar filter card** — hotel type, year, month, market segment, city,
  booking status, lead time range, ADR range, repeat-guest toggle. Every
  chart and KPI reacts live.
- **KPI row** — total bookings, cancellation rate (with delta vs. full
  dataset), average daily rate, net revenue, avg lead time, repeat-guest
  rate, avg length of stay, avg special requests.
- **Overview tab** — monthly bookings vs. revenue combo chart, hotel-type
  pie, market segment & distribution channel bar charts.
- **Demographics tab** — family composition, meal plan, customer type pies,
  length-of-stay and party-size bars, deposit type and special-requests charts.
- **Geography & Bubbles tab** — bubble charts sizing cities by volume,
  coloring by cancellation risk and revenue, plus top-city bar charts.
- **3D Explorer tab** — rotatable 3D scatter (lead time × ADR × nights),
  a 3D seasonality ribbon by hotel type, and a 3D surface of ADR by week/year.
- **Cancellations tab** — cancellation rate by lead-time bucket, deposit
  type, market segment, and an ADR distribution overlay (completed vs.
  canceled).
- **Listings tab** — searchable, sortable table of individual bookings with
  CSV export of the current filtered view.
- **Insights & Recommendations tab** — figures and recommendations that
  recompute live from whatever filters are currently applied, so you can
  stress-test them against specific hotels, seasons, or segments.

## Notes on the data

- One negative ADR value and the top 0.1% ADR outliers are clipped/trimmed
  so a data-entry glitch doesn't distort the charts.
- Missing `children`, `city`, `agent`, and `company` values are filled with
  sensible defaults (0 or "Unknown") rather than dropped, to preserve
  sample size.
