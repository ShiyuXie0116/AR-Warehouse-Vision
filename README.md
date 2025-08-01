# AR-Warehouse-Vision
Computer vision system for AR-enhanced warehouse inventory management with synthetic data generation pipeline

# AR-Enhanced Warehouse Inventory Management - Data Collection Pipeline

## Project Overview

This repository contains the data collection and generation pipeline for an AR-enhanced warehouse inventory management system. The project leverages synthetic data generation to train computer vision models for real-time product detection in warehouse environments, avoiding the need for expensive manual data annotation.

## Dataset Overview

### 1. Primary Datasets Explored

#### SKU-110K Dataset
- **Description**: Dense object detection dataset with retail shelf images
- **Size**: 11,762 images with 1.7M+ bounding boxes
- **Source**: [SKU-110K Paper](https://github.com/eg4000/SKU110K_CVPR19)
- **Usage**: Base dataset for training object detection models

#### Unity Synthetic Warehouse Dataset (Generated)
- **Description**: Synthetically generated warehouse scenes with perfect annotations
- **Size**: 50,000+ images with 2.5M+ annotations
- **Generation Method**: Unity Perception Package with domain randomization

#### Roboflow Warehouse Collections
- **Description**: Real-world warehouse and shelf detection datasets
- **Size**: 5,000+ annotated images
- **Source**: Roboflow Universe
- **Usage**: Validation and domain adaptation

### 2. Dataset Statistics

| Dataset | Images | Annotations | Size | Format |
|---------|--------|-------------|------|--------|
| SKU-110K | 11,762 | 1,733,678 | 13.6 GB | COCO JSON |
| Unity Synthetic | 50,000 | 2,500,000+ | 25 GB | Custom JSON + Images |
| Roboflow Mix | 5,000 | 150,000+ | 2.3 GB | YOLO/COCO |

Total dataset size: **40.9 GB** (stored using Git LFS and S3)

## Data Collection Pipeline

### 1. SKU-110K Dataset Collection

```python
# scripts/download_sku110k.py
import os
import wget
import tarfile

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
    
    print("SKU-110K dataset downloaded successfully!")
    
if __name__ == "__main__":
    download_sku110k()
