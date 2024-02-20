def cakes(eggs, butter, flour):
    ingredients_list = {"eggs": 5, "butter": 250, "flour": 250}

    total_cakes = min(
        eggs // ingredients_list["eggs"],
        butter // ingredients_list["butter"],
        flour // ingredients_list["flour"],
    )
    return total_cakes
