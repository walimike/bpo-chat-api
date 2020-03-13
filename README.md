# [bpo-chat-app-api](http://walimike.pythonanywhere.com/api/v1/users/hello/)
- A Chat/Messaging App 

##### API Demo
http://walimike.pythonanywhere.com/api/v1/users/hello/

## Build status
[![Build Status](https://travis-ci.org/walimike/bpo-chat-api.svg?branch=develop)](https://travis-ci.org/walimike/bpo-chat-api)                   [![Coverage Status](https://coveralls.io/repos/github/walimike/bpo-chat-api/badge.svg?branch=develop)](https://coveralls.io/github/walimike/bpo-chat-api?branch=develop)                        [![Maintainability](https://api.codeclimate.com/v1/badges/485ab8670a489a8b4bb4/maintainability)](https://codeclimate.com/github/walimike/bpo-chat-api/maintainability)

## Features
1. Personal message
- A user is able to send a personal message to another user
2. Group message​ (1:n, where n > 1)
- A user is able to send a message to a group of users
3. SignUp and LogIn​ (Django Auth)
- A user can signuo/login using Django’s Authentication system
4. Live chat
- Messages are automatically updated without having to refresh the page

## Tech stack
- Python 3
- Django
- Django Rest Framework
- PostgresQL

### Endpoint details
| Functionality | Endpoint | HTTP VERB |
| --- | --- |--- | 
| User signup | `/api/v1/users/signup/` | POST |
| User signin |  `/api/v1/users/login/` | POST |
| User refresh token |  `/api/v1/users/refresh/` | POST |
| Create a chat instance |  `/api/v1/chats/` | POST |
| Join a chat instance |  `/api/v1/chats/<chat_uri>` | PATCH |
| Send message to chat instance |  `/api/v1/chats/<chat_uri>/messages/` | POST | 
| Get messages from chat instance |  `/api/v1/chats/<chat_uri>/messages/` | GET |
 
### API Schema
```
bpo-chat-api: V1
info:
  title: 'A chat app for individuals or groups'
paths:
  /api/v1/chats/{uri}/messages/:
    get:
      operationId: listChatSessionMessages
      description: return all messages in a chat session.
      parameters:
      - name: uri
        in: path
        required: true
        description: ''
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items: {}
          description: ''
    post:
      operationId: CreateChatSessionMessage
      description: create a new message in a chat session.
      parameters:
      - name: uri
        in: path
        required: true
        description: ''
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: ''
  /api/v1/users/signup/:
    post:
      operationId: CreateRegistration
      description: Allow any user (authenticated or not) to access this endpoint
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              properties:
                email:
                  type: string
                  format: email
                  maxLength: 254
                username:
                  type: string
                  maxLength: 255
                password:
                  type: string
                  writeOnly: true
                  maxLength: 128
                  minLength: 8
                password2:
                  type: string
                  writeOnly: true
              required:
              - email
              - username
              - password
              - password2
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  email:
                    type: string
                    format: email
                    maxLength: 254
                  username:
                    type: string
                    maxLength: 255
                required:
                - email
                - username
          description: ''
  /api/v1/users/login/:
    post:
      operationId: CreateTokenObtainPair
      description: 'Takes a set of user credentials and returns an access and refresh
        JSON web
        token pair to prove the authentication of those credentials.'
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              properties:
                email:
                  type: string
                password:
                  type: string
                  writeOnly: true
              required:
              - email
              - password
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  email:
                    type: string
                required:
                - email
          description: ''
  /api/v1/users/refresh/:
    post:
      operationId: CreateTokenRefresh
      description: 'Takes a refresh type JSON web token and returns an access type
        JSON web
        token if the refresh token is valid.'
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              properties:
                refresh:
                  type: string
              required:
              - refresh
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  refresh:
                    type: string
                required:
                - refresh
          description: ''
  /api/v1/chats/:
    post:
      operationId: CreateChatSession
      description: create a new chat session.
      parameters: []
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: ''
    patch:
      operationId: PartialUpdateChatSession
      description: Add a user to a chat session.
      parameters: []
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: ''
  /api/v1/chats/{uri}/:
    post:
      operationId: CreateChatSession
      description: create a new chat session.
      parameters:
      - name: uri
        in: path
        required: true
        description: ''
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: ''
    patch:
      operationId: PartialUpdateChatSession
      description: Add a user to a chat session.
      parameters:
      - name: uri
        in: path
        required: true
        description: ''
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: ''
```

## Authors
[Michael Robert Wali](https://www.linkedin.com/in/walimike/)
