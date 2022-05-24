

Ex().check_function("print").check_args(0).has_code("sales", not_typed_msg="Вы указали DataFrame?"),

Ex().check_not(
  has_code("iqr\(\s*\)"),
  incorrect_msg="Вы не должны включать круглые скобки при указании функции агрегирования."
)

Ex().check_not(
  has_code("iqr\(.*temperature_c.*\)"),
  incorrect_msg="Вы должны использовать только *имя* функции внутри агрегации `.agg()`, не передавая функции никаких параметров."
)



alt_sol="""
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales.temperature_c.agg(iqr))
"""

msg="Вы объединили столбец `temperature_c` фрейма данных `sales` с помощью `.agg()` с пользовательской функцией `iqr'?"

Ex().check_correct(
  has_equal_output(incorrect_msg = msg),
  multi(
   check_or(
     check_function("sales.agg", missing_msg=msg).check_args(0).has_equal_ast(),
     override(alt_sol).check_function("sales.temperature_c.agg").check_args(0).has_equal_ast(),
   ),
   check_or( # the first check_function will let sales.agg(iqr) slide...
     has_code("(\"|\')temperature_c(\"|\')", not_typed_msg="Вы выбрали столбец `temperature_c` перед агрегированием?"),
     has_code("sales\.temperature_c", not_typed_msg="Вы выбрали столбец `temperature_c` перед агрегированием?")
   )
 )
)
