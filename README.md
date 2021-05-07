# project_mulytic - Super Shop
### Hosted on PythonAnywhere no need to run locally.
[Super-Shop](http://shaakib99.pythonanywhere.com/shop/)

#### Usage
- Does not require any pin or password or extra credential. You can login just typing your info in the rquired fields.
- Once you login, You can order single item by typing the order amount(Curently integer value are working ) then clicking order button on the item card.
- Clicking the order button will take you to the pdf page showing your order information.

## Installation
- Create a python virtual env and activate this created env [How to create virtual environment in python?](https://docs.python.org/3/tutorial/venv.html)
- Copy project_mulytic repo in your machine. ``` git clone https://github.com/shaakib99/project_mulytic.git ```
- Change directory to project_mulytic. ``` cd project_mulytic ```
- Install dependencies. ``` pip3 install -r requirements.txt ```
- Download sql file from [here](https://drive.google.com/file/d/1NWgOnA6RN561hCBkzY3FWgn6Tg18lZuj/view?usp=sharing)
- Fire up xamp or mamp(for macs) and create a new database named ``` project_mulytic ```
- Import downloaded database into recently created database.
- Provide database name, host, port, username, password in settings.py file.
- Start Django server. ``` python3 manage.py runserver ```

#### Tasks:

- ✅ Custom auth middleware.
- ✅ Database Connection - MySQL
- ✅ PDF Generation
- ✅ QR Code generation
- ✅ Product Categorization & Searching
- ✅ Basic HTML validation for stock limitaion

- ❌ Can not order multiple products at a time(cart system). Please visit my client side cart system project https://shaakib99.github.io/spectacle-shop/
- ❌ Less JS for other validation purposes.
- ❌ Terrible styling.
