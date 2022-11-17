from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.status import *
from django.core.serializers import serialize
import json
from core.models import *
from datetime import datetime
from django.db import IntegrityError


# importar todos nuestros modedelos
# Create your views here.

# Category
class CategoryView(APIView):

    def get(self, request, category_id=None):
        if category_id:
            if Category.objects.filter(pk=category_id).exists():
                category_response = Category.objects.filter(pk=category_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Category not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            category_response = list(Category.objects.all())
        category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=category_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        category, created = Category.objects.get_or_create(**body)
        if created:
            category.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        category.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category deleted successfully'}),
                            status=HTTP_200_OK)


# Author
class AuthorView(APIView):
    def get(self, request, author_id=None):
        if author_id:
            if Author.objects.filter(pk=author_id).exists():
                author_response = Author.objects.filter(pk=author_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            author_response = Author.objects.all()
        author_response = serialize('json', author_response)
        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        author, created = Author.objects.get_or_create(**body)  # (actor, created)
        if created:
            author.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        author.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        author.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author deleted successfully'}),
                            status=HTTP_200_OK)


# Partner
class PartnerView(APIView):
    def get(self, request, partner_id=None):
        if partner_id:
            if Partner.objects.filter(pk=partner_id).exists():
                partner_response = Partner.objects.filter(pk=partner_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            partner_response = Partner.objects.all()
        partner_response = serialize('json', partner_response)
        return HttpResponse(content_type='application/json',
                            content=partner_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        partner, created = Partner.objects.get_or_create(**body)  # (actor, created)
        if created:
            partner.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        partner.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        partner.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner deleted successfully'}),
                            status=HTTP_200_OK)


# Movie
class BookView(APIView):

    def get(self, request, book_id=None):
        if book_id:
            if Book.objects.filter(pk=book_id).exists():
                book_response = Book.objects.get(pk=book_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_response = list(Book.objects.all())
        book_response = serialize('json', book_response)
        return HttpResponse(content_type='application/json',
                            content=book_response,
                            status=HTTP_200_OK)

    # revisarlo esta bien para mi
    def post(self, request):
        body = json.loads(request.body)
        body['author'] = Author.objects.get(pk=body['author'])
        body['category'] = Category.objects.get(pk=body['category'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        book.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        book.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book deleted successfully'}),
                            status=HTTP_200_OK)


# Book Loan
class BookLoanView(APIView):
    def get(self, request, book_loan_id=None):
        if book_loan_id:
            if BookLoan.objects.filter(pk=book_loan_id).exists():
                book_loan_response = BookLoan.objects.filter(pk=book_loan_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book Loan not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_loan_response = BookLoan.objects.all()
        book_loan_response = serialize('json', book_loan_response)
        return HttpResponse(content_type='application/json',
                            content=book_loan_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['book'] = Book.objects.get(pk=body['book'])
        body['partner'] = Partner.objects.get(pk=body['partner'])
        book_loan, created = BookLoan.objects.get_or_create(**body)
        if created:
            book_loan.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book Loan created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book Loan already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_loan_id):
        book_loan = BookLoan.objects.filter(pk=book_loan_id)
        if not book_loan.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book Loan not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        book_loan.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book Loan updated successfully'}),
                            status=HTTP_200_OK)


# Category orm
class CategoryViewWithOrm(APIView):

    def get(self, request, name):
        # Obtener Categoría por Nombre(ORM-FILTRAR POR NOMBRE CATEGORY)
        queryset_iexact_field = list(Category.objects.filter(name__iexact=name).values("name",
                                                                                       "recommended_age"))

        if queryset_iexact_field:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'exact_field': queryset_iexact_field}),
                                status=HTTP_200_OK)

        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)


# Author orm
class AuthorViewWithOrm(APIView):

    def get(self, request, last_name):
        # Obtener Autores por Apellido
        queryset_iexact_field = list(Author.objects.filter(last_name__iexact=last_name).values("first_name",
                                                                                               "last_name"))

        if queryset_iexact_field:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'exact_field': queryset_iexact_field}),
                                status=HTTP_200_OK)

        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)


# Book orm
class BookViewWithOrm(APIView):
    def get(self, request, author):
        # Obtener Libros por Autor
        queryset_iexact_field = list(Book.objects.filter(author__last_name__iexact=author).values("name",
                                                                                                  "author__first_name",
                                                                                                  "author__last_name", ))

        if queryset_iexact_field:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'exact_field': queryset_iexact_field}),
                                status=HTTP_200_OK)

        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)


# Partner orm
class PartnerViewWithOrm(APIView):
    def get(self, request, dni):
        # Obtener Socio por DNI
        queryset_iexact_field = list(Partner.objects.filter(dni__iexact=dni).values("first_name",
                                                                                    "last_name",
                                                                                    "dni"))
        if queryset_iexact_field:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'exact_field': queryset_iexact_field}),
                                status=HTTP_200_OK)

        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)


# Book Loan orm
class BookLoanViewWithOrm(APIView):
    def get(self, request, dni):
        # Obtener Préstamos por DNI de Socio
        queryset_foreignkey_field = list(BookLoan.objects.filter(partner__dni__iexact=dni).values("status",
                                                                                                  "book__name",
                                                                                                  "partner__first_name",
                                                                                                  "partner__last_name"))

        if queryset_foreignkey_field:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'exact_field': queryset_foreignkey_field}),
                                status=HTTP_200_OK)

        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book Loan not found'}),
                                status=HTTP_404_NOT_FOUND)


# Book Loan orm 2
class BookLoanViewWithOrm2(APIView):
    def get(self, request, status):
        # Obtener los Préstamos por estado
        queryset_iexact_field = list(BookLoan.objects.filter(status__iexact=status).values("status",
                                                                                           "book__name",
                                                                                           "partner__first_name",
                                                                                           "partner__last_name"))
        if queryset_iexact_field:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'exact_field': queryset_iexact_field}),
                                status=HTTP_200_OK)

        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)


'''
CONSIGNAS
Endpoints a Presentar
1. Libros
PREGUNTAR BOOK
a. Registrar Libros (POST)
b. Modificar Libros (PUT)
c. Obtener todos los Libros(GET)
d. Obtener Libros por Autor(ORM-FORENKEY FILTRAR POR AUTOR)
e. Eliminar Libros (DELETE)


'''

'''
2. Categorías-1

a. Registrar Categorías(POST)
b. Modificar Categorías(PUT)
c. Obtener todas las Categorías(GET)
d. Obtener Categoría por Nombre(ORM-FILTRAR POR NOMBRE CATEGORY)
e. Eliminar Categorías(DEL)

'''
'''
3. Autores-1

a. Registrar Autores(POST)
b. Modificar Autores(PUT)
c. Obtener todos los Autores(GET)
d. Obtener Autores por Apellido(ORM-FILTRAR POR APELLIDO AUTHOR)
e. Eliminar Autores(DEL)


'''

'''
4. Socios-Many to many

a. Registrar Socios(POST)
b. Modificar Socios(UPDATE)
c. Obtener todos los Socios(GET)
d. Obtener Socio por DNI(ORM-FILTRAR POR DNI PARTNER)
e. Eliminar Socios(DEL)


'''

'''
FALTA
5. Préstamos

a. Registrar Préstamo de Libros(POST)
b. Modificar estado del Préstamo(PUT)
c. Obtener todos los Préstamos(GET)
d. Obtener Préstamos por DNI de Socio(ORM-FILTRAR POR DNI PARTNER)
e. Obtener los Préstamos por estado(ORM-FILTRAR POR ESTADO BOOL LOAN)

'''
