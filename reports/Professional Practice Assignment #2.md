# Professional Practice Assignment 1 - Test/Behavior Driven Development 

Group: Ryan Ahmed, Joshua Aird, Brock Major, Dillon McGovern, Diana Osorio

# Configuration

**Through App Engine**

To access the App Enginge deployment, click this link https://peak-seat-332320.ue.r.appspot.com/. The following endpoints are available for access: /getApiKey, /revoke, /cc_payoff, /simple_savings_calc, /cc_min_payment_calc, /mortgage_calc, and /cdCalc. All of the endpoints except for /getApiKey and /revoke require an API key for access. In order to get an API key, a user must submit a POST request to the /getApiKey endpoint consisting of the following in JSON format: 

```
data = {
      'orgName': d['orgName'],
      'industry': d['industry'],
      'fullName': d['fullName'],
      'email': d['email'],
      'ip': request.remote_addr
    }
```
Once a user has a registered API key that was returned as a response when they got the key, they must add this API key in the header of their POST request under the key "apiKey". By adding this to the header of POST requests, the user can now access the rest of the endpoints and submit POST requests with the respective parameters for each function.

**Local Execution with Dockerfile**

To deploy the app locally, go the \Test-Behavior-Driven-Development folder and run "docker build -t ppa2/docker-release .", then run "docker run -d -p 8080:5000 ppa2/docker-release". To run the tests, navigate  to the same \Test-Behavior-Driven-Development\sandbox folder and run the command "pytest flask_pytest.py -v -s -vv".

If the Docker server is not running properly on the host, install all the required dependencies by running "pip install -r requirements.txt" in the \Test-Behavior-Driven-Development\sandbox folder, then run the command "flask run".

# All Test Suites Passing
![image](https://user-images.githubusercontent.com/44078719/142134691-98a263c1-b93b-4d96-9ca9-c54f1f6f9d3f.png)


# Naming and Organizational Details

**Language: Python**

**Testing framework: Pytest**

Since we selected Python as our programming language, we decided to use Python's naming convention for functions and named all the tests with lowercase words with words seperated by underscores.

Each of the 5 functions have their own testing suite in seperate files, the test files are named the same as the function that they are testing with "_pytest" added to the end of it. The application itself, along with all the defined functions, are contained within one file.

The individual tests themselves are named using Python's conventions and describe what the test is testing for.

# Source Management Approach

Our group used the Github Flow source management approach to complete the application.

In order to not have any code conflicts and complications, each group member worked on their own branch while implementing their changes. This allowed everyone to work on their own functions without being affected by the changes of another team member.

This approach also allowed us to make sure that anything on the 'main' branch is readily deployable and working.

Finally, this approach allowed our team members to freely experiment on their own branch when implementing their code, and made sure each of our code was reviewed by another member before being merged to the 'main' branch.






