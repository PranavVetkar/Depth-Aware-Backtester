import ccxt

class DepthAnalyzer:
    def __init__(self, symbol='BTC/USDT'):
        self.exchange = ccxt.binance()
        self.symbol = symbol

    def calculate_slippage(self, target_amount_usd):
        order_book = self.exchange.fetch_order_book(self.symbol, limit=100)
        asks = order_book['asks']
        
        accumulated_usd = 0
        accumulated_btc = 0
        
        print(f"--- Analyzing Depth for ${target_amount_usd:,.2f} Buy Order ---")
        
        for price, volume in asks:
            cost_at_this_level = price * volume
            
            if accumulated_usd + cost_at_this_level >= target_amount_usd:
                remaining_usd = target_amount_usd - accumulated_usd
                accumulated_btc += remaining_usd / price
                accumulated_usd = target_amount_usd
                break
            else:
                accumulated_usd += cost_at_this_level
                accumulated_btc += volume

        avg_price = accumulated_usd / accumulated_btc
        market_price = asks[0][0]
        slippage_pct = ((avg_price - market_price) / market_price) * 100
        
        print(f"Best Market Price: ${market_price:,.2f}")
        print(f"Your Average Fill: ${avg_price:,.2f}")
        print(f"Total Slippage: {slippage_pct:.4f}%")
        return slippage_pct

if __name__ == "__main__":
    analyzer = DepthAnalyzer()
    analyzer.calculate_slippage(target_amount_usd=500000)