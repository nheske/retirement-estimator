from helloworld.Car import Car


def test_car_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 45


if __name__ == '__main__':
    test_car_brake()