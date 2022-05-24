

Ex().check_not(
  has_code('print(sales["temperature_c"].agg(iqr))', pattern=False),
  incorrect_msg="Вам необходимо изменить код."
)

Ex().check_not(
  has_code('sales\[\s*(\"|\')temperature_c(\"|\')\s*,\s*(\"|\')fuel_price_usd_per_l(\"|\')\s*,\s*(\"|\')unemployment(\"|\')\s*\]\.agg'),
  incorrect_msg="Не забывайте использовать двойные скобки `[[.., .., ...]]` при выборе нескольких столбцов!"
)

Ex().check_not(
  has_code("iqr\(\s*\)"),
  incorrect_msg="Вы не должны включать круглые скобки при указании функции агрегирования."
)
Ex().check_correct(
   has_equal_output(incorrect_msg="Суммировали ли вы столбцы `temperature_c`, `fuel_price_usd_per_l` и `unemployment` в таком порядке, используя `.agg()` с пользовательской функцией `iqr` и распечатали результат? "),
   multi(
    check_function("sales.agg").check_args(0).has_equal_ast(),
     check_not(has_code("fuel_price_usd_per_1"), incorrect_msg="Дважды проверьте, правильно ли вы вводите `fuel_price_usd_per_l`. Имя `fuel_price_usd_per_l` заканчивается строчной буквой 'L', а не цифрой 1."),
    has_code("sales\[\[\s*(\"|\')temperature_c(\"|\')\s*,\s*(\"|\')fuel_price_usd_per_l(\"|\')\s*,\s*(\"|\')unemployment(\"|\')\s*\]\]", not_typed_msg="Вы выбрали правильный столбец перед агрегированием?")
     )
  )
