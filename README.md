# Image OCR Website

This is a web application that uses Optical Character Recognition (OCR) to extract text from images. The application is built using Python, Flask, Bootstrap, and HTML.

## Installation

To run this application, you will need to have Python 3.x installed on your machine. Follow the steps below to install and run the application:

1. Clone the repository: 
   ```bash
   git clone https://github.com/bcsamrudh/image-ocr-website.git
   ```
2. Navigate to the project directory: 
   ```bash
   cd image-ocr-website
   ```
3. Install the required packages: 
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Installation of Tesseract OCR

1. Install Tesseract OCR on your machine. You can download the installer for your operating system from the following link: https://github.com/UB-Mannheim/tesseract/wiki
2. After installing Tesseract OCR, add its parent directory to your system's PATH environment variable. This will allow pytesseract to locate the tesseract executable. The location of the parent directory may vary depending on your operating system and the installation method you used. Here are some examples:

   - On Windows, the default installation location for Tesseract OCR is `C:\Program Files\Tesseract-OCR`. To add this directory to your PATH, follow these steps:
   
     - Open the Start menu and search for "Environment Variables".
     - Click on "Edit the system environment variables".
     - Click on the "Environment Variables" button.
     - In the "System Variables" section, scroll down and find the "Path" variable, then click on "Edit".
     - Click on "New" and add the path to the Tesseract OCR directory (`C:\Program Files\Tesseract-OCR` in this case).
     - Click on "OK" to close all windows.

   - On Linux or macOS, you can add the Tesseract OCR directory to your PATH by running the following command in your terminal:
   
     ```bash
     export PATH=$PATH:/usr/local/bin
     ```
   
## Usage

To use the application, follow these steps:

1. Open your web browser and go to `http://localhost:5000/` to access the application.
2. Click on the "Choose File" button to select an image from your computer.
3. Click on the "Upload" button to upload the selected image to the server.
4. The uploaded image will be displayed on the page.
5. Click on the "Extract Text" button to extract the text from the uploaded image.
6. The extracted text will be displayed on the page.

## Technologies Used

This application was built using the following technologies:

- Python 3.x
- Flask
- Bootstrap
- HTML

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
