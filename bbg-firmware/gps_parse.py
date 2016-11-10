def parse_gps():
    """ parse the CGNSINF response
    ('AT+CGNSINF\r\n+CGNSINF: 1,1,20161011222856.000,47.618717,-122.351538,38.000,0.80,328.3,1,,1.6,2.5,1.9,,11,8,,,38,,\r\n\r\nOK\r\n', 11)
    """
    word = "('AT+CGNSINF\r\n+CGNSINF: 1,1,20161011222856.000,47.618717,-122.351538,38.000,0.80,328.3,1,,1.6,2.5,1.9,,11,8,,,38,,\r\n\r\nOK\r\n', 11)"

    split_word = word.split(':')
    split_word = split_word[1].split('\r\n')
    split_word = split_word[0].split(',', )
    sw = split_word
    # print("Datetime: {} Lat: {} Lng: {} Alt: {} Speed: {} Course: {}"
    #       .format(sw[2], sw[3], sw[4], sw[5], sw[6], sw[7]))

    return split_word

parse_gps()
