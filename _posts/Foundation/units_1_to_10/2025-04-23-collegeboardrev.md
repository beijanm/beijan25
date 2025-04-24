---
layout: post
title: College Board Review
courses: {'csa': {'week': 7}}
type: ccc 
comments: true
permalink: /collegerev
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
  <h1>AP CSA Topics</h1>

  <div class="links">
    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U1';">Unit 1 — Primitive Types
        <div class="dropdown-content">
          <ul>
            <li>Define and use primitive data types: int, double, boolean, and char.</li>
            <li>Perform arithmetic operations and understand operator precedence.</li>
            <li>Declare and initialize variables; understand scope and lifetime.</li>
            <li>Apply type casting to convert between data types safely.</li>
            <li>Utilize String concatenation with primitive types.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U2';">Unit 2 — Using Objects
        <div class="dropdown-content">
          <ul>
            <li>Create objects using constructors from classes like String and Scanner.</li>
            <li>Invoke instance methods and understand method signatures.</li>
            <li>Utilize the Math class for mathematical operations like pow() and sqrt().</li>
            <li>Work with wrapper classes (Integer, Double) for primitive data types.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U3';">Unit 3 — Boolean Expressions and if Statements
        <div class="dropdown-content">
          <ul>
            <li>Understand Boolean values, logical operators (&&, ||, !), and relational operators (==, !=, >, <).</li>
            <li>Apply conditional logic using if, if-else, and nested if statements.</li>
            <li>Implement complex decision-making using compound Boolean expressions.</li>
            <li>Simplify Boolean logic using De Morgan's Laws.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U4';">Unit 4 — Iteration
        <div class="dropdown-content">
          <ul>
            <li>Explore for, while, and do-while loops for repetitive tasks.</li>
            <li>Understand nested loops and how to use them efficiently.</li>
            <li>Control loop execution using break and continue statements.</li>
            <li>Apply loops to process arrays and collections.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U5';">Unit 5 — Writing Classes
        <div class="dropdown-content">
          <ul>
            <li>Design classes with constructors, fields, and methods.</li>
            <li>Apply encapsulation using private fields and public methods.</li>
            <li>Overload methods for flexible usage.</li>
            <li>Use static variables and methods for class-wide behavior.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U6';">Unit 6 — Array
        <div class="dropdown-content">
          <ul>
            <li>Declare and initialize arrays of primitives and objects.</li>
            <li>Traverse arrays using for and for-each loops.</li>
            <li>Apply common array algorithms like searching and sorting.</li>
            <li>Understand off-by-one errors and how to prevent them.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U7';">Unit 7 — ArrayList
        <div class="dropdown-content">
          <ul>
            <li>Create and manipulate ArrayLists with add(), remove(), and get().</li>
            <li>Traverse ArrayLists using loops and iterators.</li>
            <li>Compare ArrayLists to arrays and understand dynamic sizing.</li>
            <li>Apply ArrayList methods to solve problems involving collections.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U8';">Unit 8 — 2D Array
        <div class="dropdown-content">
          <ul>
            <li>Declare and initialize two-dimensional arrays.</li>
            <li>Traverse 2D arrays using nested loops.</li>
            <li>Apply 2D arrays to represent grids, matrices, and tables.</li>
            <li>Implement algorithms that manipulate rows and columns.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U9';">Unit 9 — Inheritance
        <div class="dropdown-content">
          <ul>
            <li>Understand superclass-subclass relationships.</li>
            <li>Use the extends keyword to create subclasses.</li>
            <li>Override methods to customize behavior in subclasses.</li>
            <li>Apply polymorphism to work with objects of different classes.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="link-container">
      <div class="dropdown" onclick="window.location.href='{{site.baseurl}}/U10';">Unit 10 — Recursion
        <div class="dropdown-content">
          <ul>
            <li>Define recursive methods with base and recursive cases.</li>
            <li>Trace recursive calls to understand the flow of execution.</li>
            <li>Apply recursion to solve problems like factorials and Fibonacci sequences.</li>
            <li>Recognize when recursion is a suitable approach.</li>
          </ul>
        </div>
      </div>
    </div>

    <a href="https://github.com/beijanm/beijan25/issues/21" class="main-link">Go to My Issue</a>
    <a href="{{site.baseurl}}/collegestudy" class="main-link">View Study Plan</a>
    <a href="{{site.baseurl}}/collegetypes" class="main-link">Learn About FRQ Types</a>
    <a href="{{site.baseurl}}/ap2" class="main-link">Some MC and Reflections</a>
  </div>
</div>