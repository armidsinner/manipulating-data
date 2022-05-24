

msg1 = "Объект temperature_bool должен содержать 2400 строк (1200 с 2010 года и 1200 с 2011 года)."
msg2 = "Использовали ли вы .loc[] для среза строк в 2010 и 2011 годах?"
msg3 = "Использовали ли вы .loc[] для выборки с августа (8-го месяца) 2010 года по февраль (2-й месяц) 2011 года?"


Ex().multi(

    check_object("temperatures_bool"),
    has_equal_ast(code="(temperatures['date'] >= '2010-01-01')", exact=False,
                  incorrect_msg=msg1),
    has_equal_ast(code="(temperatures['date'] <= '2011-12-31')", exact=False,
                  incorrect_msg=msg1),

    check_function("print", 0).check_args(0).has_equal_value(),

    check_function("print", 1).multi(
        has_equal_ast(code="temperatures_ind.loc['2010':'2011']",
                      exact=False, incorrect_msg=msg2),
    ),
    check_function("print", 1).check_args(0).has_equal_value(),

    check_function("print", 2).multi(
        has_equal_ast(code="temperatures_ind.loc['2010-08':'2011-02']",
                      exact=False, incorrect_msg=msg3),
    ),
    check_function("print", 2).check_args(0).has_equal_value(),

)



success_msg(
    """ Восхитительная нарезка диапазона данных! Использование .loc[] в сочетании с индексом данных 
        обеспечивает простой способ выборки строк до или после некоторой даты."""
)
