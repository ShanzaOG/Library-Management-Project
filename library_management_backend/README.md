<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [📖 Library Management Backend ](#-library-management-backend-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
    - [Documentation ](#documentation-)
    - [Front end ](#front-end-)
    - [ERD Diagram ](#erd-diagram-)
    - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Usage](#usage)
    - [Run tests](#run-tests)
  - [👥 Author ](#-author-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# 📖 Library Management Backend <a name="about-project"></a>

**Library Management Backend** is an application that one can manage the books, members and reservations. It's powerful API's easens work.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
<summary>Server</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://flask.palletsprojects.com/en/2.3.x/">Flask</a></li>
  </ul>
</details>
<details>
<summary>database</summary>
  <ul>
    <li><a href="https://www.postgresql.org/">Postgresql</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Documentation <a name="Documentation"></a>

The apps documentation can be found [here.](https://documenter.getpostman.com/view/21501737/2s93zFXeQT)

<!-- Features -->

### Key Features <a name="key-features"></a>

- **CRUD on Books**
- **CRUD on Members**
- **CRUD on Reservations**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps:

- Create a local directory where you can clone the project
- Clone the project to your directory by running
  - `git clone https://github.com/franklinetush1/Library-Management-Project/tree/main/library_management_backend`
- Create a postgress database
- run `pip install pipenv` if you do not have it installed globally.
- run `pipenv shell` to activate the virtual environment
- Set your interpreter to be your virtual environment.
- create a .env file and place your database url. An example can be:
  -`DATABASE_URL=postgresql://postgres:PASSWORD@localhost/DATABASE_NAME`
- Run `pip install -r requirements.txt`
- Run `Python` to access the python terminal
- Run `from app.seed import seed_data`
- run `seed_data()`
- exit python terminal and run `Flask run`

### Prerequisites

To run the app you need:

- A code editor
- Install Python
- App to test API's (i.e postman, insomnia)
- Install Postgress

### Setup

Clone this repository to your desired folder:

- Create a local directory where you can clone the project
- Clone the project to your directory by running
  - `git clone https://github.com/franklinetush1/Library-Management-Project/tree/main/library_management_backend`

### Usage

To run the project, execute the following command:

```sh
  flask run
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- [ ] **Improve UI**
- [ ] **Add funcionality**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly leave a ⭐

<p align="right">(<a href="#readme-top">back to top</a>)</p>
