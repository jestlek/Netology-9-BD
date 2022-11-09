CREATE TABLE employee (
	id_employee SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	department INTEGER NOT NULL,
	id_chief INTEGER NOT NULL REFERENCES employee(id_employee)
);