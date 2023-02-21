# register_API
# API Documentation

## Authentication
All API endpoints require authentication. You must include an ***Authorization*** header with a valid token in all requests. Tokens can be obtained by logging in with valid credentials.

## Endpoints
### **POST /api/register**  

Register a new user.  

Request Body:  
{  
    "username": "testuser",  
    "password": "testpassword"  
}  
Response:  
HTTP/1.1 201 Created  
Content-Type: application/json  

{  
    "id": 1,  
    "username": "testuser",  
    "password": "********",  
    "is_staff": true  
}  


### **GET /api/works**  

Retrieve a list of works. Optionally filter by artist name or work type.  

Request Parameters:  

- ***artist***: Filter by artist name.  
- ***work_type***: Filter by ***work type***. Valid values are ***Youtube***, ***Instagram***, and ***Other***.  

Response:  

HTTP/1.1 200 OK
Content-Type: application/json

[  
    {  
        "id": 1,  
        "link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  
        "work_type": "Youtube",  
        "artists": [  
            {  
                "id": 1,  
                "name": "Rick Astley"  
            }  
        ]  
    },  
    {  
        "id": 2,  
        "link": "https://www.instagram.com/p/CGJ8Wpnjzzk/",  
        "work_type": "Instagram",  
        "artists": [  
            {  
                "id": 2,  
                "name": "Taylor Swift"  
            }  
        ]  
    }  
]  


## Error Responses  

### 400 Bad Request  

Returned when the request is invalid or cannot be processed.  

Response Body:  
{  
    "detail": "Error message."  
}  







