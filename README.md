Smart Review System <br>
The Smart Review System is a Flask-based web application designed to summarize product reviews. It extracts and analyzes reviews from a CSV file, categorizes them as positive or negative, and generates a concise summary. The application serves a simple HTML interface where users can view the summary.
Features<ul>
●	Review Summarization: Extracts and summarizes product reviews.<li>
●	Sentiment Analysis: Categorizes reviews into positive and negative sentiments.
●	Customizable Output: Configurable word count and summary formatting.
●	Web Interface: Simple HTML interface for displaying the summary.
</ul>
Prerequisites<ul>
●	Python 3.7 - 3.11: The project is compatible with these versions.
●	Flask: A web framework for Python.
●	pandas: A data analysis library.
●	textblob: A library for processing textual data.
        </ul>
Installation
Clone the repository: bash Copy code git clone https://github.com/chooomantar/smart-review-system.git
cd smart-review-system<ol>
1.	Set up a virtual environment (optional but recommended): bash Copy code python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
2.	Install dependencies: bash Copy code pip install -r requirements.txt</ol>

Project Structure
bash
Copy code
/smart-review-system
    /static
        index1.html       # Main HTML file
        styles.css        # CSS for styling (if any)
        script.js         # JavaScript for frontend functionality (if any)
    app.py               # Main Flask application
    product_review.csv   # CSV file containing product reviews
    README.md            # Project documentation
    requirements.txt     # List of Python dependencies

Running the Application<ol>
1.	Ensure the CSV file product_review.csv is present in the project directory.
2.	Start the Flask server: bash Copy code python app.py
3.	Access the application: Open a web browser and navigate to http://127.0.0.1:5000 to view the summarization results.
</ol>
Usage <ul>
●	View Summary: Click the button on the interface to generate a summary of the reviews. The system will categorize the reviews and display the result, starting with positive reviews followed by negative ones.
●	Update Reviews: To change the reviews, edit the product_review.csv file.
Troubleshooting
●	404 Errors: Ensure that all files, including index1.html and product_review.csv, are in the correct directory.
●	Errors in Summary Generation: Check the server logs for detailed error messages. Ensure that the CSV file is correctly formatted and accessible.
        </ul>
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements
●	Flask: For the web framework.
●	pandas: For data manipulation.
●	textblob: For sentiment analysis.

