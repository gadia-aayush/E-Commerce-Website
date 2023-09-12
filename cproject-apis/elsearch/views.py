from django.shortcuts import render
from django.template.loader import get_template
import typesense
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect


# Create your views here.
def search_q(request,qry,pg):

    """ Search For books"""
    query = qry
    client = typesense.Client({
                              'master_node': {
                              'host': 'localhost',
                              'port': '8108',
                              'protocol': 'http',
                              'api_key': 'pNCB36PlZveIL9s8XmvVZM1KFM6BFmwG8F6BaOKQCNIrkHGY'
                              },
                              'timeout_seconds': 2
                              })

    search_parameters = {
    'q'         :  query,
    'query_by'  : 'title,author,publication,isbn',
    'sort_by'   : 'book_id:desc',
    'page'      : pg,
    }
    result = client.collections['temp5'].documents.search(search_parameters)
    return JsonResponse(result)

