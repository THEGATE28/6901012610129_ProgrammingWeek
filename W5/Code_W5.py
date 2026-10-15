def find_max_index(prices):
    # ค้นหาตำแหน่งของสินค้าที่มีราคาสูงสุดด้วยลูป while
    max_val = prices[0]
    max_idx = 0
    i = 1
    while i < len(prices):
        if prices[i] > max_val:
            max_val = prices[i]
            max_idx = i
        i = i + 1
    return max_idx

def main():
    # ข้อมูลแบบ Parallel Lists
    products = ["Apple", "Banana", "Orange", "Grape"]
    prices = [1.20, 0.80, 1.50, 2.00]
    stocks = [30, 50, 20, 15]

    total_price = 0
    total_stock_value = 0
    i = 0

    # วนลูปอ่านข้อมูลและคำนวณผลรวม
    while i < len(products):
        print(f"Product [{i}]: {products[i]} | Price: ${prices[i]:.2f} | Stock: {stocks[i]}")
        total_price = total_price + prices[i]
        total_stock_value = total_stock_value + (prices[i] * stocks[i])
        i = i + 1

    # คำนวณค่าเฉลี่ยและหาค่าสูงสุด
    avg_price = total_price / len(prices)
    max_idx = find_max_index(prices)

    print("\n--- Summary Report ---")
    print(f"Average Price: ${avg_price:.2f}")
    print(f"Total Inventory Value: ${total_stock_value:.2f}")
    print(f"Most Expensive Item: {products[max_idx]} (${prices[max_idx]:.2f})")

if __name__ == "__main__":
    main()