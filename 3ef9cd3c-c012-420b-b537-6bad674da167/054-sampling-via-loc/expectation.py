

msg1 = "Использовали ли вы квадратные скобки для правильной фильтрации `temperatures` для строк, где столбец `city` принимает значение в `cities`?"
msg2 = "Использовали ли вы `.using()` для фильтрации `temperatures` для строк, где столбец `city` принимает значение в `cities`?"
msg3 = "Правильно ли вы использовали подмножество `.loc[]` для фильтрации `temperature_ind`?"

Ex().multi(
    check_object('cities').has_equal_value(override=["Москва", "Санкт-Петербург"]),

    check_function("print", 0).multi(
        has_equal_ast(code="temperatures['city']", exact=True, incorrect_msg=msg1),
        has_equal_ast(code="temperatures[temperatures['city'].isin(cities)]", exact=False, incorrect_msg=msg2),
    ),
    check_function("print", 1).multi(
        has_equal_ast(code="temperatures_ind.loc[cities]", exact=False, incorrect_msg=msg3),
    ),
)


success_msg(
    """ .loc[] используется всеми лучшими людьми! Установка индекса позволяет 
        использовать более сжатый код для подстановки строк через .loc[]."""
)
