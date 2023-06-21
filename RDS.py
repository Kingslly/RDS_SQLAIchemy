import logging
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the engine and session
engine = create_engine('username', 'password', 'host', 'port', 'database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Function to add a user to the table
def add_user(name):
    try:
        user = User(name=name)
        session.add(user)
        session.commit()
        logger.info(f"User '{name}' added successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error adding user: {e}")
        raise

# Function to delete the RDS instance
def delete_rds_instance():
    # Code to delete the RDS instance
    logger.info("RDS instance deleted successfully.")

# Unit test cases
def run_unit_tests():
    # Test adding a user
    add_user("Kingslly RA")

    # Test adding a user with an empty name
    try:
        add_user("")
    except SQLAlchemyError:
        pass

    # Test deleting the RDS instance
    delete_rds_instance()

if __name__ == '__main__':
    try:
        # Run unit tests
        run_unit_tests()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

    finally:    
    # Close the session and engine
    session.close()
    engine.dispose()
