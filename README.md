# bpo-chat-app-api
- A Chat/Messaging App 

## Build status
[![Build Status](https://travis-ci.org/walimike/bpo-chat-api.svg?branch=develop)](https://travis-ci.org/walimike/bpo-chat-api)                    [![Maintainability](https://api.codeclimate.com/v1/badges/485ab8670a489a8b4bb4/maintainability)](https://codeclimate.com/github/walimike/bpo-chat-api/maintainability)                           [![Coverage Status](https://coveralls.io/repos/github/walimike/bpo-chat-api/badge.svg?branch=add-test-coverage)](https://coveralls.io/github/walimike/bpo-chat-api?branch=add-test-coverage)

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
 
### Endpoint data formats

- User signup: No authentication needed
```
{
	"username":"wali",
	"email":"wali@email.com",
	"password":"password123",
	"password2":"password123"
}
```

- User login: No authentication needed
```
{
	"email":"wali@email.com",
	"password":"password123"
}
```

- Create chat instance: Authentication needed
```
{ }
```

- Join chat instance: Authentication needed. Non creator of chat instance joins
```
{
    "username": "wali"
}
```


- User refresh token:  Authorization header: Bearer Token + Acess Token from login endpoint
```
{
    "email":"wali@email.com",
    "password":"password123" 
}
```

- Send message to chat instance: Authentication needed. Must be a member of chat instance  
```
{
    "message": "Hello world"
}
```

