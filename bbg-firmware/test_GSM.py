def test_gps_get_data():
    """Test the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    from GSM import gps_get_data
    assert gps_get_data("[]") == False
