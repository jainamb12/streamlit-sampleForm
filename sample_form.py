import streamlit as st

html_code = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        label {
            font-weight: bold;
            display: block;
            margin-top: 10px;
        }
        input[type="text"],
        input[type="email"],
        select {
            width: calc(100% - 22px);
            padding: 10px;
            margin: 5px 0 10px 0;
            border: 1px solid #ddd;
            border-radius: 3px;
        }
        input[type="radio"],
        input[type="checkbox"] {
            margin-right: 10px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form action="#" method="post">
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name">

        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name">

        <label for="email">Email:</label>
        <input type="email" id="email" name="email">

        <label>Gender:</label>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">Female</label>

        <label for="branch">Branch:</label>
        <select id="branch" name="branch">
            <option value="computer_engineering">Computer Engineering</option>
            <option value="information_technology">Information Technology</option>
            <option value="electronics_communication">Electronics and Communication</option>
        </select>

        <label>Subjects Taught:</label>
        <input type="checkbox" id="subject1" name="subject" value="subject1">
        <label for="subject1">Subject 1</label><br>
        <input type="checkbox" id="subject2" name="subject" value="subject2">
        <label for="subject2">Subject 2</label><br>
        <input type="checkbox" id="subject3" name="subject" value="subject3">
        <label for="subject3">Subject 3</label><br>
        <input type="checkbox" id="subject4" name="subject" value="subject4">
        <label for="subject4">Subject 4</label><br>
        <input type="checkbox" id="subject5" name="subject" value="subject5">
        <label for="subject5">Subject 5</label><br>

        <input type="submit" value="Submit" name="submit">
    </form>
</body>
</html>
"""

st.title("Public HTML Form on Streamlit")
st.components.v1.html(html_code, height=300)
