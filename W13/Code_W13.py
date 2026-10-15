def calculate_total(price, quantity, discount_rate):
    gross_amount = price * quantity
    discount_amount = gross_amount * (discount_rate / 100)
    net_total = gross_amount - discount_amount
    return gross_amount, discount_amount, net_total

def main():
    print("=== Terminal Commerce System (CLI Mode) ===")
    try:
        unit_price = float(input("Enter unit price (THB): "))
        quantity = int(input("Enter quantity: "))
        discount = float(input("Enter discount (%): "))
        
        gross, disc, net = calculate_total(unit_price, quantity, discount)
        
        print("\n--- Transaction Summary ---")
        print(f"Gross Amount    : {gross:>10.2f} THB")
        print(f"Discount ({discount:>2.0f}%)  : {disc:>10.2f} THB")
        print(f"Net Total Due   : {net:>10.2f} THB")
    except ValueError:
        print("\n[Error] Invalid numeric input entered.")

if __name__ == "__main__":
    main()