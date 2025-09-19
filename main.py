import pandas as pd
import plotly.express as px

df = pd.read_csv("can_data.csv")

dead_cols = []
for col in df.columns:
    if "Analog Input" in col:
        if df[col].nunique(dropna=True) <= 1:
            dead_cols.append(col)

df = df.drop(columns=dead_cols)

print("\nDropped columns:", dead_cols)



if "timestamp" in df.columns:
    df["time"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
    xcol = "time"
else:
    df["sample"] = range(len(df))
    xcol = "sample"

print(f"\nUsing x-axis column: {xcol}")

def make_line(colname: str):
    if colname not in df.columns:
        print(f"Warning: '{colname}' column not found.")
        return

    d = df[[xcol, colname]].dropna(subset=[colname])
    fig = px.line(d, x=xcol, y=colname,
                  title=f"{colname} over time",
                  labels={xcol: "Time / Sample", colname: colname})
    out = f"{colname.lower()}_over_time.html"
    fig.write_html(out, auto_open=True)
    print(f"Saved: {out}")

make_line("RPM")
make_line("TPS")

