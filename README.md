# TestingWeb
Automated Testing of "Bort2an" Web App Using Selenium  The project aimed to ensure the robustness and reliability of the "Bort2an" web application by implementing automated testing using the Selenium framework. By leveraging Selenium's powerful features, the project aimed to streamline the testing process and improve overall software quality.

Web Project Testing Read Me
This Read Me document provides an overview of the testing file for your web project. The testing file includes a collection of scripts written using Selenium to automate various functionalities of your web application. The scripts cover sign in, sign up, password recovery, sign in with Google, event ticket reservation, event creation, event deletion, event editing, event liking, and following a user.

Pre-requisites
Before running the testing file, make sure you have the following pre-requisites set up:

Python: Ensure that Python is installed on your machine. You can download it from the official Python website.

Selenium: Install the Selenium library using pip. Open your command prompt or terminal and run the following command:

bash
Copy code
pip install selenium
WebDriver: Download the appropriate WebDriver for your browser. Selenium requires a WebDriver to interact with web browsers. You can find the WebDriver downloads and instructions on the official Selenium website.

Web Project Setup: Set up your web project and ensure it is running properly on a local or remote server.

Running the Testing File
To run the testing file and execute the scripts, follow these steps:

Clone the repository: Clone the repository containing the testing file to your local machine.

Configure WebDriver: Update the testing file to specify the path to the WebDriver executable. Modify the script to use the appropriate WebDriver for your browser. For example, if you are using Chrome, you would use the ChromeDriver.

Install Dependencies: Install any additional dependencies required for running the testing file. Refer to the documentation or comments within the testing file for any specific dependencies.

Execute the Testing Scripts: Run the testing file using a Python interpreter. Open your command prompt or terminal, navigate to the directory containing the testing file, and execute the following command:

bash
Copy code
python test_file.py
The testing file will execute the scripts one by one, interacting with your web application and performing various actions.

Review Test Results: After the test execution is complete, review the output generated by the testing file. It should provide information about the success or failure of each test case.

Important Considerations
Ensure that your web project is running and accessible during the test execution. The testing file relies on the availability of the web application to interact with it.

Make sure to provide valid test data, such as valid credentials for sign in and sign up, a valid email address for password recovery, and relevant data for event creation and editing. This will help the testing file to successfully complete the desired actions.

Update the testing file if your web application undergoes significant changes in its structure or functionality. The testing file may need modifications to adapt to any updates made to your web project.

Use the testing file as a starting point and extend it with additional test cases as necessary. The provided scripts cover common functionalities, but you may need to add more specific tests based on your project requirements.

Additional Resources
Python
Selenium
WebDriver Downloads
Selenium with Python Documentation
Happy testing!
