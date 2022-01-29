from search_address import search_address


def main():
    zipcode = "7984101"

    address = search_address(zipcode)

    assert "愛媛県南宇和郡愛南町御荘菊川" == address


if __name__ == '__main__':
    main()
