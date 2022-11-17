"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from core.views import *

'''
2. Categorías-1

a. Registrar Categorías(POST)
b. Modificar Categorías(PUT)
c. Obtener todas las Categorías(GET)
d. Obtener Categoría por Nombre(ORM-FILTRAR POR NOMBRE CATEGORY)
e. Eliminar Categorías(DEL)

'''

urlpatterns = [
    path('admin/', admin.site.urls),

    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<int:category_id>', CategoryView.as_view(), name='category'),

    path('author/', AuthorView.as_view(), name='authors'),
    path('author/<int:author_id>', AuthorView.as_view(), name='author'),

    path('partner/', PartnerView.as_view(), name='partners'),
    path('partner/<int:partner_id>', PartnerView.as_view(), name='partner'),

    path('book/', BookView.as_view(), name='books'),
    path('book/<int:book_id>', BookView.as_view(), name='book'),

    path('book_loan/', BookLoanView.as_view(), name='books_loan'),
    path('book_loan/<int:book_loan_id>', BookLoanView.as_view(), name='book_loan'),


    path('categories_with_name/<str:name>', CategoryViewWithOrm.as_view(), name='category'),
    path('author_with_last_name/<str:last_name>', AuthorViewWithOrm.as_view(), name='author'),
    path('book_with_author/<str:author>', BookViewWithOrm.as_view(), name='book'),
    path('partner_with_dni/<str:dni>', PartnerViewWithOrm.as_view(), name='partner'),
    path('book_loan_with_dni/<str:dni>', BookLoanViewWithOrm.as_view(), name='book_loan'),
    path('book_loan_with_status/<str:status>', BookLoanViewWithOrm2.as_view(), name='book_loan')

]
