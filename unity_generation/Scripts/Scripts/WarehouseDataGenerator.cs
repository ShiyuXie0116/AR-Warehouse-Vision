using UnityEngine;
using UnityEngine.Perception.Randomization;
using Unity.Simulation;

public class WarehouseDataGenerator : MonoBehaviour
{
    [SerializeField] private int targetImageCount = 50000;
    [SerializeField] private ScenarioBase scenario;
    
    void Start()
    {
        // Configure perception camera
        ConfigurePerceptionCamera();
        
        // Set up randomizers
        ConfigureRandomizers();
        
        // Start generation
        StartGeneration();
    }
    
    private void ConfigureRandomizers()
    {
        // Lighting randomization
        var lightRandomizer = scenario.GetRandomizer<LightingRandomizer>();
        lightRandomizer.intensityRange = new Vector2(0.5f, 2.0f);
        
        // Object placement randomization
        var placementRandomizer = scenario.GetRandomizer<PlacementRandomizer>();
        placementRandomizer.objectCountRange = new Vector2Int(50, 200);
        
        // Camera randomization (AR simulation)
        var cameraRandomizer = scenario.GetRandomizer<CameraRandomizer>();
        cameraRandomizer.enableMotionBlur = true;
    }
}