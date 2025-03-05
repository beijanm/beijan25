---
layout: post
title: Final Exam Trimester 2
courses: {'csa': {'week': 20}}
type: ccc 
comments: true
permalink: /compsci_final
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

  .main-link {
    display: inline-block;
    font-size: 22px;
    background-color: #3498db;
    color: white;
    padding: 15px 30px;
    border-radius: 5px;
    text-decoration: none;
    margin-bottom: 30px;
    transition: background-color 0.3s ease;
  }

  .main-link:hover {
    background-color: #2980b9;
  }

  .links {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .link-container {
    width: 48%;
    margin-bottom: 20px;
  }

  .dropdown {
    background-color: #3c3c3c;
    color: #f4f4f4;
    padding: 15px;
    border-radius: 5px;
    text-decoration: none;
    position: relative;
    display: block;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .dropdown:hover {
    background-color: #555555;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #555555;
    min-width: 200px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
    border-radius: 5px;
    padding: 10px;
    top: 40px;
  }

  .dropdown:hover .dropdown-content {
    display: block;
  }

  ul {
    text-align: left;
    padding-left: 20px;
  }
</style>

<div class="container">
  <h1>Final Exam Trimester 2</h1>

  <div class="links">
    <!-- Dropdown for Unit 1 -->
        <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/5p';">My 5 Points
        <div class="dropdown-content">
          <ul>
            <li>5 things I did over 12 weeks, Issues, Burn Down, lesson(s), presentation(s), analytics, personal blog.</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Dropdown for Unit 2 -->
    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/ap2';">MCQ and FRQ
        <div class="dropdown-content">
          <ul>
            <li>MCQ / FRQ work</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Dropdown for Unit 3 -->
    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/keyfeature2';">My Key Features
        <div class="dropdown-content">
          <ul>
            <li>Key Feature blog write up, visualization (drawIO, mermaid) in your blog</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Dropdown for Unit 4 -->
    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/N@TM2';">N@TM Feedback
        <div class="dropdown-content">
          <ul>
            <li>Full Stack Feature Demo, include highlighting Java and N@tM feedback</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Dropdown for Unit 4 -->
    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/reflection2';">Self Reflection
        <div class="dropdown-content">
          <ul>
            <li>How I rank myself looking back at the second trimester and what I could have and will do better next trimester</li>
          </ul>
        </div>
      </div>
    </div>
    <!-- The Link for the issue -->
    <a href="https://github.com/beijanm" class="main-link">My Github Profile</a>
  </div>
</div>

