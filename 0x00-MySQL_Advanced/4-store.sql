-- Create a Trigger to buy item
-- a trigger that decreases the quantity of an item in items table after adding a new order in orders table
CREATE TRIGGER QtyUpdate
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE NEW.item_name = name;
