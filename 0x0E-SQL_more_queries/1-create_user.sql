-- A script that creates a new user with all privilages
CREATE USER IF NOT EXISTS user_0d_1@localhost;
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO user_0d_1@localhost;
FLUSH PRIVILEGES;
