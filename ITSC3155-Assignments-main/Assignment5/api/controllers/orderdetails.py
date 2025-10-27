from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, orderdetail):
    # Create a new instance of the OrderDetail model with the provided data
    db_orderdetail = models.OrderDetail(
        amount=orderdetail.amount,
    )
    # Add the newly created OrderDetail object to the database session
    db.add(db_orderdetail)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_orderdetail)
    # Return the newly created OrderDetail object
    return db_orderdetail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, orderdetail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id).first()


def update(db: Session, orderdetail_id, orderdetail):
    # Query the database for the specific orderdetail to update
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id)
    # Extract the update data from the provided 'orderdetail' object
    update_data = orderdetail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_orderdetail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated orderdetail record
    return db_orderdetail.first()


def delete(db: Session, orderdetail_id):
    # Query the database for the specific orderdetail to delete
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id)
    # Delete the database record without synchronizing the session
    db_orderdetail.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)