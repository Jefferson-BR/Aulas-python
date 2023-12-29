carros = ['BMW', 'Mercedez-Benz', 'Audi', 'Ferrari', 'Dodge', 'Honda', 'Jagauar', 'Koenigsseg']
print("Essa é a lista original:  ", '\n')
print(carros)

carros = ['BMW', 'Mercedez-Benz', 'Audi', 'Ferrari', 'Dodge', 'Honda', 'Jagauar', 'Koenigsseg']
carros.sort()
print('\n', "Essa é a lista alterada de forma permanente: ", '\n')
print(carros)

print('\n', "Essa é a lista alterada temporariamente: ", '\n')
print(sorted(carros))

# sort() - altera a lista permanentemente.

# sorted() - altera a lista temporariamente.