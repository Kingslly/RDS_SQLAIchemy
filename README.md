# RDS_SQLAIchemy

1. The script connects to the RDS instance using the provided connection string in the create_engine() function.
2. A sample model User is defined with a table name 'users' and a single column 'name'.
3. The add_user() function is implemented to add a user to the table, logging the operation's success or failure.
4. The delete_rds_instance() function currently serves as a placeholder and should be replaced with the actual code to delete the RDS instance.
5. In the __main__ block, a user is added to the table by calling add_user("Kingslly RA").
6. At the end of the day (assuming the script is running continuously), the delete_rds_instance() function. This check ensures the RDS instance is deleted at the end of the day.
7. Any unexpected exceptions are caught and logged.
8. Finally, the session is closed, and the engine is disposed of.

#Please make sure to replace the placeholder values in the create_engine() function with the appropriate credentials for your RDS instance. Additionally, the code for deleting the RDS instance (delete_rds_instance()) should be implemented according to your specific requirements.
