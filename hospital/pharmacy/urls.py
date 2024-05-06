from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphiql.views import GraphQLView  # corrected import statement

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
