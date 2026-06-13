import json
import uuid
import os

def generate_variant(output_dir="."):
    """
    Generates a unique UUID and a corresponding JSON configuration file
    for the portfolio variants.
    """
    variant_id = str(uuid.uuid4())[:8] # Using first 8 chars for brevity, or full str(uuid.uuid4())
    
    config = {
        "id": variant_id,
        "heroBadgeGreeting": {
            "en": f"Hello, I'm Nazareno - Custom Variant {variant_id}",
            "es": f"Hola, soy Nazareno - Variante Personalizada {variant_id}"
        },
        "heroBadgeRole": {
            "en": "Custom AI Engineer",
            "es": "Ingeniero de IA a medida"
        },
        "heroHeadingHighlight": {
            "en": "revolutionary",
            "es": "revolucionarios"
        },
        "heroSubheading": {
            "en": "This content was loaded in real-time from a remote GitHub configuration file.",
            "es": "Este contenido fue cargado en tiempo real desde un archivo de configuración remoto en GitHub."
        },
        "customProjects": ["agent-system"],
        "primaryColor": "280 65% 45%" # Example purple HSL
    }
    
    file_path = os.path.join(output_dir, f"{variant_id}.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        
    print(f"Generated variant: {variant_id}")
    print(f"File saved to: {file_path}")
    return variant_id

if __name__ == "__main__":
    generate_variant()
