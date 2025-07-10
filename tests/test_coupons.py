from app.coupons import apply_coupon, get_final_price

def test_discount_sales():
    assert apply_coupon(100, "SALES10") == 90.0


def test_discount_summer():
    assert apply_coupon(100, "SUMMER20") == 80.0

def test_discount_welcome():
    assert apply_coupon(100, "WELCOME") == 85.0

def test_no_discount():
    assert apply_coupon(100, "INVALID") == 100.0

def test_final_price_sales():
    assert get_final_price(100, "SALES10") == 107.1

