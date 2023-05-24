class Catalogue:
    def __init__(self, name_catalogue):
        self.name_catalogue = name_catalogue
        self.products = []

    def add_product(self, name_products):
        self.products.append(name_products)

    def get_by_letter(self, letter):
        found = []
        self.searched_letter = letter
        for _ in range(len(self.products)):
            for el in self.products:
                product = el

                if self.searched_letter == product[0]:
                    found.append(product)

            return (found)

    def __repr__(self):
        result = "Items in the {0} catalogue:\n" \
                 "{1}".format(self.name_catalogue, '\n'.join(sorted(self.products)))
        return result



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

