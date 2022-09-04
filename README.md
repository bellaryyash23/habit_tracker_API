# 📌Habit Tracker using API Requests of Python

🌟A program which helps you track & develop your daily habits. Built using the API provided by Pixela (https://pixe.la/) which provides Github like commit graphs for free.

🌟It makes use of GET, POST, PUT & DELETE methods of the 'requests' module to send and receive and update data.

👉In the 'main.py' file the first POST request is made to create a new user for the habit tracking program. This request includes the url endpoint of pixela and other
parameters like username & acceptance to T&C.

👉Next POST request is made to create a new Graph for the provided user to track their habit. In this request the parameters like title of the graph, color of habit 
tracker pixel etc. is provided.

👉Now to add a entry for any habit completed on a given day a POST request containing the parameters of date & quantity of work completed are provided which are then 
updated to our habit tracker graph.

![Habit tracker Graph](https://github.com/bellaryyash23/habit_tracker_API/blob/master/sample.JPG?raw=true)

👆Habit Tracker graph👆

👉Other useful methods provided by Pixela API include PUT request to update previous entries made on a particular date and finally, DELETE
request to delete a particular entry from the habit tracker graph.
