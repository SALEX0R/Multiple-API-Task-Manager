api_endpoint_task_manager='''
{
     "task1": "http://127.0.0.1:5000/items/<int:item_id>",
     "params": "no parameters, just url parameter: given by item_id that signifies item to be replaced in url of function call [GET]",
     "api_type": "GET"
},

{
    "task2": http://127.0.0.1:5000/items",
    "params": " A json body with a structure as follows {
            "name": "name of the item in str based on user request",
            "description": "decription of the item in str in json format"
                } "
    "api_type": "POST"

}, 
{        
        "task3": "http://127.0.0.1:5000//items/<int:item_id>"
        "params": "url parameter as above item_id to be composed in url [DELETEs] that signifies item to be deleted in url of function call [POST]"
        "api_type": "DELETE"
}'''