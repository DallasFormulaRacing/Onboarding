import sys
import pandas as pd
import plotly.express as px

def main(csv_file):
    # 1) Load CSV
    df = pd.read_csv(csv_file)

    # 2) Drop constant 'Analog Input' columns (dead sensors)
    drop_cols = [c for c in df.columns if "Analog Input" in c and df[c].nunique(dropna=False) <= 1]
    if drop_cols:
        print(f"Dropping dead sensor columns: {drop_cols}")
        df = df.drop(columns=drop_cols)

    # 3) Columns we care about
    time_col = "timestamp"
    rpm_col = "RPM"
    tps_col = "TPS"

    # Convert timestamp (epoch seconds) into readable datetime
    try:
        if pd.api.types.is_numeric_dtype(df[time_col]) and df[time_col].max() > 10_000:
            df[time_col] = pd.to_datetime(df[time_col], unit="s")
    except Exception as e:
        print("Timestamp conversion failed, using raw values:", e)

    # 4) Plot RPM over time
    fig_rpm = px.line(df, x=time_col, y=rpm_col,
                      title="RPM over Time",
                      labels={time_col: "Time", rpm_col: "RPM"})
    fig_rpm.write_html("rpm_over_time.html")

    # 5) Plot TPS over time
    fig_tps = px.line(df, x=time_col, y=tps_col,
                      title="TPS over Time",
                      labels={time_col: "Time", tps_col: "TPS"})
    fig_tps.write_html("tps_over_time.html")

    print("✅ Plots saved: rpm_over_time.html, tps_over_time.html")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_file>")
    else:
        main(sys.argv[1])
