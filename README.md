# Trendify - An E-Commerce App

Trendify is a Django-based e-commerce application that offers a wide range of trendy products to its users. With a user-friendly interface and seamless shopping experience, Trendify aims to keep users updated with the latest trends and offer them a hassle-free shopping experience.

## Features

- Browse and search for a variety of trendy products.
- Detailed product pages with images, descriptions, and customer reviews.
- Shopping cart functionality for adding and managing products.
- Secure checkout process for seamless online payments.
- User authentication and account management.
- Order history and tracking.

## Technologies Used

- Django
- Python
- HTML/CSS
- JavaScript
- PostgreSQL (or your preferred database)
- Stripe (or any other payment gateway)

## Setup

Follow these steps to set up the Trendify app on your local machine:

1. Clone the repository: `git clone https://github.com/your-username/trendify.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Create the database: `python manage.py migrate`
6. (Optional) Load sample data: `python manage.py loaddata sample_data.json`
7. Run the development server: `python manage.py runserver`
8. Visit `http://localhost:8000` in your web browser to access the Trendify app.

Note: To process online payments, you will need to set up a Stripe account and provide the necessary API keys in your Django settings.

## Usage

Once the Trendify app is set up, users can browse products, add items to their shopping cart, proceed to checkout, and make payments securely using the integrated payment gateway. Users can also create an account to manage their orders and access order tracking information.



## Creating a Superuser

To access the Django admin interface and manage the application's data, you need to create a superuser account. Follow these steps to create a superuser:

1. Make sure the Django development server is running: `python manage.py runserver`.
2. Open a web browser and go to `http://localhost:8000/admin`.
3. Click on the "Log in" link.
4. If you haven't created a superuser yet, run the following command in the terminal or command prompt: `python manage.py createsuperuser`.
5. You will be prompted to enter a username, email address, and password for the superuser account.
6. Once the superuser is created, go back to the admin login page and log in using the superuser credentials.
7. You will now have access to the Django admin interface to manage the application's data.


## Contributing

If you would like to contribute to Trendify, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Trendify was created by [Azhar Bihari](https://github.com/azhrbhr).
## Contact

For any questions or inquiries, you can reach me at [azhrbhr@gmail.com](mailto:azhrbhr@gmail.com).
