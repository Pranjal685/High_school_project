CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS food_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  food_item_id INT NOT NULL,
  quantity INT NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (food_item_id) REFERENCES food_items(id)
);

INSERT INTO food_items (name, price)
SELECT 'Burger', 120.00
WHERE NOT EXISTS (SELECT 1 FROM food_items WHERE name = 'Burger');

INSERT INTO food_items (name, price)
SELECT 'Fries', 70.00
WHERE NOT EXISTS (SELECT 1 FROM food_items WHERE name = 'Fries');

INSERT INTO food_items (name, price)
SELECT 'Coke', 50.00
WHERE NOT EXISTS (SELECT 1 FROM food_items WHERE name = 'Coke');

INSERT INTO food_items (name, price)
SELECT 'McFlurry', 90.00
WHERE NOT EXISTS (SELECT 1 FROM food_items WHERE name = 'McFlurry');

INSERT INTO food_items (name, price)
SELECT 'Chicken Nuggets', 150.00
WHERE NOT EXISTS (SELECT 1 FROM food_items WHERE name = 'Chicken Nuggets');


