# LalaTools

LalaTools is a Python package that provides various utilities for image processing and file system management. The current version (0.0.10+) includes the following modules and functions:

## Modules

### 1. digital_image_processing (image_process)

This module provides functions for handling and processing digital images. Here are the functions included in this module:

- `match_image_check`: This function compares two images and checks if they match based on a given accuracy criterion. It returns the position and accuracy if the images match.

- `match_with_image_write`: Similar to `match_image_check`, this function also compares two images. If the images match, it generates a 'match.png' image file showing the matching areas.

- `get_capture_image_on_app`: This function captures a screenshot of a specified application window.

- `test_screen`: This function is used for testing purposes.

- `cv2_to_pil`: This function converts an image from OpenCV format to PIL format.

- `pil_to_cv2`: This function converts an image from PIL format to OpenCV format.

### 2. manage_file_system (file_system)

This module provides functions for managing and manipulating file paths. Here are the functions included in this module:

- `del_head`: This function removes the head of a given file path.

- `replace_split_mark`: This function replaces the path split marks (like '//', '/', '\\') in a given file path with a specified mark.

- `get_file_list`: This function returns a list of files in a specified directory path.

## Installation

The package can be installed using pip:

```
pip install LalaTools
```

## Usage

Here is an example of how to use the `match_image_check` function:

```python
from lalatools.digital_image_processing import image_process

# Assume 'image1.jpg' and 'image2.jpg' are images in your local directory
result = image_process.match_image_check('image1.jpg', 'image2.jpg')

print(result)  # prints the position and accuracy if the images match
```

## Contributing

If you would like to contribute to the development of LalaTools, please feel free to make a pull request.

## License

LalaTools is licensed under the MIT license.