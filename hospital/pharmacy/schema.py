import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Order
from .utils import send_sms
import datetime

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
    #time = graphene.DateTime(required=True)
    

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
        
        current_time = datetime.datetime.now()
        # Create a new order object
        order = Order.objects.create(
            customer=customer,
            item=order_data.item,
            amount=order_data.amount,
            time=current_time
        )
        
        order_details = f"Your order Item: {order_data.item}, Amount: {str(order_data.amount)}, was successfully made at: {str(order_data.time)}"

        recipient = customer.phone_number 
        send_sms(recipient, order_details)
        # Return the created order
        return AddOrder(order=order)

# Mutation for updating an existing order
class UpdateOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.Int(required=True)
        order_data = OrderInput(required=True)

    # Define the return fields of the mutation
    order = graphene.Field(OrderType)

    @staticmethod
    def mutate(root, info, order_id, order_data):
        # Retrieve the order object to update
        order = Order.objects.get(id=order_id)
        
        # Update the order fields
        order.item = order_data.item
        order.amount = order_data.amount
        
        # Save the updated order
        order.save()
        
        # Return the updated order
        return UpdateOrder(order=order)

# Mutation for deleting an existing order
class DeleteOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.Int(required=True)

    # Define the return fields of the mutation
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, order_id):
        try:
            # Retrieve the order object to delete
            order = Order.objects.get(id=order_id)
            
            # Delete the order
            order.delete()
            
            return DeleteOrder(success=True)
        except Order.DoesNotExist:
            return DeleteOrder(success=False)

# Mutation class
class Mutation(graphene.ObjectType):
    add_order = AddOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()

# Schema
schema = graphene.Schema(query=Query, mutation=Mutation)