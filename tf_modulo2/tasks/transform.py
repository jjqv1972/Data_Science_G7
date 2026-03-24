
def transform(data):
    """
    transformamos la data de paises
    """
    transform_data = []
    for user in data:
        nombre = f"{user['name']['common']}"
        capital = user['capital'][0]
        region = user['region']
        poblacion = user['population']
        transform_data.append((nombre,capital,region,poblacion))
    
    return transform_data