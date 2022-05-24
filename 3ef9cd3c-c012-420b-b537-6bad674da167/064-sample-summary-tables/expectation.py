

msg1 = "Вы использовали .loc[] в temp_by_country_city_vs_year для среза от Египет до Индия?"
msg2 = "Использовали ли вы .loc[] в temp_by_country_city_vs_year для среза от Египет, Каир до Индия, Дели?"
msg3 = "Использовали ли вы .loc[] в temp_by_country_city_vs_year для среза от Египет, Каир до Индия, Дели и с 2005 по 2010 год?"


Ex().multi(

    has_equal_ast(code="temp_by_country_city_vs_year.loc['Египет':'Индия']", exact=False, incorrect_msg=msg1),
    has_equal_ast(code="temp_by_country_city_vs_year.loc[('Египет', 'Каир'):('Индия', 'Дели')]", exact=False, incorrect_msg=msg2),
    has_equal_ast(code="temp_by_country_city_vs_year.loc[('Египет', 'Каир'):('Индия', 'Дели'), '2005':'2010']", exact=False, incorrect_msg=msg3),

)

success_msg(
    """ Супер! 
        Нарезка особенно полезна для создания сводных таблиц."""
)
