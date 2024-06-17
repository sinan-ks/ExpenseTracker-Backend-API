from django.shortcuts import render

from django.contrib.auth.models import User

from django.utils import timezone

from django.db.models import Sum

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import status

from rest_framework import authentication, permissions

from budget.models import Expense, Income

from budget.serializers import UserSerializer, ExpenseSerializer, IncomeSerializer



# Create your views here.

class SignUpView(CreateAPIView):

    serializer_class = UserSerializer

    queryset = User.objects.all()

class ExpenseListCreateView(ListAPIView, CreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ExpenseSerializer

    queryset = Expense.objects.all()

    def get_queryset(self):  #to override query
        
        qs = Expense.objects.filter(owner=self.request.user)

        return qs
    
    def perform_create(self, serializer):  #to override serializer to save

        serializer.save(owner=self.request.user)

class ExpenseDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ExpenseSerializer

    queryset = Expense.objects.all()


class IncomeListCreateView(ListAPIView, CreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = IncomeSerializer

    queryset = Income.objects.all()

    def get_queryset(self):

        qs = Income.objects.filter(owner=self.request.user)

        return qs
    
    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)

class IncomeDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = IncomeSerializer

    queryset = Income.objects.all()
    

class TransactionSummaryView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        cur_month = timezone.now().month
        cur_year = timezone.now().year

        all_expenses = Expense.objects.filter(

            owner = request.user,
            created_date__month = cur_month,
            created_date__year = cur_year

        )

        all_incomes = Income.objects.filter(
            
            owner = request.user,
            created_date__month = cur_month,
            created_date__year = cur_year

        )

        total_expense = all_expenses.values('amount').aggregate(total=Sum('amount'))
        total_income = all_incomes.values('amount').aggregate(total=Sum('amount'))

        expense_summary = list(all_expenses.values('category').annotate(total=Sum('amount')))
        income_summary = list(all_incomes.values('category').annotate(total=Sum('amount')))

        expense_priority_summary = list(all_expenses.values('priority').annotate(total=Sum('amount')))

        data = {}

        total_income = total_income.get('total') or 0
        total_expense = total_expense.get('total') or 0

        data['savings'] = total_income - total_expense
        data['expense total'] = total_expense
        data['income total'] = total_income
        data['expense summary'] = expense_summary
        data['income summary'] = income_summary
        data['expense priority summary'] = expense_priority_summary

        return Response(data=data, status=status.HTTP_200_OK)





