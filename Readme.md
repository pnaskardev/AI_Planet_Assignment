
# Hackathon Management System

The Hackathon Management System is a web application designed to streamline the process of organizing and participating in hackathons. It provides a platform for event organizers to create and manage hackathons, and for participants to register, submit their projects, and view their submissions.


## Features

- **Hackathon Creation**: Authorized users can create hackathons by providing essential details such as title, description, background image, hackathon image, type of submission, start datetime, end datetime, and reward prize.

- **Listing of Hackathons**: Users can view a list of available hackathons, including their titles and descriptions.

- **User Registration**: Students can register for hackathons by creating an account with their email, username, and password.

- **Hackathon Registration**: Registered users can enroll in hackathons they are interested in.

- **Submission Creation**: Participants can submit their projects to a hackathon, including a name, summary, and submission content (image, file, or link).

- **Submission Validation**: The system validates the submissions based on the selected type of submission (image, file, or link).

- **Authorization and Authentication**: Access to various features is restricted based on user roles. Superusers have exclusive rights to create hackathons, while regular users can register, enroll in hackathons, and make submissions.

## Run Locally

Clone the project

```bash
  git clone https://github.com/pnaskardev/Hackathon-Management-Service-Django
```

Go to the project directory

```bash
  cd Hackathon-Management-Service-Django
```

Create a python virtual environement

```bash
  python -m venv venv
```

Start the virtual environement

```bash
  venv\Scripts\activate
```

install required packages

```bash
  pip install -r requirements.txt
```

Create your own superuser

```bash
  python manage.py createsuperuser
```


Start the Server

```bash
  python manage.py runserver
```


## API Reference


#### Get all Hackathons

```http
  GET /hackathon/hackathons/
```

#### Register to the platform

```http
  POST /account/register/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username` | `string` | **Required**. your username |
| `email` | `string` | **Required**. your email |
| `password` | `string` | **Required**. your secure password |


#### Login to the platform

```http
  POST /account/login/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email` | `string` | **Required**. your email |
| `password` | `string` | **Required**. your secure password |


**Below this all the Routes require Authorization Bearer Acces Token which was recieved in the Login Route**

#### Register to a Hackathon

**Required**. accessToken

```http
  POST /account/register_hackathon
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hackathon_id` | `string` | **Required**. Id of hackathon |


#### Get list of all registered hackathons by the user

**Required**. accessToken

```http
  GET /account/registered_hackathons/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hackathon_id` | `string` | **Required**. Id of hackathon |


#### Post a submission to a Hackathon

**Required**. accessToken

```http
  POST /hackathon/submission/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name` | `string` | **Required**. name of the submission |
| `user` | `string` | **Required**. user id of the participant |
| `submission` | `string`  |**Required**. submission type |


#### Get a submission to a Hackathon by the user 

**Required**. accessToken

```http
  GET /hackathon/submission/
```


## Screenshots

![image](https://github.com/pnaskardev/Hackathon-Management-Service-Django/assets/71266237/805b1d5b-319f-4fba-b8f6-4690153d928a)

![image](https://github.com/pnaskardev/Hackathon-Management-Service-Django/assets/71266237/202c3052-1779-42c9-8021-e6187b93d3aa)

![image](https://github.com/pnaskardev/Hackathon-Management-Service-Django/assets/71266237/da40d825-82ed-4985-82a4-b3ba82297ffa)

![image](https://github.com/pnaskardev/Hackathon-Management-Service-Django/assets/71266237/7fcc8512-6fb3-49ce-8397-5eb420bba7e5)

![image](https://github.com/pnaskardev/Hackathon-Management-Service-Django/assets/71266237/b1ff8e8b-0d06-4b9f-a361-84c0c004c085)

## Authors

- [@pnaskardev](https://www.github.com/pnaskardev)

