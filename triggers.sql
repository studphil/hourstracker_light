-- Trigger for UPDATE
CREATE TRIGGER IF NOT EXISTS after_update_example_table
AFTER UPDATE ON record_entry
BEGIN
    INSERT INTO changelog (operation, old_data, new_data)
    VALUES ('UPDATE', OLD.data, NEW.data);
END;

-- Trigger for DELETE
CREATE TRIGGER IF NOT EXISTS after_delete_example_table
AFTER DELETE ON record_entry
BEGIN
    INSERT INTO changelog (operation, old_data, new_data)
    VALUES ('DELETE', OLD.data, NULL);
END;