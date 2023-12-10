subgroups = {
    'government': 'nhanuoc',
    'diploma-border': 'boderngoaigiao',
    'diploma-rotate': 'rotatengoaigiao',
    'diploma-brightness': 'brightnessngoaigiao',
    'diploma-crop': 'cropngoaigiao',
    'military-border': 'boderquandoi',
    'military-brightness': 'brightnessquandoi',
    'military-crop': 'cropquandoi',
    'military-rotate': 'rotatequandoi',
    'military': 'quandoi',
    'business': 'kinhdoanh',
    'citizen-long': 'CarLongPlate',
    'citizen-big': ['xemayBigPlate', 'xemay'],
    'unknown': '*'
}
def swap_dict_keys_values(dictionary):
    swapped_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, list):
            for item in value:
                if item not in swapped_dict:
                    swapped_dict[item] = key
                else:
                    swapped_dict[item].append(key)
        else:
            swapped_dict[value] = key
    return swapped_dict
swapped_subgroups = swap_dict_keys_values(subgroups)
print(swapped_subgroups)