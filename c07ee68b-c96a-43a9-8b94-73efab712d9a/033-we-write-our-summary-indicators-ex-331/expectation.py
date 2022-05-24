
sol = """
# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(.75) - column.quantile(.25)

# Print IQR and median of temperature_c, fuel_price_usd_per_l, and unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([np.median, iqr]))
"""

Ex().check_or(
  check_correct(
     has_equal_output(incorrect_msg="Вы объединили столбцы `temperature_c`, `fuel_price_usd_per_l` и `unemployment` в таком порядке, используя `.agg()` с пользовательской функцией `iqr` и `np.median` и распечатали результат?"),
     multi(
      check_function("sales.agg").check_args(0).has_equal_ast(incorrect_msg="Вы передали список, содержащий две функции агрегирования, `iqr` и `np.median`, в `.agg()`?"),
      has_code("sales\[\[\s*(\"|\')temperature_c(\"|\')\s*,\s*(\"|\')fuel_price_usd_per_l(\"|\')\s*,\s*(\"|\')unemployment(\"|\')\s*\]\]", not_typed_msg="Вы выбрали правильный столбец перед агрегированием?"),
    )
   ),
 override(sol).check_correct(
     has_equal_output(incorrect_msg="Вы объединили столбцы `temperature_c`, `fuel_price_usd_per_l` и `unemployment` в таком порядке, используя `.agg()` с пользовательской функцией `iqr` и `np.median` и распечатали результат?"),
     multi(
      check_function("sales.agg").check_args(0).has_equal_ast(incorrect_msg="Вы передали список, содержащий две функции агрегации?"),
      has_code("sales\[\[\s*(\"|\')temperature_c(\"|\')\s*,\s*(\"|\')fuel_price_usd_per_l(\"|\')\s*,\s*(\"|\')unemployment(\"|\')\s*\]\]", not_typed_msg="Вы выбрали правильный столбец перед агрегированием?"),
    )
   )
)


success_msg(
    """ Превосходная эффективность! Метод .agg() позволяет легко вычислять несколько 
        статистических данных по нескольким столбцам, и все это всего в одной строке кода."""
)
