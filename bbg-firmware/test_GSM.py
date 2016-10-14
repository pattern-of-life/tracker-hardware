def test_gps_get_data_time():
    """Test the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    from GSM import gps_get_data
    data = '+CGNSINF: 1,0,20161013174945.000,,,,0.00,0.0,0,,,,,,10,0,,,,,'
    time, lat, lng, elv, valid = gps_get_data(data)
    assert time == '20161013174945.000'


def test_gps_get_data_lat():
    """Test the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    from GSM import gps_get_data
    data = '+CGNSINF: 1,0,20161013174945.000,,,,0.00,0.0,0,,,,,,10,0,,,,,'
    time, lat, lng, elv, valid = gps_get_data(data)
    assert lat == 0


def test_gps_get_data_lng():
    """Test the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    from GSM import gps_get_data
    data = '+CGNSINF: 1,0,20161013174945.000,,,,0.00,0.0,0,,,,,,10,0,,,,,'
    time, lat, lng, elv, valid = gps_get_data(data)
    assert lng == 0


def test_gps_get_data_elv():
    """Test the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    from GSM import gps_get_data
    data = '+CGNSINF: 1,0,20161013174945.000,,,,0.00,0.0,0,,,,,,10,0,,,,,'
    time, lat, lng, elv, valid = gps_get_data(data)
    assert elv == 0


def test_gps_get_data_valid():
    """Test the CGNSINF response and return: time, lat, lng, elevation
        in a HTTP REST request format"""
    from GSM import gps_get_data
    data = '+CGNSINF: 1,0,20161013174945.000,,,,0.00,0.0,0,,,,,,10,0,,,,,'
    time, lat, lng, elv, valid = gps_get_data(data)
    assert valid is False
