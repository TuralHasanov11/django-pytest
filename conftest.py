import pytest

from django.contrib.auth.models import User

from pytest_factoryboy import register
from tests.factories import (UserFactory, ProductFactory, CategoryFactory)

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)

@pytest.fixture
def user_1(db):
    user = User.objects.create_user("test-user")
    print('create-user')
    return user

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user

@pytest.fixture
def new_user1(db, new_user_factory):
    return new_user_factory("Test_user","password","MyName")

@pytest.fixture
def new_user2(db, new_user_factory):
    return new_user_factory("Test_user","password", "MyName", is_staff="True")

@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    return user

@pytest.fixture
def new_category(db, category_factory):
    # not saving to db
    # category = category_factory.build()

    # saving to db
    category = category_factory.create()
    return category

@pytest.fixture
def new_product(db, product_factory):
    product = product_factory.create()
    return product
