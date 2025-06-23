from database.models import User
from fastapi import HTTPException
import traceback
from datetime import datetime


def create_user(schema, db):
    try:
        active_user = db.query(User).filter(
            User.email == schema.email,
            User.tstatus == True
        ).first()

        if active_user:
            raise HTTPException(status_code=400, detail='Active user with this email already exists.')

        new_user = User(
            name=schema.name,
            email=schema.email,
            tstatus=True
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            'status': True,
            'message': 'User created successfully',
            'data': {
                'id': new_user.id,
                'name': new_user.name,
                'email': new_user.email
            }
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        print("Error:", e)
        return {'status': False, 'message': 'Something went wrong'}


def get_data(db):
    try:
        record=db.query(User).filter(User.tstatus==True).all()
        result=[]
        print(result,'====')
        for item in record:
            result.append({
                'id':item.id,
                'name':item.name,
                'email':item.email,
                'tstatus':item.tstatus
            })
        return {'status' : True ,'message':'fetch record sucessfully','data' :result}
    
    except Exception as e:
        print('Error',e)
        return {'status': False,'message':'Something went wrong'} 
    
    
def get_data_with_id(id,db):
    try:
        user=db.query(User).filter(User.id==id).first()
        if not user:
            raise HTTPException(status_code=404,detail='Record not found')
        result={
            'id':user.id,
            'name':user.name,
            'email':user.email,
            'tstatus':user.tstatus
        }
        return {'status' : True ,'message' : 'fetch record successfully' , 'data' :result}    
    except Exception as e:
        print('error',e)    
        return {'status' : False ,'message' : 'Something went wrong'}
    
    
def update_record(id,schema,db):
    try:
        record=db.query(User).filter(User.id==id,User.tstatus==True).first()
        if not record:
            raise HTTPException(status_code=404,detail="Record not found")
        
        record.name=schema.name,
        record.email=schema.email,
        record.updated_at=datetime.utcnow()
        
        db.commit()
        db.refresh(record)
        return {
            'status':True,
            'message':'User record updated successfully'
        }
        
    except HTTPException as e:
        raise e   
     
    except Exception as e:
        print('error',e)  
        return {'status': False ,'message':'Something went wrong'}
    
    
    
def delete_record(id,db):
    try:
        record=db.query(User).filter(User.id==id,User.tstatus==True).first()
        if not record:
            raise HTTPException(status_code=404,detail='Record not found')
        
        record.tstatus=False
        db.commit()
        return {'status' : True ,'message' :'User Record deleted successfull'}
    
    except HTTPException as e:
        return e
    
    except Exception as e:
        traceback.print_exc()
        print('error',e)
        return {'status' : False ,'message' :'Something went wrong'}     
        
        