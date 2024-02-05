from django.contrib import admin
from .models import Excel_file

import csv
from django.http import HttpResponse

import pandas as pd
# Register your models here.







@admin.register(Excel_file)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['Year', 'Industry_aggregation_NZSIOC','Industry_code_NZSIOC','Industry_name_NZSIOC','Units','Variable_code','Variable_name','Variable_category','Value','Industry_code_ANZSIC06']  # Modelni ro'yxatda ko'rsatish uchun kerakli ustunlarni tanlang

    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        # Fayl nomini o'zgartiring kerakli ko'rinishda
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="my_model_data.csv"'

        # CSV faylini yaratish
        writer = csv.writer(response)
        writer.writerow(['Year', 'Industry_aggregation_NZSIOC','Industry_code_NZSIOC','Industry_name_NZSIOC','Units','Variable_code','Variable_name','Variable_category','Value','Industry_code_ANZSIC06'])  # Ustun nomlari

        # Ma'lumotlarni yozish
        for obj in queryset:
            writer.writerow([obj.name, obj.age])  # Qo'shimcha maydonlar...

        return response

    export_to_excel.short_description = "Ma'lumotlarni Excel ga eksport qilish"
