import unittest
import helloworld.HelloWorld as HelloWorld
import helloworld.hello as hello
#https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure

class MyTestCase2(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_hello(self):
        hello

    def test_hello_world(self):
        hello_world = HelloWorld.HelloWorld()
        hello_world.set_age(5)
        hello_world.age_one_year()
        self.assertEqual(6, hello_world.get_age())


if __name__ == '__main__':
    unittest.main()
