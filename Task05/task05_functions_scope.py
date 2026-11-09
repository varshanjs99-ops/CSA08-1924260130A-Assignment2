# Q5 – Functions, Parameters and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_bill(price, quantity=1, *, gst_rate=0.05):
    subtotal = price * quantity
    gst = subtotal * gst_rate
    return subtotal, gst, subtotal + gst

def scope_demo():
    message = "local"
    def change_enclosed():
        nonlocal message
        message = "changed using nonlocal"
    change_enclosed()
    return message

GLOBAL_COUNT = 10
def global_demo():
    global GLOBAL_COUNT
    GLOBAL_COUNT += 1
    return GLOBAL_COUNT

if __name__ == "__main__":
    print("Buggy calls:", add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Shared default:", add_item_buggy.__defaults__)
    print("Correct calls:", add_item("Tea"), add_item("Vada"))
    print("Explicit order:", add_item("Coffee", ["Sandwich"]))
    subtotal, gst, total = calculate_bill(100, 2, gst_rate=0.05)
    print(f"Subtotal={subtotal:.2f}, GST={gst:.2f}, Total={total:.2f}")
    print("Scope:", scope_demo(), "| global:", global_demo())
