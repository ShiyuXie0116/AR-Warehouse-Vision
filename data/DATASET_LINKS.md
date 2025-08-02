# Full Dataset Download Links

This repository contains only sample data. Full datasets are available at:

## SKU-110K Dataset (13.6 GB)
- Direct Download: http://trax-geometry.s3.amazonaws.com/cvpr_challenge/SKU110K_fixed.tar.gz
- Paper: https://arxiv.org/abs/1904.00853
- GitHub: https://github.com/eg4000/SKU110K_CVPR19

## Unity Synthetic Dataset (25 GB)
- Status: Generated using Unity Perception Package
- Storage: AWS S3 (private bucket)
- Access: Contact project maintainer
- Generation Code: See `unity_generation/` folder

## Roboflow Datasets (2.3 GB)
- Source: https://universe.roboflow.com/
- Specific datasets used:
  - Warehouse Detection: https://universe.roboflow.com/search?q=warehouse
  - Shelf Detection: https://universe.roboflow.com/search?q=shelf
  - Inventory Management: https://universe.roboflow.com/search?q=inventory

## Total Dataset Size: 40.9 GB

To download full datasets, use the scripts in the `scripts/` folder:
```bash
python scripts/collect_sku110k.py
python scripts/collect_roboflow.py --api-key YOUR_API_KEY