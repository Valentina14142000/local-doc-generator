from graph import create_doc_graph

def run():
    print("Initializing Local Documentation Generator...")
    app = create_doc_graph()

    # Sample source code to document
    sample_code = """
    class RateLimiter:
        def __init__(self, max_calls: int, period_seconds: int):
            self.max_calls = max_calls
            self.period_seconds = period_seconds
            self.calls = []

        def allow_request(self, timestamp: float) -> bool:
            self.calls = [t for t in self.calls if t > timestamp - self.period_seconds]
            if len(self.calls) < self.max_calls:
                self.calls.append(timestamp)
                return True
            return False
    """

    print(f"\nGenerating Documentation for Sample Code...\n")
    result = app.invoke({"source_code": sample_code})
    
    print("=== Generated Markdown Documentation ===")
    print(result["markdown_docs"])
    print("========================================")

if __name__ == "__main__":
    run()
