import unittest
import json
import os
import io
import sys
from models.rectangle import Rectangle

class RectangleMethods(unittest.TestCase):

  def test_id(self):
    """Tests for handling id"""
    r1 = Rectangle(10, 20, 0, 4, 5)
    self.assertEqual(r1.id, 5)

  def test_id_none(self):
    """Tests for handling id is none"""
    r1 = Rectangle(3, 5)
    self.assertEqual(r1.id, Rectangle.get_nb_objects())


  def test_constructor(self):
    """Tests for handling width"""
    r1 = Rectangle(4, 2)
    self.assertEqual(str(r1),
                     f"[Rectangle] ({Rectangle.get_nb_objects()}) 0/0 - 4/2")
    r1 = Rectangle(4, 2, 1)
    self.assertEqual(str(r1),
                     f"[Rectangle] ({Rectangle.get_nb_objects()}) 1/0 - 4/2")
    r1 = Rectangle(4, 2, 1, 2)
    self.assertEqual(str(r1),
                     f"[Rectangle] ({Rectangle.get_nb_objects()}) 1/2 - 4/2")

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
    self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
    r2 = Rectangle(5, 5, 1)
    self.assertEqual(str(r2), f"[Rectangle] ({Rectangle.get_nb_objects()}) 1/0 - 5/5")

  def test_update(self):
    """Tests for assigning an argument to each attribute"""
    r1 = Rectangle(10, 10, 10, 10, 1)
    r1.update()
    self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
    r1.update(89)
    self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
    r1.update(89, 2)
    self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
    r1.update(89, 2, 3)
    self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
    r1.update(89, 2, 3, 4)
    self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
    r1.update(89, 2, 3, 4, 5)
    self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

  def test_update_kwargs(self):
    """Tests for assigning an argument to each attribute"""
    r1 = Rectangle(10, 10, 10, 10, 1)
    r1.update()
    self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
    r1.update(id=89)
    self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
    r1.update(id=89, width=2)
    self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
    r1.update(id=89, width=2, height=3)
    self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
    r1.update(id=89, width=2, height=3, x=4)
    self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
    r1.update(id=89, width=2, height=3, x=4, y=5)
    self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

  def test_to_dictionary(self):
    r1 = Rectangle(10, 2, 1, 9, 1)
    self.assertEqual(r1.to_dictionary(),
                     {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

  def test_save_to_file(self):
    """Tests save to file"""
    r1 = Rectangle(10, 7, 2, 8, 1)
    r2 = Rectangle(2, 4, 0, 0, 2)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
      self.assertEqual(json.loads(file.read()),
                       [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
 {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])

  def test_to_save_to_file_none_list(self):
    r1 = Rectangle(10, 10)
    r1.save_to_file(None)
    with open("Rectangle.json", "r") as file:
      self.assertEqual(file.read(), "[]")
    r1.save_to_file([])
    with open("Rectangle.json", "r") as file:
      self.assertEqual(file.read(), "[]")


  def test_save_to_file_overwrite(self):
    """Tests save to file"""
    r1 = Rectangle(10, 7, 2, 8, 1)
    Rectangle.save_to_file([r1])
    r2 = Rectangle(2, 4, 0, 0, 2)
    Rectangle.save_to_file([r2])

    with open("Rectangle.json", "r") as file:
      self.assertEqual(json.loads(file.read()),
                       [{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])

  def test_from_json_string(self):
    """Tests save to file"""
    list_input = '[{"id": 89, "width": 10, "height": 4},{"id": 7, \
"width": 1, "height": 7}]'
    list_output = Rectangle.from_json_string(list_input)
    self.assertEqual(list_output, [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ])

  def test_from_json_string_none_input(self):
    self.assertEqual(Rectangle.from_json_string(None), [])

  def test_create(self):
    d = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 0}
    r = Rectangle.create(**d)
    self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 3/5")

  def test_load_from_file(self):
    """Tests load from file"""
    with open("Rectangle.json", "w") as f:
      f.write('[{"id": 89, "width": 10, "height": 4},{"id": 7, \
"width": 1, "height": 7}]')
    rects = Rectangle.load_from_file()
    self.assertEqual(str(rects[0]),"[Rectangle] (89) 0/0 - 10/4")
    self.assertEqual(str(rects[1]),"[Rectangle] (7) 0/0 - 1/7")

  def test_from_json_string_none_input(self):
    os.remove("Rectangle.json")
    self.assertEqual(Rectangle.load_from_file(), [])

  def test_display_with_no_xy(self):
    r1 = Rectangle(4, 3)
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    r1.display()
    sys.stdout = sys.__stdout__
    self.assertEqual(capturedOutput.getvalue(),
                     "####\n####\n####\n")
  def test_display_with_no_y(self):
    r1 = Rectangle(4, 3, 1)
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    r1.display()
    sys.stdout = sys.__stdout__
    self.assertEqual(capturedOutput.getvalue(),
                     " ####\n ####\n ####\n")
  def test_display_with_xy(self):
    r1 = Rectangle(4, 3, 1, 2)
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    r1.display()
    sys.stdout = sys.__stdout__
    self.assertEqual(capturedOutput.getvalue(),
                     "\n\n ####\n ####\n ####\n")

if __name__ == '__main__':
  unittest.main()
