# 🚗 Cars 2022 Dataset – India Edition

## 📄 Overview

The **Cars 2022 Dataset** provides detailed specifications of **203 new car models** available for purchase in India as of 2022. The data was sourced from [CarDekho](https://www.cardekho.com/), one of India’s leading car comparison and review platforms.

This dataset enables automotive analysis, machine learning modeling, performance clustering, and market segmentation based on technical specifications.

---

## 📊 Dataset Description

| Feature Name          | Type    | Description                                    |
| --------------------- | ------- | ---------------------------------------------- |
| `car_name`            | String  | Name of the car model                          |
| `reviews_count`       | integer | Number of user reviews                         |
| `fuel_type`           | String  | Type of fuel used (Petrol / Diesel / Electric) |
| `engine_displacement` | Integer | Engine size in cc                              |
| `no_cylinder`         | Integer | Number of cylinders (0 for electric vehicles)  |
| `seating_capacity`    | Integer | Total seating capacity                         |
| `transmission_type`   | String  | Manual / Automatic / Electric                  |
| `fuel_tank_capacity`  | Integer | Fuel tank capacity in liters (0 for EVs)       |
| `body_type`           | String  | Car category (SUV, Sedan, Hatchback, etc.)     |
| `rating`              | Integer | User rating (0 to 5)                           |
| `starting_price`      | Integer | Minimum price in INR                           |
| `ending_price`        | Integer | Maximum price in INR                           |
| `max_torque_nm`       | Integer | Maximum torque (Nm)                            |
| `max_torque_rpm`      | Integer | RPM at which max torque is delivered           |
| `max_power_bhp`       | Integer | Maximum horsepower (bhp)                       |
| `max_power_rp`        | Integer | RPM at which max power is delivered            |

---

## 📌 Notes

* Missing values may occur for electric vehicles (e.g., fuel tank capacity, engine displacement).
* Prices are in **Indian Rupees (₹)**.
* The dataset is ideal for **dimensionality reduction (PCA)**, **car clustering**, **market segmentation**, and **spec-based filtering**.