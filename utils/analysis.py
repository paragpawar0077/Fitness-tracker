import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_summary_and_chart(data):
    # if no data, return empty summary
    if not data:
        return {}, None

    # Convert MongoDB data into DataFrame
    df = pd.DataFrame(data)

    # Convert date string to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Create summary
    summary = {
        "total_calories": round(df['calories'].sum(), 2),
        "avg_calories": round(df['calories'].mean(), 2),
        "total_duration": round(df['duration'].sum(), 2),
        "avg_duration": round(df['duration'].mean(), 2),
    }

    # Create charts folder if not exists
    chart_path = os.path.join('static', 'charts', 'progress.png')
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)

    # Plot total calories burned per date
    plt.figure(figsize=(6, 4))
    df.groupby('date')['calories'].sum().plot(marker='o', color='green')
    plt.title("Calories Burned Over Time")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    plt.grid(True)
    plt.tight_layout()

    # Save the chart
    plt.savefig(chart_path)
    plt.close()

    return summary, chart_path
