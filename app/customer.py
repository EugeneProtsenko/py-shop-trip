import math
from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    money: float
    product_cart: dict
    location: list
    car: Car

    def distance(self, shop_location) -> float:
        return math.dist(self.location, shop_location)

    def cost_to_shop(self, shop_location, fuel_price, shop) -> float:
        distance_km = self.distance(shop_location)
        fuel_needed = (distance_km / 100) * self.car.fuel_consumption
        fuel_cost = (fuel_needed * fuel_price) * 2
        product_cost = sum(
            shop.products[product] * quantity
            for product, quantity in self.product_cart.items()
        )
        total_cost = fuel_cost + product_cost
        return total_cost
