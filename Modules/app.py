import reports

# Generar reporte de ventas y gastos usando funciones del módulo
sales = reports.generate_sales_report('April', 10000)
expenses = reports.generate_expenses_report('April', 5000)

print(sales)
print(expenses)