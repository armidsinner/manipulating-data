
Ex().multi(
    check_correct(
        check_object('ind_city').has_equal_value(),
        multi(
            has_code(r"""\[\s*["']individuals["']\s*,\s*["']city["']\s*\]""", not_typed_msg="Правильно ли вы выбрали столбцы `individuals` и `city`?"),

            has_equal_ast(code="census[['individuals', 'city']]", incorrect_msg="Использовали ли вы правильный синтаксис для выбора нескольких столбцов?")
        )
    ),

    check_function('ind_city.head').has_equal_value(),
    check_function('print').check_args(0).has_equal_value(),

)


success_msg(
    """ Радикальное изменение порядка! 
        Выбор и изменение порядка столбцов могут упростить работу с данными."""
)
