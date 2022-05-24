

msg1 = "Правильно ли вы вычислили `.mean()` столбца `weekly_sales`?"
msg2 = "Правильно ли вы вычислили `.median()` столбца `weekly_sales`?"

Ex().multi(
  check_function("sales.head"),
  check_function("sales.info"),
  check_function("print", index=3, missing_msg="Вы распечатали медиану столбца `weekly_sales`?").check_args(0).has_equal_value("Правильно ли вы вычислили `.median()` столбца `weekly_sales`?"),
  check_function("print", index=2, missing_msg="Вы распечатали среднее значение столбца `weekly_sales`?").check_args(0).has_equal_value("Правильно ли вы вычислили `.mean()` столбца `weekly_sales`?"),
  check_function("print", index=1, missing_msg="Вы распечатали информацию о DataFrame `sales`?").check_args(0).has_equal_value("Вы напечатали `.info()` о DataFrame `sales`?"),
  check_function("print", index=0, missing_msg="Вы распечатали заголовок DataFrame `sales`?").check_args(0).has_equal_value("Вы напечатали `.head()` DataFrame `sales`?"),
)


success_msg(
    """ Средний объем еженедельных продаж почти вдвое превышает средний объем еженедельных продаж! 
        Это может сказать вам, что есть несколько недель с очень высокими продажами, 
        из-за которых среднее значение намного превышает медиану."""
)
