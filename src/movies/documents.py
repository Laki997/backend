from django.db.models.fields import BooleanField
from django_elasticsearch_dsl import (
    Document, fields, Index
)
from elasticsearch_dsl import analyzer, field
from .models import Movie


html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    bool=["standard", "lowercase",],
    char_filter=["html_strip"]
)
PUBLISHER_INDEX = Index('movie')

PUBLISHER_INDEX.settings(
     number_of_shards=1,
     number_of_replicas=0
 )

@PUBLISHER_INDEX.doc_type
class MovieDocument(Document):
    id = fields.IntegerField(attr='id')
    title = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField()
        }
    )
    description = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField()
        }
    )
    cover_image = fields.TextField(
         analyzer=html_strip,
         fields={'raw': fields.TextField()}
     )
    isWatched = fields.ObjectField(
        attr='isWatched',
        properties={'watched': fields.BooleanField(),
                     'movie': fields.ObjectField(properties={'pk':fields.IntegerField()})}
    )
  
    genre = fields.TextField(
        analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )
    view_count = fields.IntegerField(attr='view_count')
    likes = fields.IntegerField()
    dislikes = fields.IntegerField()

    class Django:
        model = Movie
