from fastapi import FastAPI
from neo4j import GraphDatabase
import os

app = FastAPI()

# Neo4j connection details
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "test")

# Initialize the Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test-neo4j")
def test_neo4j():
    with driver.session() as session:
        result = session.run("RETURN 'Hello, Neo4j!' AS message")
        message = result.single()["message"]
        return {"message": message}
