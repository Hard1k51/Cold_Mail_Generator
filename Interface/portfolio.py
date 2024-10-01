import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="Interface/support/my_portfolio.csv"):
        self.file_path = file_path
        try:
            self.data = pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error loading CSV file: {e}")

        # Initialize the Chroma client
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        # Load the portfolio only if the collection is empty
        if not self.collection.count():
            try:
                for _, row in self.data.iterrows():
                    self.collection.add(
                        documents=row["Techstack"],  # Assuming Techstack is a string
                        metadatas={"links": row["Links"]},  # Assuming Links exists
                        ids=[str(uuid.uuid4())]  # Unique ID for each entry
                    )
            except Exception as e:
                print(f"Error adding to collection: {e}")

    def query_links(self, skills):
        try:
            # Query the collection but limit the results to only 1
            results = self.collection.query(
                query_texts=skills,
                n_results=1  # Limiting to one result
            ).get('metadatas', [])

            if results:
                return results[0]  # Return only the first result
            else:
                print("No results found.")
                return None
        except Exception as e:
            print(f"Error querying collection: {e}")
            return None

# Example usage:
portfolio = Portfolio()

# Load the portfolio data into the collection (if not already loaded)
portfolio.load_portfolio()

# Query for a specific skill (example)
skill_query = "Python"  # Replace this with the skill you're querying for
result = portfolio.query_links(skill_query)

if result:
    print(f"Link for skill {skill_query}: {result['links']}")
else:
    print("No matching skills found.")



""" import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="Interface/support/my_portfolio.csv"):
        self.file_path = file_path
        try:
            self.data = pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            try:
                for _, row in self.data.iterrows():
                    self.collection.add(
                        documents=row["Techstack"],  # Assuming Techstack is a string
                        metadatas={"links": row["Links"]},  # Assuming Links exists
                        ids=[str(uuid.uuid4())]
                    )
            except Exception as e:
                print(f"Error adding to collection: {e}")

    def query_links(self, skills):
        try:
            # Get only one result and stop after the first one
            results = self.collection.query(
                query_texts=skills,
                n_results=1  # Limiting to one result
            ).get('metadatas', [])

            if results:
                return results[0]  # Return the first result only
            else:
                print("No results found.")
                return None
        except Exception as e:
            print(f"Error querying collection: {e}")
            return None """




""" import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="Interface/support/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_excel(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', []) """