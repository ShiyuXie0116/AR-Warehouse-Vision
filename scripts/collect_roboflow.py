from roboflow import Roboflow
import requests
import zipfile
import os

def download_roboflow_datasets(api_key, output_dir='./data/roboflow'):
    """
    Downloads multiple warehouse-related datasets from Roboflow
    """
    rf = Roboflow(api_key=api_key)
    
    datasets = [
        {"workspace": "workspace-name", "project": "warehouse-shelves", "version": 1},
        {"workspace": "another-workspace", "project": "inventory-detection", "version": 2},
        {"workspace": "third-workspace", "project": "shelf-monitoring", "version": 1}
    ]
    
    os.makedirs(output_dir, exist_ok=True)
    
    for dataset_info in datasets:
        project = rf.workspace(dataset_info["workspace"]).project(dataset_info["project"])
        dataset = project.version(dataset_info["version"])
        
        # Download in COCO format
        dataset.download("coco", location=output_dir)
        
        print(f"Downloaded {dataset_info['project']} successfully!")
    
    # Merge annotations
    merge_roboflow_annotations(output_dir)
    
    return output_dir

def merge_roboflow_annotations(data_dir):
    """
    Merges multiple Roboflow datasets into unified format
    """
    # Implementation for merging COCO annotations
    pass

if __name__ == "__main__":
    # Note: API key should be stored in environment variable
    api_key = os.environ.get('ROBOFLOW_API_KEY')
    download_roboflow_datasets(api_key)