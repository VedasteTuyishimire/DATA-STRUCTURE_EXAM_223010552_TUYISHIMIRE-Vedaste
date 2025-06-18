# Traffic Light Manager

## Project Description
This project implements a traffic light management system that demonstrates key object-oriented programming concepts including inheritance, polymorphism, and dynamic memory management. The system simulates different types of traffic light controllers (Urban and Pedestrian) with their own cycling patterns.

## Implementation Process
The project was completed in several key steps:

1. **State Structure Design**
   - Created a State struct to hold traffic light state information
   - Implemented dynamic memory allocation for state arrays
   - Used fixed-size character arrays for color strings

2. **Base Class Implementation**
   - Designed abstract TrafficLightController class
   - Implemented virtual destructor for proper cleanup
   - Added pure virtual cycle() method for polymorphic behavior

3. **Derived Classes Development**
   - Created UrbanController with three states (RED, GREEN, YELLOW)
   - Implemented PedestrianController with two states (WALK, DONT_WALK)
   - Added state-specific timing configurations

4. **Manager Class Creation**
   - Implemented dynamic array management for controllers
   - Added controller addition and removal functionality
   - Ensured proper memory management with RAII principles

5. **Testing and Refinement**
   - Added console output for state transitions
   - Implemented error checking for array bounds
   - Verified memory management and cleanup

## Detailed Code Implementation

### State Structure
```cpp
struct State {
    char color[10];    // Fixed-size array to store color name (e.g., "RED", "GREEN")
    int duration;      // Duration in seconds for this state
};
```

### Abstract Base Class
```cpp
class TrafficLightController {
protected:
    State* states;         // Dynamic array to store all possible states
    int stateCount;        // Total number of states in the array
    int currentState;      // Index of the current state

public:
    // Constructor initializes all members to safe default values
    TrafficLightController() : states(nullptr), stateCount(0), currentState(0) {}
    
    // Virtual destructor ensures proper cleanup of derived classes
    virtual ~TrafficLightController() { delete[] states; }
    
    // Pure virtual function that must be implemented by derived classes
    virtual void cycle() = 0;
    
    // Accessor methods for current state information
    const char* getCurrentColor() const { return states[currentState].color; }
    int getCurrentDuration() const { return states[currentState].duration; }
};
```

### Urban Controller Implementation
```cpp
class UrbanController : public TrafficLightController {
public:
    UrbanController() {
        // Initialize with three states for urban traffic light
        stateCount = 3;
        states = new State[stateCount];
        
        // Configure RED state (30 seconds)
        strcpy(states[0].color, "RED");
        states[0].duration = 30;
        
        // Configure GREEN state (45 seconds)
        strcpy(states[1].color, "GREEN");
        states[1].duration = 45;
        
        // Configure YELLOW state (5 seconds)
        strcpy(states[2].color, "YELLOW");
        states[2].duration = 5;
    }

    // Implement cycling behavior for urban traffic light
    void cycle() override {
        // Move to next state using modulo for circular cycling
        currentState = (currentState + 1) % stateCount;
        // Output current state information
        std::cout << "Urban Light: " << getCurrentColor() 
                  << " (" << getCurrentDuration() << "s)" << std::endl;
    }
};
```

### Pedestrian Controller Implementation
```cpp
class PedestrianController : public TrafficLightController {
public:
    PedestrianController() {
        // Initialize with two states for pedestrian crossing
        stateCount = 2;
        states = new State[stateCount];
        
        // Configure DONT_WALK state (30 seconds)
        strcpy(states[0].color, "DONT_WALK");
        states[0].duration = 30;
        
        // Configure WALK state (15 seconds)
        strcpy(states[1].color, "WALK");
        states[1].duration = 15;
    }

    // Implement cycling behavior for pedestrian light
    void cycle() override {
        // Move to next state using modulo for circular cycling
        currentState = (currentState + 1) % stateCount;
        // Output current state information
        std::cout << "Pedestrian Light: " << getCurrentColor() 
                  << " (" << getCurrentDuration() << "s)" << std::endl;
    }
};
```

### Traffic Light Manager Implementation
```cpp
class TrafficLightManager {
private:
    TrafficLightController** controllers;    // Dynamic array of controller pointers
    int controllerCount;                     // Current number of controllers
    int capacity;                            // Current array capacity

public:
    // Constructor initializes all members to safe default values
    TrafficLightManager() : controllers(nullptr), controllerCount(0), capacity(0) {}
    
    // Destructor ensures proper cleanup of all controllers
    ~TrafficLightManager() {
        for (int i = 0; i < controllerCount; i++) {
            delete controllers[i];
        }
        delete[] controllers;
    }
    
    // Add a new controller to the array
    void addController(TrafficLightController* controller) {
        // Check if array needs resizing
        if (controllerCount == capacity) {
            // Double the capacity (or initialize to 1 if empty)
            capacity = capacity == 0 ? 1 : capacity * 2;
            // Create new array with increased capacity
            TrafficLightController** newControllers = new TrafficLightController*[capacity];
            // Copy existing controllers
            for (int i = 0; i < controllerCount; i++) {
                newControllers[i] = controllers[i];
            }
            // Clean up old array and update pointer
            delete[] controllers;
            controllers = newControllers;
        }
        // Add new controller
        controllers[controllerCount++] = controller;
    }

    // Remove a controller at specified index
    void removeController(int index) {
        if (index >= 0 && index < controllerCount) {
            // Delete the controller
            delete controllers[index];
            // Shift remaining controllers to fill gap
            for (int i = index; i < controllerCount - 1; i++) {
                controllers[i] = controllers[i + 1];
            }
            // Decrease count
            controllerCount--;
        }
    }

    // Accessor methods
    int getControllerCount() const { return controllerCount; }
    TrafficLightController* getController(int index) const {
        return (index >= 0 && index < controllerCount) ? controllers[index] : nullptr;
    }
};
```

### Main Program Implementation
```cpp
int main() {
    // Create traffic light manager
    TrafficLightManager manager;
    
    // Add different types of controllers
    manager.addController(new UrbanController());
    manager.addController(new PedestrianController());
    
    std::cout << "Starting Traffic Light Simulation\n" << std::endl;
    
    // Simulate 5 cycles
    for (int i = 0; i < 5; i++) {
        std::cout << "\nCycle " << (i + 1) << ":" << std::endl;
        // Cycle through all controllers
        for (int j = 0; j < manager.getControllerCount(); j++) {
            manager.getController(j)->cycle();
        }
    }
    
    std::cout << "\nSimulation Complete" << std::endl;
    return 0;
}
```

## Key Concepts Demonstrated
1. **Dynamic Memory Management**
   - Dynamic arrays for states and controllers
   - Proper memory cleanup in destructors
   - Array resizing for controller management

2. **Object-Oriented Programming**
   - Abstract base class with pure virtual functions
   - Inheritance through derived classes
   - Polymorphism in cycling behavior

3. **Pointer Arithmetic**
   - Traversal of state arrays
   - Dynamic controller management
   - Safe pointer operations

## Building and Running
1. Compile the program using a C++ compiler:
   ```bash
   g++ -o traffic_light_manager main.cpp
   ```
2. Run the executable:
   ```bash
   ./traffic_light_manager
   ```

## Requirements
- C++11 or later
- Standard C++ library
- Any modern C++ compiler (g++, clang++, MSVC)

## Notes
- The implementation uses smart memory management practices
- All dynamically allocated memory is properly freed
- The code follows RAII principles
- Error handling is implemented for array bounds checking 