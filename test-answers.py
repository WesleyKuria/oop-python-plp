phone1 = Smartphone("Samsung", "Galaxy S20", 128)
phone2 = SmartphoneWithCamera("Apple", "iPhone 14", 256, 48)

print(phone1.get_info())
phone1.make_call("123-456-7890")

print(phone2.get_info())
phone2.take_photo()
