

You can view the deployed project on http://rafay-wsdproject.herokuapp.com/authtest/
Login Credentials for developer:
Username: dani
Password: dani2819
Login Credentials for player:
Username: rafay
Password: dani2819

The project contains following features:
###Developer Module:

- Add the games to inventory
- Edit games
- Remove games
- See list of games on sales 
- See number of sales (sales statistics)


###Player Module

- View the games
- Search games by category
- Purchase the games using Niksula Payment Service api
- Play the game (hosted on the URL given by developer) 
- See game high scores while playing

###Game Service Interaction

Game and the game service communicate with window.postMessage. All the messages must contain a messageType attribute, which can be one of six things:

####SCORE

  sent from the game to the service, informing of a new score submission
  the message must also contain score attribute

####SAVE

  Sent from the game to the service, the service should now store the sent game state
  the message must also contain gameState attribute, containing game specific state information
  You can assume that the gameState is serializable by JSON.stringify

####LOAD_REQUEST

  Sent from the game to the service, requesting that a game state (if there is one saved) is sent from the service to the game
  The service will either respond with LOAD or  ERROR

####LOAD

  Sent from the service to the game
  Must contain gameState attribute, which has the game specific state to be loaded

####ERROR

  Sent from the service to the game
  Must contain info attribute, which contains textual information to be relayed to the user on what went wrong

####SETTING

  Sent from the game to the service once the game finishes loading
  Must contain options attribute, which tells game specific configuration to the service. This is mainly used to adjust the   layout in the service by providing a desired resolution in pixels, see examples for details.

###User Registration and Login
- Form created by using Django form functionality.
- Login and logout handled using Django Authentication System

###Django Rest Framework

REST API has been create using DJANGO REST framework to see the list of users. (http://rafay-wsdproject.herokuapp.com/api/)

###Responsive Design

For creating responsive design, we use bootstrap all over the project.
