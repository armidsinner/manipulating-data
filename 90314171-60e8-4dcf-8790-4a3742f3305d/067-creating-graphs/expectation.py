

msg = "После группировки по размеру вы выбрали столбец `nb_sold` перед подсчетом суммы?"

Ex().multi(
    has_import("matplotlib.pyplot", same_as=True),
    check_function('apples.head', 0, signature=False).has_equal_value(),
    check_function('print', 0, signature=False).has_equal_ast(),
    check_function('apples.groupby', 0, signature=False).check_args(0).has_equal_value(),
    has_equal_ast(code="apples.groupby('size')['nb_sold']", exact=False, incorrect_msg=msg),
    check_function('apples.groupby.sum', 0, signature=False).has_equal_value(),
    check_object("nb_sold_by_size"),
    check_function('nb_sold_by_size.plot', 0, signature=False).check_args(0).has_equal_value(),
    check_function('matplotlib.pyplot.show', 0, signature=False).has_equal_value(),
)

success_msg(
    """ Отличная работа! Похоже, что маленькие яблоки были самого покупаемого размера, 
        но большие яблоки были близки ко второму."""
)
