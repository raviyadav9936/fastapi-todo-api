from database.models import User
from fastapi import HTTPException
import traceback
from datetime import datetime


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
        record=db.query(User).filter(User.tstatus=='true').all()
        result=[]
        for item in record:
            result.append({
                'id':item.id,
                'name':item.name,
                'email':item.email,
                'tstatus':item.tstatus
            })
        return {'status' : True ,'data' :result}
    
    except Exception as e:
        print('Error',e)
        return {'status': False,'message':'Something went wrong'} 
    
def update_record(id,schema,db):
    try:
        record=db.query(User).filter(User.id==id,User.tstatus=='true').first()
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
        record=db.query(User).filter(User.id==id,User.tstatus=='true').first()
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
        
        