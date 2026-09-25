def array_of_names(names):
    result = []

    for first_name, last_name in names.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        result.append(full_name)

    return result


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
