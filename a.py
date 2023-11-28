from neo4j import GraphDatabase

graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","sceptical@1234"))

session = graphdb.session()

#Creating node using cypher query in python
# q1 = "CREATE (virat:PLAYER{name:'Virat Kohli', age: 28, number: 23, height: 2.08, weight: 115}), (MS:PLAYER{name:'MS Dhoni', age: 28, number: 23, height: 2.08, weight: 115}) "

# nodes = session.run(q1)

#Retrieving all the nodes with different conditions
# q2 = "MATCH (x:PLAYER) RETURN (x)"
# q2 = "MATCH matched_player = (p:PLAYER)-[:PLAYS_FOR]->(T:TEAM)  RETURN matched_player limit 10"
#q2 = MATCH (p:PLAYER) where p.height >=2 RETURN p

# q2 = "MATCH (p:PLAYER) where p.name = 'Virat Kohli' MATCH (q:PLAYER) where q.name = 'MS Dhoni' RETURN p,q"

# q2 = "MATCH (p:PLAYER) where p.height >= 2.1 OR p.weight >=120 RETURN p"

# q2 = "MATCH (ja {name : 'Ja Morant'}) DETACH DELETE ja"

# q2 = "MATCH (virat{name:'Virat Kohli'}) SET virat.name = 'King Kohli' RETURN virat"

q2 = "MATCH (p:PLAYER) -[gamePlayed:PLAYED_AGAINST] -> (:TEAM) RETURN p.name ,COUNT(gamePlayed)"
nodes = session.run(q2)

for node in nodes:
    print(node)