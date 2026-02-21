CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;


CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    order_status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON DELETE CASCADE
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    amount DECIMAL(10,2),
    payment_status VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON DELETE CASCADE
);


INSERT INTO users (name, email, password, phone, address) VALUES
('User1','user1@gmail.com','pass1','9000000001','Hyderabad'),
('User2','user2@gmail.com','pass2','9000000002','Delhi'),
('User3','user3@gmail.com','pass3','9000000003','Chennai'),
('User4','user4@gmail.com','pass4','9000000004','Mumbai'),
('User5','user5@gmail.com','pass5','9000000005','Bangalore'),
('User6','user6@gmail.com','pass6','9000000006','Pune'),
('User7','user7@gmail.com','pass7','9000000007','Kolkata'),
('User8','user8@gmail.com','pass8','9000000008','Goa'),
('User9','user9@gmail.com','pass9','9000000009','Jaipur'),
('User10','user10@gmail.com','pass10','9000000010','Surat');


INSERT INTO categories (category_name, description) VALUES
('Electronics','Electronic items'),
('Clothing','Fashion wear'),
('Books','Educational books'),
('Home','Home appliances'),
('Sports','Sports equipment');


INSERT INTO products (product_name, description, price, stock_quantity, category_id) VALUES
('iPhone 14','Apple smartphone',70000,15,1),
('Samsung TV','55 inch Smart TV',45000,8,1),
('Laptop Dell','Business Laptop',60000,12,1),
('Bluetooth Speaker','Portable speaker',2500,25,1),
('Men T-Shirt','Cotton T-Shirt',800,50,2),
('Women Saree','Silk Saree',3500,20,2),
('Jeans','Denim Jeans',1500,30,2),
('Python Book','Programming Book',1200,18,3),
('Data Science Book','ML Guide',1500,10,3),
('Cooking Book','Recipe Guide',900,22,3),
('Microwave','Kitchen Appliance',10000,5,4),
('Refrigerator','Double Door Fridge',30000,6,4),
('Sofa','Living Room Sofa',20000,4,4),
('Cricket Bat','Sports Bat',2000,14,5),
('Football','FIFA Standard',1200,25,5),
('Tennis Racket','Professional Racket',3500,9,5),
('Headphones','Noise Cancelling',5000,17,1),
('Smart Watch','Fitness Watch',8000,13,1),
('Office Chair','Ergonomic Chair',7000,11,4),
('Study Table','Wooden Table',9000,7,4);


INSERT INTO orders (user_id, total_amount, order_status) VALUES
(1,72000,'Completed'),
(2,45000,'Completed'),
(3,1500,'Pending'),
(4,3500,'Completed'),
(5,10000,'Completed'),
(6,2000,'Shipped'),
(7,1200,'Completed'),
(8,30000,'Completed'),
(9,2500,'Pending'),
(10,8000,'Completed'),
(1,1200,'Completed'),
(2,1500,'Cancelled'),
(3,20000,'Completed'),
(4,9000,'Completed'),
(5,5000,'Completed');


INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1,1,1,70000),
(1,4,1,2500),
(2,2,1,45000),
(3,8,1,1200),
(3,9,1,1500),
(4,6,1,3500),
(5,11,1,10000),
(6,14,1,2000),
(7,15,1,1200),
(8,12,1,30000),
(9,4,1,2500),
(10,18,1,8000),
(11,15,1,1200),
(12,9,1,1500),
(13,13,1,20000),
(14,20,1,9000),
(15,17,1,5000),
(5,5,2,800),
(6,16,1,3500),
(7,8,1,1200),
(8,19,1,7000),
(9,3,1,60000),
(10,4,2,2500),
(11,14,1,2000),
(12,5,3,800),
(13,10,2,900),
(14,1,1,70000),
(15,2,1,45000),
(3,15,1,1200),
(4,8,1,1200);



INSERT INTO payments (order_id, payment_method, amount, payment_status) VALUES
(1,'Credit Card',72000,'Paid'),
(2,'UPI',45000,'Paid'),
(3,'Debit Card',1500,'Pending'),
(4,'UPI',3500,'Paid'),
(5,'Net Banking',10000,'Paid'),
(6,'Credit Card',2000,'Paid'),
(7,'UPI',1200,'Paid'),
(8,'Net Banking',30000,'Paid'),
(9,'UPI',2500,'Pending'),
(10,'Credit Card',8000,'Paid'),
(11,'Debit Card',1200,'Paid'),
(12,'UPI',1500,'Refunded'),
(13,'Net Banking',20000,'Paid'),
(14,'Credit Card',9000,'Paid'),
(15,'UPI',5000,'Paid');
