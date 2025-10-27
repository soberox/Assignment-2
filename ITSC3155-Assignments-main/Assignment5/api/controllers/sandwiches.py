from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas
from ..models.schemas import Sandwich


def create(db: Session, sandwhich):
    # Create a new instance of the Sandwich
    # model with the provided data
    db_sandwhich = (models.Sandwich
        (
        sandwich_name=sandwhich.sandwich_name,
        price=sandwhich.price
    ))
    # Add the newly created Sandwich
    # object to the database session
    db.add(db_sandwhich)
    # Commit the changes to the database
    db.commit()
    # Refresh the Sandwich
    # object to ensure it reflects the current state in the database
    db.refresh(db_sandwhich)
    # Return the newly created Sandwich
    # object
    return db_sandwhich


def read_all(db: Session):
    return db.query(models.Sandwich
                    ).all()


def read_one(db: Session, sandwhich_id):
    return db.query(models.Sandwich
                    ).filter(models.Sandwich.id == sandwhich_id).first()


def update(db: Session, sandwhich_id, sandwhich):
    # Query the database for the specific sandwhich to update
    db_sandwhich = db.query(models.Sandwich
                            ).filter(models.Sandwich.id == sandwhich_id)
    # Extract the update data from the provided 'sandwhich' object
    update_data = sandwhich.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_sandwhich.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated sandwhich record
    return db_sandwhich.first()


def delete(db: Session, sandwhich_id):
    # Query the database for the specific sandwhich to delete
    db_sandwhich = db.query(models.Sandwich
                            ).filter(models.Sandwich.id == sandwhich_id)
    # Delete the database record without synchronizing the session
    db_sandwhich.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
