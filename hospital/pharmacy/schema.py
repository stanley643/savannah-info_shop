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
    orders_by_customer = graphene.List(OrderType, customer_code=graphene.String())
    customers_by_order = graphene.List(CustomerType, order_item=graphene.String())
    total_orders_by_customer = graphene.Int(customer_code=graphene.String())


    def resolve_all_customers(self, info, **kwargs):
        return Customer.objects.all()
    
    def resolve_all_orders(self, info, **kwargs):
        return Order.objects.all()
    
    def resolve_orders_by_customer(self, info, customer_code, **kwargs):
        return Order.objects.filter(customer__code=customer_code)
    
    def resolve_customers_by_order(self, info, order_item, **kwargs):
        return Customer.objects.filter(order__item=order_item)
    
    def resolve_total_orders_by_customer(self, info, customer_code, **kwargs):
        return Order.objects.filter(customer__code=customer_code).count()
    
schema = graphene.Schema(query=Query)
