from app.api import app

def test_get_price_sucess():
    client = app.test_client()
    response = client.post('/price', json={
        'price': 100,
        'coupon': 'SALES10',
        'tax_rate': 0.19
    })
    assert response.status_code == 200

def test_get_price_invalid_coupon():
    client = app.test_client()
    response = client.post('/price', json={
        'price': "100",
        'coupon': 'SALES10',
        'tax_rate': 0.19
    })
    assert response.status_code == 500
    
  