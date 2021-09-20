from rest_framework.pagination import CursorPagination

class ProductPagination(CursorPagination):
    page_size = 3
    cursor_query_param = 'id'
    ordering = '-price'
