SHOW DATABASES;
USE nba_cli;
DROP TABLE player;
DROP TABLE team;

CREATE TABLE team (
    id int NOT NULL AUTO_INCREMENT,
    abbreviation varchar(3) ,
    city varchar(25),
    conference varchar(10) ,
    division varchar(25) ,
    full_name varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO team (abbreviation, city, conference, division, full_name) VALUES
    ('LAL','Los Angeles', 'West','Pacific','Los Angeles Lakers'),
    ('MEM', 'Memphis','West','Southwest','Memphis Grizzlies'),
    ('BOS', 'Boston', 'East','Atlantic','Boston Celtics'),
    ('DET', 'Detroit' ,'East','Central','Detroit Pistons')
    ;


CREATE TABLE player (
    id int NOT NULL AUTO_INCREMENT,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    position varchar(2),
    team_id int ,
    PRIMARY KEY (id),
    FOREIGN KEY (team_id) REFERENCES team(id)
);


INSERT INTO player (first_name, last_name, position, team_id) VALUES
    ('Lebron','James','F', 1),
    ('Rodney','McGruder','F', 4) 
    ;

SELECT *
FROM player
INNER JOIN team
ON player.team_id = team.id;