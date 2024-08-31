import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'host': 'localhost'
}

# Create a connection to MySQL
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS virtual_time_capsule")
    cursor.execute("USE virtual_time_capsule")

    # Create tables
    tables = {
        'users': (
            "CREATE TABLE IF NOT EXISTS users ("
            "    user_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    username VARCHAR(50) NOT NULL UNIQUE,"
            "    email VARCHAR(100) NOT NULL UNIQUE,"
            "    password_hash VARCHAR(255) NOT NULL,"
            "    profile_picture_url VARCHAR(255),"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            ")"
        ),
        'friendships': (
            "CREATE TABLE IF NOT EXISTS friendships ("
            "    friendship_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    user_id1 INT,"
            "    user_id2 INT,"
            "    status ENUM('pending', 'accepted', 'rejected') DEFAULT 'pending',"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (user_id1) REFERENCES users(user_id),"
            "    FOREIGN KEY (user_id2) REFERENCES users(user_id)"
            ")"
        ),
        'messages': (
            "CREATE TABLE IF NOT EXISTS messages ("
            "    message_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    sender_id INT,"
            "    receiver_id INT,"
            "    message_text TEXT,"
            "    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (sender_id) REFERENCES users(user_id),"
            "    FOREIGN KEY (receiver_id) REFERENCES users(user_id)"
            ")"
        ),
        'time_capsules': (
            "CREATE TABLE IF NOT EXISTS time_capsules ("
            "    capsule_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    creator_id INT,"
            "    title VARCHAR(100),"
            "    description TEXT,"
            "    unlock_date DATE,"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (creator_id) REFERENCES users(user_id)"
            ")"
        ),
        'capsule_contents': (
            "CREATE TABLE IF NOT EXISTS capsule_contents ("
            "    content_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    capsule_id INT,"
            "    file_url VARCHAR(255),"
            "    content_type ENUM('file', 'image'),"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (capsule_id) REFERENCES time_capsules(capsule_id)"
            ")"
        ),
        'posts': (
            "CREATE TABLE IF NOT EXISTS posts ("
            "    post_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    user_id INT,"
            "    content TEXT,"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (user_id) REFERENCES users(user_id)"
            ")"
        ),
        'comments': (
            "CREATE TABLE IF NOT EXISTS comments ("
            "    comment_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    post_id INT,"
            "    user_id INT,"
            "    comment_text TEXT,"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (post_id) REFERENCES posts(post_id),"
            "    FOREIGN KEY (user_id) REFERENCES users(user_id)"
            ")"
        ),
        'notifications': (
            "CREATE TABLE IF NOT EXISTS notifications ("
            "    notification_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    user_id INT,"
            "    notification_text TEXT,"
            "    is_read BOOLEAN DEFAULT FALSE,"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (user_id) REFERENCES users(user_id)"
            ")"
        ),
        'user_memories': (
            "CREATE TABLE IF NOT EXISTS user_memories ("
            "    memory_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    user_id INT,"
            "    image_url VARCHAR(255),"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (user_id) REFERENCES users(user_id)"
            ")"
        ),
        'locked_capsules': (
            "CREATE TABLE IF NOT EXISTS locked_capsules ("
            "    locked_capsule_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    recipient_id INT,"
            "    capsule_id INT,"
            "    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (recipient_id) REFERENCES users(user_id),"
            "    FOREIGN KEY (capsule_id) REFERENCES time_capsules(capsule_id)"
            ")"
        ),
        'wall_comments': (
            "CREATE TABLE IF NOT EXISTS wall_comments ("
            "    comment_id INT AUTO_INCREMENT PRIMARY KEY,"
            "    user_id INT,"
            "    wall_owner_id INT,"
            "    comment_text TEXT,"
            "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "    FOREIGN KEY (user_id) REFERENCES users(user_id),"
            "    FOREIGN KEY (wall_owner_id) REFERENCES users(user_id)"
            ")"
        )
    }

    # Create each table
    for table_name, create_statement in tables.items():
        try:
            print(f"Creating table {table_name}...")
            cursor.execute(create_statement)
        except mysql.connector.Error as err:
            print(f"Failed creating table {table_name}: {err}")

    print("Database and tables created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    conn.close()
