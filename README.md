# Kaliedo - Image Editing Application

Kaliedo is a Flask-based image editing application that empowers users to edit images with precision and creativity. With an intuitive UI and a comprehensive range of features, Kaliedo caters to both basic and advanced image editing needs.

---

## Website and Report

- **Website Link:** [Kaliedo - Image Editor](https://image-editor-lo1a.onrender.com)
- **Report Link:** [Project Report](https://drive.google.com/file/d/1Ua_yjmjW9GjII7j-f-aQzRg4cIfj4C0Z/view?usp=sharing)

---

## Contributors

- **Mallesh Basavant Kamati**:
  - Selection and implementation of additional filters (Background Removal, Erasing).
  - UI/UX feature selection and rendering.
  - Report writing.
- **Sanjay V P**:
  - Implementation of basic filters (Cropping, Rotation, Blurring).
  - Integration of filters with Flask.
  - Implementation of binary-to-text conversion using Base64.
  - Frontend development using HTML and CSS.

---

## Features Overview

| **Feature**           | **Description**                                                                                            | **Python Package Used**        |
| --------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Rotation              | Adjusts the image orientation by a specified angle anticlockwise.                                          | `PIL.Image.rotate`             |
| Blurring              | Applies a Gaussian blur to the image with a customizable radius.                                           | `PIL.ImageFilter.GaussianBlur` |
| Cropping              | Selects a specific area of the image by coordinates, keeping the desired region while discarding the rest. | `PIL.Image.crop`               |
| Brightness Adjustment | Adjusts the brightness of the image for improved visibility and aesthetics.                                | `PIL.ImageEnhance.Brightness`  |
| Erasing               | Removes specific rectangular regions from an image by replacing them with black pixels.                    | `NumPy`, `Pillow`              |
| Background Removal    | Eliminates the background of an image, isolating the subject.                                              | `rembg`, `NumPy`               |

---

## Functionalities and Implementation Details

### 1. **Cropping**

- Allows users to focus on specific regions of an image by discarding unwanted parts.
- **Implementation:**
  - Utilizes the `Pillow` library's `crop()` method.
  - Receives user input specifying coordinates, width, and height.
  - Extracts the specified region and returns it.

### 2. **Rotation**

- Adjusts the image orientation by a user-defined angle.
- **Implementation:**
  - Uses `Pillow`'s `rotate()` method.
  - Applies the transformation based on the specified angle and returns the rotated image.

### 3. **Blurring**

- Softens image details using Gaussian blur for artistic or anonymizing effects.
- **Implementation:**
  - Uses the `GaussianBlur` filter from `Pillow`.
  - The blur radius is specified by the user and applied to the image.

### 4. **Background Removal**

- Removes the background, leaving only the subject of the image.
- **Implementation:**
  - Utilizes the `rembg` library for advanced background removal.
  - Converts the image to a `NumPy` array for processing.

### 5. **Brightness Adjustment**

- Enhances or reduces the brightness of an image based on user input.
- **Implementation:**
  - Implements the `Pillow.ImageEnhance.Brightness` class.
  - Accepts a brightness factor ranging from 0 (dark) to 2 (bright) via a slider.

### 6. **Erasing**

- Eliminates specific rectangular regions of the image by replacing them with black pixels.
- **Implementation:**
  - Converts the image to an RGB format and processes it as a `NumPy` array.
  - Replaces pixel values within the specified region with black.

---

## UI/UX Design

### UI Highlights

- **Color Scheme:** Gradient background with shades of purple and blue for an elegant appearance.
- **Typography:** Clean and legible fonts with bold headers.
- **Visual Elements:** Intuitive buttons and descriptive labels enhance usability.

### UX Highlights

- **User Onboarding:** Simple process for uploading and editing images with clear instructions.
- **Feature Accessibility:** Prominent placement of editing features with easy navigation.
- **Error Handling:** Informative error messages guide users in case of invalid inputs.
- **Download Option:** Users can download the edited image seamlessly.

---

## Backend Algorithm

1. Accepts image uploads through Flask routes.
2. Validates image formats and handles errors.
3. Identifies desired manipulation based on user input.
4. Applies the selected feature to the image using specific functions.
5. Encodes processed image data into Base64 for display in the frontend.
6. Provides a route for users to download the edited image.

---

## Test Cases

| **Input**                  | **Feature(s) Applied**        | **Result**                                 |
| -------------------------- | ----------------------------- | ------------------------------------------ |
| Casual photo               | Erase + Rotate + Crop         | Converts into a professional photo         |
| Any image                  | Brightness Adjustment         | Enhances or dims overall illumination      |
| Blurred image with subject | Background Removal + Blurring | Isolates the subject with a blurred effect |

---

## Future Enhancements

| **Feature**          | **Description**                                | **Status**   |
| -------------------- | ---------------------------------------------- | ------------ |
| Resizing             | Adjust image dimensions.                       | Not Included |
| Grayscale Conversion | Convert image to shades of grey.               | Not Included |
| Watermarking         | Add text or logos to images.                   | Not Included |
| Edge Enhancement     | Highlight edges within the image.              | Not Included |
| Collage Creation     | Combine multiple images into a single collage. | Not Included |

---

## References

- AI tools for implementation.
- Frontend design inspiration from [Pixlr](https://www.pixlr.com).

---

## How to Use

1. Clone the repository.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the Flask server: `python app.py`.
4. Open the application in your browser and start editing images!

---

Kaliedo: Unleash your creativity with intuitive image editing!

