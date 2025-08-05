# 🏎️ Decoding Driver Performance in Formula 1 History (1950–2024)

## 📌 Problem Statement

This analysis dissects seven decades of Formula 1 race results using the `results.csv` dataset and related files to uncover:

* The top-performing drivers and teams.
* Drivers with the most DNFs and lost positions.
* Team efficiency metrics.
* Performance evolution across decades.
* Common causes of race failures.

---

## 🔍 Key Findings

### 🔝 Top 10 Drivers by Total Points

Using total career points:

* **Lewis Hamilton** leads, followed by other modern-era titans.
* Classic legends like **Schumacher** still dominate historically despite fewer races.

📊 *Bar Chart*: Visualizes drivers' cumulative points.

### 🛠️ Team Efficiency – Points per Start

Efficiency was defined as total points divided by race starts:

* **Mercedes**, **Red Bull**, and **Ferrari** top the list.
* Smaller teams with fewer races but strong finishes (e.g., Brawn GP) rank high.

📊 *Bar Chart*: Highlights team performance normalized by starts.

### 💥 Reliability Analysis – DNFs Over the Years

* DNF (Did Not Finish) trends peaked in the 1980s and 1990s.
* Common causes: **engine**, **suspension**, and **accidents**.

📊 *Bar Chart*: DNFs per year + most frequent failure types.

### 📉 Worst Performers – Most Positions Lost

Drivers who consistently fell behind from grid to final position:

* Top offenders: **Riccardo Patrese**, **Gerhard Berger**, **Barrichello**.
* These drivers often lost hundreds of positions over their careers.

📊 *Bar Chart*: Summarizes worst 10 drivers in terms of positions lost.

> 🔴 **Note:** Some of these drivers also have high DNF counts, supporting the argument that they were among the poorest performers.

### ⏳ Era Comparison – Best Drivers by Decade

Grouping performance by decades:

* **Senna**, **Prost**, and **Schumacher** dominated their eras.
* The modern dominance of **Hamilton** and **Verstappen** is evident.

📊 *Bar Chart*: Top 3 drivers per decade using total points.

---

## 📈 Visual Insights Summary

| Insight                  | Visualization Type         |
| ------------------------ | -------------------------- |
| Top Drivers by Points    | Horizontal Bar Plot        |
| Team Efficiency          | Bar Plot with Rotation     |
| DNFs per Season          | Vertical Bar Plot          |
| Common DNF Causes        | Simple Bar Chart           |
| Positions Lost by Driver | Horizontal Bar Plot        |
| Top Drivers by Decade    | Grouped Bar Plot by Decade |

- check notebook(later will add themall in plots folder)

---

## ✅ Recommendations

1. **Teams** should prioritize **mechanical reliability**, especially during long seasons. DNFs still significantly impact season outcomes.
2. **Talent scouting** should look beyond total points. Drivers who consistently gain positions (not lose them) may offer hidden value.
3. **Data normalization** (like points per start) helps fairly compare newer and older teams/drivers despite evolving race calendars.
4. **Historical scoring changes** should be factored in when evaluating driver legacy. Consider using standardized metrics like points per race.

---

## 📎 Notes

* Data spans **1950–2024**; cleaning, merging, and validation were done via pandas.
* Feature engineering included metrics like `position_change`, `dnf`, `dns`, `podium`, and `had_fastest_lap`.
* Correlation checks ensured no redundant features skewed results.
