# app.py
import json
from datetime import datetime
from pathlib import Path

class DataProcessor:
    def __init__(self, storage_path="data"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
        
    def process_data(self, data):
        """Process input data and return transformed results."""
        if not isinstance(data, list):
            raise ValueError("Input must be a list of numbers")
            
        results = {
            "input_length": len(data),
            "sum": sum(data),
            "average": sum(data) / len(data) if data else 0,
            "processed_at": datetime.now().isoformat()
        }
        return results
        
    def save_results(self, results, filename=None):
        """Save processing results to a JSON file."""
        if filename is None:
            filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        file_path = self.storage_path / filename
        with open(file_path, 'w') as f:
            json.dump(results, f, indent=2)
        return file_path

def main():
    # Example usage
    processor = DataProcessor()
    sample_data = [1, 2, 3, 4, 5]
    
    try:
        results = processor.process_data(sample_data)
        file_path = processor.save_results(results)
        print(f"Processed data with the following results:")
        print(json.dumps(results, indent=2))
        print(f"\nResults saved to: {file_path}")
    except Exception as e:
        print(f"Error processing data: {e}")
        raise

if __name__ == "__main__":
    main()