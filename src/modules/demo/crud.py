from database.models import User

def show_user():
    try:
       user={
           'data': {'Name':'Ravi','Dept':'It'}
             }
       return user
    except Exception as e:
        print("Error:", e)
        return {"status": False, "message": "Something went wrong"}
    
def index(id:int):
    try:
        return {'data':id}
    except Exception as e:
        print('Error',e)       
        return {'status': False,'message':'Something went wrong'} 


def create_user(schema,db):
    try:
        data=User(
            name=schema.name,
            email=schema.email
        )
        db.add(data)
        db.commit()
        db.refresh(data)
        return {'status' : True ,
                'message':'data created sucessfully',
                'data':{
                    'id':data.id,
                    'name':data.name,
                    'email':data.email
                }}
    except Exception as e:
        print('Error',e)
        return {'status': False,'message':'Something went wrong'} 
    

def get_data(db):
    try:
        record=db.query(User).all()
        return {'status' : True ,'data' :record}
    except Exception as e:
        print('Error',e)
        return {'status': False,'message':'Something went wrong'} 
        
        