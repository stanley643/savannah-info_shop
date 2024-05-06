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

# Define an input type for the order data
class OrderInput(graphene.InputObjectType):
    customer_code = graphene.String(required=True)
    item = graphene.String(required=True)
    amount = graphene.Decimal(required=True)

# Mutation for adding a new order
class AddOrder(graphene.Mutation):
    class Arguments:
        order_data = OrderInput(required=True)

    # Define the return fields of the mutation
    order = graphene.Field(OrderType)

    @staticmethod
    def mutate(root, info, order_data):
        # Retrieve the customer object based on the provided code
        customer = Customer.objects.get(code=order_data.customer_code)
        
        # Create a new order object
        order = Order.objects.create(
            customer=customer,
            item=order_data.item,
            amount=order_data.amount
        )
        
        # Return the created order
        return AddOrder(order=order)

# Mutation class
class Mutation(graphene.ObjectType):
    add_order = AddOrder.Field()

# Schema
schema = graphene.Schema(query=Query, mutation=Mutation)