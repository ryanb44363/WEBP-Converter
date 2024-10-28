# Image to WebP Converter

A Python program that allows users to convert images to WebP format using a drag-and-drop interface. This tool supports popular image formats and ensures correct image orientation by applying EXIF metadata.

## Features

- Converts images to WebP format.
- Maintains correct orientation using EXIF data.
- Saves converted images in the original location.
- Drag-and-drop interface for easy file input.

## Requirements

- **Python 3.x**
- **Libraries**:
  - [Pillow (PIL)](https://pillow.readthedocs.io/) for image processing
  - [tkinterdnd2](https://pypi.org/project/tkinterdnd2/) for drag-and-drop support in Tkinter

### Installation

Install the required dependencies using `pip`:

```bash
pip install pillow tkinterdnd2
