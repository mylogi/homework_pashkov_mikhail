import unittest

import class_example


class CarTestCase(unittest.TestCase):

    def setUp(self):
        self.my_car = class_example.Car('Chevrolet', 'Impala', 1964, 'red')

    def test_repaint(self):
        self.assertEqual(self.my_car.color, 'red')
        self.my_car.repaint('black')
        self.assertEqual(self.my_car.color, 'black')

    def test_drive(self):
        self.assertEqual(self.my_car.total_driven_km, 0)
        self.my_car.drive(1000)
        self.assertEqual(self.my_car.total_driven_km, 1000)


class TruckTestCase(unittest.TestCase):

    def setUp(self):
        self.my_truck = class_example.Truck('MAN', 'TGX', 2014, 'black', 1)

    def test_attach(self):
        self.assertEqual(self.my_truck.trailers, 1)
        self.my_truck.attach_trailer()
        self.assertEqual(self.my_truck.trailers, 2)

    def test_detach(self):
        self.assertEqual(self.my_truck.trailers, 1)
        self.my_truck.detach_trailers()
        self.assertEqual(self.my_truck.trailers, 0)
