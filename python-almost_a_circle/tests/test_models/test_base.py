import unittest
from models.base import Base

class BaseMethods(unittest.TestCase):

  def test_id(self):
    b1 = Base(20)
    self.assertEqual(b1.id, 20)

  def test_id_none(self):
    b1 = Base()
    self.assertEqual(b1.id, Base.get_nb_objects())

  def test_id_none_1(self):
    b1 = Base(None)
    self.assertEqual(b1.id, Base.get_nb_objects())

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
