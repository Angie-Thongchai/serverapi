from django.urls import path
from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats

urlpatterns = [
    path('expenses_category_data', ExpenseSummaryStats.as_view(),
         name='expenses-category-summary'),
    path('income_source_data', IncomeSourcesSummaryStats.as_view(),
         name='income-source-summary')

]