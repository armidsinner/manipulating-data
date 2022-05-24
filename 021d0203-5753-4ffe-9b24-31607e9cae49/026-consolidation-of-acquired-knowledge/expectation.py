

Ex().multi(
    check_correct(
        check_df("census").check_keys("indiv_per_10k").has_equal_value(),
        has_equal_ast(code="census['individuals'] + census['family_members']",
                      incorrect_msg="Вы правильно нашли количество одиноких на 10000 человек в каждом регионе?")
    ),

    check_correct(
        check_object('high_census').has_equal_value(),
        has_equal_ast(code="census[census['indiv_per_10k'] > 20]",
                      incorrect_msg="Правильно ли вы отфильтровали `census`, чтобы включить "
                                    "только строки с `indiv_per_10k`, превышающим 20?")
    ),

    check_correct(
        check_object('high_census_srt').has_equal_value(),
        check_function("high_census.sort_values").multi(
            check_args(0).has_equal_value(),
            check_args(1).has_equal_value(),
        )
    ),

    check_correct(
        check_object('result').has_equal_value(),
        multi(
            has_code(r"""\[\s*["']city["']\s*,\s*["']indiv_per_10k["']\s*\]""",
                     not_typed_msg="Правильно ли вы выбрали столбцы `city` и `indiv_per_10k`?"),

            has_equal_ast(code="high_census_srt[['city', 'indiv_per_10k']]",
                          incorrect_msg="Использовали ли вы правильный синтаксис для выбора нескольких столбцов?")
        )
    ),
    check_function("print").check_args(0).has_equal_value()

)



success_msg(
    """ Супер! В Калининграде, самое большое число одиноких - почти 54 
        на десять тысяч человек. Это почти вдвое больше, чем в Тюмени. 
        Если вы объедините добавление новых столбцов, набор подмножеств строк, 
        сортировку и выбор столбцов, вы сможете ответить на множество подобных вопросов."""
)
