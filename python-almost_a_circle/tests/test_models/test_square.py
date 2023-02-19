import unittest
import json
import os
from models.square import Square

class SquareMethods(unittest.TestCase):

  def test_id(self):
    """Tests for handling id"""
    r1 = Square(10, 0, 4, 5)
    self.assertEqual(r1.id, 5)

  def test_id_none(self):
    """Tests for handling id is none"""
    r1 = Square(3)
    self.assertEqual(r1.id, Square.get_nb_objects())


  def test_width(self):
    """Tests for handling width"""
    r1 = Square(4, 5, 7)
    self.assertEqual(r1.width, 4)

  def test_size(self):
    """Test handling non-ints for width"""
    with self.assertRaises(TypeError):
      Square("11")

  def test_size_negative(self):
    """Test handling width <= 0 for width"""
    with self.assertRaises(ValueError):
      Square(-1)
    with self.assertRaises(ValueError):
      Square(0)

  def test_height(self):
    """Test for handling height"""
    r1 = Square(4, 5, 7)
    self.assertEqual(r1.height, 4)

  def test_x(self):
    """Test for handling x"""
    r1 = Square(2, 5, 6, 7)
    self.assertEqual(r1.x, 5)

  def test_x_non_int(self):
    """Test for handling non_int x"""
    with self.assertRaises(TypeError):
      Square(2, "hello", 5, 6)

  def test_x_negative(self):
    """Test for handling x >= 0"""
    with self.assertRaises(ValueError):
      Square(2, -2, 4, 5)

  def test_y(self):
    """Test for handling y"""
    r1 = Square(2, 5, 6, 7)
    self.assertEqual(r1.y, 6)

  def test_y_non_int(self):
    """Test for handling non_int y"""
    with self.assertRaises(TypeError):
      Square(2, 4, "hello", 6)

  def test_y_negative(self):
    """Test for handling y >= 0"""
    with self.assertRaises(ValueError):
      Square(2, 2, -4, 5)
    with self.assertRaises(ValueError):
      Square(2, 2, -4)

  def test_area(self):
    """Tests for normal functioning of area"""
    r1 = Square(3)
    self.assertEqual(r1.area(), 9)
    r2 = Square(2, 3)
    self.assertEqual(r2.area(), 4)
    r3 = Square(8, 0, 0, 12)
    self.assertEqual(r3.area(), 64)

  def test_str(self):
    """Tests for string representation of a Square"""
    r1 = Square(4, 2, 1, 12)
    self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")
    r2 = Square(5, 1)
    self.assertEqual(str(r2), f"[Square] ({Square.get_nb_objects()}) 1/0 - 5")

  def test_set_size(self):
    """Tests for assigning an argument to each attribute"""
    r1 = Square(10, 10, 10, 1)
    r1.size = 2
    self.assertEqual(str(r1), "[Square] (1) 10/10 - 2")

  def test_size_non_int(self):
    """Test for handling non_int size"""
    with self.assertRaises(TypeError):
      s = Square(2)
      s.size = "hello"

  def test_y_negative(self):
    """Test for handling size >= 0"""
    s = Square(2)
    with self.assertRaises(ValueError):
      s.size = -1

  def test_update(self):
    """Tests for assigning an argument to each attribute"""
    r1 = Square(10, 10, 10, 1)
    r1.update()
    self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
    r1.update(89)
    self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
    r1.update(89, 2)
    self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
    r1.update(89, 2, 3)
    self.assertEqual(str(r1), "[Square] (89) 3/10 - 2")
    r1.update(89, 2, 3, 4)
    self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")

  def test_update_kwargs(self):
    """Tests for assigning an argument to each attribute"""
    r1 = Square(10, 10, 10, 1)
    r1.update()
    self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
    r1.update(id=89)
    self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
    r1.update(id=89, size=2)
    self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
    r1.update(id=89, size=2, x=4)
    self.assertEqual(str(r1), "[Square] (89) 4/10 - 2")
    r1.update(id=89, size=2, x=4, y=5)
    self.assertEqual(str(r1), "[Square] (89) 4/5 - 2")

  def test_to_dictionary(self):
    r1 = Square(10, 1, 9, 1)
    self.assertEqual(r1.to_dictionary(),
                     {'x': 1, 'y': 9, 'id': 1, 'size': 10})

  def test_save_to_file(self):
    """Tests save to file"""
    r1 = Square(10, 2, 8, 1)
    r2 = Square(2, 0, 0, 2)
    Square.save_to_file([r1, r2])

    with open("Square.json", "r") as file:
      self.assertEqual(json.loads(file.read()),
                       [{"y": 8, "x": 2, "id": 1, "size": 10},
 {"y": 0, "x": 0, "id": 2, "size": 2}])

  def test_to_save_to_file_none_list(self):
    s = Square(10)
    s.save_to_file(None)
    with open("Square.json", "r") as file:
      self.assertEqual(file.read(), "[]")
    s.save_to_file([])
    with open("Square.json", "r") as file:
      self.assertEqual(file.read(), "[]")


  def test_save_to_file_overwrite(self):
    """Tests save to file"""
    r1 = Square(10, 2, 8, 1)
    Square.save_to_file([r1])
    r2 = Square(2, 0, 0, 2)
    Square.save_to_file([r2])

    with open("Square.json", "r") as file:
      self.assertEqual(json.loads(file.read()),
                       [{"y": 0, "x": 0, "id": 2, "size": 2}])

  def test_from_json_string(self):
    """Tests save to file"""
    list_input = '[{"id": 89, "size": 10},{"id": 7, \
"size": 1}]'
    list_output = Square.from_json_string(list_input)
    self.assertEqual(list_output, [
        {'id': 89, 'size': 10},
        {'id': 7, 'size': 1}
    ])

  def test_from_json_string_none_input(self):
    self.assertEqual(Square.from_json_string(None), [])

  def test_create(self):
    d = {'id': 1, 'size': 3, 'x': 1, 'y': 0}
    r = Square.create(**d)
    self.assertEqual(str(r), "[Square] (1) 1/0 - 3")

  def test_load_from_file(self):
    """Tests load from file"""
    with open("Square.json", "w") as f:
      f.write('[{"id": 89, "size": 10},{"id": 7, \
"size": 1}]')
    rects = Square.load_from_file()
    self.assertEqual(str(rects[0]),"[Square] (89) 0/0 - 10")
    self.assertEqual(str(rects[1]),"[Square] (7) 0/0 - 1")

  def test_from_json_string_none_input(self):
    os.remove("Square.json")
    self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
  unittest.main()
