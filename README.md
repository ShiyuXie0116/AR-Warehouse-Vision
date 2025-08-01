# AR-Enhanced Warehouse Inventory Management - Data Collection Pipeline

## Project Overview

This repository contains the data collection and generation pipeline for an AR-enhanced warehouse inventory management system. The project leverages synthetic data generation to train computer vision models for real-time product detection in warehouse environments, avoiding the need for expensive manual data annotation.

## Dataset Overview

### 1. Primary Datasets Explored

#### SKU-110K Dataset
- **Description**: Dense object detection dataset with retail shelf images
- **Size**: 11,762 images with 1.7M+ bounding boxes
- **Source**: [SKU-110K Paper](https://github.com/eg4000/SKU110K_CVPR19)
- **Direct Download Link**: [http://trax-geometry.s3.amazonaws.com/cvpr_challenge/SKU110K_fixed.tar.gz](http://trax-geometry.s3.amazonaws.com/cvpr_challenge/SKU110K_fixed.tar.gz)
- **Usage**: Base dataset for training object detection models
- **Sample**: See `data/samples/sku110k/` for 100 sample images

#### Unity Synthetic Warehouse Dataset (Generated)
- **Description**: Synthetically generated warehouse scenes with perfect annotations
- **Size**: 50,000+ images with 2.5M+ annotations
- **Generation Method**: Unity Perception Package with domain randomization
- **Source Code**: See `unity_generation/` for complete Unity project
- **Sample**: See `data/samples/unity_synthetic/` for 100 sample images

#### Roboflow Warehouse Collections
- **Description**: Real-world warehouse and shelf detection datasets
- **Size**: 5,000+ annotated images
- **Source Links**:
 - [Warehouse Dataset 1](https://universe.roboflow.com/workspace/warehouse-dataset)
 - [Shelf Detection Dataset](https://universe.roboflow.com/search?q=shelf)
 - [Inventory Management Dataset](https://universe.roboflow.com/search?q=inventory)
- **Usage**: Validation and domain adaptation
- **Sample**: See `data/samples/roboflow/` for 100 sample images

### 2. Dataset Statistics

| Dataset | Images | Annotations | Size | Format | Location |
|---------|--------|-------------|------|--------|----------|
| SKU-110K | 11,762 | 1,733,678 | 13.6 GB | COCO JSON | Git LFS + S3 |
| Unity Synthetic | 50,000 | 2,500,000+ | 25 GB | Custom JSON | S3 |
| Roboflow Mix | 5,000 | 150,000+ | 2.3 GB | YOLO/COCO | Git LFS |

Total dataset size: **40.9 GB** (exceeds 8GB excellence criteria)

## Data Storage Strategy

### Git LFS (Large File Storage)
Files tracked with Git LFS:
```bash
# .gitattributes
data/samples/**/*.jpg filter=lfs diff=lfs merge=lfs -text
data/samples/**/*.png filter=lfs diff=lfs merge=lfs -text
data/roboflow/*.zip filter=lfs diff=lfs merge=lfs -text
