# Pharmacy Management System

## Overview

The Pharmacy Management System is a sophisticated web application designed to streamline customer and order management within a pharmacy setting. This robust system provides pharmacists with advanced tools for efficiently handling customer records and order processing. Leveraging modern technologies, it offers a GraphQL API for seamless interaction and integration.

- **However this project stands as a technical interview for backend development** - it contains basic and less complex logics, Easy to be understand and implement. 
## Key Features

- **Customer Management**: Easily add, update, and delete customer records with a user-friendly interface.
- **Order Management**: Effortlessly create, update, and delete orders for various pharmaceutical items.
- **GraphQL API**: Access a powerful and flexible API for seamless integration with external systems.
- **Tools**: Africanstalking, Django, GraphQl API, Postgres database

## Installation

1. **Clone the Repository**: Start by cloning the project repository to your local machine.

    ```
    git clone https://github.com/stanley643/savannah-info_shop
    cd pharmacy-management-system
    ```

2. **Install Dependencies**: Use pip to install the required dependencies listed in the `requirements.txt` file.

    ```
    pip install -r requirements.txt
    ```
3. **Check Settings.py**: Check the settings file and change all personal infomation eg. API keys, Database informations and other authentications required 

4. **Apply Migrations**: Apply database migrations to set up the necessary database schema.

    ```
    python manage.py migrate
    ```

5. **Run the Development Server**: Start the Django development server to launch the application.

    ```
    python manage.py runserver
    ```

## Usage

- **Access the GraphQL Endpoint**: Navigate to `http://localhost:8000/graphql` to access the GraphQL endpoint.
- **Interact with the API**: Use tools like GraphiQL or Postman to send queries and mutations to the API.
- **API Documentation**: Explore the comprehensive API documentation available at `http://localhost:8000/graphql`.

## Challenges
- **Implement authentication and authorization via OpenID Connect**
	I was unable to implement this functionality. I got errors on default databases not defined which in result made it impossible to generate a required token.
- **Was not able to work on the frontend on time**. As a result this is just a backend api.
## Contributing

I welcome contributions from the community!
