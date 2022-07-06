import pytest
from app1.models import *

@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDesc", "slug", "4.99", "3.2", True),
        # ("NewTitle", 1, "NewDesc", "slug", "", "3.2", True)
    ]
)
def test_product_instance(db, product_factory, title, category, description, slug, regular_price, discount_price, validity):
    test = product_factory(
        title = title,
        category_id = category,
        description = description,
        slug = slug,
        regular_price = regular_price,
        discount_price = discount_price,
    )

    item = Product.objects.all().count()
    print(item)

    assert item == validity