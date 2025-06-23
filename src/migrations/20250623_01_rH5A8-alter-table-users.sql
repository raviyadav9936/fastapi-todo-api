--  alter-table-users
-- depends: 
ALTER TABLE users ADD COLUMN (
    tstatus character varying(50),
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp DEFAULT CURRENT_TIMESTAMP
    );
