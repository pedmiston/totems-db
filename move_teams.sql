UPDATE Table_Player SET Ancestor = 3 where ID_Player = 806
UPDATE Table_Player SET Ancestor = 4 where ID_Player = 825
UPDATE Table_Group SET Size=4 WHERE ID_Group = "G_10/16/2017 3:00:02 PM"
UPDATE Table_Group SET Size=4 WHERE ID_Group = "G_12/4/2017 1:29:48 PM"
UPDATE Table_Player SET ID_Group = "G_12/4/2017 1:29:48 PM" WHERE ID_Player = 806
UPDATE Table_Player SET ID_Group = "G_12/4/2017 1:29:48 PM" WHERE ID_Player = 825
