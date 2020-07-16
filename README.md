#Plant Diary

<b>Project:</b> PlantDiary <br>
<b>Made by:</b> Gary Forrow <br>

##ReadMe Content
* The Brief
* App Functionality
* Data
* Technologies Used
* CI Pipeline
* Front-End Design
* Risk Assessment
* Difficulties Faced
* Current Issues
* Improvements To Be Made
* Authors  

#####Resources:
* Trello - https://trello.com/b/mWkaYpmy/plant-diary
* Link to app - http://35.189.101.96/

<br>

##The Brief
The brief set out for this particular project was to 'Create a CRUD application with utilisation of supporting tools, 
methodologies and technologies that encapsulate all core modules covered during training'. <br>
<br>
This would involve creating an application with the functionality to <u><b>C</b></u>reate, <u><b>R</b></u>ead, 
<u><b>U</b></u>pdate, and <u><b>D</b></u>elete records in a database. We were to achieve this using multiple technologies
that were covered during out training, which will be looked at in more detail further in this readme.

###Minimum Requirements:
* Project management and tracking via Trello or equivalent Kanban board tech. 
* User stories and use cases needed to complete the project.
* A relational database use for persistent data storage, with at least 2 tables.
* Clear documentation.
* A functional CRUD application created in Python, following best practices and design principles, which meets requiorements 
set out on project management tool.
* A functioning front-end website and integrated API's, using Flask.
* Code fullt integrated into a Version Control System using Feature-Branch model, subsequently built through a
CI server and deployed to a cloud-based virtual machine.

<br>

##Functionality

To satisfy the brief, my aim was to design a Plant Diary that would allow users to keep a record of thier plants by Scientific name, 
a nickname given by the user, details of the particular plant, and any additional notes for each plant.
The goal of this was to be able to provide an easy way to track the care and development of an indoor garden for anyone
who has found their collection has grown beyond easy management. 
<br>

The user stories I set to meet the above brief were: 
 * As a user I must be able to add a plant to my colleciton
 * As a user I must be able to add details of my plants to differentiate between individuals.
 * As a user I must be able to add notes to individual plants to track particular requirements individuals.
 * As a user I must be able to edit a plant's description.
 * As a user I must be able to edit a plant's name. 
 * As a user I must be able to edit a plant's notes.
 
 See image below for full list of user stories created for the development of this application, as well as the design 
 flow implemented through the development.
 
<p align="center">
  <img src="https://i.imgur.com/DqNqSFl.png">
</p>

<br>

##Data

The final outline for the tables in the database, and the relationship between them can be see in the entity relationship diagram below.

<p align="center">
  <img src="https://i.imgur.com/mRTucar.png">
</p>

This diagram specifies the single to many relationship between a user and their plants, where a plant must always belong to a user with the user_id field.

##Technologies Used

To keep in line with the brief I made us of the following technologies that were learned during my training: 
* Trello - Project Management / Kanban Board
* Google Cloud Platform - Cloud hosting
* mySQL - Database technology implemented via GCP
* Linux - Server OS used for hosting web app in GCP
* Python - Application Back-End
* HTML - Application Front-End
* Flask - As applications Web Framework
* Git - Version Control also making use of GitHub
* Jenkins - CI Server
* Systemsd - Runs application as a service on Linux VM


##CI Pipeline
<p align="center">
  <img src="https://i.imgur.com/X9uqvFX.png">
</p>
The image above details the CI Pipeline implemented for this project.
<br>

* Source Code - Written and tested locally while being commited to preestablished GitHub Repo
* Project Tracking - We then look to Trello to confirm our previous job was complete, and look to take on the next.
* Version Control System - Git is used to branch from the functioning app repository when developing each job from Trello, before being merged back into the main branch.
* CI Server - When a new commit has been made, Jenkins will run a job to replace the old version with the new from GitHub, and rerun the app service.

<br>

##Front-End Design
A brief walkthrough of the front-end design of the website
<p align="center">
  <img src="https://i.imgur.com/dneOWlo.png">
</p>
The user is welcomed to the site with the homepage
<br>
<p align="center">
  <img src="https://i.imgur.com/A5OIy6M.png">
</p>
The user can choose to sign up to the website by creating an account. 
<p align="center">
  <img src="https://i.imgur.com/yB82yuL.png">
</p>
The user can then sign in to the website
<p align="center">
  <img src="https://i.imgur.com/nlGq4LL.png">
</p>
After signing in, the user is directed to their plant list which initially is empty. They can choose the Add New Plant button to start their diary.
<p align="center">
  <img src="https://i.imgur.com/MmsO6ap.png">
</p>
The user is then directed to the New Plant page where they can enter their plants details.
<p align="center">
  <img src="https://i.imgur.com/3ntikAB.png">
</p>
Once submitted the user is directed back to their plant list with the new entry listed. Each individual entry can be edited or deleted.
<p align="center">
  <img src="https://i.imgur.com/mBFU6a6.png">
</p>
The user also has the option to update their account details or delete their account and posts entirely.
<br>
<br>

##Risk Assessment
<p align="center">
  <img src="https://i.imgur.com/mCvxbSo.png">
</p>
<br>
<br>
<br>
<br>
<br>

Structure:<br>
* Introduction<br>
	* Introduce yourself<br>
	* Introduce the task that was given and what you chose for it in terms of the topic<br>
* Contents<br>
	* Explain the structure of the presentation<br>
* Main<br>
    * Expand your project, why have you chosen it, how it relates to you<br>
    * Explain the plan you made for this project and how well/bad did you follow it<br>
    * Expand on technologies you used<br>
    Trello for Kanban boards for user stories and sprint tracking<br>
    GCP as cloud hosting platform with Linux VM and mySQL database<br>
    Python for application back end, using Flask framework<br>
    HTML for application front end <br>
    Git for version control, using github <br>
    Jenkins CI server implemented in Linux VM <br>
    Linux Systemsd used to run app as system service for uptime <br>
        * Why have you chosen it<br>
        * What did you learn from working with it<br>
        * What went well/bad with it<br>
        * How could you improve the usage of it next time you would use it<br>
* Lessons<br>
        * What went well for the project<br>
        * What didn't go so well for the project<br>
        * What could you have done differently<br>
        * Best things you learned from this project<br>
* Demo<br>
        * Demonstrate the project<br>
        * Tools can also be demonstrated that were used for the project<br>
* Questions<br>
	2 questions<br>



This project was created to meet the following criteria p

**this would make text bold** 

_this would make it italic_

**_this would make it bold and italic_**
~~_**bold italics**_~~

~~strikethrough text~~

> example of a sentence block quote



>Example of a 
>sentence block
>quote
>on multiple lines

* bullet points
* use a *
    * indent with tab
        * more indented
        
- dashes work too
    - like this 

1. number lists
2. pretty simple
    1. can be indented
    2. doesn't work with letters, only numbers. 

Take a new line by using `<br>` 
<br>

`this is a code example`

```python
print("hello")
print("example of python code insert")
```
Tables take some extra formatting using | and ----

| Column1     | Column2     |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

<img align="left" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
<br>
<img align="right" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
<br>
<p align="center">
  <img width="460" height="300" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
</p>

[This is button text, takes us to google.com](http://www.google.com)

![This text is loaded if image cannot be found](https://qa-courseware-images.s3.eu-west-2.amazonaws.com/markdown/links_images/000.jpeg)


![Manchester City][blue]
![Manchester United][red]

[blue]: https://cdn.images.express.co.uk/img/dynamic/footballteams/x256/20.png
[red]: https://icons.iconseeker.com/png/fullsize/soccer-teams/manchester-united-fc-logo.png


moving lines around
typing on multiple lines using middle mouse click

making a commit