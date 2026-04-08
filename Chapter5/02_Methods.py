a={
    "harry":200,
    "Mansha":300,
    "Micky":500,
    600:"Aman"
}

print(a.items())  # dict_items([('harry', 200), ('Mansha', 300), ('Micky', 500), (600, 'Aman')])
print(a.keys())   # dict_keys(['harry', 'Mansha', 'Micky', 600])

a.update({"harry":600})
print(a) 

print(a.get("Harry2")) # Ptint none
# print(a["Harry"]) # return error 

# {'harry': 600, 'Mansha': 300, 'Micky': 500, 600: 'Aman'}