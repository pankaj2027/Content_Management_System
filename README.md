# Step for setup the Content_Management_System project.

Step 1. Install python(V3.9), django(V3.1.6) and djnago restframework(V3.12.2).
        
        pip install djangorestframework

Step 2. Update your SECRET_KEY in config.py file.
       
       By default it has sqlite3 but you want to use Mysql or anyother database, then remove sqlite3 config settings from setting.py file and update the                  required server configuration in Config.py file as eg given for mysql in comments
        
Step 3. Now, we are done with the pre-requisites. Run the migration command to create the tables schema by the commands as given below.
        
        1. python3 manage.py makemigrations
        2. python3 manage.py migrate
        3. python3 group.py

Step 4. Create super User:
       
       1. python3 manage.py createsuperuser(keep Group_id=1, group_id 1 is for admin , and Group_id 2 is for author)
        
Step 5. Run the server.
        
        python3 manage.py runserver
        
Step 6. Register the author by using author_registation API via POSTMAN or django server.
       request POST : http://127.0.0.1:5000/author_registration/
       
       Example request body given below,update the content in <> with the real content
       BODY :   {
                  "email": "<author@xyz.com>",
                  "first_name": "<author_firstname>",
                  "last_name": "<author_lastname>",
                  "password": "<choose your password>",
                  "profile": {
                      "phone":<0123456789>,
                      "address": "<author_address>",
                      "city": "<author_city>",
                      "state": "<author_state",
                      "country": "<author_country>",
                      "pincode": <author_pincode>
                  }
              }
              
        After the successful registration, you will be receving the response  as below   
        
        Response: Your registration has been completed Successfully!!
        
    Note:- Token is automatically generated at the time of author registation 
    
Step 7. Get the token by using login API:-
        request POST:- http://127.0.0.1:5000/login/
        
        Body :- {
                  "username":"<author_email>",
                  "password":"<author_password>"
                  }
         you will receive the token which is created for you at the time of registration.
         Example as given below,
        Response:{
                  "Token":"073789a31e881f07af617b2bc65851f7278a2339"
                  }
                
step 8. Using the user token, author and admin can access their account by using Content API.

        if user is admin then admin can view, edit and delete all the contents created by multiple authors.
        if user is author then author can create, view, edit and delete contents created by author only.
        
        Api if request is GET-
                              http://127.0.0.1:5000/content_data/
                              
        Api if request is POST-
                              http://127.0.0.1:5000/content_data/
                              
        Api if request is UPDATE- 
                              http://127.0.0.1:5000/content_data/<cotent_id>
                              
        Api if request is DELETE- 
                              http://127.0.0.1:5000/content_data/<cotent_id>
                              
  Step 9. User Can search content by matching terms in title, body, summary and categories by using search API.
  
         Request GET: http://127.0.0.1:5000/content_data/?search=<search_keyword>
         
         For example:
                  http://127.0.0.1:5000/content_data/?search=software
        
   
   
   Thankyou
