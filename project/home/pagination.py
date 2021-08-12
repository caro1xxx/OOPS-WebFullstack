# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 8:53
# @Author  : XobNcaro1xxx
# @File    : pagination.py
# @Software: PyCharm


from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = 'size'  # ?page=xx&size=??
    max_page_size = 999  # max page size