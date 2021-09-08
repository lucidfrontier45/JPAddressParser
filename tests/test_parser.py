from jpaddressparser import Address, get_default_parser


def test_parser():
    parser = get_default_parser()
    address_str = "東京都千代田区永田町１丁目７－１"
    parserd_addr = parser.parse(address_str)
    assert parserd_addr == Address("東京都", "千代田区", "永田町", "1丁目7-1")
