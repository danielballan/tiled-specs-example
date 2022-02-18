from setuptools import setup


setup(
    name="custom_client",
    packages=["my_package"],
    entry_points={
        "tiled.special_client": [
            "special_thing = my_package.client:custom_client"
        ]
    },
)
