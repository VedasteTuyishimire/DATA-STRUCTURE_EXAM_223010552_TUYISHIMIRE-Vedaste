#include <iostream>
#include <cstring>

// State structure to hold traffic light state information
struct State {
    char color[10];
    int duration;
};

// Abstract base class for traffic light controllers
class TrafficLightController {
protected:
    State* states;
    int stateCount;
    int currentState;

public:
    TrafficLightController() : states(nullptr), stateCount(0), currentState(0) {}
    virtual ~TrafficLightController() { delete[] states; }
    
    virtual void cycle() = 0;
    
    // Get current state information
    const char* getCurrentColor() const { return states[currentState].color; }
    int getCurrentDuration() const { return states[currentState].duration; }
};

// Urban traffic light controller implementation
class UrbanController : public TrafficLightController {
public:
    UrbanController() {
        stateCount = 3;
        states = new State[stateCount];
        
        strcpy(states[0].color, "RED");
        states[0].duration = 30;
        
        strcpy(states[1].color, "GREEN");
        states[1].duration = 45;
        
        strcpy(states[2].color, "YELLOW");
        states[2].duration = 5;
    }

    void cycle() override {
        currentState = (currentState + 1) % stateCount;
        std::cout << "Urban Light: " << getCurrentColor() 
                  << " (" << getCurrentDuration() << "s)" << std::endl;
    }
};

// Pedestrian traffic light controller implementation
class PedestrianController : public TrafficLightController {
public:
    PedestrianController() {
        stateCount = 2;
        states = new State[stateCount];
        
        strcpy(states[0].color, "DONT_WALK");
        states[0].duration = 30;
        
        strcpy(states[1].color, "WALK");
        states[1].duration = 15;
    }

    void cycle() override {
        currentState = (currentState + 1) % stateCount;
        std::cout << "Pedestrian Light: " << getCurrentColor() 
                  << " (" << getCurrentDuration() << "s)" << std::endl;
    }
};

// Traffic Light Manager class to handle multiple controllers
class TrafficLightManager {
private:
    TrafficLightController** controllers;
    int controllerCount;
    int capacity;

public:
    TrafficLightManager() : controllers(nullptr), controllerCount(0), capacity(0) {}
    
    ~TrafficLightManager() {
        for (int i = 0; i < controllerCount; i++) {
            delete controllers[i];
        }
        delete[] controllers;
    }
    
    void addController(TrafficLightController* controller) {
        if (controllerCount == capacity) {
            capacity = capacity == 0 ? 1 : capacity * 2;
            TrafficLightController** newControllers = new TrafficLightController*[capacity];
            for (int i = 0; i < controllerCount; i++) {
                newControllers[i] = controllers[i];
            }
            delete[] controllers;
            controllers = newControllers;
        }
        controllers[controllerCount++] = controller;
    }

    void removeController(int index) {
        if (index >= 0 && index < controllerCount) {
            delete controllers[index];
            for (int i = index; i < controllerCount - 1; i++) {
                controllers[i] = controllers[i + 1];
            }
            controllerCount--;
        }
    }

    int getControllerCount() const { return controllerCount; }
    TrafficLightController* getController(int index) const {
        return (index >= 0 && index < controllerCount) ? controllers[index] : nullptr;
    }
};

int main() {
    TrafficLightManager manager;
    
    // Add different types of controllers
    manager.addController(new UrbanController());
    manager.addController(new PedestrianController());
    
    std::cout << "Starting Traffic Light Simulation\n" << std::endl;
    
    // Simulate 5 cycles
    for (int i = 0; i < 5; i++) {
        std::cout << "\nCycle " << (i + 1) << ":" << std::endl;
        for (int j = 0; j < manager.getControllerCount(); j++) {
            manager.getController(j)->cycle();
        }
    }
    
    std::cout << "\nSimulation Complete" << std::endl;
    return 0;
} 