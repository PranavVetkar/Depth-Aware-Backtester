# 📊 Order Book Depth & Slippage Analyzer

A Python-based market microstructure tool that analyzes **order book liquidity** and estimates **slippage impact** for large crypto trades.

This project helps answer a critical execution question:
> *If I place a large market order, how much worse price will I actually get?*

---

## 🚀 What This Project Does

- Connects to Binance via **CCXT**
- Fetches live **order book depth**
- Simulates large buy execution
- Calculates:
  - Average fill price
  - Best market price
  - Total slippage %
- Models real execution cost from liquidity constraints

---

## 🧠 Why Slippage Matters

When you place a large market order:

- You don’t get filled at one price
- You “walk the book”
- Each price level adds cost

Result → **Average fill > best price**

This difference = **slippage**

---

## ⚙️ Execution Simulation Logic

For a target buy amount:

1. Fetch top 100 ask levels
2. Accumulate liquidity level by level
3. Stop once order size is filled
4. Compute:
- Average Fill Price = Total USD Spent / BTC Received
- Slippage % = (Avg Fill − Best Ask) / Best Ask × 100

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **CCXT**
- **Binance Order Book API**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Depth-Aware-Backtester.git
cd Depth-Aware-Backtester
