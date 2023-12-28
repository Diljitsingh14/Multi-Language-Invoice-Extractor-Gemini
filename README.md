# Multi-Language-Invoice-Extractor-Gemini

The "Invoice Detail Extractor from Image" project utilizes the power of Google Gemini Pro, an AI model, to extract key information from uploaded invoice images, supporting multiple languages. Users can effortlessly upload invoices in various languages, and the AI model intelligently processes the images to extract essential details such as billing amount, dates, and vendor information. This project streamlines the extraction process, enhancing efficiency in managing diverse invoices. The README file provides instructions on uploading images, highlights the multi-language support, and guides users on leveraging Google Gemini Pro for accurate and automated invoice data extraction. Streamlining invoice management across languages has never been more seamless.

## How to run the project in local.

1. create virtual environment
   `conda create -p myenv python==3.10 -y`

2. activate env
   `conda activate myenv`

3. install the libraries
   `pip install -r requirement.txt`

4. copy the .env.example file
   `cp .env.example .env`

5. generate gemini-pro api key and replace in .env file <br>
   go to 'https://makersuite.google.com/app/apikey' to get you api key

6. run the streamlit app
   `streamlit run ./app.py`
