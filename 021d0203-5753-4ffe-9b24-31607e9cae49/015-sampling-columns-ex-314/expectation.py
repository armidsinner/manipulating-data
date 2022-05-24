

Ex().multi(
    check_correct(
        check_object('city_fam').has_equal_value(),
        multi(
            has_code(r"""\[\s*["']city["']\s*,\s*["']family_members["']\s*\]""", not_typed_msg="Правильно ли вы выбрали столбцы `city` и `family_members`?"),

            has_equal_ast(code="census[['city', 'family_members']]", incorrect_msg="Использовали ли вы правильный синтаксис для выбора нескольких столбцов?")
        )
    ),

    check_function('city_fam.head').has_equal_value(),
    check_function('print').check_args(0).has_equal_value(),

)
