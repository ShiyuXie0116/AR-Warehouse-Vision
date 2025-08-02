def validate_all_datasets():
    """
    Validates data quality and completeness
    """
    validators = {
        'image_integrity': check_image_integrity,
        'annotation_validity': check_annotation_validity,
        'class_distribution': analyze_class_distribution,
        'size_requirements': check_size_requirements  # Ensures >15K samples
    }
    
    for dataset in ['sku110k', 'unity_synthetic', 'roboflow']:
        print(f"\nValidating {dataset}...")
        for name, validator in validators.items():
            result = validator(f'./data/{dataset}')
            print(f"  {name}: {'PASS' if result else 'FAIL'}")