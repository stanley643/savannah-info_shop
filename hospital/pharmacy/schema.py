import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Order

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    all_orders = graphene.List(OrderType)

    def resolve_all_customers(self, info, **kwargs):
        return Customer.objects.all()
    
    def resolve_all_orders(self, info, **kwargs):
        return Order.objects.all()
    
schema = graphene.Schema(query=Query)
