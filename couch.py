import ollama

def generate_cycling_plan():
    print("🚲 ========================================== 🚲")
    print("     TOUCH GRASS: LOCAL OFFLINE LLAMA 3.2 COACH ")
    print("🚲 ========================================== 🚲\n")
    
    location = input("Enter your trail or riding location (e.g., Karura Forest): ")
    goal = input("Enter your ride goal (e.g., 20km gravel ride): ")

    prompt = f"""
    Act as an expert outdoor cycling coach and trail mapper. The user is riding in: {location}. Their goal is: {goal}.
    Provide a structured response with:
    1. Terrain and route recommendations (surface type and elevation).
    2. Essential gear checklist (helmet, tools, water, safety lights).
    3. Wildlife and traffic safety tips for this area.
    4. A screen-free outdoor encouragement tip to stay present in nature.
    """

    print("\n⏳ Consulting your local open-weight Llama 3.2 model offline...")
    
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])

        print("\n" + "="*50)
        print("🗺️ YOUR OFFLINE LLAMA 3.2 TRAIL & SAFETY PLAN:")
        print("="*50)
        print(response.message.content)
        print("="*50)
        
    except Exception as e:
        print(f"\n[Error] Could not connect to Ollama. Make sure Ollama is open and running. Details: {e}")

if __name__ == "__main__":
    generate_cycling_plan()