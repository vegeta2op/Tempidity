# Tempidity

A fun yet simple project where we aim to Integrate ESP32 sensor readings and show it on a flask Web App (Even add it as a wallpaper)

## Instructions to start ESP32

- Firstly You will need to start ESP32 with the sensors 

- Refer [ ESP32 and Firebase Integration]()

- Once ready Clone This Repo. (Refer Intsallation Section here)
- 
## Installation And Deployment

#### Clone this Repo  

```bash
  git clone https://github.com/vegeta2op/Tempidity.git
```
- Opne the File you cloned with VS code or editor of your choice.

- Open app.py refer the `cred = credentials.Certificate`, Here change the Path file to the place where the Json file is stored, generally in Downloads.

- Also in `'databaseURL': 'URL'` replace URL with the actual URL of database from firebase .

#### Now run requirements.txt file 
```bash
pip install -r requirements.txt
```

#### Finally run app.py
```bash
python app.py
```
#### - Now You have to visit the Local Host and check the temperature readings 

## Tech Stack

**Client:** HTML,CSS,JQuery
**Server:** 

![N|Solid](https://img.icons8.com/color/48/python--v1.png)![N|Solid](https://img.icons8.com/color/48/flask.png)

## Output

![N|Solid](https://github.com/vegeta2op/Academic-App/assets/71753965/d9007f09-e4c0-49c0-9736-dbf88c07f390)

#### The Output will vary based on your location . 
- To use it as your wallpaper , download an app for windows called lively. 

#### Pro Tip : Use raspberry pi to deploy this through ssh and access it winthin the network and use this as a screen saver or wallpaper (modify it as you like)

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


