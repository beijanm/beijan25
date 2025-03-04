---
layout: post
title: My Key Features
courses: {'csa': {'week': 19}}
type: ccc 
comments: true
permalink: /keyfeature2
---

<style>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #1a1a1a;
    color: #f4f4f4;
    margin: 0;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .container {
    max-width: 800px;
    width: 100%;
    background-color: #2c2c2c;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    text-align: center;
  }

  h1 {
    font-size: 36px;
    margin-bottom: 40px;
    color: #ffffff;
  }

  p {
    font-size: 18px;
    line-height: 1.6;
    color: #f4f4f4;
  }

  .back-button {
    display: inline-block;
    font-size: 22px;
    background-color: #3498db;
    color: white;
    padding: 15px 30px;
    border-radius: 5px;
    text-decoration: none;
    margin-top: 30px;
    transition: background-color 0.3s ease;
  }

  .back-button:hover {
    background-color: #2980b9;
  }
</style>

<div class="container">
  <h1>Hacks for Unit 2</h1>

    <div>
        <p>I worked on the different methods for seed and improved a couple things from the previous version.</p>

        <p>
            <strong>Multiple Fields Updated:</strong> You can now update grade, comment, and name in one PUT request.<br>
            <img width="379" alt="Image" src="https://github.com/user-attachments/assets/1716f3e9-d22d-468b-b60b-a2002869bd9b" />
        </p>

        <p>
            <strong>Null Protection:</strong> The code only updates a field if the new value is not null.<br>
            <img width="289" alt="Image" src="https://github.com/user-attachments/assets/cb9efae1-61dd-4145-935e-8e324834a5fe" />
        </p>

        <p>
            <strong>Grade Logging:</strong> It prints both the old and new grade for easy debugging.<br>
            <img width="622" alt="Image" src="https://github.com/user-attachments/assets/293c2970-0e69-48c7-9ef1-10e3eb8323e4" />
        </p>

        <p>
            <strong>Immediate Return:</strong> The updated Seed is returned right away so the frontend sees new data immediately.<br>
            <img width="464" alt="Image" src="https://github.com/user-attachments/assets/a7153532-c21a-480c-a54c-2c0d18566fc3" />
        </p>

        <p>
            <strong>Same CRUD Flow:</strong> The existing GET, POST, and DELETE methods remain unchanged and easy to use.<br>
            <img width="737" alt="Image" src="https://github.com/user-attachments/assets/afe963cb-cf3d-46e7-9cd9-d4a538fa9ef0" />
        </p>

        <p>
            <strong>What I Plan To Work on</strong><br>
            <img width="832" alt="Image" src="https://github.com/user-attachments/assets/9dd09be0-4bd8-405a-a1bf-69cf8072237d" />
        </p>
    </div>


  <a href="javascript:window.history.back()" class="back-button">Back to Previous Page</a>
</div>
