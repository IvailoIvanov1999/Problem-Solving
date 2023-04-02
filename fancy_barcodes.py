import re

n = int(input())

pattern = r"@#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])@#{1,}"

pattern_find_digits = r"\d"

for _ in range(n):
    product_group = ""
    barcodes_input = input()

    barcode = re.findall(pattern,barcodes_input)
    if not barcode:
        print("Invalid barcode")
    else:

        digits = re.findall(pattern_find_digits,"".join(barcode))

        if not digits:
            product_group = "00"
        else:
            for d in digits:
                product_group += d

        print(f"Product group: {product_group}")


