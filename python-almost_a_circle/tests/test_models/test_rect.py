import unittest
from models.rectangle import Rectangle

class RectangleMethods(unittest.TestCase):

  def test_id(self):
    """Tests for handling id"""
    r1 = Rectangle(10, 20, 0, 4, 5)
    self.assertEqual(r1.id, 1)

  def test_id_none(self):
    """Tests for handling id is none"""
    r1 = Rectangle()
    self.assertEqual(r1.id, Rectangle.get_nb_objects())


  def test_width(self):
    """Tests for handling width"""
    r1 = Rectangle(4, 2, 5, 6, 7)
    self.assertEqual(r1.width, 4)

  def test_width_non_int(self):
    """Test handling non-ints for width"""
    with self.assertRaises(TypeError):
      Rectangle("hello", 9)

  def test_width_negative(self):
    """Test handling width <= 0 for width"""
    with self.assertRaises(ValueError):
      Rectangle(-1, 1)
    with self.assertRaises(ValueError):
      Rectangle(0, 1)

  def test_height(self):
    """Test for handling height"""
    r1 = Rectangle(2, 4, 6, 8, 5)
    self.assertEqual(r1.height, 4)

  def test_height_non_int(self):
    """Tests for handling non-int height"""
    with self.assertRaises(TypeError):
      Rectangle(5, "hello")

  def test_height_negative(self):
    """Test for handling height <= 0 """
    with self.assertRaises(ValueError):
      Rectangle(5, -5)
    with self.assertRaises(ValueError):
      Rectangle(5, 0)

  def test_x(self):
    """Test for handling x"""
    r1 = Rectangle(2, 3, 5, 6, 7)
    self.assertEqual(r1.x, 5)

  def test_x_non_int(self):
    """Test for handling non_int x"""
    with self.assertRaises(TypeError):
      Rectangle(2, 3, "hello", 5, 6)

  def test_x_negative(self):
    """Test for handling x >= 0"""
    with self.assertRaises(ValueError):
      Rectangle(2, 3, -2, 4, 5)

 def test_y(self):
    """Test for handling y"""
    r1 = Rectangle(2, 3, 5, 6, 7)
    self.assertEqual(r1.y, 6)

  def test_y_non_int(self):
    """Test for handling non_int y"""
    with self.assertRaises(TypeError):
      Rectangle(2, 3, 4, "hello", 6)

  def test_y_negative(self):
    """Test for handling y >= 0"""
    with self.assertRaises(ValueError):
      Rectangle(2, 3, 2, -4, 5)

  def test_area(self):
    """Tests for normal functioning of area"""
    r1 = Rectangle(3, 3)
    self.assertEqual(r1.area(), 9)
    r2 = Rectangle(2, 10, 3, 5)
    self.assertEqual(r2.area(), 20)
    r3 = Rectangle(8, 7, 0, 0, 12)
    self.assertEqual(r3.area(), 56)

  def test_str(self):
    """Tests for string representation of a Rectangle"""
    r1 = Rectangle(4, 6, 2, 1, 12)
    self.assertEqual(r1, "[Rectangle] (12) 2/1 - 4/6")
    r2 = Rectangle(5, 5, 1)
    self.assertEqual(r2, "[Rectangle] (1) 1/0 - 5/5")

  def test_update(self):
    """Tests for assigning an argument to each attribute"""
    r1 = Rectangle(10, 10, 10, 10)
    self.assertEqual(r1.update(), "[Rectangle] (1) 10/10 - 10/10")
     r1 = Rectangle(89)
     self.assertEqual(r1.update(), "[Rectangle] (89) 10/10 - 10/10")
     r1 = Rectangle(89, 2)
     self.assertEqual(r1.update(), "[Rectangle] (89) 10/10 - 2/10")
     r1 = Rectangle(89, 2, 3)
     self.assertEqual(r1.update(), "[Rectangle] (89) 10/10 - 2/3")
     r1 = Rectangle(89, 2, 3, 4)
     self.assertEqual(r1.update(), "[Rectangle] (89) 4/10 - 2/3")
     r1 = Rectangle(89, 2, 3, 4, 5)
     self.assertEqual(r1.update(), "[Rectangle] (89) 4/5 - 2/3")

  def test_to_json_string_list_none(self):
    json_dictionary = Base.to_json_string(None)
    self.assertEqual(json_dictionary, "[]")

  def test_to_json_string_list_empty(self):
    json_dictionary = Base.to_json_string([])
    self.assertEqual(json_dictionary, "[]")

  def test_to_json_string_list_one_element(self):
    d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
    json_dictionary = Base.to_json_string([d])
    self.assertEqual(json_dictionary,
                     '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
  def test_to_json_string_list_multiple_elemets(self):
    d = {'test': 8}
    d1 = {'test1': 1}
    json_dictionary = Base.to_json_string([d, d1])
    self.assertEqual(json_dictionary,
                     '[{"test": 8}, {"test1": 1}]')


if __name__ == '__main__':
    unittest.main()
