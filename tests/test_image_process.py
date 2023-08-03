import unittest
import os
from lalatools.digital_image_processing import image_process
from PIL import Image

class TestImageProcess(unittest.TestCase):
    def test_get_capture_image(self):
        result = image_process.get_capture_image()
        self.assertIsInstance(result, Image.Image)

    def test_get_capture_image_with_save(self):
        result = image_process.get_capture_image_with_save(filename="test_capture.jpg")
        self.assertIsInstance(result, Image.Image)
        self.assertTrue(os.path.exists("test_capture.jpg"))
        os.remove("test_capture.jpg")

# You can add more tests for other functions here...

if __name__ == '__main__':
    unittest.main()
