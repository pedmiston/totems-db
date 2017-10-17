-- Reset group 'G_10/2/2017 12:36:08 PM'
UPDATE Table_Group SET Size = 4, Open = 0 WHERE ID_Group = 'G_10/2/2017 12:36:08 PM'
-- Create new group for ID_Player = 463
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:00 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:00 PM', Ancestor = 1 WHERE ID_Player = 463
-- Create new group for ID_Player = 467
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:01 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:01 PM', Ancestor = 1 WHERE ID_Player = 467
-- Reset group 'G_10/2/2017 12:58:52 PM'
UPDATE Table_Group SET Size = 4, Open = 0 WHERE ID_Group = 'G_10/2/2017 12:58:52 PM'
-- Create new group for ID_Player = 465
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:02 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:02 PM', Ancestor = 1 WHERE ID_Player = 465
-- Create new group for ID_Player = 468
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:03 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:03 PM', Ancestor = 1 WHERE ID_Player = 468
-- Reset group 'G_10/9/2017 12:31:17 PM'
UPDATE Table_Group SET Size = 2, Open = 0 WHERE ID_Group = 'G_10/9/2017 12:31:17 PM'
UPDATE Table_Player SET Ancestor = 2 WHERE ID_Player = 447
-- Create new group for ID_Player = 451
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:04 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:04 PM', Ancestor = 1 WHERE ID_Player = 451
-- Create new group for ID_Player = 461
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:05 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:05 PM', Ancestor = 1 WHERE ID_Player = 461
-- Create new group for ID_Player = 466
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:06 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:06 PM', Ancestor = 1 WHERE ID_Player = 466
-- Create new group for ID_Player = 469
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:07 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:07 PM', Ancestor = 1 WHERE ID_Player = 469
-- Reset group 'G_10/9/2017 2:06:26 PM'
UPDATE Table_Group SET Size = 3, Open = 0 WHERE ID_Group = 'G_10/9/2017 2:06:26 PM'
UPDATE Table_Player SET Ancestor = 3 WHERE ID_Player = 454
-- Create new group for player 453
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:08 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:08 PM', Ancestor = 1 WHERE ID_Player = 453
-- Delete empty players
DELETE FROM Table_Player WHERE ID_Player IN (459, 471)
-- Reset group 'G_10/9/2017 2:30:09 PM'
UPDATE Table_Group SET Size = 4, Open = 0 WHERE ID_Group = 'G_10/9/2017 2:30:09 PM'
UPDATE Table_Player SET Ancestor = 4 WHERE ID_Player = 464
-- Create new group for player 462
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:09 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:09 PM', Ancestor = 1 WHERE ID_Player = 462
-- Create new group for player 472
INSERT INTO Table_Group (ID_Group, Size, Open, Treatment, BuildingTime, Status) VALUES ('G_10/16/2017 3:00:10 PM', 1, 0, 'Isolated', 25, '')
UPDATE Table_Player SET ID_Group = 'G_10/16/2017 3:00:10 PM', Ancestor = 1 WHERE ID_Player = 472
