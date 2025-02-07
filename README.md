# Python Modules Projects

This repository contains a collection of Python projects utilizing different modules and libraries. Each project demonstrates the use of a specific module to perform useful tasks. Below is a brief description of each project and the module used.

## Projects

### 1. YoutubeDownloader
**Module:** `pytube`

This project allows you to download videos from YouTube. It uses the `pytube` module to interact with YouTube's API and retrieve video content for offline viewing.

#### Features:
- Download videos in various resolutions
- Supports both audio and video downloads

### 2. VoiceRecorder
**Modules:** `scipy`, `wavio`

This project is a simple voice recorder that captures audio from a microphone and saves it in a `.wav` format. It uses the `scipy` and `wavio` modules for audio recording and file saving.

#### Features:
- Records audio from your microphone
- Saves audio as `.wav` files

### 3. QRGenerator
**Module:** `pyqrcode`

This project generates QR codes from text input. The `pyqrcode` module is used to create and visualize QR codes that can be scanned by QR code readers.

#### Features:
- Create QR codes from any text
- Supports saving QR codes as images

### 4. PDFConverter
**Module:** `pdf2docx`

This project converts PDF documents into Word `.docx` format. It uses the `pdf2docx` module to extract content from PDF files and save them in an editable Word format.

#### Features:
- Converts PDF files to Word `.docx` files
- Maintains the text and formatting of the original document

### 5. Background Remover
**Module:** `rembg`

This project removes the background from images using the `rembg` module. It's useful for creating clean product images or portraits without distractions in the background.

#### Features:
- Automatically removes the background from images
- Supports various image formats like `.png`, `.jpg`, etc.

## Installation

To run these projects locally, clone the repository and install the necessary dependencies using `pip`:

```bash
git clone https://github.com/tufanduzel/python-modules-projects.git
cd python-modules-projects
pip install -r requirements.txt
