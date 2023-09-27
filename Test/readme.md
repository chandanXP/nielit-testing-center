import pymongo
from django.http import HttpResponse
from .models import Todo  # Import your Todo model

def remove_todo(request, todo_id):
    if request.method == 'POST':
        try:
            # Assuming you want to remove a Todo record by its ID
            todo = Todo.objects.get(id=todo_id)

            # Connect to your MongoDB instance
            client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URL
            db = client["your_database_name"]  # Replace with your database name
            collection = db["your_collection_name"]  # Replace with your collection name

            # Remove the corresponding record from MongoDB
            collection.delete_one({"_id": todo_id})  # Assuming you have an "_id" field in your MongoDB document

            # Delete the Todo object from Django's ORM
            todo.delete()

            # Optionally, you can return a response to indicate success
            return HttpResponse("Todo removed successfully")
        except Todo.DoesNotExist:
            return HttpResponse("Todo not found")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    else:
        # Handle GET requests or other HTTP methods if needed
        return HttpResponse("Invalid request method")





----------------------------------------------

nect to your MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URL
db = client["your_database_name"]  # Replace with your database name
collection = db["your_collection_name"]  # Replace with your collection name

# Update the corresponding record in MongoDB
collection.update_one({"_id": todo_id}, {"$set": {"todo": updated_todo}})

# Update the Todo object in Django's ORM
todo.todo = updated_todo
todo.save()