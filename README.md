# Step for setup the Content_Management_System project.

step 1. Install djnago restframework.
         pip install djangorestframework

step 2. Update your SECRET_KEY in config.py file.
        By default it has sqlite3 but you want to use Mysql or anyother database then update the configuration in Config.py file
        
step 3. Run the migration command.
        1. python3 manage.py makemigrations
        2. python3 manage.py migrate
        3. python3 group.py

step 4. Create super User:
        1. python3 manage.py createsuperuser(keep Group_id=1, group_id 1 is for admin , and Group_id 2 is for author)
        
step 5. Run the server.
        python3 manage.py runserver
        
step 6. Register the author by using author_registation API via POSTMAN or django browser.
       request POST : http://127.0.0.1:5000/author_registration/
       
       BODY :   {
                  "email": "pankaj2027@gmail.com",
                  "first_name": "pankaj",
                  "last_name": "chaudhary",
                  "password": "Pankaj2027",
                  "profile": {
                      "phone": 9096324594,
                      "address": "agra",
                      "city": "Agra",
                      "state": "UTTAR PRADESH",
                      "country": "India",
                      "pincode": 282005
                  }
              }
        Response: Your registration has been completed Successfully!!
        
    Note:- Token is automatically generated at the time of author registation 
    
step 7. Get the token by using login API:-
        request POST:- http://127.0.0.1:5000/login/
        
        Body :- {
                  "username":"pankaj2027@gmail.com",
                  "password":"Pankaj2027"
                  }
        Response:{
                  "Token":"072789a31d881f07af607b2bc65851f7278a2119"
                  }
                
step 8. using user token author and admin can access their account by using Content API.

        if user is admin then he can view, edit and delete all the contents created by multiple authors.
        if user is author then he can create, view, edit and delete contents created by him only.
        
        Api if request is GET-
                              http://127.0.0.1:5000/content_data/
                              
       Api if request is POST-
                              http://127.0.0.1:5000/content_data/
                              
        Api if request is UPDATE- 
                              http://127.0.0.1:5000/content_data/<cotent_id>
                              
       Api if request is DELETE- 
                              http://127.0.0.1:5000/content_data/<cotent_id>
                              
  Step 9. Author Can search content by matching terms in title, body, summary and categories by using search API.
  
         Request GET: http://127.0.0.1:5000/content_data/?search=<title><body><summary><categories>
         eg. http://127.0.0.1:5000/content_data/?search=software pankaj 50
        
         
