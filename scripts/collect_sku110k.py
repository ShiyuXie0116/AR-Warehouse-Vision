# scripts/collect_sku110k.py
import os
import wget
import tarfile
import json
from tqdm import tqdm

def download_sku110k(output_dir='./data/sku110k'):
    """
    Downloads and extracts the SKU-110K dataset
    """
    url = 'http://trax-geometry.s3.amazonaws.com/cvpr_challenge/SKU110K_fixed.tar.gz'
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Download dataset
    print("Downloading SKU-110K dataset (13.6GB)...")
    filename = wget.download(url, out=output_dir)
    
    # Extract dataset
    print("\nExtracting dataset...")
    with tarfile.open(filename, 'r:gz') as tar:
        tar.extractall(output_dir)
    
    # Verify dataset integrity
    verify_dataset_integrity(output_dir)
    
    print("SKU-110K dataset downloaded successfully!")
    return output_dir

def create_sample_dataset(full_dataset_path, sample_size=100):
    """
    Creates a sample subset for GitHub repository
    """
    sample_path = './data/samples/sku110k'
    os.makedirs(sample_path, exist_ok=True)
    
    # Copy sample images and annotations
    # ... (implementation)
    
    return sample_path

if __name__ == "__main__":
    # Download full dataset
    full_path = download_sku110k()
    
    # Create sample for repository
    sample_path = create_sample_dataset(full_path)
    print(f"Sample dataset created at: {sample_path}")