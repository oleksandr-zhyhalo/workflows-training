import pytest
import json
from pathlib import Path
from app import DataProcessor

@pytest.fixture
def processor():
    # Use a temporary test directory
    processor = DataProcessor(storage_path="test_data")
    yield processor
    # Cleanup - remove test directory after tests
    for file in Path("test_data").glob("*.json"):
        file.unlink()
    Path("test_data").rmdir()

def test_process_data_valid_input(processor):
    data = [1, 2, 3, 4, 5]
    results = processor.process_data(data)
    
    assert results["input_length"] == 5
    assert results["sum"] == 15
    assert results["average"] == 3
    assert "processed_at" in results

def test_process_data_empty_list(processor):
    results = processor.process_data([])
    
    assert results["input_length"] == 0
    assert results["sum"] == 0
    assert results["average"] == 0

def test_process_data_invalid_input(processor):
    with pytest.raises(ValueError):
        processor.process_data("not a list")

def test_save_results(processor):
    test_data = {"test": "data"}
    file_path = processor.save_results(test_data, "test_output.json")
    
    assert file_path.exists()
    with open(file_path) as f:
        saved_data = json.load(f)
    assert saved_data == test_data