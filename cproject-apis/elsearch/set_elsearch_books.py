books_table = '/home/aayush_linux/Downloads/college-project/cproject/common/search/books.json'  ## path to books_data.json

import typesense
import json

client = typesense.Client({
                          'master_node': {
                          'host': 'localhost',
                          'port': '8108',
                          'protocol': 'http',
                          'api_key': 'pNCB36PlZveIL9s8XmvVZM1KFM6BFmwG8F6BaOKQCNIrkHGY'
                          },
                          'timeout_seconds': 2
                          })


books_schema = {
    'name': 'temp5',
        'fields': [
                   {'name': 'book_id', 'type': 'int32' },
                   {'name': 'title', 'type': 'string' },
                   {'name': 'author', 'type': 'string' },
                   {'name': 'publication', 'type': 'string' },
                   {'name': 'isbn', 'type': 'string' },
                   {'name': 'qty', 'type': 'int32' },
                   {'name': 'is_out_of_stack', 'type': 'string' },
                   ],
            'default_sorting_field': 'book_id'
}


client.collections.create(books_schema)


with open('/home/aayush_linux/Downloads/college-project/cproject/common/search/books.jsonl') as infile:
  for json_line in infile:
    book_document = json.loads(json_line)
    client.collections['temp5'].documents.create(book_document)

