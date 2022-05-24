

msg = "После группировки по дате вы выбрали столбец `nb_sold` перед подсчетом суммы?"

Ex().multi(
    has_import("matplotlib.pyplot", same_as=True),
    check_function('apples.groupby', 0, signature=False).check_args(0).has_equal_value(),
    has_equal_ast(code="apples.groupby('date')['nb_sold']", exact=False, incorrect_msg=msg),
    check_function('apples.groupby.sum', 0, signature=False).has_equal_value(),
    check_object("nb_sold_by_date"),
    check_function('nb_sold_by_date.plot', 0, signature=False).check_args(0).has_equal_value(),
    check_function('matplotlib.pyplot.show', 0, signature=False).has_equal_value(),
)



success_msg(
    """ Прекрасно! Графики отлично подходят
        для визуализации чего-либо с течением времени. Здесь, похоже, количество 
        яблок растет примерно в одно и то же время каждый год."""
)
